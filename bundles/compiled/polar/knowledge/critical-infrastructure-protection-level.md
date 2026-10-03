---
type: Business Rule
title: Critical Infrastructure Protection Level (CIPL)
description: Determines the protection level for polar critical infrastructure
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 46
---

# Definition

Infrastructure is assigned protection level 'A' (SSF > 0.8, LOSS > 0.85, and OSPI > 0.9), 'B' (SSF > 0.7, LOSS > 0.75, and OSPI > 0.8), or 'C' (other cases).

# Depends on

* [Structural Safety Factor (SSF)](/knowledge/structural-safety-factor.md)
* [Overall Safety Performance Index (OSPI)](/knowledge/overall-safety-performance-index.md)
* [Long-term Operational Stability Score (LOSS)](/knowledge/long-term-operational-stability-score.md)
