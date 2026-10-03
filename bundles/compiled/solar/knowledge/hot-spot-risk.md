---
type: Business Rule
title: Hot Spot Risk
description: Indicates conditions that suggest a panel may be developing hot spots.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 11
---

# Definition

A panel is at risk for hot spots when it shows irregular electrical parameters (Voc or Isc deviations >5% compared to other panels in the same string) combined with cell temperatures exceeding 20°C above ambient temperature.
