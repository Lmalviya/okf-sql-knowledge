---
type: Calculation
title: Cross-Border Data Volume Risk (CDVR)
description: Assesses risk from large cross-border data volumes.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 33
---

# Definition

CDVR = \text{CBRF} \times \text{VolGB}

# Columns used

* [dataprofile](/tables/dataprofile.md): `volgb`

# Depends on

* [Cross-Border Risk Factor (CBRF)](/knowledge/cross-border-risk-factor.md)
* [DataProfile.VolGB](/knowledge/dataprofile-volgb.md)

# Used by

* [Cross-Border Audit Risk](/knowledge/cross-border-audit-risk.md)
* [Cross-Border Compliance Exposure (CBCE)](/knowledge/cross-border-compliance-exposure.md)
