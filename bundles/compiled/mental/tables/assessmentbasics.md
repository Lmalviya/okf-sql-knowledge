---
type: PostgreSQL Table
title: assessmentbasics
description: '9 columns: atype, amethod, adurmin, alang, avalid, respconsist, symptvalid. Joins to patients.'
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
| `abkey` | character varying, primary key | A VARCHAR(30) primary key for each assessment (e.g., 'AB001'). |
| `atype` | USER-DEFINED | An enum (assessmenttype_enum) capturing the assessment type (Initial, Emergency, Routine, Follow-up). |
| `amethod` | USER-DEFINED | An enum (assessmentmethod_enum) for how the assessment was done (Phone, Self-report, In-person, Telehealth). |
| `adurmin` | smallint | A SMALLINT indicating assessment duration in minutes (e.g., 45). |
| `alang` | USER-DEFINED | An enum (assessmentlanguage_enum) describing which language was used (Chinese, French, Spanish, English, Other). |
| `avalid` | USER-DEFINED | An enum (assessmentvalidity_enum) capturing validity (Questionable, Invalid, Valid). |
| `respconsist` | USER-DEFINED | An enum (responseconsistency_enum) describing response consistency (Medium, High, Low). |
| `symptvalid` | USER-DEFINED | An enum (symptomvalidity_enum) describing symptom validity (Questionable, Valid, Invalid). |
| `patownerref` | character varying | A VARCHAR(20) FK referencing Patients(PatKey), linking the assessment to its patient. |

# Joins

* `patownerref` references `patkey` in [patients](/tables/patients.md).
