---
type: Business Rule
title: Critical Transport Condition
description: Identifies critically unsafe transport conditions.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 40
---

# Definition

A transport condition where TSR < 0.4 and TRS > 0.6

# Depends on

* [Transport Safety Rating (TSR)](/knowledge/transport-safety-rating.md)
* [Total Risk Score (TRS)](/knowledge/total-risk-score.md)
