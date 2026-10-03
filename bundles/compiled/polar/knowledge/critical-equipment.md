---
type: Business Rule
title: Critical Equipment
description: Identifies equipment that is essential for life support and safety in polar environments.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 11
---

# Definition

Equipment is designated as 'Critical' if it belongs to the 'Safety' equipment type, has a safety index > 0.8, and is associated with any of these life-critical systems: lifesupportstatus, oxygensupplystatus, or heater systems where temperatures are below freezing (externaltemperaturec < 0).

# Columns used

* [weatherandstructure](/tables/weatherandstructure.md): `externaltemperaturec`
* [lightingandsafety](/tables/lightingandsafety.md): `lifesupportstatus`, `oxygensupplystatus`
