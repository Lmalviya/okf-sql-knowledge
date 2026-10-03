---
type: Business Rule
title: Sustainable Response Operation
description: Identifies disaster responses with strong sustainability practices
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 25
---

# Definition

Operations where EIF < 50 AND renewenergypct > 30 AND recyclepct > 60, demonstrating environmental responsibility during emergency response

# Columns used

* [environmentandhealth](/tables/environmentandhealth.md): `recyclepct`, `renewenergypct`

# Depends on

* [Environmental Impact Factor (EIF)](/knowledge/environmental-impact-factor.md)

# Used by

* [Sustainable Operation Excellence](/knowledge/sustainable-operation-excellence.md)
