---
type: Value Illustration
title: Momentum Ignition Signals
description: Explains the signals related to attempting to artificially create price momentum.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 24
---

# Definition

`risk_indicators.momentignit`: 'Strong' indicates patterns consistent with attempts to trigger momentum algorithms or attract other traders by creating a false sense of rapid price movement (e.g., through rapid successive trades). 'Weak' suggests such patterns are less evident or absent. This is a potential indicator of manipulative behavior.

# Columns used

* [transactionrecord](/tables/transactionrecord.md): `risk_indicators`
