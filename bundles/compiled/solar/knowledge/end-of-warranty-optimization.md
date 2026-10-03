---
type: Business Rule
title: End-of-Warranty Optimization
description: Strategy for optimizing panel replacements near warranty expiration.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 44
---

# Definition

Panels should be evaluated for warranty claims when approaching warranty expiration if their Normalized Degradation Index exceeds 0.9 or if they fail to meet the Warranty Claim Threshold criteria.

# Depends on

* [Warranty Claim Threshold](/knowledge/warranty-claim-threshold.md)
* [Normalized Degradation Index (NDI)](/knowledge/normalized-degradation-index.md)
