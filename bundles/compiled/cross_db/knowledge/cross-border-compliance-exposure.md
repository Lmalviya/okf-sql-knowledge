---
type: Calculation
title: Cross-Border Compliance Exposure (CBCE)
description: Quantifies compliance risk for cross-border flows based on regulatory gaps and volume.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 54
---

# Definition

CBCE = \text{CDVR} \times \begin{cases} 2 & \text{if GdprComp = 'Non-compliant'} \\ 1 & \text{otherwise} \end{cases}

# Columns used

* [compliance](/tables/compliance.md): `gdprcomp`

# Depends on

* [Compliance.GdprComp](/knowledge/compliance-gdprcomp.md)
* [Cross-Border Data Volume Risk (CDVR)](/knowledge/cross-border-data-volume-risk.md)

# Used by

* [Overloaded Security Flow](/knowledge/overloaded-security-flow.md)
