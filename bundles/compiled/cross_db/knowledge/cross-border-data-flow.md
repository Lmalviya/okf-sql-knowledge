---
type: Business Rule
title: Cross-Border Data Flow
description: Identifies data flows where the origin and destination nations differ.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 75
---

# Definition

A data flow where OrigNation != DestNation

# Columns used

* [dataflow](/tables/dataflow.md): `orignation`, `destnation`
