---
type: PostgreSQL Table
title: fees
description: '7 columns: feerange, feerate, feetotal, feecoin, rebrate, rebtotal. Joins to orders.'
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
| `feerange` | USER-DEFINED | An enum (FeeRange_enum) describing the user's fee tier (Tier4, Tier1, Tier3, Tier2). |
| `feerate` | numeric | A DECIMAL(8,5) capturing fee percentage (e.g., '0.00050'). |
| `feetotal` | numeric | A DECIMAL(12,6) total fee charged (e.g., '0.250000'). |
| `feecoin` | USER-DEFINED | An enum (FeeCoin_enum) for the currency used to pay fees (USDC, USD, USDT). |
| `rebrate` | numeric | A DECIMAL(8,5) capturing the maker rebate rate (e.g., '0.00015'). |
| `rebtotal` | numeric | A DECIMAL(12,6) total rebate (e.g., '0.075000'). |
| `orderslink` | character | A CHAR(36) referencing Orders(RecordVault), linking fees to a specific order. |

# Joins

* `orderslink` references `recordvault` in [orders](/tables/orders.md).

# Related knowledge

* [True Cost of Execution](/knowledge/true-cost-of-execution.md)
* [Arbitrage ROI](/knowledge/arbitrage-roi.md)
