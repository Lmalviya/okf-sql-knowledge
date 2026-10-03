---
type: Calculation
title: Integrity Failure Count (IFC)
description: Counts the number of failed integrity checks per data profile.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 72
---

# Definition

IFC = \begin{cases} 1 & \text{if IntCheck = 'Failed'} \\ 0 & \text{otherwise} \end{cases} + \begin{cases} 1 & \text{if CsumVerify = 'Failed'} \\ 0 & \text{otherwise} \end{cases}

# Columns used

* [dataprofile](/tables/dataprofile.md): `intcheck`, `csumverify`
