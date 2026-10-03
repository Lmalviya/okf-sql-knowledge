---
type: Calculation
title: Monetization Value (MV)
description: Calculates the monetary value a fan brings to the platform over time
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 11
---

# Definition

MV = spendusd \times \left(1 + \frac{membdays}{365} \times 0.5\right) \times \left(1 + \frac{gifttot}{10} \times 0.2\right), \text{ where the formula adjusts spending based on membership duration and gift activity to reflect long-term value.}

# Columns used

* [interactions](/tables/interactions.md): `gifttot`
* [membershipandspending](/tables/membershipandspending.md): `membdays`, `spendusd`

# Used by

* [Fan Lifetime Value (FLV)](/knowledge/fan-lifetime-value.md)
* [Superfan](/knowledge/superfan.md)
* [Silent Supporter](/knowledge/silent-supporter.md)
* [Premium Engagement Ratio (PER)](/knowledge/premium-engagement-ratio.md)
* [Investment Recovery Period (IRP)](/knowledge/investment-recovery-period.md)
* [Loyalty Value Ratio (LVR)](/knowledge/loyalty-value-ratio.md)
* [Loyalty Underperformer](/knowledge/loyalty-underperformer.md)
* [Premium Service Candidate](/knowledge/premium-service-candidate.md)
