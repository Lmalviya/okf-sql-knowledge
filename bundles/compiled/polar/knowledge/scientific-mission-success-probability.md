---
type: Calculation
title: Scientific Mission Success Probability (SMSP)
description: Predicts the probability of successful completion of scientific missions
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 34
---

# Definition

SMSP = SER × (0.8 + 0.2 × CRI ÷ 10)

# Depends on

* [Communication Reliability Index (CRI)](/knowledge/communication-reliability-index.md)
* [Scientific Equipment Reliability (SER)](/knowledge/scientific-equipment-reliability.md)

# Used by

* [Critical Scientific Equipment Status (CSES)](/knowledge/critical-scientific-equipment-status.md)
* [Long-term Scientific Mission Viability (LSMV)](/knowledge/long-term-scientific-mission-viability.md)
