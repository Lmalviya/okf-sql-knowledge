---
type: PostgreSQL Table
title: fans
description: '7 columns: nicklabel, regmoment, tierstep, ptsval, statustag, personal_attributes.'
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
| `userregistry` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying each fan record (e.g., 'FAN001'). |
| `nicklabel` | character varying | A VARCHAR(100) storing the fan's chosen nickname or handle. |
| `regmoment` | date | A DATE noting when the fan first registered (e.g., '2025-02-15'). |
| `tierstep` | smallint | A SMALLINT that captures the fan's level or tier progression (e.g., 1, 2, 3). |
| `ptsval` | integer | An INT holding the fan's accumulated points or score within the system. |
| `statustag` | USER-DEFINED | An enum (FanStatus_enum) describing the fan’s current status (Inactive, VIP, Active, Blocked). |
| `personal_attributes` | jsonb | JSONB column. Groups personal demographic and interest-related attributes of the fan, including age, gender, location, language preference, occupation, and interests. |

# JSON fields

* `personal_attributes.demographics.agecount`: A SMALLINT representing the fan’s age in years.
* `personal_attributes.demographics.gendertype`: An enum (FanGender_enum) indicating the fan’s gender (Other, Male, Undisclosed, Female).
* `personal_attributes.demographics.locnation`: A VARCHAR(100) for the fan’s country location (e.g., 'USA', 'Japan').
* `personal_attributes.demographics.loctown`: A VARCHAR(100) for the fan’s city or town location.
* `personal_attributes.preferences.langpref`: An enum (FanLang_enum) specifying the fan's main language (Multiple, Korean, English, Japanese, Chinese).
* `personal_attributes.preferences.occupath`: An enum (FanOccupation_enum) describing the fan’s occupation (Professional, Student, Other, Creative).
* `personal_attributes.preferences.interestset`: An enum (FanInterests_enum) indicating the fan's primary interest area (Technology, Anime, Art, Music, Gaming).

# Related knowledge

* [fans.statustag](/knowledge/fans-statustag.md)
* [fans.tierstep](/knowledge/fans-tierstep.md)
* [Event ROI Potential (ERP)](/knowledge/event-roi-potential.md)
* [Superfan](/knowledge/superfan.md)
* [Tier Acceleration Factor (TAF)](/knowledge/tier-acceleration-factor.md)
* [Retention Risk Superfan](/knowledge/retention-risk-superfan.md)
