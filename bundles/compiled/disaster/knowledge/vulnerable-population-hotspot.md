---
type: Business Rule
title: Vulnerable Population Hotspot
description: Identifies areas with highly vulnerable populations requiring priority attention
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 23
---

# Definition

Areas where vulnerabilityreview is 'Complete' with distequityidx < 0.3 AND coordeffectlvl is 'Low', indicating populations with high vulnerability and inadequate coordination support

# Columns used

* [beneficiariesandassessments](/tables/beneficiariesandassessments.md): `vulnerabilityreview`, `distequityidx`
* [coordinationandevaluation](/tables/coordinationandevaluation.md): `coordeffectlvl`

# Depends on

* [coordeffectlvl](/knowledge/coordeffectlvl.md)
