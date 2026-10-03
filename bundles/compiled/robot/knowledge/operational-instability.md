---
type: Business Rule
title: Operational Instability
description: Identifies robots with unstable joint performance.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 48
---

# Definition

A robot R has Operational Instability if JTV > 50 and MJT > 60.

# Depends on

* [Joint Torque Variance (JTV)](/knowledge/joint-torque-variance.md)
* [Maximum Joint Temperature (MJT)](/knowledge/maximum-joint-temperature.md)
