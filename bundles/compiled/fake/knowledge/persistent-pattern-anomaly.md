---
type: Business Rule
title: Persistent Pattern Anomaly
description: Identifies sustained abnormal behavior patterns.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 69
---

# Definition

A Behavioral Pattern Anomaly that persists for over 30 days and maintains high TPDS

# Depends on

* [Behavioral Pattern Anomaly](/knowledge/behavioral-pattern-anomaly.md)
* [Temporal Pattern Deviation Score (TPDS)](/knowledge/temporal-pattern-deviation-score.md)
