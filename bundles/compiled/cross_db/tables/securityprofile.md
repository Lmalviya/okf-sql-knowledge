---
type: PostgreSQL Table
title: securityprofile
description: '19 columns: recordregistry, encstate, encmeth, keymanstate, masklevel, anonmeth, psymstate, authmeth, authzframe, aclstate, apisecstate, logintcheck, logretdays, bkpstate, drecstate, bcstate. Joins to dataflow, dataprofile, riskmanagement.'
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
| `flowkey` | character | CHAR(10) referencing DataFlow(RecordRegistry). Associates security details with a data flow. |
| `riskkey` | integer | INT referencing RiskManagement(RiskTrace). Links security measures to a risk record. |
| `profilekey` | integer | INT referencing DataProfile(ProfileTrace). Ties security info to a data profile. |
| `recordregistry` | character | CHAR(10) optional cross-reference historically called 'RecordID'. |
| `encstate` | USER-DEFINED | encryptionstatus_enum. Possible values: (Full, Partial). |
| `encmeth` | character varying | VARCHAR(40) describing the encryption method used (AES, RSA, etc.). Currently possible values: (SM4, Custom, RSA-2048, AES-256). |
| `keymanstate` | character varying | VARCHAR(40) for key management status. Currently possible values: (Hybrid, Distributed, Centralized). |
| `masklevel` | USER-DEFINED | partialnone_enum enumerating data masking. Currently possible values: (Partial, Full). |
| `anonmeth` | character varying | VARCHAR(40) describing the anonymization methodology. Currently possible values: (T-Closeness, K-Anonymity, L-Diversity). |
| `psymstate` | character varying | VARCHAR(40) describing pseudonymization status. Currently possible values: (Partial, Applied). |
| `authmeth` | character varying | VARCHAR(40) specifying the authentication method (Basic, OAuth, SAML, etc.). Currently possible values: (Basic, SSO, MFA). |
| `authzframe` | character varying | VARCHAR(45) specifying the authorization framework (RBAC, ABAC, etc.). Currently possible values: (ABAC, Custom, RBAC). |
| `aclstate` | character varying | VARCHAR(30) describing the current access control status. Currently possible values: (Adequate, Strong, Weak). |
| `apisecstate` | character varying | VARCHAR(30) enumerating the API security posture. Currently possible values: (Vulnerable, Secure, Review Required). |
| `logintcheck` | character varying | VARCHAR(30) specifying the log integrity check mechanism. Currently possible values: (Pending, Passed, Failed). |
| `logretdays` | smallint | SMALLINT indicating how many days audit logs are retained. |
| `bkpstate` | character varying | VARCHAR(35) describing the backup status. Currently possible values: (Current, Failed, Outdated). |
| `drecstate` | character varying | VARCHAR(35) describing the disaster recovery status. Currently possible values: (Untested, Tested, Missing). |
| `bcstate` | character varying | VARCHAR(35) storing the business continuity status or plan stage. Currently possible values: (Active, Outdated, Review Required). |

# Joins

* `flowkey` references `recordregistry` in [dataflow](/tables/dataflow.md).
* `profilekey` references `profiletrace` in [dataprofile](/tables/dataprofile.md).
* `riskkey` references `risktrace` in [riskmanagement](/tables/riskmanagement.md).

# Related knowledge

* [Security Robustness Score (SRS)](/knowledge/security-robustness-score.md)
* [SecurityProfile.EncState](/knowledge/securityprofile-encstate.md)
* [SecurityProfile.LogRetDays](/knowledge/securityprofile-logretdays.md)
* [Security Posture Maturity (SPM)](/knowledge/security-posture-maturity.md)
