---
type: Business Rule
title: Well-Resourced High-Support Environment
description: Identifies facilities that are well-resourced and serve a patient population with generally high levels of social support effectiveness.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 44
---

# Definition

A facility where FRAI \geq 2.0 and the average SSE \geq 4.5, \text{indicating high Facility Resource Adequacy Index (FRAI) and high average Social Support Effectiveness (SSE)}

# Depends on

* [Facility Resource Adequacy Index (FRAI)](/knowledge/facility-resource-adequacy-index.md)
* [Social Support Effectiveness (SSE)](/knowledge/social-support-effectiveness.md)
