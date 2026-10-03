---
type: Business Rule
title: Extreme Weather Readiness Status (EWRS)
description: A binary classification system that determines if equipment has met all necessary conditions to safely operate during extreme weather events.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 50
---

# Definition

Equipment is classified as 'Extreme Weather Ready' WHEN (SSF > 0.7) AND (heaterstatus != 'Off') AND (insulationstatus != 'Poor') AND (emergencylightstatus IN ('On', 'Testing')); OTHERWISE equipment is classified as 'Not Ready'. This evaluation combines structural integrity checks with essential operational systems status to determine immediate readiness for extreme weather exposure.

# Columns used

* [cabinenvironment](/tables/cabinenvironment.md): `heaterstatus`
* [thermalsolarwindandgrid](/tables/thermalsolarwindandgrid.md): `insulationstatus`
* [lightingandsafety](/tables/lightingandsafety.md): `emergencylightstatus`

# Depends on

* [Structural Safety Factor (SSF)](/knowledge/structural-safety-factor.md)
