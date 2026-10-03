---
type: Business Rule
title: Insecure High-Volume Flow
description: Identifies high-volume data flows with weak security controls.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 45
---

# Definition

A data flow where VolGB > 500 and SRS < 2

# Columns used

* [dataprofile](/tables/dataprofile.md): `volgb`

# Depends on

* [Security Robustness Score (SRS)](/knowledge/security-robustness-score.md)
* [DataProfile.VolGB](/knowledge/dataprofile-volgb.md)
