---
type: PostgreSQL Table
title: vendormanagement
description: '19 columns: recordregistry, vendassess, vendsecrate, vendauddate, contrstate, contrexpire, dpastate, sccstate, bcrstate, docustate, polcomp, proccomp, trainstate, certstate, monstate, repstate, stakecomm. Joins to riskmanagement, securityprofile.'
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
| `secjoin` | integer | INT referencing SecurityProfile(SecurityTrace). Ties vendor data with a security profile. |
| `riskassoc` | integer | INT referencing RiskManagement(RiskTrace). Connects vendor data to risk management info. |
| `recordregistry` | character | CHAR(10) an optional cross-ref field, historically 'RecordID'. |
| `vendassess` | character varying | VARCHAR(40) describing vendor assessment status. Currently possible values: (Completed, In Progress, Due). |
| `vendsecrate` | USER-DEFINED | securityrating_enum enumerating vendor security rating. Currently possible values: (A, B, C, D). |
| `vendauddate` | date | DATE indicating when the vendor was last audited. |
| `contrstate` | character varying | VARCHAR(30) capturing the contract state. Currently possible values: (Active, Under Review, Expired). |
| `contrexpire` | date | DATE specifying when the current contract expires. |
| `dpastate` | character varying | VARCHAR(30) referencing Data Processing Agreement status. Currently possible values: (Required, Signed, Pending). |
| `sccstate` | character varying | VARCHAR(30) referencing Standard Contractual Clauses status. Currently possible values: (Implemented, Partial, Not Required). |
| `bcrstate` | character varying | VARCHAR(30) capturing the status of Binding Corporate Rules. Currently possible values: (Approved, Pending, Not Applicable). |
| `docustate` | character varying | VARCHAR(30) describing the vendor’s documentation completeness. Currently possible values: (Complete, Incomplete, Partial). |
| `polcomp` | character varying | VARCHAR(30) enumerating vendor’s policy compliance. Currently possible values: (Partial, Full, Non-compliant). |
| `proccomp` | character varying | VARCHAR(30) enumerating vendor’s procedure compliance status. Currently possible values: (Non-compliant, Full, Partial). |
| `trainstate` | character varying | VARCHAR(30) referencing the training status of vendor employees. Currently possible values: (Due, Overdue, Current). |
| `certstate` | character varying | VARCHAR(30) referencing certifications the vendor holds. Currently possible values: (Pending, Expired, Valid). |
| `monstate` | character varying | VARCHAR(30) storing the vendor’s monitoring status or approach. Currently possible values: (Inactive, Partial, Active). |
| `repstate` | character varying | VARCHAR(30) capturing the vendor’s reporting requirements or status. Currently possible values: (Delayed, Current, Overdue). |
| `stakecomm` | text | TEXT detailing stakeholder communication or engagement strategy for the vendor relationship. Currently possible values: (Limited, Poor, Regular). |

# Joins

* `riskassoc` references `risktrace` in [riskmanagement](/tables/riskmanagement.md).
* `secjoin` references `securitytrace` in [securityprofile](/tables/securityprofile.md).

# Related knowledge

* [Vendor Reliability Index (VRI)](/knowledge/vendor-reliability-index.md)
* [Non-Compliant Vendor](/knowledge/non-compliant-vendor.md)
* [VendorManagement.VendSecRate](/knowledge/vendormanagement-vendsecrate.md)
* [Vendor Compliance Burden (VCB)](/knowledge/vendor-compliance-burden.md)
