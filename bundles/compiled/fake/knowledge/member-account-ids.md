---
type: Calculation
title: member account IDs
description: A collection (array) of the unique account indexes belonging to an identified cluster.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 83
---

# Definition

\{ \text{accindex}_a \mid a \in cluster C \}

# Columns used

* [account](/tables/account.md): `accindex`

# Depends on

* [cluster identifier](/knowledge/cluster-identifier.md)
