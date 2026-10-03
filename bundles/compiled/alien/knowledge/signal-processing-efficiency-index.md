---
type: Calculation
title: Signal Processing Efficiency Index (SPEI)
description: Evaluates the computational efficiency of signal processing relative to complexity.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 34
---

# Definition

$\text{SPEI} = \frac{\text{DecodeIters} \times \text{ProcTimeHrs}}{\text{ECI} \times \text{ComplexIdx}}$, where ECI (Encoding Complexity Index) provides the complexity component to normalize processing time and iterations.

# Columns used

* [signalclassification](/tables/signalclassification.md): `complexidx`
* [signaldecoding](/tables/signaldecoding.md): `decodeiters`, `proctimehrs`

# Depends on

* [Encoding Complexity Index (ECI)](/knowledge/encoding-complexity-index.md)
