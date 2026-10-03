---
type: PostgreSQL Table
title: networkmetrics
description: '3 columns: network_engagement_metrics. Joins to sessionbehavior.'
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
| `netkey` | character, primary key | A CHAR(12) primary key for each network metrics record (e.g., 'NE1234567890'). |
| `netsessref` | character | A CHAR(12) referencing SessionBehavior(SessRef) (e.g., 'SE1234567890'). |
| `network_engagement_metrics` | jsonb | JSONB column. Groups connection‑growth, engagement‑quality, and interaction‑diversity measures into one JSONB field for quick network‑level behaviour profiling. |

# JSON fields

* `network_engagement_metrics.connection_metrics.follownum`: A BIGINT for how many followers the user has (e.g., '12345').
* `network_engagement_metrics.connection_metrics.followingnum`: A BIGINT for how many accounts the user follows (e.g., '6789').
* `network_engagement_metrics.connection_metrics.followgrowrate`: NUMERIC(4,3) how quickly follower count grows (e.g., '1.234').
* `network_engagement_metrics.connection_metrics.followinggrowrate`: NUMERIC(5,4) how quickly following count grows (e.g., '2.5678').
* `network_engagement_metrics.connection_metrics.followratio`: NUMERIC(6,2) ratio of followers to following (e.g., '1.50').
* `network_engagement_metrics.connection_metrics.mutualconnratio`: NUMERIC(3,1) ratio of mutual connections (e.g., '0.8').
* `network_engagement_metrics.connection_metrics.conngrowpat`: An enum (ConnectionGrowthPattern_enum) describing connection growth (Suspicious, Burst, Bot-like, Organic).
* `network_engagement_metrics.connection_metrics.connqualscore`: NUMERIC(4,1) rating connection quality (e.g., '7.5').
* `network_engagement_metrics.engagement_metrics.engrate`: NUMERIC(4,3) user’s engagement rate (e.g., '0.123').
* `network_engagement_metrics.engagement_metrics.engauth`: NUMERIC(5,4) measuring authenticity of engagement (e.g., '0.8524').
* `network_engagement_metrics.engagement_metrics.likeratio`: NUMERIC(3,2) portion of interactions that are likes (e.g., '0.25').
* `network_engagement_metrics.engagement_metrics.cmtratio`: NUMERIC(3,2) portion of interactions that are comments (e.g., '0.30').
* `network_engagement_metrics.engagement_metrics.sharerate`: NUMERIC(4,3) portion of interactions that are shares (e.g., '0.456').
* `network_engagement_metrics.interaction_metrics.interactreci`: NUMERIC(5,3) reciprocity measure (e.g., '0.789').
* `network_engagement_metrics.interaction_metrics.interactdiv`: NUMERIC(4,2) diversity of interactions (e.g., '1.25').
* `network_engagement_metrics.interaction_metrics.tempinteractpat`: An enum (TemporalInteractionPattern_enum) describing interaction timing (Natural, Periodic, Random, Automated).

# Joins

* `netsessref` references `sessref` in [sessionbehavior](/tables/sessionbehavior.md).

# Related knowledge

* [networkmetrics.network_engagement_metrics.engagement_metrics.engauth](/knowledge/networkmetrics-network-engagement-metrics-engagement-metrics-engauth.md)
