---
type: Calculation
title: Shipment Quality Index (SQI)
description: Overall quality score for shipment considering multiple factors.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 33
---

# Definition

SQI = \frac{\text{VVP}}{365} \times \text{HQI} \times (1 - \text{CRI})

# Depends on

* [Vaccine Viability Period (VVP)](/knowledge/vaccine-viability-period.md)
* [Handling Quality Index (HQI)](/knowledge/handling-quality-index.md)
* [Container Risk Index (CRI)](/knowledge/container-risk-index.md)

# Used by

* [Quality Maintenance Index (QMI)](/knowledge/quality-maintenance-index.md)
