---
type: Calculation
title: Social Influence Multiplier (SIM)
description: Calculates how much a fan amplifies content through their social network
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 14
---

# Definition

SIM = \left(\frac{follcount}{100}\right) \times (engrate \times 2) \times (viralcont + 1) \times 0.5, \text{ reflecting the fan's ability to spread content through their network based on their following, engagement level, and history of creating viral content.}

# Columns used

* [engagement](/tables/engagement.md): `engrate`
* [retentionandinfluence](/tables/retentionandinfluence.md): `viralcont`

# Used by

* [Community Contribution Index (CCI)](/knowledge/community-contribution-index.md)
* [Social Amplifier](/knowledge/social-amplifier.md)
* [Social Conversion Rate (SCR)](/knowledge/social-conversion-rate.md)
* [Social Network Underutilizer](/knowledge/social-network-underutilizer.md)
