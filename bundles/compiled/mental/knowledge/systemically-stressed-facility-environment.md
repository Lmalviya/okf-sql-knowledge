---
type: Business Rule
title: Systemically Stressed Facility Environment
description: Identifies facilities potentially facing overwhelming systemic stress, characterized by a significant gap between patient needs and resources, compounded by high patient attrition risk.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 59
---

# Definition

A facility where RDD > 1.0 AND meeting criteria for Facility Attrition Risk Indicator. \text{Combines a high Resource-Demand Differential (RDD) with indicators of high attrition risk.}

# Depends on

* [Resource-Demand Differential (RDD)](/knowledge/resource-demand-differential.md)
* [Facility Attrition Risk Indicator](/knowledge/facility-attrition-risk-indicator.md)
