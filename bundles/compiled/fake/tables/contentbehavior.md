---
type: PostgreSQL Table
title: contentbehavior
description: '18 columns: postnum, postfreq, postintvar, cntsimscore, cntuniqscore, cntdiverseval, cntlangnum, cnttopicent, hashusepat, hashratio, mentionpat, mentionratio, urlsharefreq, urldomdiv, mediaupratio, mediareratio. Joins to sessionbehavior.'
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_schema.txt
  title: fake schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_column_meaning_base.json
  title: fake column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `cntref` | character, primary key | A CHAR(12) primary key for each content behavior record (e.g., 'CB1234567890'). |
| `cntsessref` | character | A CHAR(12) referencing SessionBehavior(SessRef) (e.g., 'SE1234567890'). |
| `postnum` | integer | An INTEGER counting total posts (e.g., '45'). |
| `postfreq` | numeric | NUMERIC(5,3) capturing post frequency (e.g., '1.235'). |
| `postintvar` | numeric | NUMERIC(6,3) variance in posting intervals (e.g., '0.457'). |
| `cntsimscore` | numeric | NUMERIC(4,2) content similarity (e.g., '0.85'). |
| `cntuniqscore` | numeric | NUMERIC(5,4) content uniqueness measure (e.g., '0.9432'). |
| `cntdiverseval` | numeric | NUMERIC(6,3) diversity of user’s content (e.g., '1.234'). |
| `cntlangnum` | USER-DEFINED | An enum (ContentLanguageCount_enum) showing language count in posts (1, 2, 3, 4, or 5). |
| `cnttopicent` | numeric | NUMERIC(4,3) topic entropy measure (e.g., '0.123'). |
| `hashusepat` | USER-DEFINED | An enum (HashtagUsagePattern_enum) describing hashtag usage (Trending, Normal, Random, Spam). |
| `hashratio` | numeric | NUMERIC(3,2) fraction of posts with at least one hashtag (e.g., '0.23'). |
| `mentionpat` | USER-DEFINED | An enum (MentionPattern_enum) describing mention usage (Normal, Random, Targeted, Spam). |
| `mentionratio` | numeric | NUMERIC(5,3) fraction of posts with mentions (e.g., '0.568'). |
| `urlsharefreq` | character varying | A VARCHAR(24) showing how often URLs are shared (e.g., 'HighFreq'). |
| `urldomdiv` | numeric | NUMERIC(4,2) domain diversity among shared URLs (e.g., '1.23'). |
| `mediaupratio` | numeric | NUMERIC(5,3) fraction of posts including media (e.g., '0.345'). |
| `mediareratio` | numeric | NUMERIC(6,4) how often the same media is reused (e.g., '0.2345'). |

# Joins

* `cntsessref` references `sessref` in [sessionbehavior](/tables/sessionbehavior.md).

# Related knowledge

* [Content Authenticity Score (CAS)](/knowledge/content-authenticity-score.md)
* [Content Manipulation Score (CMS)](/knowledge/content-manipulation-score.md)
* [Content Farm](/knowledge/content-farm.md)
* [contentbehavior.cntuniqscore](/knowledge/contentbehavior-cntuniqscore.md)
* [High-Impact Amplifier](/knowledge/high-impact-amplifier.md)
* [Total Post Frequency (TPF)](/knowledge/total-post-frequency.md)
