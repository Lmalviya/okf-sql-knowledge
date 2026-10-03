---
type: Calculation
title: Confirmation Confidence Score (CCS)
description: Quantifies overall confidence in signal verification across multiple parameters.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 36
---

# Definition

$\text{CCS} = (1 - \text{FalsePosProb}) \times \text{DecodeConf} \times \text{ClassConf} \times (\text{SNQI} > 0 ? \frac{\text{SNQI}}{10} + 0.5 : 0.1)$, where SNQI (Signal-to-Noise Quality Indicator) provides a quality weighting factor.

# Columns used

* [signalprobabilities](/tables/signalprobabilities.md): `falseposprob`
* [signalclassification](/tables/signalclassification.md): `classconf`
* [signaldecoding](/tables/signaldecoding.md): `decodeconf`

# Depends on

* [Signal-to-Noise Quality Indicator (SNQI)](/knowledge/signal-to-noise-quality-indicator.md)

# Used by

* [High-Confidence Technosignature](/knowledge/high-confidence-technosignature.md)
* [CCS Approximation](/knowledge/ccs-approximation.md)
* [Observation-Verified Signal](/knowledge/observation-verified-signal.md)
* [High Confidence Signals](/knowledge/high-confidence-signals.md)
