---
type: Business Rule
title: Premium Maintenance Candidate
description: Identifies panels that would benefit most from premium maintenance services.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 41
---

# Definition

A panel is considered a premium maintenance candidate when its Maintenance Return on Investment exceeds 2.0 and its Energy Production Efficiency is below 90% but above 75%.

# Depends on

* [Energy Production Efficiency (EPE)](/knowledge/energy-production-efficiency.md)
* [Maintenance Return on Investment (MROI)](/knowledge/maintenance-return-on-investment.md)
