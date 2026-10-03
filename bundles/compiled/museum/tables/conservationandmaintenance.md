---
type: PostgreSQL Table
title: conservationandmaintenance
description: '19 columns: conservetreatstatus, treatpriority, lastcleaningdate, nextcleaningdue, cleanintervaldays, maintlog, incidentreportstatus, emergencydrillstatus, stafftrainstatus, budgetallocstatus, maintbudgetstatus, conservefreq, intervhistory, prevtreatments, treateffectiveness, reversibilitypotential. Joins to artifactscore, exhibitionhalls, surfaceandphysicalreadings.'
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
| `artrefmaintained` | character | A CHAR(10) NOT NULL foreign key referencing ArtifactsCore(ArtRegistry). Ties this record to the maintained artifact. |
| `hallrefmaintained` | character | A CHAR(8) foreign key referencing ExhibitionHalls(HallRegistry), if the conservation applies to a specific hall area. |
| `surfreadrefobserved` | bigint | A BIGINT foreign key referencing SurfaceAndPhysicalReadings(SurfPhysRegistry). Links to surface/physical readings used in this maintenance record. |
| `conservetreatstatus` | character varying | A VARCHAR(50) describing the status of conservation treatment (possible values: 'In Progress', 'Not Required', 'Scheduled'). |
| `treatpriority` | character | A CHAR(10) indicating the priority of the treatment (possible values: 'High', 'Medium', 'Low', 'Urgent'). |
| `lastcleaningdate` | date | A DATE specifying the last cleaning date of the artifact/hall/showcase. |
| `nextcleaningdue` | date | A DATE indicating when the next cleaning is scheduled or recommended. |
| `cleanintervaldays` | smallint | A SMALLINT capturing the recommended cleaning interval in days. |
| `maintlog` | text | A TEXT field describing any notes, log details, or issues encountered during maintenance activities (possible values: 'Updated', 'Pending', 'Review'). |
| `incidentreportstatus` | character varying | A VARCHAR(50) summarizing the status of any incident reports (possible values: 'Closed', 'Open'). |
| `emergencydrillstatus` | character | A CHAR(15) indicating whether emergency drills are 'Current', 'Overdue', 'Due', etc. |
| `stafftrainstatus` | character | A VARCHAR(20) describing staff training status (possible values: 'Current', 'Overdue', 'Due'). |
| `budgetallocstatus` | character varying | A VARCHAR(50) describing budget allocation status (possible values: 'Review Required', 'Insufficient', 'Adequate'). |
| `maintbudgetstatus` | character | A CHAR(15) indicating if the current maintenance budget is 'Limited', 'Depleted', 'Available', etc. |
| `conservefreq` | USER-DEFINED | A VARCHAR(30) describing the frequency of conservation efforts (possible values: 'Rare', 'Occasional', 'Frequent'). |
| `intervhistory` | text | A TEXT field detailing the intervention or treatment history (possible values: 'Extensive', 'Minimal', 'Moderate'). |
| `prevtreatments` | smallint | A SMALLINT counting how many significant treatments have been done previously on this artifact/hall. |
| `treateffectiveness` | character varying | A VARCHAR(100) summarizing how effective previous treatments were (possible values: 'Low', 'Medium', 'High'). |
| `reversibilitypotential` | USER-DEFINED | A TEXT field describing if and how treatments can be reversed (possible values: 'Medium', 'High', 'Low'). |

# Joins

* `artrefmaintained` references `artregistry` in [artifactscore](/tables/artifactscore.md).
* `hallrefmaintained` references `hallrecord` in [exhibitionhalls](/tables/exhibitionhalls.md).
* `surfreadrefobserved` references `surfphysregistry` in [surfaceandphysicalreadings](/tables/surfaceandphysicalreadings.md).

# Related knowledge

* [Conservation Emergency](/knowledge/conservation-emergency.md)
* [Conservation Budget Crisis](/knowledge/conservation-budget-crisis.md)
* [Conservation Backlog Risk (CBR)](/knowledge/conservation-backlog-risk.md)
