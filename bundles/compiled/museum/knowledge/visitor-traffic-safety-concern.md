---
type: Business Rule
title: Visitor Traffic Safety Concern
description: Identifies situations where visitor traffic poses safety concerns for exhibitions.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 49
---

# Definition

Occurs when VCSF > 2 AND there is a Visitor Crowd Risk situation.

# Depends on

* [Visitor Capacity Safety Factor (VCSF)](/knowledge/visitor-capacity-safety-factor.md)
* [Visitor Crowd Risk](/knowledge/visitor-crowd-risk.md)
