---
type: Business Rule
title: Sustainable Energy Operation
description: Defines the conditions for energy-sustainable operations in polar environments.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 19
---

# Definition

An operation is considered 'Energy-Sustainable' when it maintains a REC above 70% (meaning more than 70% of energy comes from renewable sources) while maintaining full operational capability and adequate power reserves for at least 48 hours in case of emergency.

# Depends on

* [Renewable Energy Contribution (REC)](/knowledge/renewable-energy-contribution.md)

# Used by

* [Energy Sustainability Classification System (ESCS)](/knowledge/energy-sustainability-classification-system.md)
