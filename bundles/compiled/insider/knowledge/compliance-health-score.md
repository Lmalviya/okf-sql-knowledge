---
type: Calculation
title: Compliance Health Score (CHS)
description: Inverse score reflecting compliance history severity, penalizing high recidivism and poor ratings.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 32
---

# Definition

CHS = \frac{1}{1 + \text{CRS} \times \text{ComplianceRatingValue}}

# Depends on

* [Compliance Recidivism Score (CRS)](/knowledge/compliance-recidivism-score.md)
* [Compliance Rating Grade](/knowledge/compliance-rating-grade.md)

# Used by

* [Market Manipulation Pattern: Layering/Spoofing](/knowledge/market-manipulation-pattern-layering-spoofing.md)
* [Investigation Compliance Risk Index (ICRI)](/knowledge/investigation-compliance-risk-index.md)
