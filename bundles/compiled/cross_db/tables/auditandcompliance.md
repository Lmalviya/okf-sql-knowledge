---
type: PostgreSQL Table
title: auditandcompliance
description: '20 columns: recordregistry, audtrailstate, findtally, critfindnum, remedstate, remeddue, authnotify, bordermech, transimpassess, localreqs, datamapstate, sysintstate, accreqnum, delreqnum, rectreqnum, portreqnum, resptimeday. Joins to compliance, dataprofile, vendormanagement.'
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
| `profjoin` | integer | INT referencing DataProfile(ProfileTrace). Ties this audit to a specific data profile. |
| `compjoin` | integer | INT referencing Compliance(ComplianceTrace). Links the audit to a compliance record. |
| `vendjoin` | integer | INT referencing VendorManagement(VendorTrace). Connects this record to a specific vendor. |
| `recordregistry` | character | CHAR(10) optional cross-reference for older 'RecordID'. |
| `audtrailstate` | USER-DEFINED | auditstatus_enum enumerating the audit trail status. Currently possible values: (Complete, Missing, Partial). |
| `findtally` | smallint | SMALLINT storing the count of audit findings identified. |
| `critfindnum` | smallint | SMALLINT counting how many critical findings were discovered. |
| `remedstate` | character varying | VARCHAR(40) describing remediation status (e.g., 'Pending', 'In Progress'). Currently possible values: (In Progress, Not Started, Completed). |
| `remeddue` | date | DATE specifying the deadline for remediation actions. |
| `authnotify` | character varying | VARCHAR(40) describing if/when authorities must be notified. Currently possible values: (Not Required, Required, Submitted). |
| `bordermech` | character varying | VARCHAR(40) capturing cross-border mechanism (SCC, BCR, etc.) if relevant. Currently possible values: (SCCs, Adequacy Decision, Derogations, BCRs). |
| `transimpassess` | text | TEXT describing any transfer impact assessment for cross-border data flows. Currently possible values: (Required, Completed, In Progress). |
| `localreqs` | text | TEXT detailing local requirements or constraints on the data flow. Currently possible values: (Not Met, Met, Partial). |
| `datamapstate` | character varying | VARCHAR(40) describing the data mapping status (complete, partial, etc.). Currently possible values: (Partial, Complete, Outdated). |
| `sysintstate` | character varying | VARCHAR(40) referencing the system integration status. Currently possible values: (Fully Integrated, Manual, Partial). |
| `accreqnum` | smallint | SMALLINT counting how many access requests have been received. |
| `delreqnum` | smallint | SMALLINT counting how many data deletion requests were filed. |
| `rectreqnum` | smallint | SMALLINT counting how many rectification (correction) requests were made. |
| `portreqnum` | smallint | SMALLINT counting how many data portability requests were received. |
| `resptimeday` | numeric | NUMERIC(4,1) capturing the average or allowed response time (days) to subject requests. |

# Joins

* `compjoin` references `compliancetrace` in [compliance](/tables/compliance.md).
* `profjoin` references `profiletrace` in [dataprofile](/tables/dataprofile.md).
* `vendjoin` references `vendortrace` in [vendormanagement](/tables/vendormanagement.md).

# Related knowledge

* [Audit Finding Severity (AFS)](/knowledge/audit-finding-severity.md)
* [Data Subject Request Load (DSRL)](/knowledge/data-subject-request-load.md)
* [AuditAndCompliance.RespTimeDay](/knowledge/auditandcompliance-resptimeday.md)
* [Data Subject Request Pressure (DSRP)](/knowledge/data-subject-request-pressure.md)
* [Request Breakdown](/knowledge/request-breakdown.md)
* [Slow Remediation Timeline](/knowledge/slow-remediation-timeline.md)
* [Nearing Remediation Deadline](/knowledge/nearing-remediation-deadline.md)
* [High Vendor Risk Concentration](/knowledge/high-vendor-risk-concentration.md)
