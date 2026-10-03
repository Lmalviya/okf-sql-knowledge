---
type: Business Rule
title: Communication Network Resilience Assessment (CNRA)
description: Assesses the resilience and interference resistance of polar communication networks
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 45
---

# Definition

Communication networks are assessed as having 'High Resilience' (CRI > 0.8 and BSCSI > 0.85), 'Medium Resilience' (CRI > 0.6 and BSCSI > 0.7), or 'Low Resilience' (other cases).

# Depends on

* [Communication Reliability Index (CRI)](/knowledge/communication-reliability-index.md)
* [Base Station Communication Stability Index (BSCSI)](/knowledge/base-station-communication-stability-index.md)
