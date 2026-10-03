---
type: Business Rule
title: Extreme Weather Readiness (EWR)
description: Evaluates how prepared equipment and structures are for extreme weather conditions.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 10
---

# Definition

A composite rating where equipment is considered 'Extreme Weather Ready' if it maintains an SSF > 0.7 and has operational heating systems (heaterstatus not 'Off'), proper insulation (insulationstatus not 'Poor'), and functional emergency systems (emergencylightstatus = 'On' or 'Testing').

# Columns used

* [cabinenvironment](/tables/cabinenvironment.md): `heaterstatus`
* [thermalsolarwindandgrid](/tables/thermalsolarwindandgrid.md): `insulationstatus`
* [lightingandsafety](/tables/lightingandsafety.md): `emergencylightstatus`

# Depends on

* [Structural Safety Factor (SSF)](/knowledge/structural-safety-factor.md)

# Used by

* [Comprehensive Environmental Adaptability Rating (CEAR)](/knowledge/comprehensive-environmental-adaptability-rating.md)
