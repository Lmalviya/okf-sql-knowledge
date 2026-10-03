---
type: PostgreSQL Table
title: scanprocessing
description: '20 columns: flowsoft, flowhrs, proccpu, memusagegb, procgpu, stashloc, safebak, datalevel, metabench, coordframe, elevref, remaingb, stationlink, camcal, lensdist, colortune, flowstage, fmtver. Joins to equipment, sites.'
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_schema.txt
  title: archeology schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_column_meaning_base.json
  title: archeology column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `equipref` | character | Full name: 'Equipment Reference'. Explanation: Equipment ID used for processing. Data type: CHAR(10). Example: 'SN20065'. |
| `zoneref` | character varying | Full name: 'Site Reference'. Explanation: Site code for which processing applies. Data type: VARCHAR(12). Example: 'SC9016'. |
| `flowsoft` | character varying | Full name: 'Processing Software'. Explanation: Name of the software used. Data type: VARCHAR(25). Possible categories: RealityCapture, CloudCompare, Agisoft. |
| `flowhrs` | numeric | Full name: 'Processing Time (hours)'. Explanation: Time spent on processing. Data type: NUMERIC(5,2). Example: 21.9. |
| `proccpu` | smallint | Full name: 'CPU Usage (%)'. Explanation: CPU usage as an integer percentage. Data type: SMALLINT. Example: 81. |
| `memusagegb` | numeric | Full name: 'Memory Usage (GB)'. Explanation: RAM usage during processing. Data type: NUMERIC(6,2). Example: 70.3. |
| `procgpu` | smallint | Full name: 'GPU Usage (%)'. Explanation: GPU usage as an integer percentage. Data type: SMALLINT. Example: 56. |
| `stashloc` | character varying | Full name: 'Storage Location'. Explanation: Where processed data is stored. Data type: VARCHAR(12). Possible categories: Local, Network, Cloud. |
| `safebak` | character | Full name: 'Backup Status'. Explanation: Indicates progress of data backup. Data type: CHAR(8). Possible categories: In Progress, Completed, Pending. |
| `datalevel` | text | Full name: 'Data Access Level'. Explanation: Access restrictions or sharing level. Data type: TEXT. Possible categories: Confidential, Public, Restricted. |
| `metabench` | character varying | Full name: 'Metadata Standard'. Explanation: Which metadata framework is applied. Data type: VARCHAR(10). Possible categories: Dublin Core, CIDOC CRM, Custom. |
| `coordframe` | character varying | Full name: 'Coordinate System'. Explanation: Defines spatial reference frame. Data type: VARCHAR(12). Possible categories: Local, WGS84, Custom. |
| `elevref` | character varying | Full name: 'Elevation Reference'. Explanation: Reference for altitude or elevation. Data type: VARCHAR(16). Possible categories: Arbitrary, Sea Level, Local. |
| `remaingb` | numeric | Full name: 'Remaining Storage (GB)'. Explanation: Remaining disk or cloud space. Data type: NUMERIC(7,2). Example: 983.5. |
| `stationlink` | character | Full name: 'Total Station Integration'. Explanation: Indicates if total station integration is used. Data type: CHAR(6). Example: 'Yes'. |
| `camcal` | text | Full name: 'Camera Calibration Status'. Explanation: Whether camera calibration is completed or pending. Data type: TEXT. Example: 'Required'. |
| `lensdist` | character varying | Full name: 'Lens Distortion Status'. Explanation: Whether lens distortion is corrected or unknown. Data type: VARCHAR(14). Possible categories: Corrected, Unknown. |
| `colortune` | character | Full name: 'Color Balance Status'. Explanation: Indicates color adjustment requirement. Data type: CHAR(10). Possible categories: Required, Adjusted. |
| `flowstage` | character varying | Full name: 'Processing Stage'. Explanation: Current stage of the processing workflow. Data type: VARCHAR(18). Possible categories: Aligned, Meshed, Final. |
| `fmtver` | character | Full name: 'Export Format Version'. Explanation: Version tag for exported files. Data type: CHAR(3). Possible categories: 2.3, 2.7, 4.0, 1.1. |

# Joins

* `equipref` references `equipregistry` in [equipment](/tables/equipment.md).
* `zoneref` references `zoneregistry` in [sites](/tables/sites.md).

# Related knowledge

* [Processing Efficiency Ratio (PER)](/knowledge/processing-efficiency-ratio.md)
* [FlowStage (Processing Stage)](/knowledge/flowstage.md)
* [Processing Resource Utilization (PRU)](/knowledge/processing-resource-utilization.md)
