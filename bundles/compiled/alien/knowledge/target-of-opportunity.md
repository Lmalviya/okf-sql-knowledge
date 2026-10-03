---
type: Business Rule
title: Target of Opportunity (TOO)
description: Identifies high-value signals requiring immediate follow-up observation.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 12
---

# Definition

Any signal with $\text{RPI} > 3.5$, $\text{TechSigProb} > 0.8$, and $\text{AnomScore} > 5$ that has not been previously documented or explained by known phenomena.

# Columns used

* [signalprobabilities](/tables/signalprobabilities.md): `anomscore`, `techsigprob`

# Depends on

* [Research Priority Index (RPI)](/knowledge/research-priority-index.md)

# Used by

* [Research Critical Signal](/knowledge/research-critical-signal.md)
