---
type: Calculation
title: Audit Remediation Load (ARL)
description: Calculates the workload required for audit remediation based on findings and compliance gaps.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 36
---

# Definition

ARL = \text{AFS} \times \text{DSRL}

# Depends on

* [Audit Finding Severity (AFS)](/knowledge/audit-finding-severity.md)
* [Data Subject Request Load (DSRL)](/knowledge/data-subject-request-load.md)
* [Compliance.GdprComp](/knowledge/compliance-gdprcomp.md)

# Used by

* [Overburdened Compliance Flow](/knowledge/overburdened-compliance-flow.md)
* [Audit Compliance Pressure (ACP)](/knowledge/audit-compliance-pressure.md)
