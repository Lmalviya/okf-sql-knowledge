---
type: PostgreSQL Table
title: marketdata
description: '1 columns: quote_depth_snapshot.'
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
| `quote_depth_snapshot` | jsonb | JSONB column. Captures a full market‑microstructure snapshot—best quotes, size, depth, spreads, and derived mid/mark/index prices—inside a single JSONB column. |

# JSON fields

* `quote_depth_snapshot.metadata.exchnote`: A CHAR(10) for exchange code (e.g., 'FTX').
* `quote_depth_snapshot.metadata.mktcombo`: A VARCHAR(30) naming the trading pair (e.g., 'ETH/USDT').
* `quote_depth_snapshot.metadata.timetrack`: A TIMESTAMP noting when data was recorded (e.g., '2025-05-10 13:45:30').
* `quote_depth_snapshot.quotes.bidquote`: A DECIMAL(12,3) best bid price (e.g., '27550.250').
* `quote_depth_snapshot.quotes.askquote`: A DECIMAL(12,3) best ask price (e.g., '27555.100').
* `quote_depth_snapshot.quotes.midquote`: A DECIMAL(12,3) midpoint price (e.g., '27552.675').
* `quote_depth_snapshot.quotes.markquote`: A DECIMAL(12,3) reference 'mark' price for derivatives (e.g., '27553.000').
* `quote_depth_snapshot.quotes.indexquote`: A DECIMAL(12,3) index price if used (e.g., '27560.125').
* `quote_depth_snapshot.depth.bidunits`: A NUMERIC(12,4) quantity at best bid (e.g., '12.5000').
* `quote_depth_snapshot.depth.askunits`: A NUMERIC(12,4) quantity at best ask (e.g., '8.0000').
* `quote_depth_snapshot.depth.biddepth`: A REAL summarizing deeper bid liquidity (e.g., 56.7).
* `quote_depth_snapshot.depth.askdepth`: A REAL summarizing deeper ask liquidity (e.g., 42.1).
* `quote_depth_snapshot.spread.spreadband`: A DOUBLE PRECISION for raw spread (e.g., 4.850).
* `quote_depth_snapshot.spread.spreadrate`: A DECIMAL(8,4) spread as a ratio or percentage (e.g., '0.0175').
