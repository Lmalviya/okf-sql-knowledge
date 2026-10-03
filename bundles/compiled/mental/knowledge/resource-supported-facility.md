---
type: Business Rule
title: Resource-Supported Facility
description: Identifies facilities with adequate or comprehensive community resources.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 15
---

# Definition

A facility with resource_score \geq 2 \text{where } resource_score = \begin{cases} 3 & \text{if } support\_and\_resources['community\_resources'] = Comprehensive \\ 2 & \text{if } support\_and\_resources['community\_resources'] = Adequate \\ 1 & \text{if } support\_and\_resources['community\_resources'] = Limited \end{cases}.

# Depends on

* [Facility Resource Adequacy Index (FRAI)](/knowledge/facility-resource-adequacy-index.md)
