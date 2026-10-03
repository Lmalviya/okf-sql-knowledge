---
type: Business Rule
title: Depletion Rank
description: Ranks containers based on the rate of coolant depletion.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 62
---

# Definition

Rank assigned to containers based on descending order of CDR

# Depends on

* [Coolant Depletion Rate (CDR)](/knowledge/coolant-depletion-rate.md)
