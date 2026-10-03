---
type: Value Illustration
title: exectune
description: Illustrates the meaning of different values for the exectune enum.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 29
---

# Definition

An enum with values 'Maker' or 'Taker'. 'Maker' indicates the order added liquidity to the order book by not matching immediately. 'Taker' indicates the order removed liquidity from the order book by matching with existing orders immediately upon placement.

# Columns used

* [orderexecutions](/tables/orderexecutions.md): `exectune`
