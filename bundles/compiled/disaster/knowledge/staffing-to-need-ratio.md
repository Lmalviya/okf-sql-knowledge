---
type: Calculation
title: Staffing to Need Ratio (SNR)
description: Evaluates whether staffing levels match operational requirements
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 34
---

# Definition

SNR = \frac{staffingprofile->>'personnel'->>'total'}{(impactMetrics->>'population'->>'affected'/10000)} \times PER \times ppe\_factor, \text{ where ppe\_factor is 1.2 for Adequate, 0.8 for Limited, 0.5 for Critical PPE status, and 0 for else}

# Columns used

* [disasterevents](/tables/disasterevents.md): `impactmetrics`
* [humanresources](/tables/humanresources.md): `staffingprofile`

# Depends on

* [staffingProfile.readiness.ppe_status](/knowledge/staffingprofile-readiness-ppe-status.md)
* [Personnel Effectiveness Ratio (PER)](/knowledge/personnel-effectiveness-ratio.md)
