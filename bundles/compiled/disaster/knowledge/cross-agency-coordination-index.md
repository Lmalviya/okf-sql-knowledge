---
type: Calculation
title: Cross-Agency Coordination Index (CACI)
description: Quantifies how effectively multiple agencies coordinate during disaster response
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 39
---

# Definition

CACI = \frac{partnerorgs}{10} \times coordeffect\_numeric \times \left(\frac{infosharing\_numeric + 1}{3}\right), \text{ where coordeffect\_numeric maps Low=1, Medium=2, High=3, else=0 and infosharing\_numeric maps Poor=1, Limited=2, Effective=3, else=0}

# Columns used

* [coordinationandevaluation](/tables/coordinationandevaluation.md): `partnerorgs`

# Used by

* [Cross-Agency Coordination Crisis](/knowledge/cross-agency-coordination-crisis.md)
