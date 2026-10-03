---
type: Business Rule
title: Community Resilience Builder
description: Identifies operations that strengthen local community capacity
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 28
---

# Definition

Operations where localcapacitygrowth is 'Active' AND commengagelvl is 'High' AND BSI > 70, representing efforts that effectively build sustainable community resilience

# Columns used

* [beneficiariesandassessments](/tables/beneficiariesandassessments.md): `commengagelvl`, `localcapacitygrowth`

# Depends on

* [Beneficiary Satisfaction Index (BSI)](/knowledge/beneficiary-satisfaction-index.md)

# Used by

* [Community Resilience Opportunity](/knowledge/community-resilience-opportunity.md)
* [Community Resilience Classification](/knowledge/community-resilience-classification.md)
