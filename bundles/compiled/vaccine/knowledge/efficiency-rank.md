---
type: Business Rule
title: Efficiency Rank
description: Ranks containers based on their storage efficiency.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 63
---

# Definition

Rank assigned to containers based on descending order of SER

# Depends on

* [Storage Efficiency Ratio (SER)](/knowledge/storage-efficiency-ratio.md)
