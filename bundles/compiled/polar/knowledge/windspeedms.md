---
type: Value Illustration
title: windspeedms
description: Illustrates the impact of wind speed measurements on operations and safety.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 23
---

# Definition

Wind speeds in polar environments typically range from 0 to 60 m/s. Speeds below 5 m/s represent calm conditions, 5-15 m/s indicate moderate winds with minor operational impact, 15-25 m/s represent strong winds requiring additional safety measures, and speeds above 25 m/s indicate dangerous conditions that may require suspension of outdoor activities and securing of equipment.

# Columns used

* [weatherandstructure](/tables/weatherandstructure.md): `windspeedms`
