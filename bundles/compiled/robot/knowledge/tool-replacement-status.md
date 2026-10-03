---
type: Business Rule
title: Tool Replacement Status
description: Classifies robots into tool replacement priority categories based on tool wear rate and program cycles
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 47
---

# Definition

For a robot R, the Tool Replacement Status is:
- 'URGENT' if TWR > 0.001 AND TPC > 10000
- 'WARNING' if TWR > 0.0005 OR average tool wear percentage > 75
- 'NORMAL' otherwise

# Depends on

* [Tool Wear Rate (TWR)](/knowledge/tool-wear-rate.md)
* [Total Program Cycles (TPC)](/knowledge/total-program-cycles.md)
