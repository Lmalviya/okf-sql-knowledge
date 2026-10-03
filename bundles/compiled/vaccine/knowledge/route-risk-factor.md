---
type: Calculation
title: Route Risk Factor (RRF)
description: Comprehensive route risk assessment.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 38
---

# Definition

RRF = (1 - \frac{	ext{RCP}}{100}) \times \text{TRS} \times (1 - \text{CEI})

# Depends on

* [Route Completion Percentage (RCP)](/knowledge/route-completion-percentage.md)
* [Total Risk Score (TRS)](/knowledge/total-risk-score.md)
* [Coolant Efficiency Index (CEI)](/knowledge/coolant-efficiency-index.md)

# Used by

* [Critical Route Status](/knowledge/critical-route-status.md)
* [Transport Safety Alert](/knowledge/transport-safety-alert.md)
