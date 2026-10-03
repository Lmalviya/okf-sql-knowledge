---
type: Business Rule
title: High Social Support Patient
description: Identifies patients with strong social support and good relationship quality.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 16
---

# Definition

A patient with SSE \geq 5

# Depends on

* [Social Support Effectiveness (SSE)](/knowledge/social-support-effectiveness.md)
