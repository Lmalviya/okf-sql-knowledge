---
type: PostgreSQL Table
title: engagement
description: '12 columns: socintscore, engrate, actfreq, peaktime, actdayswk, avgsesscount, contpref, langpref, transuse. Joins to interactions, membershipandspending.'
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
| `engagereg` | character varying, primary key | A VARCHAR(20) primary key for engagement records (e.g., 'ENG001'). |
| `engageactivitypivot` | character varying | A VARCHAR(20) FK referencing Interactions(ActivityReg). |
| `engagememberpivot` | character varying | A VARCHAR(20) FK referencing MembershipAndSpending(MemberReg). |
| `socintscore` | numeric | A DECIMAL(6,2) rating social interaction (e.g., '85.20'). |
| `engrate` | numeric | A DECIMAL(6,3) indicating engagement rate (e.g., '0.512'). |
| `actfreq` | USER-DEFINED | An enum (InteractionFrequency_enum) for how often interactions occur (Weekly, Monthly, Occasional, Daily). |
| `peaktime` | USER-DEFINED | An enum (PeakActivityTime_enum) describing the highest activity period (Afternoon, Evening, Night, Morning). |
| `actdayswk` | smallint | A SMALLINT number of days per week the fan is active (e.g., 5). |
| `avgsesscount` | smallint | A SMALLINT average number of sessions per day/week (e.g., 3). |
| `contpref` | USER-DEFINED | An enum (ContentPreference_enum) capturing the fan's preferred content (Music, Dance, Gaming, Chat). |
| `langpref` | USER-DEFINED | An enum (ContentLanguagePreference_enum) for content language (Both, Original, Translated). |
| `transuse` | USER-DEFINED | An enum (TranslationUsage_enum) describing translation usage (Always, Sometimes, Never). |

# Joins

* `engageactivitypivot` references `activityreg` in [interactions](/tables/interactions.md).
* `engagememberpivot` references `memberreg` in [membershipandspending](/tables/membershipandspending.md).

# Related knowledge

* [engagement.actfreq](/knowledge/engagement-actfreq.md)
* [engagement.engrate](/knowledge/engagement-engrate.md)
* [Fan Engagement Index (FEI)](/knowledge/fan-engagement-index.md)
* [Social Influence Multiplier (SIM)](/knowledge/social-influence-multiplier.md)
* [Loyalty Progression Rate (LPR)](/knowledge/loyalty-progression-rate.md)
* [Churn Candidate](/knowledge/churn-candidate.md)
* [Silent Supporter](/knowledge/silent-supporter.md)
* [Community Pillar](/knowledge/community-pillar.md)
* [Multi-Idol Supporter](/knowledge/multi-idol-supporter.md)
* [Content Quality to Engagement Ratio (CQER)](/knowledge/content-quality-to-engagement-ratio.md)
* [Tier-Stuck Veteran](/knowledge/tier-stuck-veteran.md)
* [Content Preference Classification](/knowledge/content-preference-classification.md)
