---
type: Business Rule
title: High Cancellation/Modification Trader
description: Identifies traders who frequently cancel or modify orders, potentially indicating manipulative intent or poor execution strategy.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 18
---

# Definition

A trader is flagged if their average cancelpct > 0.5 OR their average OMI > 1.5 across their transactions.

# Columns used

* [transactionrecord](/tables/transactionrecord.md): `cancelpct`

# Depends on

* [Order Modification Intensity (OMI)](/knowledge/order-modification-intensity.md)

# Used by

* [Potentially Evasive Order Modifier](/knowledge/potentially-evasive-order-modifier.md)
* [Confirmed Evasive Layering/Spoofing](/knowledge/confirmed-evasive-layering-spoofing.md)
