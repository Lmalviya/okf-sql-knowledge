---
type: Value Illustration
title: Order Type Distribution
description: Illustrates the mix of primary order types used by a trader.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 23
---

# Definition

`ordertypedist`: 'Market' indicates primarily using market orders (execute immediately at the best available price, prioritizing speed over price). 'Limit' indicates primarily using limit orders (execute only at a specified price or better, prioritizing price over speed). 'Mixed' suggests a combination of order types, reflecting varied trading strategies or objectives.

# Columns used

* [transactionrecord](/tables/transactionrecord.md): `ordertypedist`

# Used by

* [Aggressive Event Speculator](/knowledge/aggressive-event-speculator.md)
