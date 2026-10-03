---
type: PostgreSQL Table
title: patients
description: '16 columns: patage, patgender, pateth, edulevel, empstat, maristat, livingarr, insurtype, insurstat, disabstat, housestable, cultfactor, stigmaimp, finstress. Joins to clinicians.'
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
| `patkey` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying each patient (e.g., 'PAT001'). |
| `patage` | smallint | A SMALLINT indicating the patient's age in years. |
| `patgender` | USER-DEFINED | An enum (patientgender_enum) for the patient's gender (Other, F, M). |
| `pateth` | USER-DEFINED | An enum (patientethnicity_enum) indicating the patient's ethnicity (Other, Hispanic, African, Asian, Caucasian). |
| `edulevel` | USER-DEFINED | An enum (educationlevel_enum) describing highest education achieved (High School, Other, Bachelor, Master, Doctorate). |
| `empstat` | USER-DEFINED | An enum (employmentstatus_enum) capturing employment status (Retired, Employed, Unemployed, Disabled, Student). |
| `maristat` | USER-DEFINED | An enum (maritalstatus_enum) describing marital status (Widowed, Married, Single, Divorced). |
| `livingarr` | USER-DEFINED | An enum (livingarrangement_enum) for living arrangement (Alone, Partner, Family, Group Home, Homeless). |
| `insurtype` | USER-DEFINED | An enum (insurancetype_enum) referencing type of insurance (Medicaid, Medicare, Private). |
| `insurstat` | USER-DEFINED | An enum (insurancestatus_enum) describing insurance status (Pending, Approved, Denied). |
| `disabstat` | USER-DEFINED | An enum (disabilitystatus_enum) indicating disability status (Pending, Permanent, Temporary). |
| `housestable` | USER-DEFINED | An enum (housingstability_enum) describing housing stability (Homeless, Stable, At Risk, Unstable). |
| `cultfactor` | USER-DEFINED | An enum (culturalfactors_enum) capturing relevant cultural factors (Language, Beliefs, Family, Multiple). |
| `stigmaimp` | USER-DEFINED | An enum (stigmaimpact_enum) describing stigma impact (Moderate, Mild, Severe). |
| `finstress` | USER-DEFINED | An enum (financialstress_enum) describing financial stress level (Severe, Mild, Moderate). |
| `clinleadref` | character varying |  |

# Joins

* `clinleadref` references `clinkey` in [clinicians](/tables/clinicians.md).
