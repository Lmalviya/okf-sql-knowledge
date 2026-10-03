---
type: Business Rule
title: Community Resilience Opportunity
description: Identifies high-potential areas for community resilience building
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 46
---

# Definition

Areas where CEE > 2.5 AND vulnerabilityreview is 'Complete' BUT NOT qualifying as Community Resilience Builder, representing opportunities where community engagement is strong but resilience building efforts need strengthening

# Columns used

* [beneficiariesandassessments](/tables/beneficiariesandassessments.md): `vulnerabilityreview`

# Depends on

* [Community Resilience Builder](/knowledge/community-resilience-builder.md)
* [Community Engagement Effectiveness (CEE)](/knowledge/community-engagement-effectiveness.md)

# Used by

* [Community Resilience Classification](/knowledge/community-resilience-classification.md)
