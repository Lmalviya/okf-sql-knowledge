---
type: PostgreSQL Table
title: scanregistration
description: '9 columns: logaccumm, refmark, ctrlpts, logmethod, transform, errscale, errvalmm. Joins to personnel, projects.'
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
| `crewref` | character | Full name: 'Operator Reference'. Explanation: Operator ID who performed registration. Data type: CHAR(8). Example: 'OP4641'. |
| `arcref` | character varying | Full name: 'Project Reference'. Explanation: Project ID linked to registration data. Data type: VARCHAR(10). Example: 'PR7509'. |
| `logaccumm` | numeric | Full name: 'Registration Accuracy (mm)'. Explanation: Accuracy of the registration in mm. Data type: NUMERIC(5,3). Example: 0.84. |
| `refmark` | character varying | Full name: 'Reference Markers'. Explanation: Numeric codes for registration targets. Data type: VARCHAR(6). Possible categories: 40, 31, 25, 21. |
| `ctrlpts` | character varying | Full name: 'Control Points'. Explanation: Numeric codes for control points. Data type: VARCHAR(6). Possible categories: 73, 99, 6, 84. |
| `logmethod` | character varying | Full name: 'Registration Method'. Explanation: Method for aligning scans. Data type: VARCHAR(15). Possible categories: Target-based, Hybrid, Automatic. |
| `transform` | character varying | Full name: 'Transformation Matrix'. Explanation: Identifier for the transform matrix used. Data type: VARCHAR(15). Possible categories: Matrix-47, Matrix-113, Matrix-543. |
| `errscale` | character varying | Full name: 'Error Metrics'. Explanation: Type of error measurement. Data type: VARCHAR(20). Possible categories: Cloud-to-Mesh, Cloud-to-Cloud, RMSE. |
| `errvalmm` | numeric | Full name: 'Error Value (mm)'. Explanation: Measured error in millimeters. Data type: NUMERIC(6,3). Example: 6.962. |

# Joins

* `arcref` references `arcregistry` in [projects](/tables/projects.md).
* `crewref` references `crewregistry` in [personnel](/tables/personnel.md).

# Related knowledge

* [Registration Quality Threshold](/knowledge/registration-quality-threshold.md)
* [LogMethod (Registration Method)](/knowledge/logmethod.md)
* [Registration Accuracy Ratio (RAR)](/knowledge/registration-accuracy-ratio.md)
* [Digital Preservation Quality (DPQ)](/knowledge/digital-preservation-quality.md)
* [Registration Confidence Level](/knowledge/registration-confidence-level.md)
