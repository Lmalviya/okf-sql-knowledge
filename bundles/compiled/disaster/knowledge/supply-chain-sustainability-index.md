---
type: Calculation
title: Supply Chain Sustainability Index (SCSI)
description: Assesses the environmental sustainability of the disaster supply chain
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 33
---

# Definition

SCSI = 100 - EIF \times \frac{totaldeliverytons}{1000} \times \left(\frac{fuelefficiencylpk}{20}\right), \text{ where EIF measures the environmental impact and higher scores represent more sustainable supply chains}

# Columns used

* [transportation](/tables/transportation.md): `totaldeliverytons`, `fuelefficiencylpk`

# Depends on

* [Environmental Impact Factor (EIF)](/knowledge/environmental-impact-factor.md)
