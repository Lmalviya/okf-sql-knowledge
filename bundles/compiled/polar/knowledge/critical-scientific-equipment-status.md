---
type: Business Rule
title: Critical Scientific Equipment Status (CSES)
description: Determines the operational status and reliability of critical scientific equipment
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 43
---

# Definition

Scientific equipment is classified as 'Fully Operational' (SER > 0.9 and SMSP > 0.85), 'Degraded Operation' (SER > 0.7 and SMSP > 0.6), or 'Needs Repair' (other cases).

# Depends on

* [Scientific Equipment Reliability (SER)](/knowledge/scientific-equipment-reliability.md)
* [Scientific Mission Success Probability (SMSP)](/knowledge/scientific-mission-success-probability.md)
