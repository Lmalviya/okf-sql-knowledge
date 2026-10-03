---
type: Calculation
title: Combined Manipulation Indicator (CMI)
description: A combined score reflecting both general suspicious activity and specific pattern anomalies.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 31
---

# Definition

CMI = (\text{SAI} + \text{PAS}) / 2 \\ \text{where SAI is Suspicious Activity Index  and PAS is Pattern Anomaly Score .}

# Depends on

* [Suspicious Activity Index (SAI)](/knowledge/suspicious-activity-index.md)
* [Pattern Anomaly Score (PAS)](/knowledge/pattern-anomaly-score.md)

# Used by

* [Market Manipulation Pattern: Layering/Spoofing](/knowledge/market-manipulation-pattern-layering-spoofing.md)
