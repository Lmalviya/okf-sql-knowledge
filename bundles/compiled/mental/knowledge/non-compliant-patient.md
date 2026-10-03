---
type: Business Rule
title: Non-Compliant Patient
description: Identifies patients with consistent non-compliance in treatment.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 18
---

# Definition

A patient with txadh = Non-compliant and medadh = Non-compliant

# Columns used

* [treatmentbasics](/tables/treatmentbasics.md): `medadh`
* [treatmentoutcomes](/tables/treatmentoutcomes.md): `txadh`
