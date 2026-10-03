---
type: Calculation
title: Security Robustness Score (SRS)
description: Measures the strength of security controls based on encryption and access controls.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 5
---

# Definition

SRS = \begin{cases} 3 & \text{if EncState = 'Full' and AclState = 'Strong'} \\ 2 & \text{if EncState = 'Full' or AclState = 'Adequate'} \\ 1 & \text{otherwise} \end{cases}

# Columns used

* [securityprofile](/tables/securityprofile.md): `encstate`, `aclstate`

# Used by

* [Secure Data Flow](/knowledge/secure-data-flow.md)
* [Sensitive Data Exposure](/knowledge/sensitive-data-exposure.md)
* [Security Control Cost Ratio (SCCR)](/knowledge/security-control-cost-ratio.md)
* [Encryption Coverage Ratio (ECR)](/knowledge/encryption-coverage-ratio.md)
* [Insecure High-Volume Flow](/knowledge/insecure-high-volume-flow.md)
