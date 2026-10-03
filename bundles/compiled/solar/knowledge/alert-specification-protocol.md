---
type: Business Rule
title: Alert Specification Protocol
description: Comprehensive rules for generating performance alerts
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 53
---

# Definition

Mandates that critical alerts must: (1) Reference the plant ID, panel ID and performance record; (2) Set status to 'Critical'; (3) Assign 'High' maintenance priority; (4) Set replacement priority to 'High' if performance <60% of expected, otherwise 'Medium'; (5) Mark optimization potential as 'High'; (6) Use 'ALERT_' prefix with random hash for IDs; (7) Update existing alerts within 30-day window rather than creating duplicates
