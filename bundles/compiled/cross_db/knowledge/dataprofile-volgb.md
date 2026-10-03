---
type: Value Illustration
title: DataProfile.VolGB
description: Illustrates the volume of data in gigabytes.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 22
---

# Definition

Ranges from 0 to millions. A VolGB of 1000 might represent a large dataset, while 0.1 is typical for small logs, from DataProfile.

# Columns used

* [dataprofile](/tables/dataprofile.md): `volgb`

# Used by

* [Cross-Border Data Volume Risk (CDVR)](/knowledge/cross-border-data-volume-risk.md)
* [Insecure High-Volume Flow](/knowledge/insecure-high-volume-flow.md)
