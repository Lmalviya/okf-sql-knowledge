---
type: PostgreSQL Table
title: trader
description: '9 columns: tradekind, acctdays, acctbal, freqscope, voldaily, posavg, posspan, trading_performance.'
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
| `tradereg` | character varying, primary key | VARCHAR(50). Primary key uniquely identifying each trader account (e.g., 'TRD‑987654'). |
| `tradekind` | USER-DEFINED | trader_type_enum (enum: 'Market Maker', 'Broker', 'Individual', 'Institution'). Broad category of the trader. |
| `acctdays` | integer | INT. Age of the trading account in days since opening (e.g., 782). |
| `acctbal` | numeric | NUMERIC(20,2). Current cash equity in the trader’s account in USD (e.g., 2 150 345.75). |
| `freqscope` | USER-DEFINED | trading_frequency_enum (enum: 'Low', 'Medium', 'High'). Average trading frequency classification. |
| `voldaily` | numeric | NUMERIC(20,4). Mean daily share volume traded across all symbols (e.g., 1 250 000.0000). |
| `posavg` | numeric | NUMERIC(20,4). Average position size in USD held per trade (e.g., 350 000.0000). |
| `posspan` | USER-DEFINED | position_holding_period_enum (enum: 'Intraday', 'Position', 'Long-term', 'Swing'). Typical holding‑period style. |
| `trading_performance` | jsonb | JSONB column. Stores metrics related to the trader's performance and risk profile, including win rate, profit-to-loss ratio, and risk characteristics. |

# JSON fields

* `trading_performance.winpct`: NUMERIC(5,2). Historical win‑rate percentage across trades (e.g., 57.35).
* `trading_performance.plratio`: NUMERIC(7,4). Profit‑to‑loss ratio of realised trades (e.g., 1.2430).
* `trading_performance.risklevel.risklevel`: risk_tolerance_enum (enum: 'Conservative', 'Aggressive', 'Moderate'). Stated or inferred risk appetite.
* `trading_performance.risklevel.margpct`: NUMERIC(5,2). Percentage of margin utilisation versus account equity (e.g., 28.50).
* `trading_performance.risklevel.levratio`: NUMERIC(7,4). Leverage ratio applied to positions (e.g., 2.3500).

# Related knowledge

* [Daily Turnover Rate (DTR)](/knowledge/daily-turnover-rate.md)
* [Trader Leverage Exposure (TLE)](/knowledge/trader-leverage-exposure.md)
* [Compliance Recidivism Score (CRS)](/knowledge/compliance-recidivism-score.md)
* [Enforcement Financial Impact Ratio (EFIR)](/knowledge/enforcement-financial-impact-ratio.md)
* [High-Risk Trader Profile](/knowledge/high-risk-trader-profile.md)
* [Trader Position Holding Style](/knowledge/trader-position-holding-style.md)
* [High-Frequency High-Risk Trader](/knowledge/high-frequency-high-risk-trader.md)
* [High-Volume Wash Trading Concern](/knowledge/high-volume-wash-trading-concern.md)
* [Capital-Adjusted Investigation Intensity (CAII)](/knowledge/capital-adjusted-investigation-intensity.md)
* [Risk-Adjusted Win Rate (RAWR)](/knowledge/risk-adjusted-win-rate.md)
* [Peer Correlation Z-Score](/knowledge/peer-correlation-z-score.md)
