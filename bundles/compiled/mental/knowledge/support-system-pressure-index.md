---
type: Calculation
title: Support System Pressure Index (SSPI)
description: Index assessing the pressure on support systems based on crisis frequency relative to social support effectiveness.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 39
---

# Definition

SSPI = \frac{CIF}{SSE_{avg} + 1}, \text{calculating Crisis Intervention Frequency (CIF) relative to average Social Support Effectiveness (SSE) (adding 1 to avoid division by zero)}

# Depends on

* [Crisis Intervention Frequency (CIF)](/knowledge/crisis-intervention-frequency.md)
* [Social Support Effectiveness (SSE)](/knowledge/social-support-effectiveness.md)
