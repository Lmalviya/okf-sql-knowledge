---
type: Business Rule
title: Digital Conservation Priority
description: Classification system for prioritizing digital conservation efforts based on site conditions, historical significance, and preservation status.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 16
---

# Definition

A scoring system where sites in Degradation Risk Zones with GuessDate older than 1000 BCE or with TypeSite = 'Rare' or 'Unique' receive highest priority for digital preservation through Premium Quality Scans, requiring immediate allocation of scanning resources.

# Columns used

* [sites](/tables/sites.md): `guessdate`, `typesite`

# Depends on

* [Premium Quality Scan](/knowledge/premium-quality-scan.md)
* [Degradation Risk Zone](/knowledge/degradation-risk-zone.md)
