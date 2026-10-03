---
type: Business Rule
title: Elevated Regulatory Scrutiny
description: Identifies compliance cases under intense review or investigation.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 14
---

# Definition

A case is under Elevated Regulatory Scrutiny if `alertlvl` is 'High' or 'Critical' AND `invstprior` is 'High' AND `monitint` is 'Intensive'.

# Columns used

* [compliancecase](/tables/compliancecase.md): `alertlvl`, `invstprior`, `monitint`

# Depends on

* [Logarithmic Enforcement Fine Impact (LEFI)](/knowledge/logarithmic-enforcement-fine-impact.md)

# Used by

* [Confirmed Manipulator Under Scrutiny](/knowledge/confirmed-manipulator-under-scrutiny.md)
* [High-Scrutiny Wash Trading Case](/knowledge/high-scrutiny-wash-trading-case.md)
* [Severe Chronic Violator Case](/knowledge/severe-chronic-violator-case.md)
