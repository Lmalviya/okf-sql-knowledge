---
type: Calculation
title: Technological Origin Likelihood Score (TOLS)
description: Combines multiple factors to estimate likelihood of technological origin.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 3
---

# Definition

$\text{TOLS} = \text{TechSigProb} \times (1 - \text{NatSrcProb}) \times \text{SigUnique} \times (0.5 + \frac{\text{AnomScore}}{10})$, where values above 0.75 warrant further investigation as potential technosignatures.

# Columns used

* [signalprobabilities](/tables/signalprobabilities.md): `sigunique`, `anomscore`, `techsigprob`, `natsrcprob`

# Used by

* [Artificial Intelligence Detection Probability (AIDP)](/knowledge/artificial-intelligence-detection-probability.md)
* [Habitable Zone Signal Relevance (HZSR)](/knowledge/habitable-zone-signal-relevance.md)
* [Directed Transmission](/knowledge/directed-transmission.md)
* [TOLS Category](/knowledge/tols-category.md)
