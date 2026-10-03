---
type: Calculation
title: Investigation Compliance Risk Index (ICRI)
description: Combines the weighted investigation score with the inverse compliance health score, highlighting cases that are both problematic and under intense investigation.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 50
---

# Definition

ICRI = \text{WIS} \times (1 - \text{CHS}) \\ \text{where WIS is Weighted Investigation Score  and CHS is Compliance Health Score .}

# Depends on

* [Compliance Health Score (CHS)](/knowledge/compliance-health-score.md)
* [Weighted Investigation Score (WIS)](/knowledge/weighted-investigation-score.md)
