---
type: Calculation
title: Financial Efficiency Metric (FEM)
description: Measures the cost-effectiveness of disaster operations
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 35
---

# Definition

FEM = \frac{benefeedbackscore}{costbeneusd} \times FSR \times \left(1 + \frac{OEI}{10}\right), \text{ where higher scores represent more efficient use of financial resources}

# Columns used

* [beneficiariesandassessments](/tables/beneficiariesandassessments.md): `benefeedbackscore`
* [financials](/tables/financials.md): `costbeneusd`

# Depends on

* [Operational Efficiency Index (OEI)](/knowledge/operational-efficiency-index.md)
* [Financial Sustainability Ratio (FSR)](/knowledge/financial-sustainability-ratio.md)
