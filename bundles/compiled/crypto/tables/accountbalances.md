---
type: PostgreSQL Table
title: accountbalances
description: '7 columns: walletsum, availsum, frozensum, margsum, unrealline, realline. Joins to users.'
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
| `walletsum` | numeric | A DECIMAL(12,3) total wallet balance (e.g., '1500.500'). |
| `availsum` | numeric | A DECIMAL(12,3) freely available portion (e.g., '1000.250'). |
| `frozensum` | numeric | A DECIMAL(12,3) locked/frozen portion (e.g., '500.250'). |
| `margsum` | numeric | A DECIMAL(12,3) margin account balance (e.g., '2000.000'). |
| `unrealline` | double precision | A DOUBLE PRECISION unrealized PNL (e.g., 120.75). |
| `realline` | double precision | A DOUBLE PRECISION realized PNL (e.g., -45.25). |
| `usertag` | character | A CHAR(36) FK referencing Users(UserStamp). |

# Joins

* `usertag` references `userstamp` in [users](/tables/users.md).

# Related knowledge

* [Realized Risk Ratio (RRR)](/knowledge/realized-risk-ratio.md)
* [Margin Utilization](/knowledge/margin-utilization.md)
* [Risk-Adjusted Return](/knowledge/risk-adjusted-return.md)
* [Effective Leverage](/knowledge/effective-leverage.md)
* [Profit Factor](/knowledge/profit-factor.md)
