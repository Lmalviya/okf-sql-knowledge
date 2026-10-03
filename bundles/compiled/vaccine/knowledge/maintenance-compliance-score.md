---
type: Calculation
title: Maintenance Compliance Score (MCS)
description: Calculates compliance with maintenance schedules.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 7
---

# Definition

MCS = CompScore \times (1 - \frac{Incidents}{10})

# Columns used

* [regulatoryandmaintenance](/tables/regulatoryandmaintenance.md): `compscore`, `incidents`

# Used by

* [Maintenance Due](/knowledge/maintenance-due.md)
* [Combined Maintenance Risk (CMR)](/knowledge/combined-maintenance-risk.md)
* [Quality Maintenance Index (QMI)](/knowledge/quality-maintenance-index.md)
