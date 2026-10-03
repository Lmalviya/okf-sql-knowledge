---
type: Business Rule
title: Warranty Claim Threshold
description: Criteria for when warranty claims should be initiated based on performance degradation.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 17
---

# Definition

A warranty claim should be considered when a panel's Energy Production Efficiency falls more than 10% below the manufacturer's warranty curve for its age, with at least three consecutive measurements confirming the underperformance.

# Depends on

* [Energy Production Efficiency (EPE)](/knowledge/energy-production-efficiency.md)

# Used by

* [End-of-Warranty Optimization](/knowledge/end-of-warranty-optimization.md)
