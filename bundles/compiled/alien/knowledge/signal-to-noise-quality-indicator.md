---
type: Calculation
title: Signal-to-Noise Quality Indicator (SNQI)
description: Combines SNR and noise floor to provide a unified signal quality metric.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 0
---

# Definition

$\text{SNQI} = \text{SnrRatio} - 0.1 \times |\text{NoiseFloorDbm}|$, where higher values indicate better detection quality. Positive values generally indicate analyzable signals.

# Columns used

* [signals](/tables/signals.md): `snrratio`, `noisefloordbm`

# Used by

* [Confirmation Confidence Score (CCS)](/knowledge/confirmation-confidence-score.md)
* [Analyzable Signals](/knowledge/analyzable-signals.md)
