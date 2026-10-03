---
type: Calculation
title: Risk Exposure Score (RES)
description: Calculates the overall risk exposure by combining risk assessment and residual risk.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 2
---

# Definition

RES = \text{RiskAssess} \times \text{CtrlEff}^{-1}

# Columns used

* [riskmanagement](/tables/riskmanagement.md): `riskassess`, `ctrleff`

# Used by

* [Cross-Border Risk Factor (CBRF)](/knowledge/cross-border-risk-factor.md)
* [High-Risk Data Flow](/knowledge/high-risk-data-flow.md)
* [Vendor Risk Amplification (VRA)](/knowledge/vendor-risk-amplification.md)
* [Critical Data Flow Risk](/knowledge/critical-data-flow-risk.md)
* [Bandwidth-Constrained Risk](/knowledge/bandwidth-constrained-risk.md)
* [Incident Impact Factor (IIF)](/knowledge/incident-impact-factor.md)
