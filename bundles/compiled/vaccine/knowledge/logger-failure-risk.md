---
type: Business Rule
title: Logger Failure Risk
description: Identifies loggers at risk of failure.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 15
---

# Definition

A logger where LHI < 0.3 or (BatteryPct < 20 and PwrBackupFlag='Not Available')

# Columns used

* [container](/tables/container.md): `batterypct`, `pwrbackupflag`

# Depends on

* [Logger Health Index (LHI)](/knowledge/logger-health-index.md)
