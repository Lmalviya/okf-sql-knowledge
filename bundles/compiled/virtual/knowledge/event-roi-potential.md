---
type: Calculation
title: Event ROI Potential (ERP)
description: Estimates the potential return on investment for inviting a fan to exclusive events
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 18
---

# Definition

ERP = FLV \times \left(\frac{evtpart\_numeric}{3}\right) \times \left(\frac{tierstep}{5}\right) \times \left(1 + \frac{inflscore}{100}\right), \text{ where evtpart\_numeric maps participation\_summary.event\_attendance.evtpart enum values: Never=0, Rare=1, Regular=2, Always=3. Higher scores indicate fans likely to generate more value when included in events.}

# Columns used

* [fans](/tables/fans.md): `tierstep`
* [loyaltyandachievements](/tables/loyaltyandachievements.md): `inflscore`

# Depends on

* [Fan Lifetime Value (FLV)](/knowledge/fan-lifetime-value.md)

# Used by

* [Event Champion](/knowledge/event-champion.md)
