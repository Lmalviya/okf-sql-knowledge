---
type: Calculation
title: Support Efficiency Index (SEI)
description: Measures the efficiency of platform resources spent on supporting a fan
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 19
---

# Definition

SEI = \frac{satrate}{(supptix + 1)} \times \left(1 + \frac{FLV}{100}\right), \text{ where higher values indicate fans who provide good platform ratings with minimal support requirements, adjusted by their lifetime value.}

# Columns used

* [supportandfeedback](/tables/supportandfeedback.md): `supptix`, `satrate`

# Depends on

* [Fan Lifetime Value (FLV)](/knowledge/fan-lifetime-value.md)

# Used by

* [Premium Service Candidate](/knowledge/premium-service-candidate.md)
