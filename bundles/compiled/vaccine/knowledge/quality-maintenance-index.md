---
type: Calculation
title: Quality Maintenance Index (QMI)
description: Combined quality and maintenance metric.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 37
---

# Definition

QMI = \text{MCS} \times \text{SQI} \times (1 - \frac{\text{TBS}}{10})

# Depends on

* [Maintenance Compliance Score (MCS)](/knowledge/maintenance-compliance-score.md)
* [Shipment Quality Index (SQI)](/knowledge/shipment-quality-index.md)
* [Temperature Breach Severity (TBS)](/knowledge/temperature-breach-severity.md)

# Used by

* [High Maintenance Priority](/knowledge/high-maintenance-priority.md)
* [Quality Alert Status](/knowledge/quality-alert-status.md)
