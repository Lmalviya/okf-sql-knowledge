---
type: PostgreSQL Table
title: sessions
description: '23 columns: seshstart, seshdur, seshviews, bncrate, seshdepth, engscore, seshrecs, seshclicks, ctrval, langcode, tzoffset, ipaddr, geoctry, georeg, geocity, expref, persver, recset, relscore, persacc, recutil. Joins to devices, users.'
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
| `userel` | bigint | A BIGINT FK referencing Users(UserKey) to link the session to a user. |
| `devrel` | bigint | A BIGINT FK referencing Devices(DevKey) to link the session to a device. |
| `seshstart` | timestamp without time zone | A TIMESTAMP indicating when the session started (e.g., '2025-03-12 14:00:00'). |
| `seshdur` | integer | An INT capturing the session's total duration in seconds (e.g., 1200 = 20 minutes). |
| `seshviews` | integer | An INT counting how many pages/articles the user viewed in this session (e.g., 5). |
| `bncrate` | numeric | A NUMERIC(5,2) measuring the bounce rate for the session (e.g., 25.00). |
| `seshdepth` | integer | An INT measuring how deep the user navigated (e.g., 3 screens). |
| `engscore` | numeric | A NUMERIC(5,2) measuring session engagement (e.g., 70.00). |
| `seshrecs` | integer | An INT indicating how many recommendations were shown to the user (e.g., 10). |
| `seshclicks` | integer | An INT counting how many recommendation clicks occurred (e.g., 2). |
| `ctrval` | numeric | A NUMERIC(5,2) capturing the click-through rate for recommendations (e.g., 20.00). |
| `langcode` | USER-DEFINED | An enum (languagecode_enum) describing the user's language (fr, es, en, de, zh). |
| `tzoffset` | USER-DEFINED | An enum (timezoneoffset_enum) for the user’s time zone offset (8, 1, 0, -5, -8). |
| `ipaddr` | inet | An INET column storing the user's IP address (e.g., '192.168.0.10'). |
| `geoctry` | character varying | A VARCHAR(100) referencing the user’s country based on IP geo (e.g., 'USA'). |
| `georeg` | character varying | A VARCHAR(100) referencing the user’s region or state (e.g., 'California'). |
| `geocity` | character varying | A VARCHAR(100) referencing the user’s city (e.g., 'San Francisco'). |
| `expref` | character varying | A VARCHAR(30) referencing an experiment ID or tag (e.g., 'EXP123'). |
| `persver` | USER-DEFINED | An enum (personalizationversion_enum) for personalization system version (v4, v1, v3, v2, v5). |
| `recset` | character varying | A VARCHAR(50) referencing a recommendation set ID if used (e.g., 'RecSetXYZ'). |
| `relscore` | numeric | A NUMERIC(5,2) capturing overall content relevance (e.g., 75.50). |
| `persacc` | numeric | A NUMERIC(5,2) referencing personalization accuracy (e.g., 80.00). |
| `recutil` | numeric | A NUMERIC(5,2) measuring recommendation utility or value (e.g., 70.25). |

# Joins

* `devrel` references `devkey` in [devices](/tables/devices.md).
* `userel` references `userkey` in [users](/tables/users.md).

# Related knowledge

* [User Engagement Rate (UER)](/knowledge/user-engagement-rate.md)
* [Recommendation Relevance Score (RRS)](/knowledge/recommendation-relevance-score.md)
* [Session Bounce Rate Adjustment (SBRA)](/knowledge/session-bounce-rate-adjustment.md)
* [CTR Percentile](/knowledge/ctr-percentile.md)
* [Elite User Interaction Metric (EUIM)](/knowledge/elite-user-interaction-metric.md)
