---
type: Business Rule
title: Transfer Path
description: Describes the data flow path from origin to destination nation.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 70
---

# Definition

A string concatenating OrigNation and DestNation as 'OrigNation -> DestNation'

# Columns used

* [dataflow](/tables/dataflow.md): `orignation`, `destnation`
