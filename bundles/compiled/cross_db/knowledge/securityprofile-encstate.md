---
type: Value Illustration
title: SecurityProfile.EncState
description: Illustrates the encryption status of data.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 23
---

# Definition

Enum: 'Full', 'Partial'. 'Full' indicates all data is encrypted, while 'Partial' suggests gaps, from SecurityProfile.

# Columns used

* [securityprofile](/tables/securityprofile.md): `encstate`
