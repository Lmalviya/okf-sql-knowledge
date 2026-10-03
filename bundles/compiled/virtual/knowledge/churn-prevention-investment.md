---
type: Calculation
title: Churn Prevention Investment (CPI)
description: Calculates the optimal investment for preventing churn based on fan value and risk
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 39
---

# Definition

CPI = FLV \times \frac{RRF}{5} \times 0.1, \text{ suggesting investing up to 10\% of at-risk value, scaled according to churn risk level.}

# Depends on

* [Retention Risk Factor (RRF)](/knowledge/retention-risk-factor.md)
* [Fan Lifetime Value (FLV)](/knowledge/fan-lifetime-value.md)
