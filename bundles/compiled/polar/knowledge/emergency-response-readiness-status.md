---
type: Business Rule
title: Emergency Response Readiness Status (ERRS)
description: Assesses a polar site's preparedness to respond to emergency situations
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 41
---

# Definition

A polar site is rated as 'emergency response ready' when its critical equipment maintains OSPI > 0.75 and LSSR > 0.8, with emergencycommunicationstatus = 'Operational' and backuppowerstatus = 'Active' and batterystatus.level_percent > 85.

# Columns used

* [thermalsolarwindandgrid](/tables/thermalsolarwindandgrid.md): `backuppowerstatus`
* [powerbattery](/tables/powerbattery.md): `batterystatus`

# Depends on

* [Overall Safety Performance Index (OSPI)](/knowledge/overall-safety-performance-index.md)
* [Life Support System Reliability (LSSR)](/knowledge/life-support-system-reliability.md)
