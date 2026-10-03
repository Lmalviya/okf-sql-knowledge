---
type: Business Rule
title: Facility Demonstrating Strong Patient Retention
description: Identifies facilities showing positive performance indicators related to high patient adherence and low missed appointment rates.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 48
---

# Definition

A facility where TAR > 0.75 and MAR < 1.0, \text{based on Treatment Adherence Rate (TAR) and Missed Appointment Rate (MAR)}

# Depends on

* [Treatment Adherence Rate (TAR)](/knowledge/treatment-adherence-rate.md)
* [Missed Appointment Rate (MAR)](/knowledge/missed-appointment-rate.md)
