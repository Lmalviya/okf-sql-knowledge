---
type: Calculation
title: Safety Incident Score (SIS)
description: Aggregates safety incidents from JSONB safety_metrics.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 34
---

# Definition

For a given robot R, SIS = \sum_{ps \in \text{performance_and_safety} \mid \text{effectivenessrobot = R}} (safety_metrics->>'overloads'::int + safety_metrics->>'collisions'::int + safety_metrics->>'emergency_stops'::int + safety_metrics->>'speed_violations'::int), \text{where JSONB fields are extracted and summed.}

# Columns used

* [performance_and_safety](/tables/performance_and_safety.md): `effectivenessrobot`, `safety_metrics`

# Used by

* [High Safety Concern](/knowledge/high-safety-concern.md)
