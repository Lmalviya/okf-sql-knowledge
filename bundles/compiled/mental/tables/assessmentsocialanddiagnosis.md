---
type: PostgreSQL Table
title: assessmentsocialanddiagnosis
description: '20 columns: recstatus, socsup, faminv, relqual, workfunc, socfunc, adlfunc, strslvl, copskill, resscr, inlevel, motivlevel, primdx, secdx, dxdurm, prevhosp, lasthospdt, qolscr, funcimp. Joins to assessmentbasics.'
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
| `asdkey` | character varying, primary key | A VARCHAR(30) primary key matching ABKey from AssessmentBasics (FK). |
| `recstatus` | USER-DEFINED | An enum (recoverystatus_enum) describing recovery status (Relapse, Stable, Advanced, Early). |
| `socsup` | USER-DEFINED | An enum (socialsupportlevel_enum) measuring social support (Strong, Limited, Moderate). |
| `faminv` | USER-DEFINED | An enum (familyinvolvement_enum) indicating family involvement level (Low, High, Medium). |
| `relqual` | USER-DEFINED | An enum (relationshipquality_enum) describing overall relationship quality (Poor, Conflicted, Good, Fair). |
| `workfunc` | USER-DEFINED | An enum (workfunctioning_enum) referencing work functioning (Disabled, Poor, Fair, Good). |
| `socfunc` | USER-DEFINED | An enum (socialfunctioning_enum) referencing social functioning (Isolated, Fair, Good, Poor). |
| `adlfunc` | USER-DEFINED | An enum (adlfunctioning_enum) describing ADL performance (Minimal Help, Independent, Moderate Help, Dependent). |
| `strslvl` | numeric | A NUMERIC(3,1) measuring perceived stress level (e.g., 6.0). |
| `copskill` | USER-DEFINED | An enum (copingskills_enum) capturing coping skill quality (Good, Poor, Fair, Limited). |
| `resscr` | numeric | A NUMERIC(3,1) measuring resilience (e.g., 5.5). |
| `inlevel` | USER-DEFINED | An enum (insightlevel_enum) describing insight (Fair, Good, Poor). |
| `motivlevel` | USER-DEFINED | An enum (motivationlevel_enum) referencing motivation (High, Low, Medium). |
| `primdx` | USER-DEFINED | An enum (primarydx_enum) for the primary diagnosis (Anxiety, PTSD, Bipolar, Schizophrenia, Depression). |
| `secdx` | USER-DEFINED | An enum (secondarydx_enum) for secondary diagnosis (OCD, Personality Disorder, Substance Use, Eating Disorder). |
| `dxdurm` | smallint | A SMALLINT specifying diagnosis duration in months (e.g., 12). |
| `prevhosp` | smallint | A SMALLINT counting past hospitalizations (e.g., 2). |
| `lasthospdt` | date | A DATE capturing the date of the last hospitalization (e.g., '2025-01-10'). |
| `qolscr` | smallint | A SMALLINT measuring Quality of Life score (0–100). |
| `funcimp` | USER-DEFINED | An enum (functionalimpairment_enum) describing functional impairment (Severe, Moderate, Mild). |

# Joins

* `asdkey` references `abkey` in [assessmentbasics](/tables/assessmentbasics.md).

# Related knowledge

* [Patient Functional Impairment Score (PFIS)](/knowledge/patient-functional-impairment-score.md)
* [Social Support Effectiveness (SSE)](/knowledge/social-support-effectiveness.md)
* [Stable Recovery Patient](/knowledge/stable-recovery-patient.md)
* [Patient with Strong Recovery Capital](/knowledge/patient-with-strong-recovery-capital.md)
* [Patient with Severe Comorbid Distress Profile](/knowledge/patient-with-severe-comorbid-distress-profile.md)
