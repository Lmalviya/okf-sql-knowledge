---
type: PostgreSQL Table
title: eventsandclub
description: '5 columns: clubjdate, participation_summary. Joins to membershipandspending, socialcommunity.'
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
| `eventsreg` | character varying, primary key | A VARCHAR(20) primary key for events & club records (e.g., 'EVC001'). |
| `eventssocialpivot` | character varying | A VARCHAR(20) FK referencing SocialCommunity(SocialReg). |
| `eventsmemberpivot` | character varying | A VARCHAR(20) FK referencing MembershipAndSpending(MemberReg). |
| `clubjdate` | date | A DATE the fan joined the club (if applicable). |
| `participation_summary` | jsonb | JSONB column. Summarizes fan participation in events and fan club activities, including event attendance, voting participation, and club contribution level. |

# JSON fields

* `participation_summary.event_attendance.evtpart`: An enum (EventParticipation_enum) describing event participation (Regular, Rare, Always, Never).
* `participation_summary.event_attendance.offevtatt`: A SMALLINT capturing how many offline events the fan attended (e.g., 2).
* `participation_summary.event_attendance.onevtatt`: A SMALLINT capturing how many online events the fan attended (e.g., 5).
* `participation_summary.event_attendance.meetatt`: A SMALLINT counting meet-and-greet or fan meeting attendance (e.g., 1).
* `participation_summary.event_attendance.concatt`: A SMALLINT capturing concert attendance (e.g., 0 for none).
* `participation_summary.engagement.votepartrate`: A DECIMAL(4,1) measuring how often the fan participates in voting (e.g., '75.0').
* `participation_summary.engagement.camppart`: An enum (CampaignParticipation_enum) for participation in idol or brand campaigns (Selective, All, Active).
* `participation_summary.club.clubstat`: An enum (FanClubStatus_enum) describing fan club membership (Non-member, Premium, Elite, Basic).
* `participation_summary.club.clubcontrib`: An enum (FanClubContribution_enum) capturing the fan’s contribution level (Medium, Outstanding, Low, High).

# Joins

* `eventsmemberpivot` references `memberreg` in [membershipandspending](/tables/membershipandspending.md).
* `eventssocialpivot` references `socialreg` in [socialcommunity](/tables/socialcommunity.md).

# Related knowledge

* [Event Champion](/knowledge/event-champion.md)
