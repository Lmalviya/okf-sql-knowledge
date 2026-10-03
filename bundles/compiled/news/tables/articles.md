---
type: PostgreSQL Table
title: articles
description: '21 columns: catlabel, subcatlbl, pubtime, authname, srcref, wordlen, readsec, difflevel, freshscore, qualscore, sentscore, contrscore, tagset, conttype, contformat, accscore, mediacount, vidsec, paywall, engagement_metrics. Joins to users.'
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
| `catlabel` | USER-DEFINED | An enum (articlecategory_enum) for article category (Entertainment, Business, Sports, News, Technology). |
| `subcatlbl` | USER-DEFINED | An enum (articlesubcategory_enum) for article subcategory (International, Opinion, Local, Feature). |
| `pubtime` | timestamp without time zone | A TIMESTAMP for when the article was published (e.g., '2025-02-10 08:00:00'). |
| `authname` | character varying | A VARCHAR(200) capturing the article’s author (e.g., 'John Smith'). |
| `srcref` | character varying | A VARCHAR(150) referencing the article source or publication name (e.g., 'Reuters'). |
| `wordlen` | integer | An INT for the article's word count (e.g., 1200). |
| `readsec` | integer | An INT measuring the estimated reading time in seconds (e.g., 300). |
| `difflevel` | USER-DEFINED | An enum (articledifficultylevel_enum) describing the reading complexity (Basic, Intermediate, Advanced). |
| `freshscore` | numeric | A NUMERIC(5,2) measuring how fresh or recent the content is (e.g., 65.50). |
| `qualscore` | numeric | A NUMERIC(5,2) capturing an overall quality rating (e.g., 80.00). |
| `sentscore` | numeric | A NUMERIC(5,2) referencing sentiment positivity (e.g., 40.25). |
| `contrscore` | numeric | A NUMERIC(5,2) measuring controversy level (e.g., 10.50 = low controversy). |
| `tagset` | text | A TEXT field listing associated tags/keywords (e.g., 'politics, election'). |
| `conttype` | USER-DEFINED | An enum (contenttype_enum) describing the article's content type (Article, Gallery, Video, Interactive). |
| `contformat` | USER-DEFINED | An enum (contentformat_enum) specifying format (Mobile, Text, HTML, AMP). |
| `accscore` | numeric | A NUMERIC(5,2) referencing accessibility or ease-of-use score (e.g., 90.00). |
| `mediacount` | integer | An INT indicating how many media elements (images, videos) are included (e.g., 3). |
| `vidsec` | integer | An INT measuring video duration in seconds if it's a video-based article (e.g., 120). |
| `paywall` | USER-DEFINED | An enum (paywallstatus_enum) describing paywall status (Metered, Premium, Free). |
| `authref` | bigint | A BIGINT FK referencing Users(UserKey) if the author is also a user in the system. |
| `engagement_metrics` | jsonb | JSONB column. Aggregates metrics related to article engagement and performance, such as popularity, engagement rate, and social interactions. |

# JSON fields

* `engagement_metrics.popularity_score`: A NUMERIC(5,2) for the article's popularity score (e.g., 75.40).
* `engagement_metrics.engagement_rate`: A NUMERIC(5,2) capturing how engaging the article is (e.g., 55.75).
* `engagement_metrics.completion_rate`: A NUMERIC(5,2) for article completion rate (e.g., 45.50).
* `engagement_metrics.social.shares`: An INT counting how many times the article was shared on social platforms (e.g., 200).
* `engagement_metrics.social.comments`: An INT capturing the number of comments the article received (e.g., 50).
* `engagement_metrics.average_rating`: A NUMERIC(3,1) average user rating (e.g., 4.2).

# Joins

* `authref` references `userkey` in [users](/tables/users.md).

# Related knowledge

* [Article Quality Index (AQI)](/knowledge/article-quality-index.md)
* [Article Readability Score (ARS)](/knowledge/article-readability-score.md)
* [Adjusted Read Time Estimator (ARTE)](/knowledge/adjusted-read-time-estimator.md)
