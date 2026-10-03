---
type: Calculation
title: Beneficiary Satisfaction Index (BSI)
description: Measures the satisfaction level of aid recipients
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 19
---

# Definition

BSI = benefeedbackscore \times 10 + (commengage\_numeric \times 20) + distequityidx \times 50, \text{ where commengage\_numeric maps Low=1, Medium=2, High=3}

# Columns used

* [beneficiariesandassessments](/tables/beneficiariesandassessments.md): `distequityidx`, `benefeedbackscore`

# Used by

* [Community Resilience Builder](/knowledge/community-resilience-builder.md)
* [Community Engagement Effectiveness (CEE)](/knowledge/community-engagement-effectiveness.md)
