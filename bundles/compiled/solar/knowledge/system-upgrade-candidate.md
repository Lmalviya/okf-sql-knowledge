---
type: Business Rule
title: System Upgrade Candidate
description: Identifies plants that would benefit most from component upgrades.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 46
---

# Definition

A plant qualifies as an upgrade candidate when the Financial Impact of Degradation exceeds 10% of replacement cost and Effective Performance Index is below 0.85 for three consecutive months.

# Depends on

* [Effective Performance Index (EPI)](/knowledge/effective-performance-index.md)
* [Financial Impact of Degradation (FID)](/knowledge/financial-impact-of-degradation.md)
