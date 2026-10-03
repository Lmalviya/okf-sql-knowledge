---
type: PostgreSQL Table
title: recommendations
description: '11 columns: alglabel, stratlabel, posval, recpage, recsec, recscore, confval, divval, novval, seryval. Joins to articles.'
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
| `alglabel` | USER-DEFINED | An enum (recalgorithm_enum) describing the recommendation algorithm (Contextual, Content-based, Collaborative, Hybrid). |
| `stratlabel` | USER-DEFINED | An enum (recstrategy_enum) capturing strategy used (Trending, Editorial, Similar, Personalized). |
| `posval` | integer | An INT for the recommendation position or rank in a list (e.g., 3). |
| `recpage` | USER-DEFINED | An enum (recpage_enum) describing where the recommendation is displayed (Search, Category, Home, Article). |
| `recsec` | USER-DEFINED | An enum (recsection_enum) describing the section used for recommendation (Bottom, Sidebar, Related, Top). |
| `recscore` | numeric | A NUMERIC(5,2) capturing the recommendation relevance or ranking score (e.g., 85.40). |
| `confval` | numeric | A NUMERIC(5,2) measuring algorithm’s confidence (e.g., 70.00). |
| `divval` | numeric | A NUMERIC(5,2) rating how diverse the recommendation is (e.g., 20.00). |
| `novval` | numeric | A NUMERIC(5,2) measuring novelty (e.g., 50.00). |
| `seryval` | numeric | A NUMERIC(5,2) measuring serendipity factor (e.g., 10.25). |
| `artlink` | bigint | A BIGINT FK referencing Articles(ArtKey), linking recommended article with the recommendation record. |

# Joins

* `artlink` references `artkey` in [articles](/tables/articles.md).

# Related knowledge

* [Recommendation Relevance Score (RRS)](/knowledge/recommendation-relevance-score.md)
