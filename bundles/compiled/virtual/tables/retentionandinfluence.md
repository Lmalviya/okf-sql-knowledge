---
type: PostgreSQL Table
title: retentionandinfluence
description: '10 columns: churnflag, reactcount, refcount, contreach, viralcont, trendpart, hashuse. Joins to engagement, loyaltyandachievements.'
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
| `retreg` | character varying, primary key | A VARCHAR(20) primary key for retention/influence records (e.g., 'RET001'). |
| `retainengagepivot` | character varying | A VARCHAR(20) FK referencing Engagement(EngageReg). |
| `retainloyaltypivot` | character varying | A VARCHAR(20) FK referencing LoyaltyAndAchievements(LoyaltyReg). |
| `churnflag` | USER-DEFINED | An enum (ChurnRisk_enum) capturing churn risk (High, Medium, Low, None). |
| `reactcount` | smallint | A SMALLINT how many times the fan reactivated after inactivity (e.g., 2). |
| `refcount` | smallint | A SMALLINT number of referrals the fan made (e.g., 3). |
| `contreach` | integer | An INT measuring content reach or audience size (e.g., 500). |
| `viralcont` | smallint | A SMALLINT how many viral posts or content pieces the fan created (e.g., 1). |
| `trendpart` | smallint | A SMALLINT times the fan participated in trending topics or challenges (e.g., 4). |
| `hashuse` | smallint | A SMALLINT count of hashtags the fan used (e.g., 10). |

# Joins

* `retainengagepivot` references `engagereg` in [engagement](/tables/engagement.md).
* `retainloyaltypivot` references `loyaltyreg` in [loyaltyandachievements](/tables/loyaltyandachievements.md).

# Related knowledge

* [retentionandinfluence.churnflag](/knowledge/retentionandinfluence-churnflag.md)
* [Retention Risk Factor (RRF)](/knowledge/retention-risk-factor.md)
* [Social Influence Multiplier (SIM)](/knowledge/social-influence-multiplier.md)
* [Social Amplifier](/knowledge/social-amplifier.md)
* [Event Champion](/knowledge/event-champion.md)
* [Social Conversion Rate (SCR)](/knowledge/social-conversion-rate.md)
* [Churn Risk Numeric Mapping](/knowledge/churn-risk-numeric-mapping.md)
