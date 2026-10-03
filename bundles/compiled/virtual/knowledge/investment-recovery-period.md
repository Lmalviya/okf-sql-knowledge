---
type: Calculation
title: Investment Recovery Period (IRP)
description: Estimates how many months it will take to recover platform investment in a fan
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 32
---

# Definition

IRP = \frac{supptix \times 30}{MV \times (1 - \frac{RRF}{10})}, \text{ where supptix represents support tickets as a proxy for platform resources invested in the fan.}

# Columns used

* [supportandfeedback](/tables/supportandfeedback.md): `supptix`

# Depends on

* [Monetization Value (MV)](/knowledge/monetization-value.md)
* [Retention Risk Factor (RRF)](/knowledge/retention-risk-factor.md)
