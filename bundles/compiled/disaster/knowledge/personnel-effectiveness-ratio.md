---
type: Calculation
title: Personnel Effectiveness Ratio (PER)
description: Evaluates how effectively human resources are utilized in operations
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 13
---

# Definition

PER = \frac{staffingprofile->>'personnel'->>'total'}{(personnelcostsusd / 10000)} \times \frac{staffingprofile->>'readiness'->>'availability_percent'}{100}

# Columns used

* [humanresources](/tables/humanresources.md): `staffingprofile`
* [financials](/tables/financials.md): `personnelcostsusd`

# Used by

* [Staffing to Need Ratio (SNR)](/knowledge/staffing-to-need-ratio.md)
* [Critical Resource Prioritization Need](/knowledge/critical-resource-prioritization-need.md)
