---
type: Calculation
title: Signal Complexity Ratio (SCR)
description: Measures the relationship between signal complexity and information density.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 2
---

# Definition

$\text{SCR} = \frac{\text{ComplexIdx} \times \text{InfoDense}}{\log(\text{BwHz})}$, where higher values suggest potential artificial origin rather than natural phenomena.

# Columns used

* [signals](/tables/signals.md): `bwhz`
* [signalclassification](/tables/signalclassification.md): `complexidx`, `infodense`

# Used by

* [Pattern Recognition Confidence (PRC)](/knowledge/pattern-recognition-confidence.md)
