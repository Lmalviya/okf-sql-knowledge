---
type: Calculation
title: Container Efficiency Score (CES)
description: Overall container efficiency considering multiple metrics.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 36
---

# Definition

CES = \text{SER} \times \text{CEI} \times (1 - \text{CRI})

# Depends on

* [Storage Efficiency Ratio (SER)](/knowledge/storage-efficiency-ratio.md)
* [Coolant Efficiency Index (CEI)](/knowledge/coolant-efficiency-index.md)
* [Container Risk Index (CRI)](/knowledge/container-risk-index.md)

# Used by

* [Severe Container Risk](/knowledge/severe-container-risk.md)
* [Unsafe Vaccine Condition](/knowledge/unsafe-vaccine-condition.md)
* [Container Alert Status](/knowledge/container-alert-status.md)
