---
type: PostgreSQL Table
title: interactionmetrics
description: '2 columns: interaction_behavior. Joins to interactions.'
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
| `intmetkey` | bigint, primary key | A BIGINT primary key referencing Interactions(IntKey). |
| `interaction_behavior` | jsonb | JSONB column. Captures user interaction behavior metrics, including scroll depth, time spent, and conversion details. |

# JSON fields

* `interaction_behavior.scroll.depth`: An INT measuring how deep the user scrolled or engaged (e.g., 2 screen lengths).
* `interaction_behavior.scroll.percentage`: A NUMERIC(5,2) capturing scroll depth percentage (e.g., 75.50).
* `interaction_behavior.scroll.speed`: A NUMERIC(6,2) measuring scroll speed in px/sec (e.g., 50.25).
* `interaction_behavior.time_spent.duration_seconds`: An INT measuring the total seconds spent in this interaction (e.g., 30).
* `interaction_behavior.time_spent.reading_seconds`: A NUMERIC(6,2) how many seconds the user spent actually reading (e.g., 15.00).
* `interaction_behavior.time_spent.viewport_time`: A NUMERIC(6,2) time the content was in the viewport (e.g., 20.00).
* `interaction_behavior.time_spent.attention_time`: A NUMERIC(6,2) capturing user’s attention time (e.g., 18.50).
* `interaction_behavior.click_seconds`: A NUMERIC(6,2) time to first click in seconds (e.g., 10.50).
* `interaction_behavior.bounce_status`: An enum (bouncestatus_enum) indicating if this was a bounce (Yes, No).
* `interaction_behavior.exit_type`: An enum (exittype_enum) describing exit type (Timeout, Natural, Bounce, External).
* `interaction_behavior.next_action`: An enum (nextaction_enum) referencing the next action the user took (Exit, Another Article, Share, Search).
* `interaction_behavior.conversion.status`: An enum (conversionstatus_enum) describing a conversion event (Share, Newsletter, Subscription).
* `interaction_behavior.conversion.value`: A NUMERIC(10,2) capturing any monetary or point value of the conversion (e.g., 5.00).

# Joins

* `intmetkey` references `intkey` in [interactions](/tables/interactions.md).
