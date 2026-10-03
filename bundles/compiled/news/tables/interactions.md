---
type: PostgreSQL Table
title: interactions
description: '13 columns: artval, intts, evttype, seqval, agentval, clkts, clkpos, clktype, clksrc, clkctx, inttype. Joins to recommendations, sessions.'
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
| `seshlink2` | bigint | A BIGINT FK referencing Sessions(SeshKey). |
| `reclink` | bigint | A BIGINT FK referencing Recommendations(RecKey). |
| `artval` | bigint | A BIGINT storing the article ID related to the interaction (non-FK). |
| `intts` | timestamp without time zone | A TIMESTAMP capturing when the interaction occurred (e.g., '2025-04-01 10:15:00'). |
| `evttype` | USER-DEFINED | An enum (eventtype_enum) describing the event (bookmark, click, scroll, share, view). |
| `seqval` | integer | An INT for the event's sequence or position in the session (e.g., 3). |
| `agentval` | USER-DEFINED | An enum (useragent_enum) describing the user agent (Desktop, App, Mobile, Tablet). |
| `clkts` | timestamp without time zone | A TIMESTAMP specifically for when a click event happened (if applicable). |
| `clkpos` | USER-DEFINED | An enum (clickposition_enum) capturing the click position (1–10). |
| `clktype` | USER-DEFINED | An enum (clicktype_enum) describing type of click (Related, Trending, Direct, Recommended). |
| `clksrc` | USER-DEFINED | An enum (clicksource_enum) referencing where the click originated (Article, Homepage, Search, External). |
| `clkctx` | USER-DEFINED | An enum (clickcontext_enum) capturing context of the click (Headline, Summary, Image, Author). |
| `inttype` | USER-DEFINED | An enum (interactiontype_enum) describing the type of user interaction (Scroll, Share, Click, Hover). |

# Joins

* `reclink` references `reckey` in [recommendations](/tables/recommendations.md).
* `seshlink2` references `seshkey` in [sessions](/tables/sessions.md).

# Related knowledge

* [Content Interaction Efficiency (CIE)](/knowledge/content-interaction-efficiency.md)
