---
type: Value Illustration
title: lastmilestatus
description: Illustrates the state of final delivery operations to affected populations
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 3
---

# Definition

On Track indicates deliveries proceeding as scheduled, Delayed shows deliveries facing non-critical setbacks, and Suspended means deliveries have temporarily halted due to severe constraints

# Columns used

* [transportation](/tables/transportation.md): `lastmilestatus`

# Used by

* [Logistics Breakdown](/knowledge/logistics-breakdown.md)
