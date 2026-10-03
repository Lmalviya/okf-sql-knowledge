---
type: Business Rule
title: Environmental Control Failure
description: Identifies situations where environmental controls are failing to protect artifacts.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 47
---

# Definition

Occurs when ECI < 4 AND there is an Environmental Instability Event.

# Depends on

* [Environmental Compliance Index (ECI)](/knowledge/environmental-compliance-index.md)
* [Environmental Instability Event](/knowledge/environmental-instability-event.md)
