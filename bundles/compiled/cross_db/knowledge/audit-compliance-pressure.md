---
type: Calculation
title: Audit Compliance Pressure (ACP)
description: Quantifies pressure from audit findings and compliance remediation needs.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 57
---

# Definition

ACP = \text{ARL} \times \text{AFS}

# Depends on

* [Audit Finding Severity (AFS)](/knowledge/audit-finding-severity.md)
* [Audit Remediation Load (ARL)](/knowledge/audit-remediation-load.md)

# Used by

* [Audit-Stressed Data Flow](/knowledge/audit-stressed-data-flow.md)
* [High-Impact Audit Risk Flow](/knowledge/high-impact-audit-risk-flow.md)
* [High Audit Compliance Pressure](/knowledge/high-audit-compliance-pressure.md)
