---
type: Calculation
title: Resource Distribution Equity (RDE)
description: Evaluates the fairness of resource distribution across affected areas
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 31
---

# Definition

RDE = distequityidx \times \left(1 + \frac{distributionpoints}{20}\right) \times \left(1 - \frac{100 - deliverysuccessrate}{100}\right) \times coordeffect\_factor, \text{ where coordeffect\_factor is 1.2 for High, 1.0 for Medium, 0.8 for Low coordination effectiveness level, and 0 for else}

# Columns used

* [beneficiariesandassessments](/tables/beneficiariesandassessments.md): `distequityidx`
* [transportation](/tables/transportation.md): `distributionpoints`, `deliverysuccessrate`

# Depends on

* [coordeffectlvl](/knowledge/coordeffectlvl.md)

# Used by

* [Resource Distribution Inequity](/knowledge/resource-distribution-inequity.md)
