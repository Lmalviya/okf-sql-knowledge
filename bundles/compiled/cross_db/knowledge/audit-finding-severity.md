---
type: Calculation
title: Audit Finding Severity (AFS)
description: Quantifies the severity of audit findings based on critical findings.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 7
---

# Definition

AFS = \frac{\text{CritFindNum}}{\text{FindTally} + 1}

# Columns used

* [auditandcompliance](/tables/auditandcompliance.md): `findtally`, `critfindnum`

# Used by

* [Critical Audit Issue](/knowledge/critical-audit-issue.md)
* [Vendor Compliance Burden (VCB)](/knowledge/vendor-compliance-burden.md)
* [Audit Remediation Load (ARL)](/knowledge/audit-remediation-load.md)
* [Cross-Border Audit Risk](/knowledge/cross-border-audit-risk.md)
* [Audit Compliance Pressure (ACP)](/knowledge/audit-compliance-pressure.md)
