---
type: Value Illustration
title: Marking the Close Patterns
description: Explains the patterns associated with influencing the closing price of a security.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 25
---

# Definition

`risk_indicators.markclosepat`: 'Frequent' indicates repeated trading activity near the market close, potentially intended to manipulate the closing price (e.g., to affect margin calls, NAV calculations, or settlement prices). 'Occasional' suggests such activity is infrequent or less patterned. Marking the close is a prohibited manipulative practice.

# Columns used

* [transactionrecord](/tables/transactionrecord.md): `risk_indicators`
