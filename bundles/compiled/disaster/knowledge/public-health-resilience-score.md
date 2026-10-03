---
type: Calculation
title: Public Health Resilience Score (PHRS)
description: Evaluates the resilience of public health systems during disasters
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 17
---

# Definition

PHRS = waterqualityindex \times 0.4 + sanitationcoverage \times 0.3 + vaccinationcoverage \times 0.3

# Columns used

* [environmentandhealth](/tables/environmentandhealth.md): `waterqualityindex`, `sanitationcoverage`, `vaccinationcoverage`

# Used by

* [Public Health Emergency](/knowledge/public-health-emergency.md)
* [Health System Capacity Index (HSCI)](/knowledge/health-system-capacity-index.md)
