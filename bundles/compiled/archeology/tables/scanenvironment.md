---
type: PostgreSQL Table
title: scanenvironment
description: '10 columns: ambictemp, humepct, illumelux, geosignal, trackstatus, linkstatus, photomap, imgcount. Joins to equipment, sites.'
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
| `zoneref` | character varying | Full name: 'Site Reference'. Explanation: Links environment conditions to a specific site code. Data type: VARCHAR(12). Example: 'SC9016'. |
| `equipref` | character | Full name: 'Equipment Reference'. Explanation: Identifies which equipment these environment data refer to. Data type: CHAR(10). Example: 'SN20065'. |
| `ambictemp` | numeric | Full name: 'Ambient Temperature (C)'. Explanation: Air temperature in Celsius. Data type: NUMERIC(5,2). Example: 25.3. |
| `humepct` | numeric | Full name: 'Relative Humidity (%)'. Explanation: Humidity as a percentage. Data type: NUMERIC(5,2). Example: 60.4. |
| `illumelux` | integer | Full name: 'Light Conditions (lux)'. Explanation: Measured illumination in lux. Data type: INTEGER. Example: 86054. |
| `geosignal` | character varying | Full name: 'GPS Signal Quality'. Explanation: Quality rating for GPS reception. Data type: VARCHAR(15). Possible categories: None, Poor, Good, Excellent. |
| `trackstatus` | character varying | Full name: 'RTK Status'. Explanation: Real-Time Kinematic correction state. Data type: VARCHAR(12). Possible categories: None, Fixed. |
| `linkstatus` | character varying | Full name: 'Network Status'. Explanation: Status of network connectivity. Data type: VARCHAR(12). Possible categories: Disconnected, Connected. |
| `photomap` | character | Full name: 'Photogrammetry Overlap'. Explanation: Percentage overlap for photogrammetry images. Data type: CHAR(4). Possible categories: 80%, 60%, 90%. |
| `imgcount` | smallint | Full name: 'Number of Images'. Explanation: How many images were taken for photogrammetry. Data type: SMALLINT. Example: 248. |

# Joins

* `equipref` references `equipregistry` in [equipment](/tables/equipment.md).
* `zoneref` references `zoneregistry` in [sites](/tables/sites.md).

# Related knowledge

* [Environmental Suitability Index (ESI)](/knowledge/environmental-suitability-index.md)
