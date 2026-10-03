---
type: Calculation
title: Base Station Communication Stability Index (BSCSI)
description: Evaluates the stability and reliability of polar base station communication systems
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 32
---

# Definition

BSCSI = CRI × (1 + 0.2 × signalmetrics.radio_strength_dbm ÷ 100) × (1 - 0.01 × (1000 - signalmetrics.latency_ms))

# Columns used

* [communication](/tables/communication.md): `signalmetrics`

# Depends on

* [Communication Reliability Index (CRI)](/knowledge/communication-reliability-index.md)

# Used by

* [Communication Network Resilience Assessment (CNRA)](/knowledge/communication-network-resilience-assessment.md)
