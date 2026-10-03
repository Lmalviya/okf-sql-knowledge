---
type: Calculation
title: Communication Resilience Factor (CRF)
description: Measures the resilience of communication systems during disasters
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 32
---

# Definition

CRF = 100 - \frac{CSR}{2} \times communication\_factor, \text{ where communication\_factor is 1.0 for Operational, 0.6 for Limited, and 0.3 for Down communication status from impactMetrics.communication}

# Columns used

* [disasterevents](/tables/disasterevents.md): `impactmetrics`

# Depends on

* [Communication Security Risk (CSR)](/knowledge/communication-security-risk.md)

# Used by

* [High-Impact Communication Failure](/knowledge/high-impact-communication-failure.md)
