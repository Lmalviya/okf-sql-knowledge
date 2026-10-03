---
type: Calculation
title: Operational Efficiency Index (OEI)
description: Quantifies operational efficiency based on resource allocation and supply flow
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 11
---

# Definition

OEI = \frac{deliverysuccessrate}{100} \times \left(1 - \frac{avgdeliveryhours}{24}\right) \times \left(1 + \frac{distributionpoints}{10}\right)

# Columns used

* [transportation](/tables/transportation.md): `distributionpoints`, `avgdeliveryhours`, `deliverysuccessrate`

# Used by

* [Operational Excellence](/knowledge/operational-excellence.md)
* [Financial Efficiency Metric (FEM)](/knowledge/financial-efficiency-metric.md)
* [Rapid Response Success Model](/knowledge/rapid-response-success-model.md)
