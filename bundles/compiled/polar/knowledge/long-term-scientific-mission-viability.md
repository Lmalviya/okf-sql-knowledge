---
type: Business Rule
title: Long-term Scientific Mission Viability (LSMV)
description: Assesses the viability of long-term scientific missions under polar conditions
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 47
---

# Definition

Scientific missions are assessed as 'long-term viable' when all involved scientific equipment maintains SMSP > 0.8 and overall site operations maintain CORI > 0.75, with calibrationstatus = 'Valid' and dataloggingstatus = 'Active'.

# Columns used

* [scientific](/tables/scientific.md): `dataloggingstatus`, `calibrationstatus`

# Depends on

* [Scientific Mission Success Probability (SMSP)](/knowledge/scientific-mission-success-probability.md)
* [Comprehensive Operational Reliability Indicator (CORI)](/knowledge/comprehensive-operational-reliability-indicator.md)
