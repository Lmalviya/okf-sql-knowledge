---
type: Business Rule
title: Technosignature
description: Defines the concept of signals that indicate technological activity.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 10
---

# Definition

A signal with $\text{TechSigProb} > 0.7$, $\text{NatSrcProb} < 0.3$, and $\text{ArtSrcProb} < 50$ that exhibits narrow bandwidth ($\text{BFR} < 0.001$) and high information density ($\text{InfoDense} > 0.8$).

# Columns used

* [signalprobabilities](/tables/signalprobabilities.md): `techsigprob`, `natsrcprob`, `artsrcprob`
* [signalclassification](/tables/signalclassification.md): `infodense`

# Depends on

* [Bandwidth-Frequency Ratio (BFR)](/knowledge/bandwidth-frequency-ratio.md)

# Used by

* [High-Confidence Technosignature](/knowledge/high-confidence-technosignature.md)
* [Habitable Zone Transmission](/knowledge/habitable-zone-transmission.md)
* [Signal of Galactic Significance](/knowledge/signal-of-galactic-significance.md)
