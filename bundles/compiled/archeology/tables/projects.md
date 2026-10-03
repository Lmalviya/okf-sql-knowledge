---
type: PostgreSQL Table
title: projects
description: '5 columns: vesseltag, fundflux, authpin, authhalt.'
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
| `arcregistry` | character varying, primary key | Full name: 'Project ID'. Explanation: Primary key for Projects, a unique project identifier. Data type: VARCHAR(10). Example: 'PR7509'. |
| `vesseltag` | character varying | Full name: 'Project Name'. Explanation: Label or name for the project. Data type: VARCHAR(60). Example: 'Project Happy'. |
| `fundflux` | text | Full name: 'Funding Source'. Explanation: Source of funds for the project. Data type: TEXT. Example: 'Government'. |
| `authpin` | character | Full name: 'Permit Number'. Explanation: Authorization or permit ID. Data type: CHAR(6). Example: 'PMT4719'. |
| `authhalt` | date | Full name: 'Permit Expiry Date'. Explanation: Date on which the permit expires. Data type: DATE. Example: '2025-12-05'. |
