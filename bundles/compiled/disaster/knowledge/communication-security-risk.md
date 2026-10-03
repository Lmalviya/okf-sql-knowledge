---
type: Calculation
title: Communication Security Risk (CSR)
description: Measures the security risk associated with communication systems during disaster response
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 12
---

# Definition

CSR = secincidentcount \times 5 + (100 - reportcompliance) + 90 - (dataqualityvalue \times 3)

# Columns used

* [coordinationandevaluation](/tables/coordinationandevaluation.md): `secincidentcount`, `reportcompliance`, `dataqualityvalue`

# Used by

* [Communication Resilience Factor (CRF)](/knowledge/communication-resilience-factor.md)
