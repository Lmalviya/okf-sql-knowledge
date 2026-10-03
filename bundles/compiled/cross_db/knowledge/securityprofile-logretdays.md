---
type: Value Illustration
title: SecurityProfile.LogRetDays
description: Illustrates the retention period for audit logs.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 29
---

# Definition

Integer ≥ 0 days. A LogRetDays of 365 meets many compliance needs, while <30 may violate regulations, from SecurityProfile.

# Columns used

* [securityprofile](/tables/securityprofile.md): `logretdays`

# Used by

* [Security Posture Maturity (SPM)](/knowledge/security-posture-maturity.md)
