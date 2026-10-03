---
type: Business Rule
title: Problematic Compliance History
description: Identifies traders with a poor track record of compliance.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 15
---

# Definition

A trader has a Problematic Compliance History if they have `prevviol` > 3 OR their `comprate` is 'C' or 'D' OR their CRS > 1.0.

# Columns used

* [compliancecase](/tables/compliancecase.md): `prevviol`, `comprate`

# Depends on

* [Compliance Recidivism Score (CRS)](/knowledge/compliance-recidivism-score.md)
* [Aggressive Trading Intensity (ATI)](/knowledge/aggressive-trading-intensity.md)

# Used by

* [Chronic Compliance Violator](/knowledge/chronic-compliance-violator.md)
* [Escalated Compliance Failure](/knowledge/escalated-compliance-failure.md)
