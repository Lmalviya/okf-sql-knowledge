---
type: PostgreSQL Table
title: sentimentandfundamentals
description: '16 columns: newsscore, socscore, anlycount, inholdpct, instownpct, shortintrt, optvolrt, putcallrt, impvolrank, unuoptact, corpeventprx, eventannotm, infoleaksc. Joins to trader, transactionrecord.'
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_schema.txt
  title: insider schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_column_meaning_base.json
  title: insider column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `sentreg` | character varying, primary key | VARCHAR(50). Primary key for combined sentiment/fundamental snapshot. |
| `transref` | character varying | VARCHAR(50). Foreign‑key to TransactionRecord.TransReg. |
| `newsscore` | numeric | NUMERIC(5,2). Normalised sentiment score from news feeds (e.g., 68.25). |
| `socscore` | numeric | NUMERIC(5,2). Social‑media sentiment score (e.g., 54.90). |
| `anlycount` | integer | INT. Number of active analyst coverage reports (e.g., 12). |
| `inholdpct` | numeric | NUMERIC(5,2). Insider ownership percentage of the stock (e.g., 4.75). |
| `instownpct` | numeric | NUMERIC(5,2). Institutional ownership percentage (e.g., 65.20). |
| `shortintrt` | numeric | NUMERIC(7,4). Short‑interest ratio (days to cover, e.g., 2.3475). |
| `optvolrt` | numeric | NUMERIC(7,4). Option volume ratio versus average (e.g., 1.1520). |
| `putcallrt` | numeric | NUMERIC(7,4). Put‑to‑call volume ratio (e.g., 0.6425). |
| `impvolrank` | numeric | NUMERIC(7,4). Implied‑volatility rank (0‑1 scale, e.g., 0.7831). |
| `unuoptact` | USER-DEFINED | unusual_option_activity_enum (enum: 'Moderate', 'High'). Degree of unusual option activity detected. |
| `corpeventprx` | USER-DEFINED | corporate_event_proximity_enum (enum: 'Earnings', 'Restructuring', 'M&A'). Type of corporate event in close temporal proximity. |
| `eventannotm` | USER-DEFINED | event_announcement_timing_enum (enum: 'Pre-market', 'Intraday', 'Post-market'). Timing of the relevant event announcement. |
| `infoleaksc` | numeric | NUMERIC(5,2). Information‑leakage suspicion score (e.g., 22.80). |
| `trdref2` | character varying | VARCHAR(50). Optional foreign‑key to Trader.TradeReg for analyst or insider reference. |

# Joins

* `transref` references `transreg` in [transactionrecord](/tables/transactionrecord.md).
* `trdref2` references `tradereg` in [trader](/tables/trader.md).

# Related knowledge

* [Sentiment Divergence Factor (SDF)](/knowledge/sentiment-divergence-factor.md)
* [Relative Short Interest (RSI)](/knowledge/relative-short-interest.md)
* [Potential Insider Trading Flag](/knowledge/potential-insider-trading-flag.md)
* [Event-Driven Trader](/knowledge/event-driven-trader.md)
* [Unusual Option Activity Level](/knowledge/unusual-option-activity-level.md)
* [Information Leakage Score Interpretation](/knowledge/information-leakage-score-interpretation.md)
* [Sentiment-Weighted Option Volume (SWOV)](/knowledge/sentiment-weighted-option-volume.md)
* [Sentiment-Driven Leakage Risk (SDLR)](/knowledge/sentiment-driven-leakage-risk.md)
