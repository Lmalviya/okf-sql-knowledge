---
type: Calculation
title: Habitable Zone Signal Relevance (HZSR)
description: Assesses signal relevance based on source's position in habitable zone.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 37
---

# Definition

$\text{HZSR} = \text{TOLS} \times (\text{ObjType} == \text{'Dwarf'} ? (0.7 \leq \text{ObjMassSol} \leq 1.4 ? (0.8 \leq \frac{\text{SourceDistLy}}{\sqrt{\text{ObjMassSol}}} \leq 1.7 ? 2 : 0.5) : 0.3) : 0.1)$, where TOLS (Technological Origin Likelihood Score) is weighted by stellar habitability factors.

# Columns used

* [sourceproperties](/tables/sourceproperties.md): `sourcedistly`, `objtype`, `objmasssol`

# Depends on

* [Technological Origin Likelihood Score (TOLS)](/knowledge/technological-origin-likelihood-score.md)

# Used by

* [Habitable Zone Transmission](/knowledge/habitable-zone-transmission.md)
