---
type: Business Rule
title: Stale Treatment Outcome Records
description: Treatment outcome records associated with encounters that occurred before a specific time threshold (e.g., older than 60 days).
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 62
---

# Definition

Records in the `treatmentoutcomes` table where the `timemark` of the linked encounter in the `encounters` table is older than a defined interval (e.g., 60 days).

# Columns used

* [encounters](/tables/encounters.md): `timemark`
