---
type: PostgreSQL Table
title: moderationandcompliance
description: '11 columns: rptcount, warncount, violhist, modstat, contcomp, ageverif, payverif, idverif. Joins to interactions, socialcommunity.'
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
| `modreg` | character varying, primary key | A VARCHAR(20) primary key for moderation records (e.g., 'MOD001'). |
| `moderationinteractpivot` | character varying | A VARCHAR(20) FK referencing Interactions(ActivityReg). |
| `moderationsocialpivot` | character varying | A VARCHAR(20) FK referencing SocialCommunity(SocialReg). |
| `rptcount` | smallint | A SMALLINT count of how many times the fan was reported (e.g., 2). |
| `warncount` | smallint | A SMALLINT count of how many warnings were issued to the fan (e.g., 1). |
| `violhist` | USER-DEFINED | An enum (ViolationHistory_enum) describing any prior infractions (Major, Minor). |
| `modstat` | USER-DEFINED | An enum (ModerationStatus_enum) showing moderation status (Warning, Good Standing, Restricted). |
| `contcomp` | USER-DEFINED | An enum (ContentCompliance_enum) for compliance with content policy (Warning, Violation, Compliant). |
| `ageverif` | USER-DEFINED | An enum (AgeVerification_enum) indicating age verification state (Not Required, Verified, Pending). |
| `payverif` | USER-DEFINED | An enum (PaymentVerification_enum) verifying payment info (Pending, Verified). |
| `idverif` | character varying | A VARCHAR(50) capturing any identity verification code or status (e.g., 'IDCheck#123'). |

# Joins

* `moderationinteractpivot` references `activityreg` in [interactions](/tables/interactions.md).
* `moderationsocialpivot` references `socialreg` in [socialcommunity](/tables/socialcommunity.md).
