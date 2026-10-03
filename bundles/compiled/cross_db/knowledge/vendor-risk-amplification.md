---
type: Calculation
title: Vendor Risk Amplification (VRA)
description: Quantifies how vendor issues amplify overall risk exposure.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 38
---

# Definition

VRA = \text{VRI} \times \text{RES}

# Depends on

* [Risk Exposure Score (RES)](/knowledge/risk-exposure-score.md)
* [Vendor Reliability Index (VRI)](/knowledge/vendor-reliability-index.md)

# Used by

* [Vendor-Driven Risk Flow](/knowledge/vendor-driven-risk-flow.md)
* [Vendor Risk Concentration (VRC)](/knowledge/vendor-risk-concentration.md)
* [Costly Vendor Risk Flow](/knowledge/costly-vendor-risk-flow.md)
