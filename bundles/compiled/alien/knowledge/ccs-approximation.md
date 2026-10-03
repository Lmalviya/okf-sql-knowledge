---
type: Calculation
title: CCS Approximation
description: Simplified CCS calculation using direct signal-to-noise ratio values when full Signal-to-Noise Quality Indicator (SNQI) data is unavailable.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 47
---

# Definition

$(1 - \text{FalsePosProb}) \times \text{DecodeConf} \times (\text{SNR} - 0.1 \times |\text{NoiseFloorDbm}| > 0 ? \frac{\text{SNR} - 0.1 \times |\text{NoiseFloorDbm}|}{10} + 0.5 : 0.1)$

# Columns used

* [signals](/tables/signals.md): `noisefloordbm`
* [signalprobabilities](/tables/signalprobabilities.md): `falseposprob`
* [signaldecoding](/tables/signaldecoding.md): `decodeconf`

# Depends on

* [Confirmation Confidence Score (CCS)](/knowledge/confirmation-confidence-score.md)
