---
type: PostgreSQL Table
title: account
description: '9 columns: acctident, platident, plattype, acctcreatedate, acctagespan, acctstatus, acctcategory, authstatus.'
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_schema.txt
  title: fake schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_column_meaning_base.json
  title: fake column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `accindex` | character, primary key | A CHAR(12) primary key uniquely identifying each account record (e.g., 'AC1234567890'). |
| `acctident` | character varying | A VARCHAR(14) field holding an external-facing or system-defined account identifier (e.g., 'ACC2686094'). |
| `platident` | character varying | An 8-character field indicating which platform ID the account is associated with (e.g., 'PL784'). |
| `plattype` | USER-DEFINED | An enum (PlatformType_enum) describing the platform type (Microblog, Social Network, Video Platform, Forum). |
| `acctcreatedate` | date | A DATE indicating when the account was created (e.g., '2025-02-20'). |
| `acctagespan` | smallint | A SMALLINT showing the account’s age in days since creation (e.g., '45'). |
| `acctstatus` | USER-DEFINED | An enum (AccountStatus_enum) capturing the account status (Active, Deleted, Suspended, Dormant). |
| `acctcategory` | USER-DEFINED | An enum (AccountType_enum) labeling the account type (Personal, Bot, Hybrid, Business). |
| `authstatus` | USER-DEFINED | An enum (VerificationStatus_enum) describing the verification state (Unverified, Pending, Failed, Suspicious). |

# Related knowledge

* [Account Activity Frequency (AAF)](/knowledge/account-activity-frequency.md)
* [Dormant Bot](/knowledge/dormant-bot.md)
* [cluster identifier](/knowledge/cluster-identifier.md)
* [member account IDs](/knowledge/member-account-ids.md)
