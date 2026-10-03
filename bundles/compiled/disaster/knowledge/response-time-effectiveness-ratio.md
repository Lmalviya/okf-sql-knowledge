---
type: Calculation
title: Response Time Effectiveness Ratio (RTER)
description: Measures how quickly and effectively disaster response operations are deployed
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 30
---

# Definition

RTER = \frac{100}{estdurationdays + 1} \times \frac{deliverysuccessrate}{100} \times \left(\frac{4 - respphase\_numeric}{3}\right), \text{ where respphase\_numeric maps Initial=1, Emergency=2, Recovery=3, Reconstruction=4, else=0, representing faster deployment relative to disaster phase}

# Columns used

* [operations](/tables/operations.md): `respphase`, `estdurationdays`
* [transportation](/tables/transportation.md): `deliverysuccessrate`

# Depends on

* [respphase](/knowledge/respphase.md)

# Used by

* [Rapid Response Success Model](/knowledge/rapid-response-success-model.md)
