---
type: Business Rule
title: Public Health Emergency
description: Identifies situations with severe public health implications
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 26
---

# Definition

Conditions where diseaserisk is 'High' AND waterqualityindex < 50 AND PHRS < 40, indicating critical threats to public health requiring immediate intervention

# Columns used

* [environmentandhealth](/tables/environmentandhealth.md): `waterqualityindex`, `diseaserisk`

# Depends on

* [Public Health Resilience Score (PHRS)](/knowledge/public-health-resilience-score.md)

# Used by

* [Critical Health Response Requirement](/knowledge/critical-health-response-requirement.md)
