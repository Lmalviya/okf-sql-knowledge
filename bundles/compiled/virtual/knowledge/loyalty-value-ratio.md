---
type: Calculation
title: Loyalty Value Ratio (LVR)
description: Evaluates the relationship between a fan's loyalty points and their economic value
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 37
---

# Definition

LVR = \frac{loypts}{MV \times 10}, \text{ where higher values indicate fans accumulating loyalty faster than their spending would predict.}

# Depends on

* [loyaltyandachievements.reward_progress.loyalty.loypts](/knowledge/loyaltyandachievements-reward-progress-loyalty-loypts.md)
* [Monetization Value (MV)](/knowledge/monetization-value.md)

# Used by

* [Loyalty Underperformer](/knowledge/loyalty-underperformer.md)
