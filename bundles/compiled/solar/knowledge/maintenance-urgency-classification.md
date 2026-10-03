---
type: Business Rule
title: Maintenance Urgency Classification
description: Four-tier system prioritizing maintenance actions based on combined financial and operational factors
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 50
---

# Definition

URGENT: Having critical alerts AND MROI>2.0; HIGH: Having critical alerts; MEDIUM: MROI>2.0; LOW: All other cases

# Depends on

* [Maintenance Return on Investment (MROI)](/knowledge/maintenance-return-on-investment.md)
