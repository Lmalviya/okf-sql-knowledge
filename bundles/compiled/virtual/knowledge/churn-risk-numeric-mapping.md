---
type: Value Illustration
title: Churn Risk Numeric Mapping
description: Converts the churn risk enum values to numeric form for analytical calculations
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 52
---

# Definition

Transforms the churnflag enum values into numeric equivalents for use in calculations and risk models: 'None' maps to 0 (representing minimal risk), 'Low' maps to 1 (representing slight risk), 'Medium' maps to 2 (representing moderate risk), and 'High' maps to 3 (representing severe risk). This numeric mapping enables mathematical operations in retention analysis formulas, especially for the Retention Risk Factor (RRF) calculation.

# Columns used

* [retentionandinfluence](/tables/retentionandinfluence.md): `churnflag`

# Depends on

* [retentionandinfluence.churnflag](/knowledge/retentionandinfluence-churnflag.md)

# Used by

* [Retention Risk Factor (RRF)](/knowledge/retention-risk-factor.md)
