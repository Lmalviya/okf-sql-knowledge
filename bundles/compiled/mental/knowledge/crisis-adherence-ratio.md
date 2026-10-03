---
type: Calculation
title: Crisis Adherence Ratio (CAR)
description: Calculates the ratio of crisis intervention frequency to the treatment adherence rate, indicating crises occurring per unit of adherence.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 54
---

# Definition

CAR = \frac{CIF}{TAR + 0.01}, \text{dividing Crisis Intervention Frequency (CIF) by Treatment Adherence Rate (TAR) (adjusted to prevent division by zero). Higher values indicate more crises relative to adherence levels.}

# Depends on

* [Crisis Intervention Frequency (CIF)](/knowledge/crisis-intervention-frequency.md)
* [Treatment Adherence Rate (TAR)](/knowledge/treatment-adherence-rate.md)
