---
type: Business Rule
title: High-Impact Audit Risk Flow
description: Identifies data flows with severe audit findings and regulatory risks.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 69
---

# Definition

A data flow where Regulatory Risk Exposure exists and ACP > 5

# Depends on

* [Regulatory Risk Exposure](/knowledge/regulatory-risk-exposure.md)
* [Audit Compliance Pressure (ACP)](/knowledge/audit-compliance-pressure.md)
