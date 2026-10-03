---
type: PostgreSQL Table
title: treatmentoutcomes
description: '14 columns: thprog, txadh, txresp, sideburd, txgoalstat, recgoalstat, sympimp, funcimpv, workstatchg, satscr, theralliance, txeng, txsat. Joins to treatmentbasics.'
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
| `txref` | integer | An INT FK referencing TreatmentBasics(TxKey). |
| `thprog` | USER-DEFINED | An enum (therapyprogress_enum) describing therapy progress (Fair, Good, Poor). |
| `txadh` | USER-DEFINED | An enum (treatmentadherence_enum) referencing overall treatment adherence (Non-compliant, Medium, Low, High). |
| `txresp` | USER-DEFINED | An enum (treatmentresponse_enum) for treatment response (Poor, Good, Partial). |
| `sideburd` | USER-DEFINED | An enum (sideeffectburden_enum) describing side effect burden (Mild, Moderate, Severe). |
| `txgoalstat` | USER-DEFINED | An enum (treatmentgoalsstatus_enum) for treatment goals status (Not Started, Achieved, In Progress, Modified). |
| `recgoalstat` | USER-DEFINED | An enum (recoverygoalsstatus_enum) for recovery goals status (Not Started, Achieved, In Progress, Modified). |
| `sympimp` | USER-DEFINED | An enum (symptomimprovement_enum) indicating symptom improvement (Moderate, Minimal, Significant). |
| `funcimpv` | USER-DEFINED | An enum (functionalimprovement_enum) capturing functional improvement (Moderate, Minimal, Significant). |
| `workstatchg` | USER-DEFINED | An enum (workstatuschanges_enum) referencing changes in work status (Leave, Reduced Hours, Terminated). |
| `satscr` | numeric | A NUMERIC(3,1) satisfaction score (0–10 scale) (e.g., 8.5). |
| `theralliance` | USER-DEFINED | An enum (therapeuticalliance_enum) describing alliance (Moderate, Poor, Strong, Weak). |
| `txeng` | USER-DEFINED | An enum (treatmentengagement_enum) describing overall engagement (Non-compliant, High, Medium, Low). |
| `txsat` | USER-DEFINED | An enum (treatmentsatisfaction_enum) describing treatment satisfaction (Medium, Dissatisfied, Low, High). |

# Joins

* `txref` references `txkey` in [treatmentbasics](/tables/treatmentbasics.md).

# Related knowledge

* [Treatment Adherence Rate (TAR)](/knowledge/treatment-adherence-rate.md)
* [Treatment-Resistant Patient](/knowledge/treatment-resistant-patient.md)
* [Stable Recovery Patient](/knowledge/stable-recovery-patient.md)
* [Low Engagement Risk](/knowledge/low-engagement-risk.md)
* [Non-Compliant Patient](/knowledge/non-compliant-patient.md)
* [Therapeutic Alliance & Engagement Score (TAES)](/knowledge/therapeutic-alliance-engagement-score.md)
* [Recovery Trajectory Index (RTI)](/knowledge/recovery-trajectory-index.md)
