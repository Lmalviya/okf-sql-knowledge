---
type: Business Rule
title: Equipment Problems
description: Defines what counts as an abnormal condition for a telescope’s subsystems.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 55
---

# Definition

A telescope is considered to have an equipment problem whenever **any** of its key subsystem states are not in their nominal condition: • Equipment status is not “Operational”; • Calibration status is not “Current”; • Cooling-system status is not “Normal”.
