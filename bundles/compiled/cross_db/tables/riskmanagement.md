---
type: PostgreSQL Table
title: riskmanagement
description: '21 columns: recordregistry, riskassess, riskmitstate, secureaction, breachnotify, incidentplan, incidentcount, breachcount, nearmissnum, avgresolhrs, slapct, costusd, penusd, coveragestate, residrisklevel, ctrleff, compscore, maturitylevel, nextrevdate, planstate. Joins to dataflow.'
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_schema.txt
  title: cross_db schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_column_meaning_base.json
  title: cross_db column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `flowlink` | character | CHAR(10) referencing DataFlow(RecordRegistry), linking this risk record to a specific data flow. |
| `recordregistry` | character | CHAR(10) formerly 'RecordID'; can be used for cross-references or historical reasons. |
| `riskassess` | numeric | NUMERIC(4,2) storing the assessed risk score (0–100 or custom). |
| `riskmitstate` | character varying | VARCHAR(40) describing how the risk is being mitigated. Currently possible values: (Pending, Partial, Implemented). |
| `secureaction` | text | TEXT describing security measures or controls used to reduce identified risks. Currently possible values: (Adequate, Strong, Insufficient). |
| `breachnotify` | text | TEXT outlining the procedure for breach notification if a security event occurs. Currently possible values: (Partial, Established, Missing). |
| `incidentplan` | text | TEXT capturing the incident response plan or steps for handling security/operational events. Currently possible values: (Missing, Active, Outdated). |
| `incidentcount` | smallint | SMALLINT counting incidents recorded for this data flow or scenario. |
| `breachcount` | smallint | SMALLINT counting data breaches recorded. |
| `nearmissnum` | smallint | SMALLINT enumerating near misses (close calls that didn't escalate). |
| `avgresolhrs` | numeric | NUMERIC(5,2) average incident resolution time in hours. |
| `slapct` | numeric | NUMERIC(4,2) indicating SLA (Service Level Agreement) compliance percentage (0–100%). |
| `costusd` | numeric | NUMERIC(11,2) capturing the cost of compliance in USD (security, risk measures, etc.). |
| `penusd` | numeric | NUMERIC(11,2) storing potential or actual penalty/fine risk in USD. |
| `coveragestate` | character varying | VARCHAR(40) describing insurance coverage status (e.g., 'Full', 'Partial', 'None'). Currently possible values for discovered data: (Limited, Adequate). |
| `residrisklevel` | character varying | VARCHAR(40) naming the residual risk level after mitigation (Low, Medium, High, etc.). Currently possible values: (Medium, High, Low). |
| `ctrleff` | numeric | NUMERIC(4,2) rating the effectiveness of current controls (0–100). |
| `compscore` | numeric | NUMERIC(4,2) measuring overall compliance posture (0–100 or custom). |
| `maturitylevel` | character varying | VARCHAR(40) describing the maturity of processes (Initial, Managed, Optimized, etc.). Currently possible values: (Optimized, Managed, Initial). |
| `nextrevdate` | date | DATE specifying when the next risk/compliance review is scheduled. |
| `planstate` | character varying | VARCHAR(45) capturing improvement or remediation plan status (e.g., 'Planned', 'Completed'). Currently possible values: (On Track, Not Started, Delayed). |

# Joins

* `flowlink` references `recordregistry` in [dataflow](/tables/dataflow.md).

# Related knowledge

* [Risk Exposure Score (RES)](/knowledge/risk-exposure-score.md)
* [Compliance Cost Ratio (CCR)](/knowledge/compliance-cost-ratio.md)
* [RiskManagement.RiskAssess](/knowledge/riskmanagement-riskassess.md)
* [RiskManagement.CtrlEff](/knowledge/riskmanagement-ctrleff.md)
* [Security Control Cost Ratio (SCCR)](/knowledge/security-control-cost-ratio.md)
* [Incident Resolution Efficiency (IRE)](/knowledge/incident-resolution-efficiency.md)
* [Compliance Overhead Ratio (COR)](/knowledge/compliance-overhead-ratio.md)
