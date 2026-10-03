---
type: Business Rule
title: Maintenance Priority Level
description: Classifies equipment based on the urgency of required maintenance.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 12
---

# Definition

Equipment is categorized into maintenance priority levels: 'Immediate Attention' (operationhours > maintenancecyclehours OR operationalstatus = 'Repair'), 'Scheduled Service' (operationhours > 0.8 * maintenancecyclehours), and 'Routine Maintenance' (all other cases), helping prioritize resource allocation.

# Columns used

* [operationmaintenance](/tables/operationmaintenance.md): `operationhours`, `maintenancecyclehours`, `operationalstatus`
