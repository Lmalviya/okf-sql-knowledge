---
type: Business Rule
title: Critical Safety Condition
description: Identifies critically unsafe overall conditions.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 49
---

# Definition

A condition where VSI < 0.3 and TSR < 0.4

# Depends on

* [Vaccine Safety Index (VSI)](/knowledge/vaccine-safety-index.md)
* [Transport Safety Rating (TSR)](/knowledge/transport-safety-rating.md)
