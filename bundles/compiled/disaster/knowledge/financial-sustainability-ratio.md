---
type: Calculation
title: Financial Sustainability Ratio (FSR)
description: Assesses the financial sustainability of disaster response operations
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 18
---

# Definition

FSR = \frac{donorcommitmentsusd}{budgetallotusd} \times \left(1 - \frac{fundsutilpct}{100}\right) - \frac{resourcegapsusd}{budgetallotusd}

# Columns used

* [financials](/tables/financials.md): `budgetallotusd`, `fundsutilpct`, `donorcommitmentsusd`, `resourcegapsusd`

# Used by

* [Financial Crisis Risk](/knowledge/financial-crisis-risk.md)
* [Financial Efficiency Metric (FEM)](/knowledge/financial-efficiency-metric.md)
