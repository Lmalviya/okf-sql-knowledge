---
type: Business Rule
title: Conservation Emergency
description: Identifies artifacts requiring immediate conservation intervention.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 12
---

# Definition

A situation where an artifact has ConserveStatus='Critical' AND a TreatPriority='Urgent'.

# Columns used

* [artifactscore](/tables/artifactscore.md): `conservestatus`
* [conservationandmaintenance](/tables/conservationandmaintenance.md): `treatpriority`

# Used by

* [Critical Conservation Alert](/knowledge/critical-conservation-alert.md)
