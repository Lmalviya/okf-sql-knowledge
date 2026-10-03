---
type: Business Rule
title: Community Pillar
description: Identifies fans who form the foundation of the idol community
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 25
---

# Definition

A fan with CCI > 7, actfreq = 'Daily', membdays > 180, and community_engagement.group_involvement.grprole = 'Moderator' or community_engagement.group_involvement.grprole = 'Leader'. These fans play essential roles in maintaining community structure and culture.

# Columns used

* [membershipandspending](/tables/membershipandspending.md): `membdays`
* [engagement](/tables/engagement.md): `actfreq`
* [socialcommunity](/tables/socialcommunity.md): `community_engagement`

# Depends on

* [Community Contribution Index (CCI)](/knowledge/community-contribution-index.md)
