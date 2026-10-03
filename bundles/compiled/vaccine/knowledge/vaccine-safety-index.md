---
type: Calculation
title: Vaccine Safety Index (VSI)
description: Overall safety index for vaccine shipment.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 39
---

# Definition

VSI = \frac{	ext{VVP}}{365} \times \text{CEI} \times (1 - \text{TRS})

# Depends on

* [Vaccine Viability Period (VVP)](/knowledge/vaccine-viability-period.md)
* [Coolant Efficiency Index (CEI)](/knowledge/coolant-efficiency-index.md)
* [Total Risk Score (TRS)](/knowledge/total-risk-score.md)

# Used by

* [Unsafe Vaccine Condition](/knowledge/unsafe-vaccine-condition.md)
* [Quality Alert Status](/knowledge/quality-alert-status.md)
* [Critical Safety Condition](/knowledge/critical-safety-condition.md)
* [Compound Quality Risk](/knowledge/compound-quality-risk.md)
