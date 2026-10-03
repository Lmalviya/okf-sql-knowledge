---
type: Value Illustration
title: retentionandinfluence.churnflag
description: Explains the judgment basis for churn risk rating
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 8
---

# Definition

'None' indicates extremely low churn risk, with users maintaining high-frequency interaction and recent consumption; 'Low' represents slight churn risk with slightly decreased login frequency; 'Medium' indicates moderate churn risk with significantly decreased interaction and consumption frequency and increased login intervals; 'High' represents severe churn risk with no logins or interactions in the past 14-30 days, requiring immediate intervention.

# Columns used

* [retentionandinfluence](/tables/retentionandinfluence.md): `churnflag`

# Used by

* [Churn Risk Numeric Mapping](/knowledge/churn-risk-numeric-mapping.md)
