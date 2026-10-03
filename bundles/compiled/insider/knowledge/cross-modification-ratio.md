---
type: Calculation
title: Cross-Modification Ratio (CMR)
description: Calculates the ratio of cross-trade frequency to order modification intensity, potentially indicating coordinated or manipulative crossing activity.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 57
---

# Definition

CMR = \frac{\text{crossfreq}}{\text{Max}(0.01, \text{OMI})} \\ \text{where OMI is Order Modification Intensity .}

# Columns used

* [transactionrecord](/tables/transactionrecord.md): `crossfreq`

# Depends on

* [Order Modification Intensity (OMI)](/knowledge/order-modification-intensity.md)
