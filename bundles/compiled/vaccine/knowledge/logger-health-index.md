---
type: Calculation
title: Logger Health Index (LHI)
description: Overall health score for data logger.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 6
---

# Definition

LHI = \frac{BatteryPct}{100} \times (1 - \frac{MemUsePct}{100}) \times \frac{DataPct}{100}

# Columns used

* [container](/tables/container.md): `batterypct`
* [datalogger](/tables/datalogger.md): `datapct`, `memusepct`

# Used by

* [Logger Failure Risk](/knowledge/logger-failure-risk.md)
* [Combined Maintenance Risk (CMR)](/knowledge/combined-maintenance-risk.md)
* [Logger Reliability Score (LRS)](/knowledge/logger-reliability-score.md)
