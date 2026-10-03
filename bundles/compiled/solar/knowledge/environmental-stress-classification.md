---
type: Business Rule
title: Environmental Stress Classification
description: Categorizes the level of environmental stress a panel is experiencing.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 48
---

# Definition

Environmental stress is classified based on combining Weather Severity Index and exposure time outside the Optimal Performance Window, with high stress potentially accelerating the Panel Efficiency Loss Rate.

# Depends on

* [Panel Efficiency Loss Rate (PELR)](/knowledge/panel-efficiency-loss-rate.md)
* [Optimal Performance Window](/knowledge/optimal-performance-window.md)
* [Weather Severity Index](/knowledge/weather-severity-index.md)
