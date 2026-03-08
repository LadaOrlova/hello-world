# Юнит-экономика: From Zero to First Product

Дата: 2026-03-01
Версия: 1.0

---

## Бизнес-модель
- Тип: Freemium → одноразовая покупка (с upsell)
- Ценообразование: Standard $199 / Premium $399

## Ключевые допущения

| Метрика | Значение | Источник | Статус |
|---------|----------|----------|--------|
| ARPU (blended) | $250 | Среднее $199/$399, 70/30 split | [ПРОВЕРИТЬ] |
| CR visitor → signup | 15% | Бенчмарк education landing | [ПРОВЕРИТЬ] |
| CR signup → Module 1 complete | 40% | Target из PRD | [ПРОВЕРИТЬ] |
| CR Module 1 → aha moment | 60% | Target из PRD | [ПРОВЕРИТЬ] |
| CR aha → purchase | 15% | Target из PRD | [ПРОВЕРИТЬ] |
| End-to-end CR visitor → paid | 0.54% | 15% x 40% x 60% x 15% | Расчёт |
| Course completion rate | 35% | Target из PRD | [ПРОВЕРИТЬ] |
| Refund rate | 5% | 14-day money-back | [ПРОВЕРИТЬ] |
| CAC organic (SEO) | $10 | Допущение | [ПРОВЕРИТЬ] |
| CAC paid (Google/Meta) | $80 | Бенчмарк education US | [ПРОВЕРИТЬ] |
| Blended CAC | $40 | 60% organic, 40% paid | [ПРОВЕРИТЬ] |
| Cross-sell CR | 15% | Бенчмарк | [ПРОВЕРИТЬ] |
| Cross-sell ARPU | $30 | Средний чек cross-sell | [ПРОВЕРИТЬ] |
| Upsell CR (advanced course) | 5% | Бенчмарк | [ПРОВЕРИТЬ] |
| Upsell ARPU | $350 | Advanced Course | [ПРОВЕРИТЬ] |
| Gross margin | 85% | Digital product, minimal COGS | Допущение |

## Расчёт LTV

**Для одноразовой покупки + cross/upsell:**

Base LTV = ARPU x Gross Margin = $250 x 0.85 = $212.50
Cross-sell LTV = Cross-sell CR x Cross-sell ARPU x Margin = 15% x $30 x 0.85 = $3.83
Upsell LTV = Upsell CR x Upsell ARPU x Margin = 5% x $350 x 0.85 = $14.88

**Total LTV = $212.50 + $3.83 + $14.88 = $231.21**

## Расчёт CAC по каналам

| Канал | Бюджет/мес | Visitors | CR→paid | Клиенты/мес | CAC |
|-------|-----------|----------|---------|-------------|-----|
| SEO/Content | $500 | 5,000 | 0.54% | 27 | $18.5 |
| Google Ads | $2,000 | 2,500 | 0.54% | 13.5 | $148 |
| Meta Ads | $2,000 | 4,000 | 0.40% | 16 | $125 |
| Twitter/X | $0 | 2,000 | 0.30% | 6 | $0 |
| Referral | $0 | 1,000 | 1.0% | 10 | $0 |
| **Total** | **$4,500** | **14,500** | | **72.5** | **$62** |

## Ключевые метрики

| Метрика | Значение | Целевое | Статус |
|---------|----------|---------|--------|
| LTV/CAC ratio | 3.7 | > 3.0 | OK |
| Payback period | 0 мес (one-time) | < 3 мес | OK |
| Monthly revenue (Year 1 avg) | $6,250 | $6,000+ | OK |
| Annual revenue | $75,000 | $75K-150K | [ПРОВЕРИТЬ] |
| Gross profit/year | $63,750 | | Расчёт |
| Break-even | Месяц 3 | < 6 мес | [ПРОВЕРИТЬ] |

## Payback Period
One-time purchase → CAC paid back immediately at purchase.
Break-even: Fixed costs $4,500/мес → нужно ~20 продаж/мес для покрытия.

## Точка безубыточности
- Фиксированные расходы/мес: $4,500 (ads) + $500 (infra) + $500 (tools) = $5,500
- Маржа с клиента: $212.50
- Клиентов для безубыточности: 26/мес ~ 312/год

## Когортный анализ (шаблон)

| Когорта | M0 | M1 | M2 | M3 | M6 | M12 |
|---------|----|----|----|----|----|----|
| Free signups | 100% | — | — | — | — | — |
| Module 1 complete | 40% | — | — | — | — | — |
| Aha reached | 24% | — | — | — | — | — |
| Purchased | 3.6% | — | — | — | — | — |
| Course complete | 1.3% | — | — | — | — | — |
| Cross-sell | — | 0.5% | — | — | — | — |
| Upsell | — | — | 0.2% | — | — | — |

## Эксперименты для валидации

По принципу RAT (самые рискованные — первые):

1. **CR visitor → signup (15%):** Landing page + $500 paid ads → реальный CR. Бюджет: $500, срок: 1 неделя
2. **CR aha → purchase (15%):** Smoke test с paywall после Module 1. Бюджет: $0 (organic traffic), срок: 2 недели
3. **CAC paid ($80):** Тестовые кампании Google + Meta по $500. Бюджет: $1,000, срок: 2 недели
4. **Blended ARPU ($250):** A/B тест $199 vs $299 vs $399. Бюджет: $0, срок: 4 недели
5. **Cross-sell CR (15%):** Предложить Templates Pack после Module 5. Бюджет: $0, срок: 6 недель

## Сценарии

| Сценарий | ARPU | CR visitor→paid | CAC | LTV | LTV/CAC | Annual Rev | Вердикт |
|----------|------|-----------------|-----|-----|---------|------------|---------|
| Оптимистичный | $300 | 0.8% | $40 | $280 | 7.0 | $120K | Отличный бизнес |
| Базовый | $250 | 0.54% | $62 | $231 | 3.7 | $75K | Жизнеспособный |
| Пессимистичный | $199 | 0.3% | $100 | $175 | 1.75 | $40K | На грани, нужен pivot |

**Вывод:** В базовом сценарии бизнес жизнеспособен (LTV/CAC 3.7, break-even на 26 клиентах/мес). Главные рычаги: (1) CR aha→purchase и (2) CAC. Если удастся снизить CAC до $40 через SEO — экономика отличная. Если CAC > $100 (пессимистичный) — нужно пивотить на более высокую цену или другой канал.
