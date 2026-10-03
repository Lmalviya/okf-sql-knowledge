---
type: Calculation
title: Observation Quality Factor (OQF)
description: Provides a comprehensive measure of observational conditions quality.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 32
---

# Definition

$\text{OQF} = \text{AOI} \times (1 - \text{LIF}) \times (\text{PointAccArc} < 2 ? 1 : \frac{2}{\text{PointAccArc}})$, where AOI (Atmospheric Observability Index) and LIF (Lunar Interference Factor) are combined with telescope pointing accuracy.

# Columns used

* [telescopes](/tables/telescopes.md): `pointaccarc`

# Depends on

* [Atmospheric Observability Index (AOI)](/knowledge/atmospheric-observability-index.md)
* [Lunar Interference Factor (LIF)](/knowledge/lunar-interference-factor.md)

# Used by

* [Observation-Verified Signal](/knowledge/observation-verified-signal.md)
