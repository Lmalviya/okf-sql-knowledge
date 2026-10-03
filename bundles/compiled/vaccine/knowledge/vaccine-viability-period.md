---
type: Calculation
title: Vaccine Viability Period (VVP)
description: Calculates remaining viable days for vaccines considering temperature deviations.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 3
---

# Definition

VVP = (ExpireDay - Current_Date) \times TSS

# Columns used

* [vaccinedetails](/tables/vaccinedetails.md): `expireday`

# Depends on

* [Temperature Stability Score (TSS)](/knowledge/temperature-stability-score.md)

# Used by

* [Quality Compromise](/knowledge/quality-compromise.md)
* [Shipment Quality Index (SQI)](/knowledge/shipment-quality-index.md)
* [Vaccine Safety Index (VSI)](/knowledge/vaccine-safety-index.md)
* [Time-Weighted Quality Decay (TWQD)](/knowledge/time-weighted-quality-decay.md)
