---
type: PostgreSQL Table
title: scanqc
description: '11 columns: accucheck, ctrlstate, valimeth, valistate, archstat, pubstat, copystat, refmention, remark. Joins to personnel, projects.'
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
| `arcref` | character varying | Full name: 'Project Reference'. Explanation: Points to a project for QC. Data type: VARCHAR(10). Example: 'PR7509'. |
| `crewref` | character | Full name: 'Operator Reference'. Explanation: Identifies the operator associated with QC. Data type: CHAR(8). Example: 'OP4641'. |
| `accucheck` | character varying | Full name: 'Accuracy Assessment'. Explanation: Indicates if accuracy check was done. Data type: VARCHAR(22). Possible categories: Pending, Completed, Not Required. |
| `ctrlstate` | character | Full name: 'Quality Control Status'. Explanation: State of QC checks. Data type: CHAR(10). Possible categories: Failed, Pending. |
| `valimeth` | character varying | Full name: 'Validation Method'. Explanation: How the data was validated (automated or manual). Data type: VARCHAR(18). Possible categories: Automated, Visual. |
| `valistate` | text | Full name: 'Validation Status'. Explanation: Final status of validation. Data type: TEXT. Possible categories: Rejected, Approved. |
| `archstat` | character varying | Full name: 'Archival Status'. Explanation: Indicates if data is archived. Data type: VARCHAR(10). Possible categories: Verified, Pending. |
| `pubstat` | character varying | Full name: 'Publication Status'. Explanation: Whether data is published, drafted, etc. Data type: VARCHAR(24). Possible categories: Draft, Submitted. |
| `copystat` | character | Full name: 'Copyright Status'. Explanation: Copyright or licensing restriction. Data type: CHAR(10). Possible categories: Reserved, Restricted, Open Access. |
| `refmention` | character varying | Full name: 'Data Citation'. Explanation: Reference or citation code for the data. Data type: VARCHAR(60). Possible categories: Citation-8447, Citation-6197, Citation-8090, Citation-2238. |
| `remark` | text | Full name: 'Additional Notes'. Explanation: Any free-text remarks or comments. Data type: TEXT. Example: 'Sell shoulder understand serious degree particular game.' |

# Joins

* `arcref` references `arcregistry` in [projects](/tables/projects.md).
* `crewref` references `crewregistry` in [personnel](/tables/personnel.md).
