---
type: Business Rule
title: Quality Compromise
description: Identifies quality-compromised shipments.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 19
---

# Definition

A shipment where VVP < 30 or QualCheck='Failed'

# Columns used

* [shipments](/tables/shipments.md): `qualcheck`

# Depends on

* [Vaccine Viability Period (VVP)](/knowledge/vaccine-viability-period.md)
