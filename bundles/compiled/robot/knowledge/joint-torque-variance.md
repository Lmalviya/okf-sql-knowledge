---
type: Calculation
title: Joint Torque Variance (JTV)
description: Calculates the variance of joint torques to assess operational stability.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 38
---

# Definition

For a given robot R, JTV = \frac{\sum_{jp \in \text{joint_performance} \mid \text{jperfdetref = R}} \sum_{i=1}^6 ((joint_metrics->>'jointi'->>'torque'::float - \mu_i)^2)}{\text{|}\{jp \in \text{joint_performance} \mid \text{jperfdetref = R}\}| \cdot 6}, \text{where } \mu_i = \frac{\sum_{jp} joint_metrics->>'jointi'->>'torque'::float}{\text{|}\{jp\}|}, \text{and jointi is joint i's metrics.}

# Columns used

* [joint_performance](/tables/joint_performance.md): `jperfdetref`, `joint_metrics`

# Used by

* [Operational Instability](/knowledge/operational-instability.md)
