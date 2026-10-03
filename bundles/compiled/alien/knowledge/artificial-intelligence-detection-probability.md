---
type: Calculation
title: Artificial Intelligence Detection Probability (AIDP)
description: Calculates likelihood of artificial intelligence origin based on encoding complexity and technosignature indicators.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 31
---

# Definition

$\text{AIDP} = \frac{\text{ECI} \times \text{TOLS}}{1 + \text{NatSrcProb}}$, where ECI (Encoding Complexity Index) and TOLS (Technological Origin Likelihood Score) are weighted against natural source probability.

# Columns used

* [signalprobabilities](/tables/signalprobabilities.md): `natsrcprob`

# Depends on

* [Encoding Complexity Index (ECI)](/knowledge/encoding-complexity-index.md)
* [Technological Origin Likelihood Score (TOLS)](/knowledge/technological-origin-likelihood-score.md)

# Used by

* [High-Confidence Technosignature](/knowledge/high-confidence-technosignature.md)
* [Signal of Galactic Significance](/knowledge/signal-of-galactic-significance.md)
