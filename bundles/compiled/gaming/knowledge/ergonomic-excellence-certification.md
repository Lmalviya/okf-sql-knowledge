---
type: Business Rule
title: Ergonomic Excellence Certification
description: Designates devices specifically designed to prevent repetitive strain injuries and support extended professional gaming sessions.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 41
---

# Definition

A device with ESF > 8.5, ErgoRate > 8, CI > 8.5, and at least one specialized ergonomic feature (WristFlag = true or PalmAngle between 10-20°), designed to maintain player comfort and prevent strain during marathon gaming sessions.

# Columns used

* [mechanical](/tables/mechanical.md): `wristflag`, `palmangle`, `ergorate`

# Depends on

* [Ergonomic Sustainability Factor (ESF)](/knowledge/ergonomic-sustainability-factor.md)
* [Comfort Index (CI)](/knowledge/comfort-index.md)
