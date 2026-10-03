---
type: Business Rule
title: Premium Service Candidate
description: Identifies fans who would benefit from and likely pay for enhanced support services
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 46
---

# Definition

A fan with SEI < 0.8, MV > 300, and supptix > 5, representing users who require substantial support and have demonstrated significant economic value.

# Columns used

* [supportandfeedback](/tables/supportandfeedback.md): `supptix`

# Depends on

* [Monetization Value (MV)](/knowledge/monetization-value.md)
* [Support Efficiency Index (SEI)](/knowledge/support-efficiency-index.md)
