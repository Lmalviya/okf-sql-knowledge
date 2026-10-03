---
type: Calculation
title: Health System Capacity Index (HSCI)
description: Measures the disaster area's health system ability to handle medical emergencies
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 37
---

# Definition

HSCI = PHRS \times medcap\_numeric \times \left(1 - \frac{hazlevel\_numeric}{6}\right), \text{ where medcap\_numeric maps Adequate=1.0, Limited=0.6, Critical=0.3, else=0 for medical emergency capacity, and hazlevel\_numeric represents severity level from 1-5}

# Columns used

* [disasterevents](/tables/disasterevents.md): `hazlevel`

# Depends on

* [hazlevel](/knowledge/hazlevel.md)
* [Public Health Resilience Score (PHRS)](/knowledge/public-health-resilience-score.md)

# Used by

* [Critical Health Response Requirement](/knowledge/critical-health-response-requirement.md)
