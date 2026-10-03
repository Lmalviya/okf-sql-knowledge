---
type: PostgreSQL Table
title: compliancecase
description: '21 columns: regfilestat, disclosecmp, brokrepstat, exchnotif, prevviol, comprate, risksc, alertlvl, invstprior, casestat, revfreq, lastrevdt, nextrevdt, monitint, survsys, detectmth, fposrate, modelconf. Joins to advancedbehavior, transactionrecord.'
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_schema.txt
  title: insider schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_column_meaning_base.json
  title: insider column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `compreg` | character varying, primary key | VARCHAR(50). Primary key for a compliance‑case record. |
| `transref` | character varying | VARCHAR(50). Foreign‑key to TransactionRecord.TransReg that triggered the case. |
| `regfilestat` | USER-DEFINED | regulatory_filing_status_enum (enum: 'Delayed', 'Missing', 'Current'). Status of mandatory regulatory filings. |
| `disclosecmp` | USER-DEFINED | disclosure_compliance_enum (enum: 'Full', 'Non-compliant', 'Partial'). Disclosure compliance status. |
| `brokrepstat` | USER-DEFINED | broker_reporting_status_enum (enum: 'Incomplete', 'Late', 'Complete'). Broker‑dealer reporting standing. |
| `exchnotif` | USER-DEFINED | exchange_notification_enum (enum: 'Warning', 'Inquiry'). Exchange notifications issued. |
| `prevviol` | integer | INT. Count of previous compliance violations on record. |
| `comprate` | USER-DEFINED | compliance_rating_enum (enum: 'A', 'B', 'C', 'D'). Overall compliance rating grade. |
| `risksc` | numeric | NUMERIC(7,4). Composite compliance risk score (e.g., 0.3270). |
| `alertlvl` | USER-DEFINED | alert_level_enum (enum: 'Low', 'Medium', 'High', 'Critical'). Current alert severity. |
| `invstprior` | USER-DEFINED | investigation_priority_enum (enum: 'Low', 'Medium', 'High'). Priority assigned for investigation. |
| `casestat` | USER-DEFINED | case_status_enum (enum: 'Investigation', 'Monitoring', 'Closed'). Lifecycle state of the compliance case. |
| `revfreq` | USER-DEFINED | review_frequency_enum (enum: 'Daily', 'Weekly', 'Monthly'). Frequency of periodic reviews. |
| `lastrevdt` | date | DATE. Date of the last formal case review. |
| `nextrevdt` | date | DATE. Scheduled date for the next review. |
| `monitint` | USER-DEFINED | monitoring_intensity_enum (enum: 'Standard', 'Enhanced', 'Intensive'). Ongoing monitoring intensity level. |
| `survsys` | USER-DEFINED | surveillance_system_enum (enum: 'Primary', 'Secondary', 'Multiple'). Surveillance system(s) producing the alert. |
| `detectmth` | USER-DEFINED | detection_method_enum (enum: 'Automated', 'Manual', 'Hybrid'). How the behaviour was detected. |
| `fposrate` | numeric | NUMERIC(5,2). False‑positive rate of the detection model (e.g., 4.10). |
| `modelconf` | numeric | NUMERIC(7,4). Confidence score returned by the detection algorithm (e.g., 0.9132). |
| `abhvref` | character varying | VARCHAR(50). Optional foreign‑key to AdvancedBehavior.AbhvReg ties deeper pattern analytics to the case. |

# Joins

* `abhvref` references `abhvreg` in [advancedbehavior](/tables/advancedbehavior.md).
* `transref` references `transreg` in [transactionrecord](/tables/transactionrecord.md).

# Related knowledge

* [Compliance Recidivism Score (CRS)](/knowledge/compliance-recidivism-score.md)
* [Elevated Regulatory Scrutiny](/knowledge/elevated-regulatory-scrutiny.md)
* [Problematic Compliance History](/knowledge/problematic-compliance-history.md)
* [Event-Driven Trader](/knowledge/event-driven-trader.md)
* [Compliance Rating Grade](/knowledge/compliance-rating-grade.md)
