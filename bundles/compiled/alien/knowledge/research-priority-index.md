---
type: Calculation
title: Research Priority Index (RPI)
description: Helps researchers prioritize signals for follow-up based on multiple factors.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 8
---

# Definition

$\text{RPI} = (\text{TechSigProb} \times 4 + \frac{\text{BioSigProb}}{100} + \text{SigUnique} \times 2 + \frac{\text{AnomScore}}{2}) \times (1 - \text{FalsePosProb})$, where values above 3 indicate high research priority.

# Columns used

* [signalprobabilities](/tables/signalprobabilities.md): `falseposprob`, `sigunique`, `anomscore`, `techsigprob`, `biosigprob`

# Used by

* [Target of Opportunity (TOO)](/knowledge/target-of-opportunity.md)
