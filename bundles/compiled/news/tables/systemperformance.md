---
type: PostgreSQL Table
title: systemperformance
description: '12 columns: perfts, resptime, loadscore, errcount, warncount, perfscore, cachestate, apiver, cliver, featset. Joins to devices, sessions.'
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_schema.txt
  title: news schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_column_meaning_base.json
  title: news column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `perfts` | timestamp without time zone | A TIMESTAMP capturing when this system performance record was logged. |
| `resptime` | integer | An INT measuring system response time in milliseconds (e.g., 120). |
| `loadscore` | numeric | A NUMERIC(5,2) rating system load (e.g., 60.00). |
| `errcount` | USER-DEFINED | An enum (errorcount_enum) capturing how many errors occurred (0–5). |
| `warncount` | integer | An INT counting warnings (e.g., 2). |
| `perfscore` | numeric | A NUMERIC(5,2) rating system performance (e.g., 80.00). |
| `cachestate` | USER-DEFINED | An enum (cachestatus_enum) describing cache usage (Hit, Expired, Miss). |
| `apiver` | USER-DEFINED | An enum (apiversion_enum) for the API version (v3, v2, v1). |
| `cliver` | character varying | A VARCHAR(50) storing the client version if relevant (e.g., 'web-1.2'). |
| `featset` | text | A TEXT field for feature flags or toggles (e.g., 'newUI, improvedSearch'). |
| `devlink` | bigint | A BIGINT referencing Devices(DevKey), linking performance data to a device. |
| `seshlink` | bigint | A BIGINT referencing Sessions(SeshKey), linking performance data to a session. |

# Joins

* `devlink` references `devkey` in [devices](/tables/devices.md).
* `seshlink` references `seshkey` in [sessions](/tables/sessions.md).

# Related knowledge

* [System Performance Index (SPI)](/knowledge/system-performance-index.md)
* [Performance Status](/knowledge/performance-status.md)
