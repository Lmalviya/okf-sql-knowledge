---
type: Calculation
title: Temperature Breach Severity (TBS)
description: Calculates severity of temperature breaches.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 9
---

# Definition

TBS = \frac{|TempNowC - StoreTempC|}{TempTolC} \times TempDevCount

# Columns used

* [sensordata](/tables/sensordata.md): `storetempc`, `temptolc`, `tempnowc`, `tempdevcount`

# Used by

* [Container Health Status](/knowledge/container-health-status.md)
* [Temperature Alert](/knowledge/temperature-alert.md)
* [Total Risk Score (TRS)](/knowledge/total-risk-score.md)
* [Combined Maintenance Risk (CMR)](/knowledge/combined-maintenance-risk.md)
* [Quality Maintenance Index (QMI)](/knowledge/quality-maintenance-index.md)
* [Multi-Parameter Risk Assessment (MPRA)](/knowledge/multi-parameter-risk-assessment.md)
* [Time-Weighted Quality Decay (TWQD)](/knowledge/time-weighted-quality-decay.md)
* [Environmental Stress Factor (ESF)](/knowledge/environmental-stress-factor.md)
* [Multi-System Failure Risk](/knowledge/multi-system-failure-risk.md)
