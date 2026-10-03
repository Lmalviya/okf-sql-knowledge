---
type: Business Rule
title: Degradation Risk Zone
description: Identifies archaeological sites at risk of degradation requiring urgent conservation intervention based on multiple factors.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 14
---

# Definition

A site with PresStat containing 'Poor' or 'Critical' and StructState not containing 'Stable', signaling immediate conservation needs due to active deterioration processes.

# Columns used

* [sites](/tables/sites.md): `presstat`
* [scanconservation](/tables/scanconservation.md): `structstate`

# Depends on

* [StructState (Structural State)](/knowledge/structstate.md)

# Used by

* [Digital Conservation Priority](/knowledge/digital-conservation-priority.md)
* [Conservation Priority Index (CPI)](/knowledge/conservation-priority-index.md)
* [Conservation Emergency](/knowledge/conservation-emergency.md)
* [Risk Zone Category](/knowledge/risk-zone-category.md)
