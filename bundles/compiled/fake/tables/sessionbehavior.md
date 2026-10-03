---
type: PostgreSQL Table
title: sessionbehavior
description: '9 columns: logintimepat, loginfreq, loginlocvar, sesslenmean, sesscount, actregval, acttimedist. Joins to profile.'
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_schema.txt
  title: fake schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_column_meaning_base.json
  title: fake column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `sessref` | character, primary key | A CHAR(12) primary key uniquely identifying each session behavior record (e.g., 'SE1234567890'). |
| `sessprofref` | character | A CHAR(12) referencing Profile(ProfKey) (e.g., 'PF1234567890'). |
| `logintimepat` | USER-DEFINED | An enum (LoginTimePattern_enum) describing login times (Burst, Bot-like, Random, Regular). |
| `loginfreq` | USER-DEFINED | An enum (LoginFrequency_enum) labeling login frequency (Medium, High, Low, Suspicious). |
| `loginlocvar` | numeric | NUMERIC(4,1) measuring variance in login locations (e.g., '2.7'). |
| `sesslenmean` | numeric | NUMERIC(7,2) average session length (e.g., '123.45'). |
| `sesscount` | integer | An INTEGER counting total sessions (e.g., '57'). |
| `actregval` | numeric | NUMERIC(4,2) measuring how regularly the user logs in (e.g., '0.75'). |
| `acttimedist` | jsonb | A JSONB structure capturing session activity distribution (e.g., '{"morning": 30, "night": 70}'). |

# Joins

* `sessprofref` references `profkey` in [profile](/tables/profile.md).

# Related knowledge

* [Account Activity Frequency (AAF)](/knowledge/account-activity-frequency.md)
* [Session Count (SC)](/knowledge/session-count.md)
* [Total Post Frequency (TPF)](/knowledge/total-post-frequency.md)
