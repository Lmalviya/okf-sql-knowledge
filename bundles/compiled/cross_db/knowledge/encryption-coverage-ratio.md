---
type: Calculation
title: Encryption Coverage Ratio (ECR)
description: Measures the extent of encryption coverage relative to data sensitivity.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 35
---

# Definition

ECR = \text{SRS} \times \text{DSI}

# Depends on

* [Data Sensitivity Index (DSI)](/knowledge/data-sensitivity-index.md)
* [Security Robustness Score (SRS)](/knowledge/security-robustness-score.md)

# Used by

* [Unprotected Sensitive Data](/knowledge/unprotected-sensitive-data.md)
* [Security Posture Maturity (SPM)](/knowledge/security-posture-maturity.md)
