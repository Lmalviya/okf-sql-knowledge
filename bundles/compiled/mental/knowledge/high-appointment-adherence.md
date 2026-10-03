---
type: Business Rule
title: High Appointment Adherence
description: Identifies patients with low missed appointment rates.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 19
---

# Definition

A patient with MAR < 1

# Depends on

* [Missed Appointment Rate (MAR)](/knowledge/missed-appointment-rate.md)
