---
type: Business Rule
title: Facility Attrition Risk Indicator
description: Identifies facilities potentially experiencing high patient dropout, characterized by low engagement/adherence and high missed appointment rates.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 43
---

# Definition

A facility where EAS < 1.5 and MAR > 2.5, \text{based on low Engagement-Adherence Score (EAS) and high Missed Appointment Rate (MAR)}

# Depends on

* [Engagement-Adherence Score (EAS)](/knowledge/engagement-adherence-score.md)
* [Missed Appointment Rate (MAR)](/knowledge/missed-appointment-rate.md)

# Used by

* [Systemically Stressed Facility Environment](/knowledge/systemically-stressed-facility-environment.md)
