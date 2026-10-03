---
type: Business Rule
title: Social Network Underutilizer
description: Identifies fans with large social networks but low conversion to platform activity
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 47
---

# Definition

A fan with follcount > 1000 but SCR < 0.5%, indicating a substantial but largely untapped potential for platform growth through their social connections.

# Depends on

* [Social Influence Multiplier (SIM)](/knowledge/social-influence-multiplier.md)
* [Social Conversion Rate (SCR)](/knowledge/social-conversion-rate.md)
