---
type: Calculation
title: Vendor Reliability Index (VRI)
description: Assesses vendor reliability based on security rating and contract status.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 6
---

# Definition

VRI = \text{VendSecRate value} \times \begin{cases} 1 & \text{if ContrState = 'Active'} \\ 0.5 & \text{otherwise} \end{cases}

# Columns used

* [vendormanagement](/tables/vendormanagement.md): `vendsecrate`, `contrstate`

# Used by

* [Vendor Risk Tier](/knowledge/vendor-risk-tier.md)
* [Vendor Risk Amplification (VRA)](/knowledge/vendor-risk-amplification.md)
* [Vendor Risk Concentration (VRC)](/knowledge/vendor-risk-concentration.md)
