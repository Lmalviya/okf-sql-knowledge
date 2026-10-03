---
type: Calculation
title: Vendor Security Cost Index (VSCI)
description: Evaluates the cost-effectiveness of vendor security relative to compliance burden.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 59
---

# Definition

VSCI = \text{VCB} / (\text{SCCR} + 1)

# Depends on

* [Security Control Cost Ratio (SCCR)](/knowledge/security-control-cost-ratio.md)
* [Vendor Compliance Burden (VCB)](/knowledge/vendor-compliance-burden.md)

# Used by

* [Costly Vendor Risk Flow](/knowledge/costly-vendor-risk-flow.md)
