---
type: Calculation
title: Event Response Factor (ERF)
description: Measures a fan's response rate to official events and activities
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 38
---

# Definition

ERF = \frac{(eventsandclub.participation\_summary->>'event\_attendance.onevtatt')::int + (eventsandclub.participation\_summary->>'event\_attendance.offevtatt')::int}{10} \times \left(1 + \frac{FEI}{2}\right), \text{ where onevtatt and offevtatt represent online and offline events attended.}

# Depends on

* [Fan Engagement Index (FEI)](/knowledge/fan-engagement-index.md)
