---
type: Calculation
title: Social Conversion Rate (SCR)
description: Measures a fan's ability to convert their social network into active platform participants
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 35
---

# Definition

SCR = \frac{refcount}{(socialcommunity.community\_engagement->>'network.follcount')::int} \times 100, \text{ expressed as a percentage of followers successfully converted to platform users.}

# Columns used

* [retentionandinfluence](/tables/retentionandinfluence.md): `refcount`

# Depends on

* [Social Influence Multiplier (SIM)](/knowledge/social-influence-multiplier.md)

# Used by

* [Social Network Underutilizer](/knowledge/social-network-underutilizer.md)
