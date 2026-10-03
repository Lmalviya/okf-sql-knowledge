---
type: Value Illustration
title: FillFactor (Fill Factor)
description: Illustrates the ratio of actual maximum power to theoretical power.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 24
---

# Definition

A dimensionless value between 0 and 1 representing the ratio of maximum power point (Vmp × Imp) to open-circuit voltage times short-circuit current (Voc × Isc). High-quality commercial panels typically have fill factors between 0.75 and 0.85.

# Used by

* [Electrical Degradation Index (EDI)](/knowledge/electrical-degradation-index.md)
