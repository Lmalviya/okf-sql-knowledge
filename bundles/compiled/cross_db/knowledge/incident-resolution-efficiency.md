---
type: Calculation
title: Incident Resolution Efficiency (IRE)
description: Measures how efficiently incidents are resolved relative to SLA compliance.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 48
---

# Definition

IRE = \text{SLApct} / (\text{AvgResolHrs} + 1), \text{where SLApct and AvgResolHrs are from RiskManagement, adding 1 to avoid division by zero.}

# Columns used

* [riskmanagement](/tables/riskmanagement.md): `avgresolhrs`, `slapct`

# Used by

* [Incident Impact Factor (IIF)](/knowledge/incident-impact-factor.md)
