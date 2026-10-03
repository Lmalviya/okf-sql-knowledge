---
type: PostgreSQL Table
title: riskassessments
description: '7 columns: riskassesslevel, emergresponseplan, evacpriority, handlerestrictions, conservepriorityscore. Joins to artifactscore, exhibitionhalls.'
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
| `artrefconcerned` | character | A CHAR(10) NOT NULL foreign key referencing ArtifactsCore(ArtRegistry), linking this record to a specific artifact. |
| `hallrefconcerned` | character | A CHAR(8) foreign key referencing ExhibitionHalls(HallRegistry), indicating which hall is involved in this risk assessment (if any). |
| `riskassesslevel` | USER-DEFINED | A VARCHAR(50) describing the level of risk (possible values: 'Medium', 'High', 'Low'). |
| `emergresponseplan` | text | A TEXT field outlining the emergency response procedures if the risk materializes (possible values: 'Review Required', 'Under Revision', 'Updated'). |
| `evacpriority` | character varying | A CHAR(15) indicating the priority for evacuation (possible values: 'Priority 3', 'Priority 1', 'Priority 2'). |
| `handlerestrictions` | character varying | A VARCHAR(100) describing any handling restrictions (possible values: 'Minimal', 'Strict'). |
| `conservepriorityscore` | smallint | A SMALLINT rating (e.g., 1–10) indicating the urgency or priority for conservation actions based on identified risks. |

# Joins

* `artrefconcerned` references `artregistry` in [artifactscore](/tables/artifactscore.md).
* `hallrefconcerned` references `hallrecord` in [exhibitionhalls](/tables/exhibitionhalls.md).
