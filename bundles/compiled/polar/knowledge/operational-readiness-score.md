---
type: Calculation
title: Operational Readiness Score (ORS)
description: Quantifies how ready equipment is for immediate deployment based on operational status and maintenance schedule.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 1
---

# Definition

ORS = \begin{cases} 10 \times (1 - \frac{operationhours}{maintenancecyclehours}) & \text{if operationalstatus = 'Active'} \\ 5 \times (1 - \frac{operationhours}{maintenancecyclehours}) & \text{if operationalstatus = 'Standby'} \\ 0 & \text{otherwise} \end{cases}

# Columns used

* [operationmaintenance](/tables/operationmaintenance.md): `operationhours`, `maintenancecyclehours`, `operationalstatus`

# Used by

* [Life Support System Reliability (LSSR)](/knowledge/life-support-system-reliability.md)
* [Long-term Operational Stability Score (LOSS)](/knowledge/long-term-operational-stability-score.md)
* [Comprehensive Operational Reliability Indicator (CORI)](/knowledge/comprehensive-operational-reliability-indicator.md)
