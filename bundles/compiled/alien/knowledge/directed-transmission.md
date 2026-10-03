---
type: Business Rule
title: Directed Transmission
description: Identifies signals that appear specifically directed rather than omnidirectional.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 45
---

# Definition

Signals with high spatial stability ($\text{SpatStab} = \text{'Moderate'}$), narrow beam characteristics ($\text{PolarMode} = \text{'Linear'}$ with stable $\text{PolarAngleDeg}$), and high $\text{TOLS} > 0.85$, suggesting intentional transmission toward our location.

# Columns used

* [signaldynamics](/tables/signaldynamics.md): `spatstab`
* [signals](/tables/signals.md): `polarmode`, `polarangledeg`

# Depends on

* [Technological Origin Likelihood Score (TOLS)](/knowledge/technological-origin-likelihood-score.md)
