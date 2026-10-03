---
type: Calculation
title: Market Stability Index (MSI)
description: Assesses the stability and reliability of disaster response operations over time
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 14
---

# Definition

MSI = \frac{estdurationdays}{365.0} \times \frac{deliverysuccessrate}{100.0} \times \left(1 - \frac{secincidentcount}{partnerorgs::integer \times 10 + 1}\right) \times 100, \text{ where estdurationdays represents operation duration from operations table, deliverysuccessrate captures logistics reliability from transportation table, and secincidentcount/partnerorgs ratio approximates system disruptions per partner organization}

# Columns used

* [operations](/tables/operations.md): `estdurationdays`
* [coordinationandevaluation](/tables/coordinationandevaluation.md): `secincidentcount`, `partnerorgs`
* [transportation](/tables/transportation.md): `deliverysuccessrate`
