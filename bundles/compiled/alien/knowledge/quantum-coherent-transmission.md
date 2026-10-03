---
type: Business Rule
title: Quantum-Coherent Transmission
description: Describes signals potentially employing quantum properties for communication.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 43
---

# Definition

Signals with $\text{QuantEffects}$ containing 'Significant' or 'Observed' patterns, exhibiting unusually high information density ($\text{InfoDense} > 1.5$) while maintaining an $\text{ECI} > 2.5$, suggesting advanced transmission technologies beyond conventional radiofrequency methods.

# Columns used

* [signaladvancedphenomena](/tables/signaladvancedphenomena.md): `quanteffects`
* [signalclassification](/tables/signalclassification.md): `infodense`

# Depends on

* [Encoding Complexity Index (ECI)](/knowledge/encoding-complexity-index.md)
