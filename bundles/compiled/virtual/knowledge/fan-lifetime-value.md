---
type: Calculation
title: Fan Lifetime Value (FLV)
description: Projects the total economic value of a fan throughout their relationship with the platform
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 16
---

# Definition

FLV = MV \times \left(1 - \frac{RRF}{10}\right) \times (1 + FEI) \times 24, \text{ estimating 24-month value adjusted by retention risk and engagement level.}

# Depends on

* [Fan Engagement Index (FEI)](/knowledge/fan-engagement-index.md)
* [Monetization Value (MV)](/knowledge/monetization-value.md)
* [Retention Risk Factor (RRF)](/knowledge/retention-risk-factor.md)

# Used by

* [Event ROI Potential (ERP)](/knowledge/event-roi-potential.md)
* [Support Efficiency Index (SEI)](/knowledge/support-efficiency-index.md)
* [Churn Prevention Investment (CPI)](/knowledge/churn-prevention-investment.md)
* [Fan Value Segmentation](/knowledge/fan-value-segmentation.md)
