---
type: PostgreSQL Table
title: commerceandcollection
description: '9 columns: merchbuy, merchspendusd, digown, physown, collcomprate, tradelevel. Joins to engagement, membershipandspending.'
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
| `commercereg` | character varying, primary key | A VARCHAR(20) primary key for commerce/collection records (e.g., 'COM001'). |
| `commerceengagepivot` | character varying | A VARCHAR(20) FK referencing Engagement(EngageReg). |
| `commercememberpivot` | character varying | A VARCHAR(20) FK referencing MembershipAndSpending(MemberReg). |
| `merchbuy` | smallint | A SMALLINT tally of merchandise purchases (e.g., 5). |
| `merchspendusd` | numeric | A DECIMAL(10,2) total spent on merchandise in USD (e.g., 120.00). |
| `digown` | integer | An INT indicating how many digital items the fan owns (e.g., 20). |
| `physown` | integer | An INT indicating how many physical items the fan owns (e.g., 10). |
| `collcomprate` | numeric | A DECIMAL(5,1) measuring the fan’s collection completion percentage (e.g., '75.5'). |
| `tradelevel` | USER-DEFINED | An enum (TradingActivityLevel_enum) describing the fan’s trading or exchange activity (High, Low, Medium). |

# Joins

* `commerceengagepivot` references `engagereg` in [engagement](/tables/engagement.md).
* `commercememberpivot` references `memberreg` in [membershipandspending](/tables/membershipandspending.md).
