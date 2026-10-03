---
type: PostgreSQL Table
title: personnel
description: '4 columns: crewlabel, leadregistry, leadlabel.'
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
| `crewregistry` | character, primary key | Full name: 'Operator ID'. Explanation: Primary key for Personnel, representing an operator. Data type: CHAR(8). Example: 'OP4641'. |
| `crewlabel` | character varying | Full name: 'Operator Name'. Explanation: Name or label for the operator. Data type: VARCHAR(50). Example: 'Joel Wallace'. |
| `leadregistry` | character | Full name: 'Supervisor ID'. Explanation: Identifies a supervisor. Data type: CHAR(8). Example: 'SV7658'. |
| `leadlabel` | character varying | Full name: 'Supervisor Name'. Explanation: Name of the supervisor. Data type: VARCHAR(40). Example: 'Michael Kaiser'. |
