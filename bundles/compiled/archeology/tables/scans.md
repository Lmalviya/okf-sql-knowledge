---
type: PostgreSQL Table
title: scans
description: '12 columns: chronotag, scancount, climtune, huecatch, fmtfile, gbsize, pressratio, spanmin. Joins to personnel, projects, sites.'
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
| `questregistry` | character varying, primary key | Full name: 'Scan ID'. Explanation: Primary key identifying a particular scan. Data type: VARCHAR(16). Example: 'ASD409481'. |
| `chronotag` | timestamp without time zone | Full name: 'Scan Timestamp'. Explanation: Timestamp representing the scan date/time. Data type: TIMESTAMP. If stored as a numeric like 44302.55648, it may be an Excel serial date/time (days since 1900-01-00). Example: 44302.55648. |
| `arcref` | character varying | Full name: 'Project Reference'. Explanation: Links a scan to a specific project. Data type: VARCHAR(10). Example: 'PR7509'. |
| `crewref` | character | Full name: 'Operator Reference'. Explanation: Records which operator performed the scan. Data type: CHAR(8). Example: 'OP4641'. |
| `zoneref` | character varying | Full name: 'Site Reference'. Explanation: Associates the scan with a site code. Data type: VARCHAR(12). Example: 'SC9016'. |
| `scancount` | smallint | Full name: 'Number of Scans'. Explanation: Numeric count of scans in a set. Data type: SMALLINT. Example: 5. |
| `climtune` | character varying | Full name: 'Weather Conditions'. Explanation: Indicates the weather during scanning. Data type: VARCHAR(22). Possible categories: Windy, Rainy, Cloudy, Clear. |
| `huecatch` | character varying | Full name: 'Color Capture'. Explanation: Mode of color recording. Data type: VARCHAR(10). Possible categories: RGB, Grayscale, None. |
| `fmtfile` | character | Full name: 'File Format'. Explanation: Format in which scan data is saved. Data type: CHAR(4). Possible categories: PTS, PLY, OBJ, LAS, E57. |
| `gbsize` | numeric | Full name: 'File Size (GB)'. Explanation: Size of the scan file in gigabytes. Data type: NUMERIC(5,2). Example: 24.71. |
| `pressratio` | numeric | Full name: 'Compression Ratio'. Explanation: Compression level applied to scan data. Data type: NUMERIC(4,2). Example: 3.22. |
| `spanmin` | numeric | Full name: 'Scan Duration (min)'. Explanation: Duration of the scanning process, in minutes. Data type: NUMERIC(5,2). Example: 63. |

# Joins

* `arcref` references `arcregistry` in [projects](/tables/projects.md).
* `crewref` references `crewregistry` in [personnel](/tables/personnel.md).
* `zoneref` references `zoneregistry` in [sites](/tables/sites.md).

# Related knowledge

* [Processing Efficiency Ratio (PER)](/knowledge/processing-efficiency-ratio.md)
* [Scan Time Efficiency (STE)](/knowledge/scan-time-efficiency.md)
* [Processing Resource Utilization (PRU)](/knowledge/processing-resource-utilization.md)
