---
type: Calculation
title: Container Risk Index (CRI)
description: Calculates overall risk level for a container based on temperature stability and coolant status.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 2
---

# Definition

CRI = (1 - TSS) \times (1 - \frac{CoolRemainPct}{100})

# Columns used

* [container](/tables/container.md): `coolremainpct`

# Depends on

* [Temperature Stability Score (TSS)](/knowledge/temperature-stability-score.md)

# Used by

* [Container Health Status](/knowledge/container-health-status.md)
* [High-Risk Route](/knowledge/high-risk-route.md)
* [Total Risk Score (TRS)](/knowledge/total-risk-score.md)
* [Shipment Quality Index (SQI)](/knowledge/shipment-quality-index.md)
* [Container Efficiency Score (CES)](/knowledge/container-efficiency-score.md)
* [Multi-Parameter Risk Assessment (MPRA)](/knowledge/multi-parameter-risk-assessment.md)
* [Multi-System Failure Risk](/knowledge/multi-system-failure-risk.md)
* [Risk Rank](/knowledge/risk-rank.md)
