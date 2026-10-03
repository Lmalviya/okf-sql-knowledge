---
type: Calculation
title: Security Posture Maturity (SPM)
description: Evaluates the maturity of security controls based on encryption and audit log retention.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 52
---

# Definition

SPM = \text{ECR} \times \frac{\text{LogRetDays}}{365}

# Columns used

* [securityprofile](/tables/securityprofile.md): `logretdays`

# Depends on

* [SecurityProfile.LogRetDays](/knowledge/securityprofile-logretdays.md)
* [Encryption Coverage Ratio (ECR)](/knowledge/encryption-coverage-ratio.md)

# Used by

* [Overloaded Security Flow](/knowledge/overloaded-security-flow.md)
