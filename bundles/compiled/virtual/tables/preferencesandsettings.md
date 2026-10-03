---
type: PostgreSQL Table
title: preferencesandsettings
description: '20 columns: privset, dsconsent, notifpref, commpref, markpref, langset, accessset, devcount, logfreq, lastlogdt, sesscount, timehrs, avgdailymin, peaksess, intconsist, platstable, connqual. Joins to membershipandspending, socialcommunity.'
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
| `prefreg` | character varying, primary key | A VARCHAR(20) primary key for preferences/settings (e.g., 'PREF001'). |
| `preferencesmemberpivot` | character varying | A VARCHAR(20) FK referencing MembershipAndSpending(MemberReg). |
| `preferencessocialpivot` | character varying | A VARCHAR(20) FK referencing SocialCommunity(SocialReg). |
| `privset` | USER-DEFINED | An enum (PrivacySettings_enum) for privacy level (Private, Friends Only, Public). |
| `dsconsent` | USER-DEFINED | An enum (DataSharingConsent_enum) capturing how much data the fan consents to share (Partial, Minimal, Full). |
| `notifpref` | USER-DEFINED | An enum (NotifPref_enum) describing notifications setting (Important, All). |
| `commpref` | USER-DEFINED | An enum (CommPref_enum) for communication method (SMS, Email, Push). |
| `markpref` | USER-DEFINED | An enum (MarkPref_enum) describing marketing preference (Opted In, Selective, Opted Out). |
| `langset` | USER-DEFINED | An enum (LangSet_enum) specifying how language is handled (Translated, Auto, Original). |
| `accessset` | USER-DEFINED | An enum (AccessSet_enum) describing access or UI customization (Standard, Custom, Enhanced). |
| `devcount` | smallint | A SMALLINT number of devices the fan uses with the service (e.g., 2). |
| `logfreq` | USER-DEFINED | An enum (LoginFrequency_enum) for login frequency (Rare, Monthly, Weekly, Daily). |
| `lastlogdt` | date | A DATE indicating last login date (e.g., '2025-03-15'). |
| `sesscount` | integer | An INT counting total sessions (e.g., 150). |
| `timehrs` | integer | An INT representing total hours spent online (e.g., 120). |
| `avgdailymin` | smallint | A SMALLINT average daily minutes used (e.g., 45). |
| `peaksess` | smallint | A SMALLINT peak number of concurrent sessions (e.g., 3). |
| `intconsist` | numeric | A DECIMAL(3,2) measuring interaction consistency (0.00–1.00) (e.g., '0.85'). |
| `platstable` | numeric | A DECIMAL(3,2) rating platform stability from the user’s perspective (0.00–1.00) (e.g., '0.90'). |
| `connqual` | USER-DEFINED | An enum (ConnectionQuality_enum) describing connectivity (Poor, Excellent, Good, Fair). |

# Joins

* `preferencesmemberpivot` references `memberreg` in [membershipandspending](/tables/membershipandspending.md).
* `preferencessocialpivot` references `socialreg` in [socialcommunity](/tables/socialcommunity.md).

# Related knowledge

* [Retention Risk Factor (RRF)](/knowledge/retention-risk-factor.md)
* [Churn Candidate](/knowledge/churn-candidate.md)
* [Silent Supporter](/knowledge/silent-supporter.md)
* [Content Quality Consistency (CQC)](/knowledge/content-quality-consistency.md)
