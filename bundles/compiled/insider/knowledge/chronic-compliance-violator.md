---
type: Business Rule
title: Chronic Compliance Violator
description: Identifies traders with a problematic history and a high recidivism score.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 44
---

# Definition

A trader identified as having a Problematic Compliance History  AND whose Compliance Recidivism Score (CRS)  is greater than 1.5.

# Depends on

* [Compliance Recidivism Score (CRS)](/knowledge/compliance-recidivism-score.md)
* [Problematic Compliance History](/knowledge/problematic-compliance-history.md)

# Used by

* [Severe Chronic Violator Case](/knowledge/severe-chronic-violator-case.md)
