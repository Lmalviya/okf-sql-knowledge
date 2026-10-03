---
type: Business Rule
title: Anomalous Quantum Signal
description: Describes signals exhibiting quantum properties inconsistent with current physics models.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 49
---

# Definition

Signals with $\text{QuantEffects}$ indicating anomalous behavior, $\text{AnomScore} > 8$, and unusually high $\text{MCS} (> 2.0)$, suggesting either unknown natural quantum phenomena or extremely advanced transmission technologies beyond current human capabilities.

# Columns used

* [signalprobabilities](/tables/signalprobabilities.md): `anomscore`
* [signaladvancedphenomena](/tables/signaladvancedphenomena.md): `quanteffects`

# Depends on

* [Modulation Complexity Score (MCS)](/knowledge/modulation-complexity-score.md)
