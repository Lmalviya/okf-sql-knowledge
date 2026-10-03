---
type: PostgreSQL Table
title: users
description: '10 columns: regmoment, typelabel, seglabel, substatus, subdays, ageval, gendlbl, occulbl, testgrp, user_preferences.'
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_schema.txt
  title: news schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_column_meaning_base.json
  title: news column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `regmoment` | date | A DATE indicating when the user registered (e.g., '2024-05-10'). |
| `typelabel` | USER-DEFINED | An enum (usertype_enum) representing the user type (Trial, Premium, Free). |
| `seglabel` | USER-DEFINED | An enum (usersegment_enum) describing the user's segment (New, Dormant, Active, Regular). |
| `substatus` | USER-DEFINED | An enum (subscriptionstatus_enum) indicating subscription status (Premium, Enterprise, Basic). |
| `subdays` | integer | An INT specifying how many days the user has been subscribed (e.g., 60). |
| `ageval` | integer | An INT capturing the user's age in years (e.g., 30). |
| `gendlbl` | USER-DEFINED | An enum (usergender_enum) for the user's gender (M, F, Other). |
| `occulbl` | USER-DEFINED | An enum (useroccupation_enum) describing the user's occupation (Retired, Professional, Other, Student). |
| `testgrp` | USER-DEFINED | An enum (abtestgroup_enum) labeling which A/B test group the user belongs to (Control, Variant_A, Variant_B). |
| `user_preferences` | jsonb | JSONB column. Stores user-related preferences and feedback details, including interests, activity level, and satisfaction metrics. |

# JSON fields

* `user_preferences.interests`: A TEXT field storing user interests (e.g., 'sports, technology').
* `user_preferences.activity_level`: An enum (useractivitylevel_enum) describing the user's activity level (Low, High, Medium).
* `user_preferences.preference_score`: A NUMERIC(5,2) capturing how much the user’s profile aligns with personalized content (e.g., 75.50).
* `user_preferences.feedback.type`: An enum (userfeedback_enum) capturing user feedback (Like, Dislike).
* `user_preferences.feedback.value`: An enum (feedbackscore_enum) referencing the numeric feedback rating (1.0–5.0).
* `user_preferences.feedback.category`: An enum (feedbackcategory_enum) describing the feedback category (Relevance, Content, Format).
* `user_preferences.satisfaction_score`: A NUMERIC(5,2) measuring user satisfaction (e.g., 80.50).

# Related knowledge

* [User Subscription Value (USV)](/knowledge/user-subscription-value.md)
* [User Demographic Score (UDS)](/knowledge/user-demographic-score.md)
