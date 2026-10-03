---
type: Business Rule
title: Cleaning Triggers
description: Combined conditions that determine when solar panel cleaning is economically justified.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 51
---

# Definition

A panel cleaning should be triggered when either: (1) meet Soiling Cleaning Threshold (2) >30 days since last cleaning—whichever occurs first.

# Depends on

* [Soiling Cleaning Threshold](/knowledge/soiling-cleaning-threshold.md)
