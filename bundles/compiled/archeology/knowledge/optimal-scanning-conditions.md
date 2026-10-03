---
type: Business Rule
title: Optimal Scanning Conditions
description: Defines the environmental conditions considered optimal for archaeological scanning based on instrument sensitivity profiles.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 15
---

# Definition

Conditions with ESI > 85, where ESI is the Environmental Suitability Index (knowledge #7), characterized by moderate temperature, humidity around 50%, and good illumination, minimizing environmental interference with scanning accuracy.

# Depends on

* [Environmental Suitability Index (ESI)](/knowledge/environmental-suitability-index.md)

# Used by

* [Environmental Condition Classification System (ECCS)](/knowledge/environmental-condition-classification-system.md)
