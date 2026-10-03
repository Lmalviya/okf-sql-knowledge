---
type: Calculation
title: Bandwidth Compliance Risk (BCR)
description: Assesses compliance risk from bandwidth-constrained data flows.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 58
---

# Definition

BCR = \text{BRF} \times \begin{cases} 1.5 & \text{if GdprComp = 'Partial'} \\ 2 & \text{if GdprComp = 'Non-compliant'} \\ 1 & \text{otherwise} \end{cases}

# Columns used

* [compliance](/tables/compliance.md): `gdprcomp`

# Depends on

* [Compliance.GdprComp](/knowledge/compliance-gdprcomp.md)
* [Bandwidth Risk Factor (BRF)](/knowledge/bandwidth-risk-factor.md)

# Used by

* [Bandwidth-Limited Compliance Risk](/knowledge/bandwidth-limited-compliance-risk.md)
