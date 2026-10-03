---
type: Value Illustration
title: AirQualityReadings.PM25Conc
description: Illustrates fine particulate matter measurements and their conservation implications.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 30
---

# Definition

Values represent PM2.5 concentration in µg/m³. Clean museum air should measure below 5 µg/m³. Values of 5-15 indicate acceptable conditions, 15-30 indicate potential risk to sensitive materials, and above 30 represent hazardous conditions requiring immediate air filtration review.

# Columns used

* [airqualityreadings](/tables/airqualityreadings.md): `pm25conc`
