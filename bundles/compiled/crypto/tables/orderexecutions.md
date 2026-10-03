---
type: PostgreSQL Table
title: orderexecutions
description: '8 columns: fillcount, remaincount, fillquote, fillsum, expirespot, cancelnote, exectune. Joins to orders.'
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
| `fillcount` | numeric | A DECIMAL(8,4) showing how many units were filled (e.g., '0.0500'). |
| `remaincount` | numeric | A NUMERIC(8,4) showing how many units remain unfilled (e.g., '0.0750'). |
| `fillquote` | numeric | A DECIMAL(12,3) capturing the fill price (e.g., '27699.150'). |
| `fillsum` | numeric | A DECIMAL(12,3) notional of the fill (e.g., '1384.958'). |
| `expirespot` | timestamp without time zone | A TIMESTAMP if the partial fill or order slice expires (e.g., '2025-05-10 15:00:00'). |
| `cancelnote` | USER-DEFINED | An enum (CancelNote_enum) describing cancel reason (Expired, InsufficientFunds, UserRequested). |
| `exectune` | USER-DEFINED | An enum (ExecTune_enum) indicating execution style (Maker, Taker). |
| `ordersmark` | character | A CHAR(36) referencing Orders(RecordVault) to link back to the original order. |

# Joins

* `ordersmark` references `recordvault` in [orders](/tables/orders.md).

# Related knowledge

* [Order Fill Rate](/knowledge/order-fill-rate.md)
* [Market Maker Activity](/knowledge/market-maker-activity.md)
* [exectune](/knowledge/exectune.md)
