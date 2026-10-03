---
type: Business Rule
title: Market Maker Activity
description: Identifies periods of high market maker participation.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 14
---

# Definition

Market conditions where exectune is predominantly 'Maker' and makermotion is 'High', indicating strong liquidity provision by market makers.

# Columns used

* [orderexecutions](/tables/orderexecutions.md): `exectune`

# Used by

* [Optimal Trading Window](/knowledge/optimal-trading-window.md)
