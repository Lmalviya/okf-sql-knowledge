---
type: Calculation
title: Maintenance Return on Investment (MROI)
description: Evaluates the financial return of maintenance activities.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 32
---

# Definition

MROI = RLR / MCE, where RLR is the Revenue Loss Rate and MCE is the Maintenance Cost Efficiency. Higher values indicate better return on maintenance investments.

# Depends on

* [Maintenance Cost Efficiency (MCE)](/knowledge/maintenance-cost-efficiency.md)
* [Revenue Loss Rate (RLR)](/knowledge/revenue-loss-rate.md)

# Used by

* [Premium Maintenance Candidate](/knowledge/premium-maintenance-candidate.md)
* [Total Economic Performance](/knowledge/total-economic-performance.md)
* [Maintenance Urgency Classification](/knowledge/maintenance-urgency-classification.md)
