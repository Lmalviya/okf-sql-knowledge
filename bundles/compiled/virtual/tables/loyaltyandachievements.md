---
type: PostgreSQL Table
title: loyaltyandachievements
description: '8 columns: rankpos, inflscore, reputelv, trustval, reward_progress. Joins to engagement, eventsandclub.'
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
| `loyaltyreg` | character varying, primary key | A VARCHAR(20) primary key for loyalty & achievements (e.g., 'LOY001'). |
| `loyaltyeventspivot` | character varying | A VARCHAR(20) FK referencing EventsAndClub(EventsReg). |
| `loyaltyengagepivot` | character varying | A VARCHAR(20) FK referencing Engagement(EngageReg). |
| `rankpos` | integer | An INT rank position among all fans (e.g., 120). |
| `inflscore` | numeric | A DECIMAL(5,2) measuring influencer or leadership potential (e.g., '85.50'). |
| `reputelv` | USER-DEFINED | An enum (ReputationLevel_enum) describing the fan’s reputation (Respected, Elite, New, Established). |
| `trustval` | numeric | A DECIMAL(4,1) representing trust or reliability score (e.g., '9.2'). |
| `reward_progress` | jsonb | JSONB column. Aggregates data related to the fan’s loyalty rewards and achievements, including points, tier, badges, and special titles. |

# JSON fields

* `reward_progress.loyalty.loypts`: An INT storing loyalty points earned (e.g., 2500).
* `reward_progress.loyalty.rewtier`: An enum (RewardTier_enum) for the reward tier (Bronze, Platinum, Gold, Silver).
* `reward_progress.achievements.achcount`: An INT number of achievements unlocked (e.g., 5).
* `reward_progress.achievements.badgecoll`: An INT count of badges collected by the fan (e.g., 3).
* `reward_progress.achievements.spectitles`: An INT how many special titles the fan holds (e.g., 1).

# Joins

* `loyaltyengagepivot` references `engagereg` in [engagement](/tables/engagement.md).
* `loyaltyeventspivot` references `eventsreg` in [eventsandclub](/tables/eventsandclub.md).

# Related knowledge

* [loyaltyandachievements.reward_progress.loyalty.loypts](/knowledge/loyaltyandachievements-reward-progress-loyalty-loypts.md)
* [Event ROI Potential (ERP)](/knowledge/event-roi-potential.md)
* [Potential Ambassador](/knowledge/potential-ambassador.md)
