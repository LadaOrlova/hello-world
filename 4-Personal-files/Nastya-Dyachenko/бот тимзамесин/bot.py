import asyncio
import logging
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import aiosqlite
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_PATH = "chats.db"
NOTIFY_AFTER_HOURS = 2
WORK_START = 10
WORK_END = 19
MSK = ZoneInfo("Europe/Moscow")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler()


# --- База данных ---

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS pending_chats (
                chat_id INTEGER PRIMARY KEY,
                client_name TEXT,
                last_message TEXT,
                last_message_at TIMESTAMP,
                status TEXT DEFAULT 'active'
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS sent_messages (
                message_id INTEGER PRIMARY KEY
            )
        """)
        for col, definition in [
            ("status", "TEXT DEFAULT 'active'"),
            ("username", "TEXT"),
        ]:
            try:
                await db.execute(f"ALTER TABLE pending_chats ADD COLUMN {col} {definition}")
            except Exception:
                pass
        await db.commit()


async def get_setting(key: str):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT value FROM settings WHERE key = ?", (key,))
        row = await cursor.fetchone()
        return row[0] if row else None


async def set_setting(key: str, value: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)",
            (key, str(value))
        )
        await db.commit()


async def add_or_update_pending(chat_id: int, client_name: str, last_message: str, username: str | None = None):
    async with aiosqlite.connect(DB_PATH) as db:
        now = datetime.now(timezone.utc).isoformat()
        cursor = await db.execute(
            "SELECT chat_id FROM pending_chats WHERE chat_id = ?", (chat_id,)
        )
        existing = await cursor.fetchone()
        if existing:
            await db.execute("""
                UPDATE pending_chats
                SET last_message = ?, last_message_at = ?, status = 'active', username = ?
                WHERE chat_id = ?
            """, (last_message, now, username, chat_id))
        else:
            await db.execute("""
                INSERT INTO pending_chats
                    (chat_id, client_name, last_message, last_message_at, status, username)
                VALUES (?, ?, ?, ?, 'active', ?)
            """, (chat_id, client_name, last_message, now, username))
        await db.commit()


async def remove_pending(chat_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("DELETE FROM pending_chats WHERE chat_id = ?", (chat_id,))
        await db.commit()


async def archive_chat(chat_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE pending_chats SET status = 'archived' WHERE chat_id = ?",
            (chat_id,)
        )
        await db.commit()


async def save_sent_message(message_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR IGNORE INTO sent_messages (message_id) VALUES (?)",
            (message_id,)
        )
        await db.commit()


async def delete_previous_messages(chat_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT message_id FROM sent_messages")
        rows = await cursor.fetchall()
        for (message_id,) in rows:
            try:
                await bot.delete_message(chat_id, message_id)
            except Exception:
                pass
        await db.execute("DELETE FROM sent_messages")
        await db.commit()


def notify_keyboard(chat_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Убрать из списка", callback_data=f"archive_{chat_id}"),
    ]])


def format_waiting(waiting: timedelta) -> str:
    hours = int(waiting.total_seconds() // 3600)
    minutes = int((waiting.total_seconds() % 3600) // 60)
    return f"{hours} ч {minutes} мин" if hours > 0 else f"{minutes} мин"


async def get_active_chats():
    now = datetime.now(timezone.utc)
    threshold = now - timedelta(hours=NOTIFY_AFTER_HOURS)
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT chat_id, client_name, last_message, last_message_at, username "
            "FROM pending_chats WHERE status = 'active' AND last_message_at <= ? "
            "ORDER BY last_message_at ASC",
            (threshold.isoformat(),)
        )
        return await cursor.fetchall(), now


# --- Отправка списка ---

async def send_list(chat_id: int):
    chats, now = await get_active_chats()

    await delete_previous_messages(chat_id)

    if not chats:
        msg = await bot.send_message(chat_id, "Нет чатов без ответа.")
        await save_sent_message(msg.message_id)
        return

    header = await bot.send_message(
        chat_id, f"<b>Чатов без ответа: {len(chats)}</b>", parse_mode="HTML"
    )
    await save_sent_message(header.message_id)

    for c_id, client_name, last_message, last_message_at, username in chats:
        last_message_dt = datetime.fromisoformat(last_message_at)
        waiting = now - last_message_dt
        time_str = format_waiting(waiting)
        preview = last_message[:100] + ("..." if len(last_message) > 100 else "")

        chat_link = f"https://t.me/{username}" if username else f"tg://user?id={c_id}"
        username_line = f"\n@{username}" if username else ""
        text = (
            f"\U0001f464 <b>{client_name}</b> — {time_str} без ответа\n"
            f"\U0001f4ac {preview}\n"
            f"\U0001f517 <a href='{chat_link}'>Открыть чат</a>{username_line}"
        )
        msg = await bot.send_message(
            chat_id, text, parse_mode="HTML", reply_markup=notify_keyboard(c_id)
        )
        await save_sent_message(msg.message_id)


async def send_hourly_list():
    owner_chat_id = await get_setting("owner_chat_id")
    if not owner_chat_id:
        return
    await send_list(int(owner_chat_id))


# --- Обработчики кнопок ---

@dp.callback_query(F.data.startswith("archive_"))
async def on_archive(callback: CallbackQuery):
    chat_id = int(callback.data.split("_")[1])
    await archive_chat(chat_id)
    await callback.message.edit_text(
        callback.message.text + "\n\n<i>Убрано из списка.</i>",
        parse_mode="HTML"
    )
    await callback.answer()


# --- Обработчики команд ---

@dp.message(Command("list"))
async def cmd_list(message: Message):
    await send_list(message.chat.id)


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await set_setting("owner_chat_id", str(message.chat.id))
    await set_setting("owner_user_id", str(message.from_user.id))
    await message.answer(
        "Бот запущен!\n\n"
        "Я буду отправлять список чатов без ответа (>2 ч) "
        "каждый час с 10:00 до 19:00 МСК.\n\n"
        "Предыдущий список автоматически удаляется — "
        "в чате всегда только актуальная информация.\n\n"
        "Команды:\n"
        "/list — показать список прямо сейчас"
    )


# --- Обработчик бизнес-сообщений ---

@dp.business_message()
async def handle_business_message(message: Message):
    owner_user_id = await get_setting("owner_user_id")
    if not owner_user_id:
        return

    if not message.from_user:
        logger.warning("business_message без from_user, пропускаем")
        return

    owner_user_id = int(owner_user_id)
    chat_id = message.chat.id

    if message.from_user.id == owner_user_id:
        await remove_pending(chat_id)
        return

    client_name = message.from_user.full_name
    last_message = message.text or "[медиафайл]"
    username = message.from_user.username
    await add_or_update_pending(chat_id, client_name, last_message, username)


# --- Запуск ---

async def main():
    await init_db()
    # Каждый час с 10:00 до 18:00 МСК (последний список в 18:00)
    scheduler.add_job(
        send_hourly_list,
        CronTrigger(hour="10-18", minute=0, timezone=MSK),
        misfire_grace_time=3600,
    )
    scheduler.start()
    logger.info("Бот запущен. Список каждый час с 10:00 до 18:00 МСК.")

    # Если бот запустился в рабочее время — сразу отправить список
    now_msk = datetime.now(MSK)
    if WORK_START <= now_msk.hour < WORK_END:
        logger.info("Запуск в рабочее время — отправляю список сразу.")
        await send_hourly_list()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
