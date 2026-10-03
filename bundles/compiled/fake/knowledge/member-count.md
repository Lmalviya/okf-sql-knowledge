---
type: Calculation
title: member count
description: The total number of unique accounts within an identified cluster.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 81
---

# Definition

Calculated using COUNT(DISTINCT account_index) for accounts grouped by the cluster identifier.

# Depends on

* [cluster identifier](/knowledge/cluster-identifier.md)
