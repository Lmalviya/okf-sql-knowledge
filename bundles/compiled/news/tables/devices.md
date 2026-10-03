---
type: PostgreSQL Table
title: devices
description: '9 columns: devtype, brwtype, osver, appver, scrres, vpsize, conntype, netspd. Joins to users.'
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
| `devtype` | USER-DEFINED | An enum (devicetype_enum) describing device OS type (iOS, Windows, MacOS, Android). |
| `brwtype` | USER-DEFINED | An enum (browsertype_enum) referencing the browser used (Safari, Edge, Chrome, Firefox). |
| `osver` | character varying | A VARCHAR(40) capturing the specific OS version (e.g., 'Windows10.0.19042'). |
| `appver` | character varying | A VARCHAR(20) for the app version if used (e.g., 'v3.1.2'). |
| `scrres` | character varying | A VARCHAR(15) for screen resolution (e.g., '1920x1080'). |
| `vpsize` | character varying | A VARCHAR(15) describing the viewport size in the browser/app (e.g., '414x896'). |
| `conntype` | USER-DEFINED | An enum (connectiontype_enum) for the network type (Cable, 5G, 4G, WiFi). |
| `netspd` | numeric | A NUMERIC(6,2) measuring network speed in Mbps (e.g., 25.75). |
| `uselink` | bigint | A BIGINT FK linking to Users(UserKey) to show which user owns or uses this device. |

# Joins

* `uselink` references `userkey` in [users](/tables/users.md).
