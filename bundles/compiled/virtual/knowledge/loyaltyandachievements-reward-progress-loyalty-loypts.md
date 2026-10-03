---
type: Value Illustration
title: loyaltyandachievements.reward_progress.loyalty.loypts
description: Explains the accumulation and application value of loyalty points
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 9
---

# Definition

Loyalty points (loypts) are cumulative rewards for fan activities: 0-1000 points is entry-level (redeemable for basic digital items); 1001-5000 points is intermediate level (redeemable for limited-time privileges and mid-level digital items); 5001-20000 points is advanced level (redeemable for limited merchandise and activity priorities); above 20000 points is expert level (invitations to participate in platform decisions and idol development). Points are typically earned through logins, purchases, and activity participation.

# Columns used

* [loyaltyandachievements](/tables/loyaltyandachievements.md): `reward_progress`

# Used by

* [Loyalty Value Ratio (LVR)](/knowledge/loyalty-value-ratio.md)
