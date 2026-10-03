---
type: Calculation
title: Fan Engagement Index (FEI)
description: A comprehensive metric measuring fan activity level with platform and virtual idols
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 10
---

# Definition

FEI = (engrate \times 0.4) + (\frac{socintscore}{100} \times 0.3) + (\frac{actdayswk}{7} \times 0.2) + (\frac{avgsesscount}{10} \times 0.1), \text{ where weights reflect each factor's different contribution to engagement, with results ranging from 0-1. Higher values indicate more engaged fans.}

# Columns used

* [engagement](/tables/engagement.md): `socintscore`, `engrate`, `actdayswk`, `avgsesscount`

# Used by

* [Fan Lifetime Value (FLV)](/knowledge/fan-lifetime-value.md)
* [Community Contribution Index (CCI)](/knowledge/community-contribution-index.md)
* [Superfan](/knowledge/superfan.md)
* [Potential Ambassador](/knowledge/potential-ambassador.md)
* [Premium Engagement Ratio (PER)](/knowledge/premium-engagement-ratio.md)
* [Event Response Factor (ERF)](/knowledge/event-response-factor.md)
* [Engagement-Deficient Whale](/knowledge/engagement-deficient-whale.md)
