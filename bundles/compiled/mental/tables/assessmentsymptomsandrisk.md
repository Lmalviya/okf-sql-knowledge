---
type: PostgreSQL Table
title: assessmentsymptomsandrisk
description: '9 columns: suicideation, suicrisk, selfharm, violrisk, subuse, subusefreq, subusesev, mental_health_scores. Joins to assessmentbasics.'
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
| `asrkey` | character varying, primary key | A VARCHAR(30) primary key matching ABKey from AssessmentBasics (FK). |
| `suicideation` | USER-DEFINED | An enum (suicidalideation_enum) capturing suicidal ideation (Intent, Active, Plan, Passive). |
| `suicrisk` | USER-DEFINED | An enum (suiciderisk_enum) describing suicide risk level (Medium, High, Low, Severe). |
| `selfharm` | USER-DEFINED | An enum (selfharm_enum) indicating self-harm history (Recent, Past, Current). |
| `violrisk` | USER-DEFINED | An enum (violencerisk_enum) for violence risk (Medium, Low, High). |
| `subuse` | USER-DEFINED | An enum (substanceuse_enum) describing which substance is used (Cannabis, Opioids, Alcohol, Multiple). |
| `subusefreq` | USER-DEFINED | An enum (substanceusefrequency_enum) for how often substances are used (Daily, Never, Occasional, Regular). |
| `subusesev` | USER-DEFINED | An enum (substanceuseseverity_enum) describing severity (Mild, Moderate, Severe). |
| `mental_health_scores` | jsonb | JSONB column. Aggregates scores related to mental health symptoms and risk factors, such as depression, anxiety, and other symptom metrics. |

# JSON fields

* `mental_health_scores.depression.phq9_score`: A SMALLINT for PHQ-9 score (0–27).
* `mental_health_scores.depression.phq9_severity`: An enum (phq9severity_enum) for depression severity (Moderately Severe, Mild, Severe, Moderate).
* `mental_health_scores.anxiety.gad7_score`: A SMALLINT for GAD-7 score (0–21).
* `mental_health_scores.anxiety.gad7_severity`: An enum (gad7severity_enum) for anxiety severity (Mild, Moderate, Severe).
* `mental_health_scores.symptom_scores`: ['A NUMERIC(3,1) measuring mood status (e.g., 5.0).', 'A NUMERIC(3,1) measuring anxiety level (e.g., 4.5).', 'A NUMERIC(3,1) measuring sleep quality (e.g., 3.0).', 'A NUMERIC(3,1) measuring appetite (e.g., 2.5).', 'A NUMERIC(3,1) measuring energy (e.g., 6.0).', 'A NUMERIC(3,1) measuring concentration (e.g., 5.5).', 'A NUMERIC(3,1) measuring interest/enjoyment (e.g., 4.0).', 'A NUMERIC(3,1) measuring hopelessness (e.g., 2.0).']

# Joins

* `asrkey` references `abkey` in [assessmentbasics](/tables/assessmentbasics.md).

# Related knowledge

* [Suicide Risk Prevalence (SRP)](/knowledge/suicide-risk-prevalence.md)
* [High-Risk Patient](/knowledge/high-risk-patient.md)
* [Complex Care Needs](/knowledge/complex-care-needs.md)
* [Patient with Severe Comorbid Distress Profile](/knowledge/patient-with-severe-comorbid-distress-profile.md)
* [High Severity, High Risk Patient Group](/knowledge/high-severity-high-risk-patient-group.md)
