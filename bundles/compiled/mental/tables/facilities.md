---
type: PostgreSQL Table
title: facilities
description: '8 columns: rsource, envstress, lifeimpact, seasonpat, leglissue, ssystemchg, support_and_resources.'
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
| `fackey` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying the facility (e.g., 'FAC001'). |
| `rsource` | USER-DEFINED | An enum (referralsource_enum) for how the patient was referred (Self, Court, Physician, Emergency, Family). |
| `envstress` | USER-DEFINED | An enum (environmentalstressors_enum) describing stressors in the environment (Mild, Moderate, Severe). |
| `lifeimpact` | USER-DEFINED | An enum (lifeeventsimpact_enum) showing how life events impact the patient (Mild, Moderate, Severe). |
| `seasonpat` | USER-DEFINED | An enum (seasonalpattern_enum) capturing any seasonal pattern in symptoms (Summer, Winter, Variable). |
| `leglissue` | USER-DEFINED | An enum (legalissues_enum) describing the patient's legal issues (Resolved, Pending, Ongoing). |
| `ssystemchg` | USER-DEFINED | An enum (supportsystemchanges_enum) describing changes in support system (Variable, Improved, Declined). |
| `support_and_resources` | jsonb | JSONB column. Stores information about the facility's support services, community resources, emergency contacts, and plan statuses. |

# JSON fields

* `support_and_resources.support_services`: A VARCHAR(200) listing available or recommended support services (e.g., 'Peer support group, vocational rehab').
* `support_and_resources.community_resources`: An enum (communityresources_enum) describing local resource availability (Limited, Comprehensive, Adequate).
* `support_and_resources.emergency_contact`: A VARCHAR(200) capturing emergency contact info or phone numbers (e.g., 'Hotline: 1-800-xxx').
* `support_and_resources.plans.safety_plan_status`: An enum (safetyplanstatus_enum) for the safety plan status (Needs Update, In Place, Not Needed).
* `support_and_resources.plans.crisis_plan_status`: An enum (crisisplanstatus_enum) for the crisis plan status (Not Needed, Needs Update, In Place).
