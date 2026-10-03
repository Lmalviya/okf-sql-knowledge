---
type: Value Illustration
title: Compliance.GdprComp
description: Illustrates GDPR compliance status.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 25
---

# Definition

Enum: 'Compliant', 'Non-compliant', 'Partial'. 'Compliant' meets all GDPR rules, 'Non-compliant' fails key requirements, from Compliance.

# Columns used

* [compliance](/tables/compliance.md): `gdprcomp`

# Used by

* [Audit Remediation Load (ARL)](/knowledge/audit-remediation-load.md)
* [Regulatory Overload Flow](/knowledge/regulatory-overload-flow.md)
* [Cross-Border Compliance Exposure (CBCE)](/knowledge/cross-border-compliance-exposure.md)
* [Bandwidth Compliance Risk (BCR)](/knowledge/bandwidth-compliance-risk.md)
* [Incident-Prone Compliance Flow](/knowledge/incident-prone-compliance-flow.md)
