---
type: Business Rule
title: High Safety Concern
description: Flags robots with significant safety incidents.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 44
---

# Definition

A robot R has High Safety Concern if SIS > 20.

# Depends on

* [Safety Incident Score (SIS)](/knowledge/safety-incident-score.md)
