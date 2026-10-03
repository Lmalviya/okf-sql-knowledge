---
type: Business Rule
title: High-Need, Under-Resourced Facility
description: Identifies facilities facing significant aggregate patient risk without adequate community resources.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 40
---

# Definition

A facility where FRPI > 4.5 and FRAI < 1.5, \text{indicating high Facility Risk Profile Index (FRPI) and low Facility Resource Adequacy Index (FRAI)}

# Depends on

* [Facility Risk Profile Index (FRPI)](/knowledge/facility-risk-profile-index.md)
* [Facility Resource Adequacy Index (FRAI)](/knowledge/facility-resource-adequacy-index.md)
