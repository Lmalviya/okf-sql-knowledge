---
type: Business Rule
title: Inverter-Panel Compatibility Index
description: Assesses the compatibility between panels and their connected inverters.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 47
---

# Definition

An inverter-panel combination is considered optimally compatible when the panel's Weather Corrected Efficiency stays within 5% of the manufacturer's specifications and the inverter's Inverter Efficiency Percentage exceeds 97%.

# Depends on

* [InvertEffPct (Inverter Efficiency Percentage)](/knowledge/inverteffpct.md)
* [Weather Corrected Efficiency (WCE)](/knowledge/weather-corrected-efficiency.md)
