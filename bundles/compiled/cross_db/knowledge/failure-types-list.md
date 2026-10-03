---
type: Business Rule
title: Failure Types List
description: Concatenates the types of integrity failures for a data profile into a single string.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 73
---

# Definition

A comma-separated string listing failure types: 'Integrity Check' if IntCheck = 'Failed', 'Checksum Verification' if CsumVerify = 'Failed'.

# Columns used

* [dataprofile](/tables/dataprofile.md): `intcheck`, `csumverify`
