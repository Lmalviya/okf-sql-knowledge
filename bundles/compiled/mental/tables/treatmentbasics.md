---
type: PostgreSQL Table
title: treatmentbasics
description: '7 columns: curmed, medadh, medside, medchg, crisisint, therapy_details. Joins to encounters.'
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
| `encref` | character varying | A VARCHAR(30) FK referencing Encounters(EncKey). |
| `curmed` | text | A TEXT field listing current medications (e.g., 'SSRIs, Mood stabilizer'). |
| `medadh` | USER-DEFINED | An enum (medicationadherence_enum) for medication adherence (Medium, Low, Non-compliant, High). |
| `medside` | USER-DEFINED | An enum (medicationsideeffects_enum) describing side effect severity (Mild, Moderate, Severe). |
| `medchg` | USER-DEFINED | An enum (medicationchanges_enum) for medication changes (Dose Adjustment, Augmentation, Switch). |
| `crisisint` | numeric | A NUMERIC(2,1) capturing any crisis interventions count or measure (e.g., 2.0). |
| `therapy_details` | jsonb | JSONB column. Captures details about the therapy provided, including type, frequency, duration, engagement, and changes. |

# JSON fields

* `therapy_details.type`: An enum (therapytype_enum) describing therapy modality (DBT, Group, Psychodynamic, CBT).
* `therapy_details.frequency`: An enum (therapyfrequency_enum) describing therapy frequency (Biweekly, Monthly, Weekly).
* `therapy_details.duration_months`: A SMALLINT capturing the therapy duration in months (e.g., 6).
* `therapy_details.engagement`: An enum (therapyengagement_enum) describing engagement (Medium, High, Low, Non-compliant).
* `therapy_details.changes`: An enum (therapychanges_enum) for therapy changes (Frequency Change, Modality Change, Therapist Change).

# Joins

* `encref` references `enckey` in [encounters](/tables/encounters.md).

# Related knowledge

* [Non-Compliant Patient](/knowledge/non-compliant-patient.md)
* [Patient with High Crisis & Low Support Profile](/knowledge/patient-with-high-crisis-low-support-profile.md)
