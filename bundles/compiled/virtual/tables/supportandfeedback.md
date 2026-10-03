---
type: PostgreSQL Table
title: supportandfeedback
description: '12 columns: techissuerpt, supptix, fbsubs, survpart, betapart, featreqsubs, bugsubs, satrate, npsval. Joins to interactions, preferencesandsettings.'
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
| `supportreg` | character varying, primary key | A VARCHAR(20) primary key for support/feedback records (e.g., 'SUP001'). |
| `supportinteractpivot` | character varying | A VARCHAR(20) FK referencing Interactions(ActivityReg). |
| `supportprefpivot` | character varying | A VARCHAR(20) FK referencing PreferencesAndSettings(PrefReg). |
| `techissuerpt` | smallint | A SMALLINT number of technical issues reported (e.g., 2). |
| `supptix` | smallint | A SMALLINT how many support tickets the fan opened (e.g., 1). |
| `fbsubs` | smallint | A SMALLINT count of feedback submissions (e.g., 3). |
| `survpart` | USER-DEFINED | An enum (SurveyParticipation_enum) describing survey participation (Never, Active, Occasional). |
| `betapart` | USER-DEFINED | An enum (BetaTestingParticipation_enum) for beta test participation (Former, Yes, No). |
| `featreqsubs` | smallint | A SMALLINT how many feature requests the fan submitted (e.g., 1). |
| `bugsubs` | smallint | A SMALLINT how many bug reports the fan submitted (e.g., 0). |
| `satrate` | numeric | A DECIMAL(3,1) overall satisfaction rating (e.g., '8.5'). |
| `npsval` | smallint | A SMALLINT Net Promoter Score value (e.g., 9). |

# Joins

* `supportinteractpivot` references `activityreg` in [interactions](/tables/interactions.md).
* `supportprefpivot` references `prefreg` in [preferencesandsettings](/tables/preferencesandsettings.md).

# Related knowledge

* [Support Efficiency Index (SEI)](/knowledge/support-efficiency-index.md)
* [Investment Recovery Period (IRP)](/knowledge/investment-recovery-period.md)
* [Premium Service Candidate](/knowledge/premium-service-candidate.md)
