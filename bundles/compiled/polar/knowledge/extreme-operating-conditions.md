---
type: Business Rule
title: Extreme Operating Conditions (EOC)
description: Defines the extreme environmental conditions under which equipment can safely operate
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 40
---

# Definition

Equipment is considered to 'operate safely under extreme conditions' when its SSF > 0.65 and ECAC > 0.8.

# Depends on

* [Structural Safety Factor (SSF)](/knowledge/structural-safety-factor.md)
* [Extreme Climate Adaptation Coefficient (ECAC)](/knowledge/extreme-climate-adaptation-coefficient.md)
