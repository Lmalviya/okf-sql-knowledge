---
type: PostgreSQL Table
title: transactionrecord
description: '12 columns: transtime, ordervar, ordertimepat, ordertypedist, cancelpct, modfreq, darkusage, offmkt, crossfreq, risk_indicators. Joins to trader.'
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
| `transreg` | character varying, primary key | VARCHAR(50). Primary key for an individual trade‑day record (e.g., 'REC‑20250117‑0001'). |
| `transtime` | timestamp without time zone | TIMESTAMP. Date‑time the trade blotter snapshot was taken (e.g., '2025‑04‑17 13:42:05'). |
| `trdref` | character varying | VARCHAR(50). Foreign‑key linking this record to Trader.TradeReg. |
| `ordervar` | numeric | NUMERIC(20,4). Variance of order sizes submitted during the session. |
| `ordertimepat` | USER-DEFINED | order_timing_pattern_enum (enum: 'Irregular', 'Regular', 'Suspicious'). Pattern of order entry times. |
| `ordertypedist` | USER-DEFINED | order_type_distribution_enum (enum: 'Market', 'Mixed', 'Limit'). Distribution of order types used. |
| `cancelpct` | numeric | NUMERIC(7,4). Percentage of orders cancelled before execution (e.g., 35.8125). |
| `modfreq` | numeric | NUMERIC(7,4). Average number of order modifications per original order (e.g., 0.7430). |
| `darkusage` | character varying | VARCHAR(100). Qualitative or venue list describing dark‑pool usage (e.g., 'ATS‑X, ATS‑Y'). |
| `offmkt` | character varying | VARCHAR(100). Summary of off‑exchange trade activity (e.g., 'Internal crosses'). |
| `crossfreq` | numeric | NUMERIC(10,4). Frequency of cross trades relative to total trades (e.g., 0.1520). |
| `risk_indicators` | jsonb | JSONB column. Aggregates indicators of potential market abuse or risky trading behaviors, such as spoofing probability, front-running risk, and wash trade suspicion. |

# JSON fields

* `risk_indicators.spoofprob`: NUMERIC(5,2). Probability score that spoofing behaviour occurred (0‑100, e.g., 18.75).
* `risk_indicators.frontscore`: NUMERIC(7,4). Front‑running risk score (e.g., 0.5620).
* `risk_indicators.qstuffindex`: NUMERIC(7,4). Quote‑stuffing index value computed for the session (e.g., 1.8345).
* `risk_indicators.washsus`: wash_trade_suspicion_enum (enum: 'Low', 'Medium', 'High'). System‑derived wash‑trading suspicion level.
* `risk_indicators.layerind`: layering_indicator_enum (enum: 'Confirmed', 'Suspected'). Presence of order‑layering indicators.
* `risk_indicators.momentignit`: momentum_ignition_signal_enum (enum: 'Strong', 'Weak'). Strength of detected momentum‑ignition patterns.
* `risk_indicators.markclosepat`: marking_close_pattern_enum (enum: 'Occasional', 'Frequent'). Pattern of marking‑the‑close activity.

# Joins

* `trdref` references `tradereg` in [trader](/tables/trader.md).

# Related knowledge

* [Order Modification Intensity (OMI)](/knowledge/order-modification-intensity.md)
* [Suspicious Activity Index (SAI)](/knowledge/suspicious-activity-index.md)
* [Market Manipulation Pattern: Layering/Spoofing](/knowledge/market-manipulation-pattern-layering-spoofing.md)
* [Wash Trading Alert](/knowledge/wash-trading-alert.md)
* [Event-Driven Trader](/knowledge/event-driven-trader.md)
* [High Cancellation/Modification Trader](/knowledge/high-cancellation-modification-trader.md)
* [Dark Pool Usage Venues](/knowledge/dark-pool-usage-venues.md)
* [Off-Market Trading Activity](/knowledge/off-market-trading-activity.md)
* [Order Type Distribution](/knowledge/order-type-distribution.md)
* [Momentum Ignition Signals](/knowledge/momentum-ignition-signals.md)
* [Marking the Close Patterns](/knowledge/marking-the-close-patterns.md)
* [Cross-Modification Ratio (CMR)](/knowledge/cross-modification-ratio.md)
* [Confirmed Evasive Layering/Spoofing](/knowledge/confirmed-evasive-layering-spoofing.md)
