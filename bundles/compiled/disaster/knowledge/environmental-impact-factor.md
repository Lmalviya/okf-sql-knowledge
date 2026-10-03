---
type: Calculation
title: Environmental Impact Factor (EIF)
description: Quantifies the environmental footprint of disaster response operations
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 16
---

# Definition

EIF = carbontons \times \left(1 - \frac{renewenergypct}{100}\right) + (100 - recyclepct) \times 0.5

# Columns used

* [environmentandhealth](/tables/environmentandhealth.md): `recyclepct`, `carbontons`, `renewenergypct`

# Used by

* [Sustainable Response Operation](/knowledge/sustainable-response-operation.md)
* [Supply Chain Sustainability Index (SCSI)](/knowledge/supply-chain-sustainability-index.md)
* [Environmental Impact Classification](/knowledge/environmental-impact-classification.md)
