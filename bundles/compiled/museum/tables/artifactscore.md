---
type: PostgreSQL Table
title: artifactscore
description: '6 columns: artname, artdynasty, artageyears, mattype, conservestatus.'
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
| `artregistry` | character, primary key | CHAR(10) PRIMARY KEY uniquely identifying each artifact record (e.g., 'ART000012'). |
| `artname` | character varying | VARCHAR(100) providing the artifact’s name or label (free text, no strict list). |
| `artdynasty` | character varying | VARCHAR(50) indicating the historical period/era/dynasty (e.g., 'Ming', 'Song', 'Qing', 'Han', 'Tang', 'Yuan'). No strict enumeration. |
| `artageyears` | integer | INT denoting the artifact’s approximate age in years (any integer value). |
| `mattype` | USER-DEFINED | CHAR(30) showing the artifact’s primary material (e.g., 'Stone', 'Textile', 'Bronze', 'Jade', 'Wood', 'Ceramic', 'Paper'). Could be enumerated by your policy but often open-ended. |
| `conservestatus` | USER-DEFINED | VARCHAR(150) describing the artifact’s current conservation condition. Possible values might include 'Excellent', 'Good', 'Fair', 'Poor', 'Critical'. |

# Related knowledge

* [Conservation Priority Index (CPI)](/knowledge/conservation-priority-index.md)
* [Material Deterioration Rate (MDR)](/knowledge/material-deterioration-rate.md)
* [Conservation Emergency](/knowledge/conservation-emergency.md)
* [Conservation Budget Crisis](/knowledge/conservation-budget-crisis.md)
* [Organic Material Vulnerability](/knowledge/organic-material-vulnerability.md)
* [ArtifactsCore.ConserveStatus](/knowledge/artifactscore-conservestatus.md)
