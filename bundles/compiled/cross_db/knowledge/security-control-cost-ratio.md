---
type: Calculation
title: Security Control Cost Ratio (SCCR)
description: Evaluates the cost-effectiveness of security controls relative to compliance costs.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 31
---

# Definition

SCCR = \text{SRS} / (\text{CostUSD} + 1)

# Columns used

* [riskmanagement](/tables/riskmanagement.md): `costusd`

# Depends on

* [Security Robustness Score (SRS)](/knowledge/security-robustness-score.md)

# Used by

* [Vendor Security Cost Index (VSCI)](/knowledge/vendor-security-cost-index.md)
