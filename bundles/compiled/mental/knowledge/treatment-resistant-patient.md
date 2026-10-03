---
type: Business Rule
title: Treatment-Resistant Patient
description: Identifies patients with poor treatment response despite adherence.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 11
---

# Definition

A patient with txresp = Poor and txadh \in \{Medium, High\}

# Columns used

* [treatmentoutcomes](/tables/treatmentoutcomes.md): `txadh`, `txresp`
