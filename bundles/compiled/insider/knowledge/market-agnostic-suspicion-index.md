---
type: Calculation
title: Market-Agnostic Suspicion Index (MASI)
description: Combines the general suspicion index with market-adjusted pattern anomaly, focusing on suspicious activity independent of market moves.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 56
---

# Definition

MASI = (\text{SAI} + \text{MAPA}) / 2 \\ \text{where SAI is Suspicious Activity Index  and MAPA is Market-Adjusted Pattern Anomaly .}

# Depends on

* [Suspicious Activity Index (SAI)](/knowledge/suspicious-activity-index.md)
* [Market-Adjusted Pattern Anomaly (MAPA)](/knowledge/market-adjusted-pattern-anomaly.md)
