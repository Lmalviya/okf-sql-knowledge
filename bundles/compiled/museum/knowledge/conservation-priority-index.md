---
type: Calculation
title: Conservation Priority Index (CPI)
description: Calculates the overall conservation priority for an artifact based on multiple factors.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 0
---

# Definition

CPI = \frac{(HistSignRating + ResearchValRating + CultScore) \times (10 - ConserveStatus)}{30}, \text{where ConserveStatus is numerically mapped: Excellent=1, Good=3, Fair=5, Poor=7, Critical=10}

# Columns used

* [artifactscore](/tables/artifactscore.md): `conservestatus`
* [artifactratings](/tables/artifactratings.md): `histsignrating`, `researchvalrating`, `cultscore`

# Used by

* [Artifact Vulnerability Score (AVS)](/knowledge/artifact-vulnerability-score.md)
* [Conservation Budget Efficiency (CBE)](/knowledge/conservation-budget-efficiency.md)
* [Conservation Backlog Risk (CBR)](/knowledge/conservation-backlog-risk.md)
* [Exhibition Rotation Priority Score (ERPS)](/knowledge/exhibition-rotation-priority-score.md)
* [Conservation Priority Level](/knowledge/conservation-priority-level.md)
