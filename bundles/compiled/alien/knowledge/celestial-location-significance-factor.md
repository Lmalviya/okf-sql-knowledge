---
type: Calculation
title: Celestial Location Significance Factor (CLSF)
description: Calculates significance of signal source location based on astronomical targets of interest.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 35
---

# Definition

$\text{CLSF} = (\text{CelestObj} ? 2 : 1) \times (\text{ObjType} == \text{'Giant'} \&\& \text{ObjMassSol} \text{ between } 0.8 \text{ and } 1.2 ? 1.5 : 1) \times (\text{ObjMetal} > 0 ? \text{ObjMetal} + 1 : 0.5)$, where higher values indicate source locations more likely to harbor intelligent life.

# Columns used

* [sourceproperties](/tables/sourceproperties.md): `celestobj`, `objtype`, `objmasssol`, `objmetal`

# Used by

* [Signal of Galactic Significance](/knowledge/signal-of-galactic-significance.md)
