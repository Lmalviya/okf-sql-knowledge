---
type: Value Illustration
title: hazlevel
description: Illustrates the severity classification of disaster events
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 0
---

# Definition

Level 1 represents minimal threat, Level 2 indicates moderate danger, Level 3 shows significant hazard, Level 4 denotes severe emergency situation, and Level 5 signifies catastrophic conditions requiring maximum response

# Columns used

* [disasterevents](/tables/disasterevents.md): `hazlevel`

# Used by

* [Health System Capacity Index (HSCI)](/knowledge/health-system-capacity-index.md)
