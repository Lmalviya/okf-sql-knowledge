---
type: Business Rule
title: High Severity, High Risk Patient Group
description: Identifies patients presenting with both high symptom severity (depression/anxiety) and elevated suicide risk.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 49
---

# Definition

A patient where (mental_health_scores['depression']['phq9_score'] > 19 OR mental_health_scores['anxiety']['gad7_score'] > 14) AND suicrisk IN {'High', 'Severe'}.

# Columns used

* [assessmentsymptomsandrisk](/tables/assessmentsymptomsandrisk.md): `suicrisk`, `mental_health_scores`
