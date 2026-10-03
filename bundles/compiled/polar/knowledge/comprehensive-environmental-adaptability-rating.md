---
type: Business Rule
title: Comprehensive Environmental Adaptability Rating (CEAR)
description: Assesses the overall adaptability of equipment and systems to the polar environment
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 49
---

# Definition

Equipment and systems are rated as having 'Excellent Adaptability' (ECAC > 0.85 and SSF > 0.8 and thermalsolarwindandgrid.insulationstatus = 'Good'), 'Good Adaptability' (ECAC > 0.7 and SSF > 0.65 and thermalsolarwindandgrid.insulationstatus != 'Poor'), or 'Limited Adaptability' (other cases).

# Columns used

* [thermalsolarwindandgrid](/tables/thermalsolarwindandgrid.md): `insulationstatus`

# Depends on

* [Extreme Weather Readiness (EWR)](/knowledge/extreme-weather-readiness.md)
* [Extreme Climate Adaptation Coefficient (ECAC)](/knowledge/extreme-climate-adaptation-coefficient.md)
