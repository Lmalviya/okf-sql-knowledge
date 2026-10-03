---
type: Calculation
title: Comprehensive Operational Reliability Indicator (CORI)
description: Comprehensively assesses the overall reliability of polar equipment operations
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 39
---

# Definition

CORI = 0.4 × EER + 0.4 × ORS + 0.2 × CRI

# Depends on

* [Equipment Efficiency Rating (EER)](/knowledge/equipment-efficiency-rating.md)
* [Operational Readiness Score (ORS)](/knowledge/operational-readiness-score.md)
* [Communication Reliability Index (CRI)](/knowledge/communication-reliability-index.md)

# Used by

* [Long-term Scientific Mission Viability (LSMV)](/knowledge/long-term-scientific-mission-viability.md)
