---
type: Calculation
title: maximum coordination score
description: The highest coordination score observed among the members of an identified cluster.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 82
---

# Definition

\max_{a \in cluster C} (\text{coordscore}_a)

# Columns used

* [moderationaction](/tables/moderationaction.md): `coordscore`

# Depends on

* [cluster identifier](/knowledge/cluster-identifier.md)
