---
type: PostgreSQL Table
title: beneficiariesandassessments
description: '10 columns: beneregister, vulnerabilityreview, needsassessstatus, distequityidx, benefeedbackscore, commengagelvl, localcapacitygrowth. Joins to disasterevents, operations.'
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_schema.txt
  title: disaster schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_column_meaning_base.json
  title: disaster column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `beneregistry` | character varying, primary key | A VARCHAR(20) primary key for the beneficiary or assessment record (e.g., 'BENE0001'). |
| `benedistref` | character varying | A VARCHAR(20) referencing DisasterEvents(DistRegistry), connecting beneficiaries to an event (e.g., 'DIST0001'). |
| `beneopsref` | character varying | A VARCHAR(20) referencing Operations(OpsRegistry), linking to the ongoing operations (e.g., 'OPS0001'). |
| `beneregister` | USER-DEFINED | An enum (BeneRegister_enum) describing beneficiary registration; values: 'Complete', 'Pending', 'Partial'. |
| `vulnerabilityreview` | USER-DEFINED | An enum (VulnerabilityReview_enum) indicating vulnerability assessment; values: 'Complete', 'Pending', 'In Progress'. |
| `needsassessstatus` | USER-DEFINED | An enum (NeedsAssessStatus_enum) capturing needs assessment status; values: 'Due', 'Overdue', 'Updated'. |
| `distequityidx` | numeric | A DECIMAL(5,2) for distribution equity index (e.g., 0.85). |
| `benefeedbackscore` | numeric | A DECIMAL(5,2) measuring beneficiary feedback (e.g., 90.50). |
| `commengagelvl` | USER-DEFINED | An enum (CommEngageLvl_enum) describing community engagement; values: 'High', 'Low', 'Medium'. |
| `localcapacitygrowth` | USER-DEFINED | An enum (LocalCapacityGrowth_enum) tracking local capacity building; values: 'Limited', 'Active'. |

# Joins

* `benedistref` references `distregistry` in [disasterevents](/tables/disasterevents.md).
* `beneopsref` references `opsregistry` in [operations](/tables/operations.md).

# Related knowledge

* [Beneficiary Satisfaction Index (BSI)](/knowledge/beneficiary-satisfaction-index.md)
* [Vulnerable Population Hotspot](/knowledge/vulnerable-population-hotspot.md)
* [Community Resilience Builder](/knowledge/community-resilience-builder.md)
* [Resource Distribution Equity (RDE)](/knowledge/resource-distribution-equity.md)
* [Financial Efficiency Metric (FEM)](/knowledge/financial-efficiency-metric.md)
* [Community Resilience Opportunity](/knowledge/community-resilience-opportunity.md)
* [Resource Distribution Inequity](/knowledge/resource-distribution-inequity.md)
