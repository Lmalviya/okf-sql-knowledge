---
type: PostgreSQL Table
title: scanconservation
description: '7 columns: harmassess, curerank, structstate, intervhistory, priordocs. Joins to projects, sites.'
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_schema.txt
  title: archeology schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_column_meaning_base.json
  title: archeology column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `arcref` | character varying | Full name: 'Project Reference'. Explanation: Associates conservation data with a project. Data type: VARCHAR(10). Example: 'PR7509'. |
| `zoneref` | character varying | Full name: 'Site Reference'. Explanation: Associates conservation data with a site code. Data type: VARCHAR(12). Example: 'SC9016'. |
| `harmassess` | character varying | Full name: 'Damage Assessment'. Explanation: Indicates severity of damage. Data type: VARCHAR(15). Possible categories: None, Moderate, Severe. |
| `curerank` | character varying | Full name: 'Conservation Priority'. Explanation: Priority level for conservation efforts. Data type: VARCHAR(15). Possible categories: Critical, Low, High. |
| `structstate` | character varying | Full name: 'Structural Stability'. Explanation: Stability level of the structure. Data type: VARCHAR(15). Possible categories: Stable, Moderate, Unstable. |
| `intervhistory` | text | Full name: 'Intervention History'. Explanation: Past restoration or intervention records. Data type: TEXT. Possible categories: None, Major, Minor. |
| `priordocs` | text | Full name: 'Previous Documentation'. Explanation: Level of existing documentation. Data type: TEXT. Possible categories: None, Partial, Complete. |

# Joins

* `arcref` references `arcregistry` in [projects](/tables/projects.md).
* `zoneref` references `zoneregistry` in [sites](/tables/sites.md).

# Related knowledge

* [Degradation Risk Zone](/knowledge/degradation-risk-zone.md)
* [StructState (Structural State)](/knowledge/structstate.md)
