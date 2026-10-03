---
type: PostgreSQL Table
title: conditionassessments
description: '6 columns: condassessscore, conserveassessdate, nextassessdue. Joins to artifactscore, lightandradiationreadings, showcases.'
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
| `artrefexamined` | text | TEXT NOT NULL FOREIGN KEY referencing ArtifactsCore(ArtRegistry). Links to the artifact under assessment. (In practice, should match CHAR(10) type if needed.) |
| `showcaserefexamined` | text | TEXT FOREIGN KEY referencing Showcases(ShowcaseReg). Ties the record to the showcase if it was part of the assessment. |
| `lightreadrefobserved` | bigint | BIGINT FOREIGN KEY referencing LightAndRadiationReadings(LightRadRegistry). Associates the assessment with relevant light data. |
| `condassessscore` | integer | INT rating or score representing the artifact/showcase condition (scale is flexible). |
| `conserveassessdate` | date | DATE when the conservation assessment took place. |
| `nextassessdue` | date | DATE by which the next condition assessment should occur. |

# Joins

* `artrefexamined` references `artregistry` in [artifactscore](/tables/artifactscore.md).
* `lightreadrefobserved` references `lightradregistry` in [lightandradiationreadings](/tables/lightandradiationreadings.md).
* `showcaserefexamined` references `showcasereg` in [showcases](/tables/showcases.md).
