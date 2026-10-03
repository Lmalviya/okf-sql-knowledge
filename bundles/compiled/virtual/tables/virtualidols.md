---
type: PostgreSQL Table
title: virtualidols
description: '7 columns: nametag, kindtag, debdate, assocgroup, genretag, primlang.'
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_schema.txt
  title: virtual schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_column_meaning_base.json
  title: virtual column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `entityreg` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying the virtual idol (e.g., 'IDOL001'). |
| `nametag` | character varying | A VARCHAR(100) for the idol’s name or stage name. |
| `kindtag` | USER-DEFINED | An enum (IdolType_enum) describing the idol's nature (2D, AI Generated, 3D, Mixed Reality). |
| `debdate` | date | A DATE for the idol's debut (e.g., '2023-06-01'). |
| `assocgroup` | character varying | A VARCHAR(100) naming the idol's company or group affiliation. |
| `genretag` | USER-DEFINED | An enum (IdolGenre_enum) indicating the idol’s main genre (Electronic, Dance, Pop, Traditional, Rock). |
| `primlang` | character varying | A VARCHAR(50) referencing the idol's primary performance language (e.g., 'English'). |

# Related knowledge

* [virtualidols.kindtag](/knowledge/virtualidols-kindtag.md)
