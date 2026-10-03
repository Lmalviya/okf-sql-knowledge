---
type: Calculation
title: Facility Efficiency Index (FEI)
description: Estimates facility efficiency by relating the achieved patient stability metric to the available facility resource adequacy.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 51
---

# Definition

FEI = PSM \times FRAI, \text{multiplying Patient Stability Metric (PSM) by Facility Resource Adequacy Index (FRAI). Higher scores suggest better stability achieved per resource level.}

# Depends on

* [Patient Stability Metric (PSM)](/knowledge/patient-stability-metric.md)
* [Facility Resource Adequacy Index (FRAI)](/knowledge/facility-resource-adequacy-index.md)
