---
type: PostgreSQL Table
title: humanresources
description: '4 columns: staffingprofile. Joins to disasterevents, operations.'
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
| `hrregistry` | character varying, primary key | A VARCHAR(20) primary key for the human resources record (e.g., 'HR0001'). |
| `hrdistref` | character varying | A VARCHAR(20) referencing DisasterEvents(DistRegistry), associating staff with an event (e.g., 'DIST0001'). |
| `hropsref` | character varying | A VARCHAR(20) referencing Operations(OpsRegistry), linking staff resources to operations (e.g., 'OPS0001'). |
| `staffingprofile` | jsonb | JSONB column. Consolidates staffing information, including personnel counts by specialty, volunteer resources, and operational readiness metrics. |

# JSON fields

* `staffingprofile.personnel.total`: An INTEGER counting total staff members (e.g., 50).
* `staffingprofile.personnel.medical`: An INT specifying how many medical personnel (e.g., 10).
* `staffingprofile.personnel.logistics`: An INTEGER for logistics staff count (e.g., 8).
* `staffingprofile.personnel.security`: An INT labeling security staff (e.g., 5).
* `staffingprofile.personnel.volunteers`: An INT enumerating the number of volunteers (e.g., 20).
* `staffingprofile.readiness.availability_percent`: A DECIMAL(5,2) for percentage of staff availability (e.g., 85.50).
* `staffingprofile.readiness.training_status`: An enum (TrainingState_enum) describing training progress; values: 'Complete', 'In Progress', 'Required'.
* `staffingprofile.readiness.ppe_status`: An enum (PPEStatus_enum) indicating PPE availability; values: 'Limited', 'Critical', 'Adequate'.
* `staffingprofile.readiness.comm_equipment`: An enum (CommEquipment_enum) for communication gear; values: 'Sufficient', 'Insufficient', 'Limited'.

# Joins

* `hrdistref` references `distregistry` in [disasterevents](/tables/disasterevents.md).
* `hropsref` references `opsregistry` in [operations](/tables/operations.md).

# Related knowledge

* [staffingProfile.readiness.ppe_status](/knowledge/staffingprofile-readiness-ppe-status.md)
* [Personnel Effectiveness Ratio (PER)](/knowledge/personnel-effectiveness-ratio.md)
* [Staffing to Need Ratio (SNR)](/knowledge/staffing-to-need-ratio.md)
* [Critical Health Response Requirement](/knowledge/critical-health-response-requirement.md)
