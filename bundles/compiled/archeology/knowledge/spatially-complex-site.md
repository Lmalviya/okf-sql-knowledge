---
type: Business Rule
title: Spatially Complex Site
description: Defines sites with complex spatial characteristics requiring specialized scanning approaches based on dimensional analysis.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 40
---

# Definition

A site with AreaM2 > 100 and SDI > 50, where SDI is the Spatial Density Index, requiring strategic planning for comprehensive documentation with multiple scanning stations and methodologies to capture complex spatial relationships.

# Columns used

* [scanspatial](/tables/scanspatial.md): `aream2`

# Depends on

* [Spatial Density Index (SDI)](/knowledge/spatial-density-index.md)
