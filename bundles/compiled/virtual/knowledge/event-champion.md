---
type: Business Rule
title: Event Champion
description: Identifies fans who excel at event participation and promotion
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 28
---

# Definition

A fan with participation_summary.event_attendance.evtpart = 'Always', ERP > 50, and hashuse > 15, representing users who consistently attend events and actively promote them through social channels.

# Columns used

* [eventsandclub](/tables/eventsandclub.md): `participation_summary`
* [retentionandinfluence](/tables/retentionandinfluence.md): `hashuse`

# Depends on

* [Event ROI Potential (ERP)](/knowledge/event-roi-potential.md)
