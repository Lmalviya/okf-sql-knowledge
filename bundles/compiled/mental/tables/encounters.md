---
type: PostgreSQL Table
title: encounters
description: '11 columns: timemark, clinid, facid, missappt, txbarrier, nxapptdt, dqscore, assesscomplete. Joins to assessmentbasics, patients.'
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_schema.txt
  title: mental schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_column_meaning_base.json
  title: mental column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `enckey` | character varying, primary key | A VARCHAR(30) primary key identifying the encounter (e.g., 'ENC001'). |
| `timemark` | timestamp without time zone | A TIMESTAMP for when the encounter or record was created/logged. |
| `abref` | character varying | A VARCHAR(30) FK referencing AssessmentBasics(ABKey). |
| `patref` | character varying | A VARCHAR(20) FK referencing Patients(PatKey). |
| `clinid` | character varying | A VARCHAR(20) referencing the clinician ID (not an enforced FK). |
| `facid` | character varying | A VARCHAR(20) referencing the facility ID (not an enforced FK). |
| `missappt` | numeric | A NUMERIC(2,1) capturing how many appointments were missed or how frequently (e.g., 1.0). |
| `txbarrier` | USER-DEFINED | An enum (treatmentbarriers_enum) indicating barriers to treatment (Multiple, Time, Financial, Transportation). |
| `nxapptdt` | date | A DATE capturing the next appointment date (e.g., '2025-06-10'). |
| `dqscore` | smallint | A SMALLINT data quality score (0–100 scale). |
| `assesscomplete` | character varying | A VARCHAR(250) note on assessment completeness (e.g., 'Sections B & C incomplete'). |

# Joins

* `abref` references `abkey` in [assessmentbasics](/tables/assessmentbasics.md).
* `patref` references `patkey` in [patients](/tables/patients.md).

# Related knowledge

* [Average GAD-7 Score by Facility (AGSF)](/knowledge/average-gad-7-score-by-facility.md)
* [Patient Exhibiting Fragile Stability](/knowledge/patient-exhibiting-fragile-stability.md)
* [Stale Treatment Outcome Records](/knowledge/stale-treatment-outcome-records.md)
