---
type: PostgreSQL Table
title: clinicians
description: '11 columns: clinconf, assesslim, docustat, billcode, nxtrevdt, carecoord, refneed, fuptype, fupfreq. Joins to facilities.'
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
| `clinkey` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying the clinician (e.g., 'CLN001'). |
| `clinconf` | USER-DEFINED | An enum (clinicianconfidence_enum) capturing the clinician's confidence (Medium, Low, High). |
| `assesslim` | USER-DEFINED | An enum (assessmentlimitations_enum) describing any limitations (Cognitive, Engagement, Language). |
| `docustat` | USER-DEFINED | An enum (documentationstatus_enum) for documentation status (Complete, Incomplete, Pending). |
| `billcode` | character varying | A VARCHAR(15) storing billing or service code (e.g., '99214'). |
| `nxtrevdt` | date | A DATE indicating next planned review date (e.g., '2025-06-01'). |
| `carecoord` | USER-DEFINED | An enum (carecoordination_enum) describing care coordination level (Intensive, Regular, Limited). |
| `refneed` | USER-DEFINED | An enum (referralneeds_enum) capturing referral needs (Services, Testing, Specialist). |
| `fuptype` | USER-DEFINED | An enum (followuptype_enum) describing follow-up type (Therapy, Routine, Urgent, Medication Check). |
| `fupfreq` | USER-DEFINED | An enum (followupfrequency_enum) describing follow-up frequency (Weekly, Quarterly, Biweekly, Monthly). |
| `facconnect` | character varying | A VARCHAR(20) FK referencing Facilities(FacKey), linking this clinician to a facility. |

# Joins

* `facconnect` references `fackey` in [facilities](/tables/facilities.md).
