---
type: Value Illustration
title: AnnDegRate (Annual Degradation Rate)
description: Illustrates the yearly performance degradation of solar panels.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 26
---

# Definition

Expressed as a percentage, representing how much a panel's output decreases per year. Quality silicon panels typically degrade at 0.5% to 0.7% annually, while lower quality or certain thin-film technologies may degrade at rates above 1% annually.

# Used by

* [Normalized Degradation Index (NDI)](/knowledge/normalized-degradation-index.md)
