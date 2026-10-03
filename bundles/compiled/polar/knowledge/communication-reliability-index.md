---
type: Calculation
title: Communication Reliability Index (CRI)
description: Assesses the reliability of communication systems based on signal metrics and antenna status.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 4
---

# Definition

CRI = \begin{cases} 0 & \text{if antennastatus = 'Error'} \\ 5 & \text{if antennastatus = 'Warning'} \\ 10 & \text{if antennastatus = 'Normal'} \\ 0 & \text{otherwise} \end{cases} \times (1 - \frac{signalmetrics.latency\_ms}{1000}), \text{ where lower latency and better antenna status result in higher reliability.}

# Columns used

* [communication](/tables/communication.md): `antennastatus`, `signalmetrics`

# Used by

* [Communication Zone Status](/knowledge/communication-zone-status.md)
* [Base Station Communication Stability Index (BSCSI)](/knowledge/base-station-communication-stability-index.md)
* [Scientific Mission Success Probability (SMSP)](/knowledge/scientific-mission-success-probability.md)
* [Comprehensive Operational Reliability Indicator (CORI)](/knowledge/comprehensive-operational-reliability-indicator.md)
* [Communication Network Resilience Assessment (CNRA)](/knowledge/communication-network-resilience-assessment.md)
