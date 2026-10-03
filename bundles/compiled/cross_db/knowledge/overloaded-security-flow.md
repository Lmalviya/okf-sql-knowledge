---
type: Business Rule
title: Overloaded Security Flow
description: Flags data flows with high security burden and compliance exposure.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 61
---

# Definition

A data flow where SPM < 1 and CBCE > 100

# Depends on

* [Security Posture Maturity (SPM)](/knowledge/security-posture-maturity.md)
* [Cross-Border Compliance Exposure (CBCE)](/knowledge/cross-border-compliance-exposure.md)
