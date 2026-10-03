---
type: Business Rule
title: Potential Biosignature
description: Defines characteristics of signals potentially associated with biological processes.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 17
---

# Definition

Signals with $\text{BioSigProb} > 0.6$, $\text{TechSigProb} < 0.4$, and spectral features that match known biological emission patterns, often associated with specific molecular transitions.

# Columns used

* [signalprobabilities](/tables/signalprobabilities.md): `techsigprob`, `biosigprob`
