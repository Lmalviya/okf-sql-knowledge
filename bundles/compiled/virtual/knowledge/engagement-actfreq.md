---
type: Value Illustration
title: engagement.actfreq
description: Analyzes the significance of interaction frequency for fan classification
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 4
---

# Definition

'Daily' users log into the platform at least once per day on average; 'Weekly' users log in 3-5 times per week; 'Monthly' users log in 1-2 times per month; 'Occasional' users have login intervals exceeding one month. Interaction frequency affects platform push priority, content recommendations, and event invitations, with Daily users considered the platform's core active group.

# Columns used

* [engagement](/tables/engagement.md): `actfreq`
