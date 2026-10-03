---
type: Business Rule
title: High-Impact Communication Failure
description: Identifies disaster areas with severe communication infrastructure breakdown
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 41
---

# Definition

Areas where impactMetrics.communication is 'Down' AND CRF < 40 AND coordeffectlvl is 'Low', representing critical communication failures that severely impede response coordination

# Columns used

* [disasterevents](/tables/disasterevents.md): `impactmetrics`
* [coordinationandevaluation](/tables/coordinationandevaluation.md): `coordeffectlvl`

# Depends on

* [impactMetrics.communication](/knowledge/impactmetrics-communication.md)
* [coordeffectlvl](/knowledge/coordeffectlvl.md)
* [Communication Resilience Factor (CRF)](/knowledge/communication-resilience-factor.md)
