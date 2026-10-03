---
type: Calculation
title: Bandwidth Risk Factor (BRF)
description: Evaluates risk from bandwidth overuse in sensitive data flows.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 37
---

# Definition

BRF = \text{BSI} \times \text{DSI}

# Depends on

* [Bandwidth Saturation Index (BSI)](/knowledge/bandwidth-saturation-index.md)
* [Data Sensitivity Index (DSI)](/knowledge/data-sensitivity-index.md)

# Used by

* [Bandwidth-Constrained Risk](/knowledge/bandwidth-constrained-risk.md)
* [Bandwidth Compliance Risk (BCR)](/knowledge/bandwidth-compliance-risk.md)
