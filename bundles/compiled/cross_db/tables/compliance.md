---
type: PostgreSQL Table
title: compliance
description: '16 columns: recordregistry, legalbase, consentstate, consentcoll, consentexp, purplimit, purpdesc, gdprcomp, ccpacomp, piplcomp, loclawcomp, regapprovals, privimpassess, datasubjright. Joins to riskmanagement, vendormanagement.'
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
| `risktie` | integer | INT referencing RiskManagement(RiskTrace). Links compliance data to a specific risk record. |
| `vendortie` | integer | INT referencing VendorManagement(VendorTrace). Connects compliance info to a specific vendor record. |
| `recordregistry` | character | CHAR(10) optionally referencing an older 'RecordID'. May be used for cross references. |
| `legalbase` | character varying | VARCHAR(150) describing the legal basis for data processing (e.g., 'Consent', 'Legal Obligation'). Currently possible values: (Legal Obligation, Contract, Legitimate Interest, Consent). |
| `consentstate` | character varying | VARCHAR(30) capturing the status of consent (e.g., 'Obtained', 'Revoked'). Currently possible values: (Not Required, Valid, Expired, Pending). |
| `consentcoll` | date | DATE indicating when user consent was collected. |
| `consentexp` | date | DATE indicating when that consent expires or needs renewal. |
| `purplimit` | character varying | VARCHAR(300) specifying the purpose limitation or constraints (GDPR principle). Currently possible values: (General, Multiple, Specific). |
| `purpdesc` | text | TEXT describing the purpose for data processing in detail. Currently possible values: (Business Operations, Research, Marketing, Compliance). |
| `gdprcomp` | USER-DEFINED | compliancelevel_enum enumerating GDPR compliance level. Currently possible values: (Partial, Non-compliant, Compliant). |
| `ccpacomp` | USER-DEFINED | compliancelevel_enum enumerating CCPA compliance level. Currently possible values: (Compliant, Non-compliant, Partial). |
| `piplcomp` | USER-DEFINED | compliancelevel_enum enumerating PIPL compliance level. Currently possible values: (Non-compliant, Partial, Compliant). |
| `loclawcomp` | USER-DEFINED | compliancelevel_enum enumerating local law compliance. Currently possible values: (Non-compliant, Compliant, Partial). |
| `regapprovals` | character varying | VARCHAR(300) listing any regulatory approvals or licenses obtained. Currently possible values: (Obtained, Not Required, Pending). |
| `privimpassess` | text | TEXT capturing the privacy impact assessment details or outcome. Currently possible values: (Completed, In Progress, Required). |
| `datasubjright` | character varying | VARCHAR(40) describing data subject rights or status (access, erasure, portability, etc.). Currently possible values: (Partial, Fully Supported, Limited). |

# Joins

* `risktie` references `risktrace` in [riskmanagement](/tables/riskmanagement.md).
* `vendortie` references `vendortrace` in [vendormanagement](/tables/vendormanagement.md).

# Related knowledge

* [Cross-Border Compliance Gap](/knowledge/cross-border-compliance-gap.md)
* [Compliance.GdprComp](/knowledge/compliance-gdprcomp.md)
* [Regulatory Overload Flow](/knowledge/regulatory-overload-flow.md)
* [Cross-Border Compliance Exposure (CBCE)](/knowledge/cross-border-compliance-exposure.md)
* [Bandwidth Compliance Risk (BCR)](/knowledge/bandwidth-compliance-risk.md)
* [Incident-Prone Compliance Flow](/knowledge/incident-prone-compliance-flow.md)
