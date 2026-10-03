---
type: PostgreSQL Table
title: investigation
description: '20 columns: investstat, lawinterest, regrisklvl, compliancescore, investpriority, resptimemins, escalationlevel, casestatus, resolutiontimehours, actiontaken, followuprequired, reviewfrequency, nextreviewdate, notescount, dataretentionstatus, lastupdated, updatefrequencyhours. Joins to riskanalysis, securitymonitoring.'
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_schema.txt
  title: cybermarket schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_column_meaning_base.json
  title: cybermarket column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `investregistry` | character varying, primary key | Primary key (VARCHAR(30)) for an investigation record (e.g., 'INV-abc123'). |
| `investstat` | USER-DEFINED | An enum (InvestStat_enum) for investigation status (Monitoring, Closed, Active). |
| `lawinterest` | USER-DEFINED | An enum (RiskLevel_enum) for law enforcement interest (Low, Medium, High, Unknown). |
| `regrisklvl` | USER-DEFINED | An enum (RiskLevel_enum) describing regulatory risk (Low, Medium, High, Unknown). |
| `compliancescore` | numeric | A NUMERIC(4,2) (0–99.99) measuring how compliant the subject is (e.g., 75.50). |
| `investpriority` | USER-DEFINED | An enum (InvestPriority_enum) for priority (Low, Medium, High). |
| `resptimemins` | integer | An INT for average response time in minutes (e.g., 45). |
| `escalationlevel` | USER-DEFINED | An enum (EscalationLevel_enum) describing how far it's escalated (Level1, Level2, Level3). |
| `casestatus` | USER-DEFINED | An enum (CaseStatus_enum) describing the case state (New, In Progress, Resolved, Closed). |
| `resolutiontimehours` | smallint | A SMALLINT for hours from case open to resolution (e.g., 72). |
| `actiontaken` | USER-DEFINED | An enum (ActionTaken_enum) describing final actions (Termination, Warning, Restriction). |
| `followuprequired` | USER-DEFINED | An enum (FollowupRequired_enum) (Yes, No) for follow-up necessity. |
| `reviewfrequency` | USER-DEFINED | An enum (ReviewFrequency_enum) for re-check intervals (Weekly, Monthly, Daily). |
| `nextreviewdate` | date | A DATE specifying the next scheduled review (e.g., '2025-06-01'). |
| `notescount` | smallint | A SMALLINT tally of internal notes on the case (e.g., 4). |
| `dataretentionstatus` | USER-DEFINED | An enum (DataRetentionStatus_enum) describing how data is stored (Deleted, Active, Archived). |
| `lastupdated` | timestamp without time zone | A TIMESTAMP capturing last update time (e.g., '2025-03-30 14:00:00'). |
| `updatefrequencyhours` | integer | An INT for how often the case is updated or reviewed automatically (e.g., 24). |
| `secref` | character varying | FK referencing SecurityMonitoring(SecMonRegistry). Ties the investigation to security data. |
| `riskref` | character varying | FK referencing RiskAnalysis(RiskRegistry). Associates the investigation with a risk record. |

# Joins

* `riskref` references `riskregistry` in [riskanalysis](/tables/riskanalysis.md).
* `secref` references `secmonregistry` in [securitymonitoring](/tables/securitymonitoring.md).

# Related knowledge

* [Investigation Priority Score (IPS)](/knowledge/investigation-priority-score.md)
* [Priority Investigation Target](/knowledge/priority-investigation-target.md)
* [Market Vulnerability Index (MVI)](/knowledge/market-vulnerability-index.md)
* [Cross-Platform Risk Amplification (CPRA)](/knowledge/cross-platform-risk-amplification.md)
