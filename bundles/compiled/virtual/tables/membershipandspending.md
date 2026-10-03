---
type: PostgreSQL Table
title: membershipandspending
description: '7 columns: membkind, membdays, spendusd, spendfreq, paymethod. Joins to fans.'
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_schema.txt
  title: virtual schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_column_meaning_base.json
  title: virtual column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `memberreg` | character varying, primary key | A VARCHAR(20) primary key for membership & spending records (e.g., 'MEM001'). |
| `memberfanpivot` | character varying | A VARCHAR(20) FK referencing Fans(UserRegistry). |
| `membkind` | USER-DEFINED | An enum (MembershipType_enum) describing membership tier (Free, Basic, Diamond, Premium). |
| `membdays` | smallint | A SMALLINT capturing how many days the fan has been a member (e.g., 120). |
| `spendusd` | numeric | A DECIMAL(10,2) total USD spent (e.g., 350.75). |
| `spendfreq` | USER-DEFINED | An enum (SpendingFrequency_enum) for spending pattern (Occasional, Weekly, Monthly, Daily). |
| `paymethod` | USER-DEFINED | An enum (PaymentMethod_enum) indicating how the fan pays (Credit Card, Mobile Payment, PayPal, Crypto). |

# Joins

* `memberfanpivot` references `userregistry` in [fans](/tables/fans.md).

# Related knowledge

* [membershipandspending.membkind](/knowledge/membershipandspending-membkind.md)
* [Monetization Value (MV)](/knowledge/monetization-value.md)
* [Loyalty Progression Rate (LPR)](/knowledge/loyalty-progression-rate.md)
* [Community Pillar](/knowledge/community-pillar.md)
* [Whale](/knowledge/whale.md)
* [Tier Acceleration Factor (TAF)](/knowledge/tier-acceleration-factor.md)
* [Engagement-Deficient Whale](/knowledge/engagement-deficient-whale.md)
* [Tier-Stuck Veteran](/knowledge/tier-stuck-veteran.md)
* [Gift-Focused Supporter](/knowledge/gift-focused-supporter.md)
