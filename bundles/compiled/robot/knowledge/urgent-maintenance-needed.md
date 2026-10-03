---
type: Business Rule
title: Urgent Maintenance Needed
description: Indicates if urgent maintenance is needed based on minimum Remaining Useful Life.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 16
---

# Definition

Urgent maintenance is needed if MRUL < 100.

# Depends on

* [Minimum Remaining Useful Life (MRUL)](/knowledge/minimum-remaining-useful-life.md)
