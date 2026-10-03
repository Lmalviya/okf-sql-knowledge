---
type: PostgreSQL Table
title: socialcommunity
description: '5 columns: collabcount, community_engagement. Joins to commerceandcollection, engagement.'
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
| `socialreg` | character varying, primary key | A VARCHAR(20) primary key for social community records (e.g., 'SOC001'). |
| `socialengagepivot` | character varying | A VARCHAR(20) FK referencing Engagement(EngageReg). |
| `socialcommercepivot` | character varying | A VARCHAR(20) FK referencing CommerceAndCollection(CommerceReg). |
| `collabcount` | smallint | A SMALLINT measuring how many collaborations the fan participated in (e.g., 3). |
| `community_engagement` | jsonb | JSONB column. Groups metrics related to the fan’s social network and community contributions, including network size, roles, and content creation activities. |

# JSON fields

* `community_engagement.network.socnetsz`: An INT capturing the size of the fan's social network (e.g., 500).
* `community_engagement.network.follcount`: An INT indicating how many followers the fan has (e.g., 300).
* `community_engagement.network.fingcount`: An INT indicating how many accounts the fan follows (e.g., 250).
* `community_engagement.network.friendcon`: An INT number of direct friend connections (e.g., 75).
* `community_engagement.group_involvement.grpmemb`: A SMALLINT counting group memberships (e.g., 2).
* `community_engagement.group_involvement.grprole`: An enum (GroupRole_enum) showing the fan's role (Member, Leader, Moderator).
* `community_engagement.content_creation.commcontrib`: An enum (CommunityContribution_enum) indicating how much the fan contributes (Low, High, Medium).
* `community_engagement.content_creation.contcreatestat`: An enum (ContentCreationStatus_enum) capturing the fan’s creation level (Active, Occasional).
* `community_engagement.content_creation.artsubs`: An INT counting art submissions by the fan (e.g., 4).
* `community_engagement.content_creation.ficsubs`: An INT counting fan fiction submissions (e.g., 2).
* `community_engagement.content_creation.coverperfcnt`: An INT number of cover performances (e.g., 1).
* `community_engagement.content_creation.ugcval`: An INT measuring user-generated content volume (e.g., 30 posts).
* `community_engagement.content_creation.contqualrate`: A DECIMAL(3,1) rating the overall quality of the fan’s content (e.g., '8.5').

# Joins

* `socialcommercepivot` references `commercereg` in [commerceandcollection](/tables/commerceandcollection.md).
* `socialengagepivot` references `engagereg` in [engagement](/tables/engagement.md).

# Related knowledge

* [socialcommunity.community_engagement.content_creation.contqualrate](/knowledge/socialcommunity-community-engagement-content-creation-contqualrate.md)
* [Community Contribution Index (CCI)](/knowledge/community-contribution-index.md)
* [Community Pillar](/knowledge/community-pillar.md)
