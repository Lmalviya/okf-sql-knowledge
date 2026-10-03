---
type: Calculation
title: Vendor Risk Concentration (VRC)
description: Assesses the concentration of risk from a vendor’s compliance and security issues.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 53
---

# Definition

VRC = \text{VRA} \times (1 - \text{VRI})

# Depends on

* [Vendor Reliability Index (VRI)](/knowledge/vendor-reliability-index.md)
* [Vendor Risk Amplification (VRA)](/knowledge/vendor-risk-amplification.md)

# Used by

* [Vendor Compliance Risk Cluster](/knowledge/vendor-compliance-risk-cluster.md)
