---
type: Calculation
title: Investigation Intensity Index (III)
description: Combines behavioral and network analysis scores from an investigation.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 6
---

# Definition

III = (0.6 \times \text{behansc}) + (0.4 \times \text{netansc})

# Columns used

* [investigationdetails](/tables/investigationdetails.md): `behansc`, `netansc`

# Used by

* [Weighted Investigation Score (WIS)](/knowledge/weighted-investigation-score.md)
* [Capital-Adjusted Investigation Intensity (CAII)](/knowledge/capital-adjusted-investigation-intensity.md)
* [High-Intensity Insider Investigation](/knowledge/high-intensity-insider-investigation.md)
* [Premature Resolution Block](/knowledge/premature-resolution-block.md)
