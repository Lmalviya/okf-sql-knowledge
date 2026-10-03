---
type: Business Rule
title: Critical Health Response Requirement
description: Identifies areas needing urgent health system reinforcement
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 44
---

# Definition

Areas experiencing Public Health Emergency where HSCI < 30 AND staffingProfile.readiness.ppe_status is 'Critical', indicating severely compromised health response capacity requiring immediate intervention

# Columns used

* [humanresources](/tables/humanresources.md): `staffingprofile`

# Depends on

* [staffingProfile.readiness.ppe_status](/knowledge/staffingprofile-readiness-ppe-status.md)
* [Public Health Emergency](/knowledge/public-health-emergency.md)
* [Health System Capacity Index (HSCI)](/knowledge/health-system-capacity-index.md)
