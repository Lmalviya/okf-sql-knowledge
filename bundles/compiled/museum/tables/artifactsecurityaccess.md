---
type: PostgreSQL Table
title: artifactsecurityaccess
description: '12 columns: loanstatus, insvalueusd, seclevel, accessrestrictions, docustatus, photodocu, condreportstatus, conserverecstatus, researchaccessstatus, digitalrecstatus. Joins to artifactratings, artifactscore.'
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_schema.txt
  title: museum schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_column_meaning_base.json
  title: museum column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `artref` | character | A CHAR(10) NOT NULL foreign key referencing ArtifactsCore(ArtRegistry). Links this security record to a specific artifact. |
| `ratingref` | bigint | A BIGINT foreign key referencing ArtifactRatings(RatingRecordRegistry). Associates this security record with a particular artifact rating, if relevant. |
| `loanstatus` | character | A CHAR(15) indicating the artifact’s loan status (possible values: 'On Loan', 'Available', 'Not Available'). |
| `insvalueusd` | numeric | A NUMERIC(15,2) specifying the artifact’s insured value in USD. |
| `seclevel` | character varying | A VARCHAR(50) describing the security level (possible values: 'Level 3', 'Level 2', 'Level 1'). |
| `accessrestrictions` | text | A TEXT field detailing constraints on handling/viewing (possible values: 'Public', 'Restricted', 'Limited'). |
| `docustatus` | character varying | A VARCHAR(60) indicating the completeness of documentation (possible values: 'Updating', 'Partial', 'Complete'). |
| `photodocu` | character varying | A VARCHAR(100) noting photographic documentation status (possible values: 'Outdated', 'Required', 'Recent'). |
| `condreportstatus` | character varying | A VARCHAR(80) describing the artifact’s condition report status (possible values: 'Current', 'Due', 'Overdue'). |
| `conserverecstatus` | character | A CHAR(20) summarizing conservation record status (possible values: 'Review Required', 'Pending', 'Updated'). |
| `researchaccessstatus` | character varying | A VARCHAR(40) indicating if the artifact is open to researchers (possible values: 'Limited', 'Available', 'Restricted'). |
| `digitalrecstatus` | text | A TEXT field specifying any digital records or scans (possible values: 'In Progress', 'Partial', 'Complete'). |

# Joins

* `artref` references `artregistry` in [artifactscore](/tables/artifactscore.md).
* `ratingref` references `ratingrecordregistry` in [artifactratings](/tables/artifactratings.md).

# Related knowledge

* [High-Value Artifact](/knowledge/high-value-artifact.md)
* [Visitor Crowd Risk](/knowledge/visitor-crowd-risk.md)
* [Security Risk Exposure (SRE)](/knowledge/security-risk-exposure.md)
* [High-Value Category](/knowledge/high-value-category.md)
