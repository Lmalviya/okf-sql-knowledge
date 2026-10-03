---
type: Business Rule
title: Financial Crisis Risk
description: Identifies operations at risk of financial collapse
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 27
---

# Definition

Operations where fundsutilpct > 80 AND fundingstate is 'Critical' AND FSR < 0.2, indicating severe financial strain that threatens operational continuity

# Columns used

* [financials](/tables/financials.md): `fundsutilpct`, `fundingstate`

# Depends on

* [fundingstate](/knowledge/fundingstate.md)
* [Financial Sustainability Ratio (FSR)](/knowledge/financial-sustainability-ratio.md)

# Used by

* [Financial Vulnerability Zone](/knowledge/financial-vulnerability-zone.md)
