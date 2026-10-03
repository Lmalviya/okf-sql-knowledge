---
type: PostgreSQL Table
title: artifactratings
description: '11 columns: histsignrating, researchvalrating, exhibitvalrating, cultscore, publicaccessrating, eduvaluerating, conservediff, treatcomplexity, matstability, deteriorrate. Joins to artifactscore.'
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_schema.txt
  title: museum schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_column_meaning_base.json
  title: museum column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `artref` | character | CHAR(10) FOREIGN KEY referencing ArtifactsCore(ArtRegistry). Links the record to a specific artifact. |
| `histsignrating` | smallint | SMALLINT rating for historical significance (scale is flexible). |
| `researchvalrating` | integer | INT rating for research value (range is flexible). |
| `exhibitvalrating` | integer | INT rating evaluating the artifact’s exhibition value (scale is flexible). |
| `cultscore` | smallint | SMALLINT measuring the artifact’s cultural importance (common range or flexible scale). |
| `publicaccessrating` | smallint | SMALLINT rating the artifact’s public accessibility or appeal (scale is flexible). |
| `eduvaluerating` | bigint | BIGINT rating for how much educational value the artifact provides (scale is flexible). |
| `conservediff` | USER-DEFINED | VARCHAR(100) describing difficulty in conserving the artifact (possible values: 'Medium', 'High', 'Low'). |
| `treatcomplexity` | character | CHAR(10) indicating treatment complexity (possible values: 'Complex', 'Moderate', 'Simple'). |
| `matstability` | character varying | VARCHAR(30) for material stability classification (possible values: 'Unstable', 'Stable', 'Moderate'). |
| `deteriorrate` | text | TEXT field detailing the specific deterioration rate or pattern (e.g., 'Moderate', 'Rapid', 'Slow'). |

# Joins

* `artref` references `artregistry` in [artifactscore](/tables/artifactscore.md).

# Related knowledge

* [Conservation Priority Index (CPI)](/knowledge/conservation-priority-index.md)
* [High-Value Artifact](/knowledge/high-value-artifact.md)
* [Dynasty Value Artifact](/knowledge/dynasty-value-artifact.md)
* [ArtifactRatings.HistSignRating](/knowledge/artifactratings-histsignrating.md)
* [High-Value Category](/knowledge/high-value-category.md)
