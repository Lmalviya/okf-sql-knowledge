---
type: PostgreSQL Table
title: systemmonitoring
description: '13 columns: apireqtotal, apierrtotal, apilatmark, wsstate, rateremain, lastupdnote, seqcode, slipratio, exectimespan, queueline, mkteffect, priceeffect. Joins to analyticsindicators.'
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_schema.txt
  title: crypto schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_column_meaning_base.json
  title: crypto column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `apireqtotal` | integer | An INTEGER counting total API requests in a window (e.g., 45230). |
| `apierrtotal` | integer | An INTEGER total of API errors (e.g., 123). |
| `apilatmark` | real | A REAL capturing average API latency (e.g., 150.2). |
| `wsstate` | USER-DEFINED | An enum (WSState_enum) describing websocket state (Connected, Disconnected). |
| `rateremain` | smallint | A SMALLINT for remaining requests before rate limit (e.g., 75). |
| `lastupdnote` | character varying | A VARCHAR(60) short note on last system update (e.g., 'AutoScale triggered'). |
| `seqcode` | character varying | A VARCHAR(60) sequence/version code for real-time updates (e.g., 'seq-0012'). |
| `slipratio` | numeric | A DECIMAL(12,3) average slippage measure (e.g., '0.250'). |
| `exectimespan` | numeric | A DECIMAL(8,2) typical order execution time in ms or s (e.g., '12.50'). |
| `queueline` | integer | An INTEGER tracking queued tasks or orders (e.g., 45). |
| `mkteffect` | real | A REAL approximating internal market impact (e.g., 1.2). |
| `priceeffect` | real | A REAL approximating net price improvement (e.g., 0.4). |
| `aitrack` | bigint | A BIGINT FK to AnalyticsIndicators(AnalyticsIndicatorsNode), linking to advanced analytics. |

# Joins

* `aitrack` references `analyticsindicatorsnode` in [analyticsindicators](/tables/analyticsindicators.md).

# Related knowledge

* [Market Impact Cost (MIC)](/knowledge/market-impact-cost.md)
* [Market Efficiency Ratio (MER)](/knowledge/market-efficiency-ratio.md)
