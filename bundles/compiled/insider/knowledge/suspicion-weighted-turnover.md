---
type: Calculation
title: Suspicion-Weighted Turnover (SWT)
description: Calculates daily turnover weighted by the Suspicious Activity Index.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 37
---

# Definition

SWT = \text{SAI} \times \text{DTR} \\ \text{where SAI is Suspicious Activity Index  and DTR is Daily Turnover Rate .}

# Depends on

* [Daily Turnover Rate (DTR)](/knowledge/daily-turnover-rate.md)
* [Suspicious Activity Index (SAI)](/knowledge/suspicious-activity-index.md)

# Used by

* [Collusion Network Indicator](/knowledge/collusion-network-indicator.md)
