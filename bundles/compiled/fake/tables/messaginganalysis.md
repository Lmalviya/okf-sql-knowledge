---
type: PostgreSQL Table
title: messaginganalysis
description: '13 columns: msgsimscore, msgfreq, msgtgtdiv, resptimepat, convnatval, sentvar, langsoph, txtuniq, keypatmatch, topiccoh. Joins to contentbehavior, networkmetrics.'
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
| `msgkey` | character, primary key | A CHAR(12) primary key for each messaging analysis record (e.g., 'MA1234567890'). |
| `msgcntref` | character | References ContentBehavior(CntRef) (e.g., 'CB1234567890'). |
| `msgnetref` | character | References NetworkMetrics(NetKey) (e.g., 'NE1234567890'). |
| `msgsimscore` | numeric | NUMERIC(4,3) message similarity measure (e.g., '0.562'). |
| `msgfreq` | numeric | NUMERIC(6,2) how frequently messages are sent (e.g., '45.67'). |
| `msgtgtdiv` | numeric | NUMERIC(4,2) diversity of message targets (e.g., '1.25'). |
| `resptimepat` | USER-DEFINED | An enum (ResponseTimePattern_enum) labeling response speed (Natural, Delayed, Random, Instant). |
| `convnatval` | numeric | NUMERIC(4,3) how natural conversation flow is (e.g., '0.753'). |
| `sentvar` | numeric | NUMERIC(6,4) sentiment variation (e.g., '0.1234'). |
| `langsoph` | numeric | NUMERIC(5,3) linguistic sophistication (e.g., '0.763'). |
| `txtuniq` | numeric | NUMERIC(4,2) text uniqueness across messages (e.g., '0.85'). |
| `keypatmatch` | character varying | A VARCHAR(32) describing detected keyword/pattern (e.g., 'spam_trigger'). |
| `topiccoh` | numeric | NUMERIC(5,4) topic coherence rating (e.g., '0.8743'). |

# Joins

* `msgcntref` references `cntref` in [contentbehavior](/tables/contentbehavior.md).
* `msgnetref` references `netkey` in [networkmetrics](/tables/networkmetrics.md).

# Related knowledge

* [Content Authenticity Score (CAS)](/knowledge/content-authenticity-score.md)
* [Bot Behavior Index (BBI)](/knowledge/bot-behavior-index.md)
* [Content Manipulation Score (CMS)](/knowledge/content-manipulation-score.md)
* [messaginganalysis.convnatval](/knowledge/messaginganalysis-convnatval.md)
