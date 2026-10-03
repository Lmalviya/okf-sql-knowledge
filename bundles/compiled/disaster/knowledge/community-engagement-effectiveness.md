---
type: Calculation
title: Community Engagement Effectiveness (CEE)
description: Evaluates how effectively operations engage with affected communities
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 38
---

# Definition

CEE = \frac{BSI}{100} \times commengage\_numeric \times \left(\frac{stakeholdersatisf + 1}{5}\right), \text{ where commengage\_numeric maps Low=1, Medium=2, High=3, else=0 for community engagement level}

# Columns used

* [coordinationandevaluation](/tables/coordinationandevaluation.md): `stakeholdersatisf`

# Depends on

* [Beneficiary Satisfaction Index (BSI)](/knowledge/beneficiary-satisfaction-index.md)

# Used by

* [Community Resilience Opportunity](/knowledge/community-resilience-opportunity.md)
* [Community Resilience Classification](/knowledge/community-resilience-classification.md)
