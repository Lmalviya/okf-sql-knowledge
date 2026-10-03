---
type: Business Rule
title: Declining Credit Health
description: Identifies customers with deteriorating credit health requiring intervention.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 47
---

# Definition

A customer with negative CHM (Credit Health Momentum < 0), increasing CRI (Credit Risk Intensity growing by >10% in 6 months), and rising DTI (Debt-to-Income Ratio increasing by >5% in 6 months).

# Depends on

* [Debt-to-Income Ratio (DTI)](/knowledge/debt-to-income-ratio.md)
* [Credit Risk Intensity (CRI)](/knowledge/credit-risk-intensity.md)
* [Credit Health Momentum (CHM)](/knowledge/credit-health-momentum.md)
