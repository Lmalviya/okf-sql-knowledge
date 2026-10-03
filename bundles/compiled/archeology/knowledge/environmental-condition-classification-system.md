---
type: Business Rule
title: Environmental Condition Classification System (ECCS)
description: A comprehensive classification system for archaeological site environments based on their suitability for scanning operations.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 50
---

# Definition

A four-tier classification where 'Optimal Scanning Conditions' have ESI > 85, 'Good Scanning Conditions' have ESI between 70-85, 'Acceptable Scanning Conditions' have ESI between 50-70, and 'Challenging Scanning Conditions' have ESI < 50. This classification guides scanning schedule planning and equipment selection to maximize data quality.

# Depends on

* [Environmental Suitability Index (ESI)](/knowledge/environmental-suitability-index.md)
* [Optimal Scanning Conditions](/knowledge/optimal-scanning-conditions.md)
