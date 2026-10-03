---
type: Business Rule
title: High-Risk Patient
description: Identifies patients with elevated suicide risk or severe symptoms.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 10
---

# Definition

A patient with suicrisk \in \{High, Severe\} or mental\_health\_scores['depression']['phq9\_score'] > 15 or mental\_health\_scores['anxiety']['gad7\_score'] > 15,

# Columns used

* [assessmentsymptomsandrisk](/tables/assessmentsymptomsandrisk.md): `suicrisk`
