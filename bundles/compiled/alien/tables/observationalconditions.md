---
type: PostgreSQL Table
title: observationalconditions
description: '4 columns: obstime, obsdate, obsdurhrs. Joins to signals.'
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_schema.txt
  title: alien schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_column_meaning_base.json
  title: alien column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `signalref` | character, primary key | Full name: 'Signal Registry Reference'. Explanation: Primary key referencing the signal. Data type: CHAR(36). Example: 'SIG-PQR-9876'. |
| `obstime` | time without time zone | Full name: 'Observation Time'. Explanation: Local time of the observation in HH:MM:SS. Data type: TIME. Example: '13:45:59'. |
| `obsdate` | date | Full name: 'Observation Date'. Explanation: Local date of the observation (YYYY-MM-DD). Data type: DATE. Example: '2025-08-01'. |
| `obsdurhrs` | numeric | Full name: 'Observation Duration (hours)'. Explanation: How long the observation lasted in hours. Data type: NUMERIC(5,2). Example: '2.50'. |

# Joins

* `signalref` references `signalregistry` in [signals](/tables/signals.md).
