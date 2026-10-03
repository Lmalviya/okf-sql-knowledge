---
type: Business Rule
title: Risk Rank
description: Ranks containers based on their risk level.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 64
---

# Definition

Rank assigned to containers based on descending order of CRI

# Depends on

* [Container Risk Index (CRI)](/knowledge/container-risk-index.md)
