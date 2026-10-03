---
type: PostgreSQL Table
title: scanspatial
description: '10 columns: aream2, volm3, boxx, boxy, boxz, angleaz, angletilt, groundspan. Joins to personnel, projects.'
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
| `arcref` | character varying | Full name: 'Project Reference'. Explanation: Project ID linking spatial data. Data type: VARCHAR(10). Example: 'PR7509'. |
| `crewref` | character | Full name: 'Operator Reference'. Explanation: Operator ID for these spatial records. Data type: CHAR(8). Example: 'OP4641'. |
| `aream2` | numeric | Full name: 'Surface Area (m²)'. Explanation: Calculated area in square meters. Data type: NUMERIC(8,3). Example: 78.01. |
| `volm3` | numeric | Full name: 'Volume (m³)'. Explanation: Computed volume in cubic meters. Data type: NUMERIC(9,4). Example: 76.7. |
| `boxx` | numeric | Full name: 'Bounding Box X (m)'. Explanation: Size of bounding box along X-axis, in meters. Data type: NUMERIC(8,2). Example: 40.12. |
| `boxy` | numeric | Full name: 'Bounding Box Y (m)'. Explanation: Size of bounding box along Y-axis, in meters. Data type: NUMERIC(8,3). Example: 1.06. |
| `boxz` | numeric | Full name: 'Bounding Box Z (m)'. Explanation: Size of bounding box along Z-axis, in meters. Data type: NUMERIC(9,2). Example: 16.41. |
| `angleaz` | real | Full name: 'Orientation (degrees)'. Explanation: Azimuth or rotation angle around vertical axis. Data type: REAL. Example: 342.4. |
| `angletilt` | double precision | Full name: 'Tilt Angle (degrees)'. Explanation: Inclination angle from horizontal. Data type: DOUBLE PRECISION. Example: 23.9. |
| `groundspan` | numeric | Full name: 'Ground Sampling Distance (mm)'. Explanation: Effective resolution on the ground, in mm. Data type: NUMERIC(6,3). Example: 4.13. |

# Joins

* `arcref` references `arcregistry` in [projects](/tables/projects.md).
* `crewref` references `crewregistry` in [personnel](/tables/personnel.md).

# Related knowledge

* [Point Cloud Density Ratio (PCDR)](/knowledge/point-cloud-density-ratio.md)
* [Spatial Density Index (SDI)](/knowledge/spatial-density-index.md)
* [Spatially Complex Site](/knowledge/spatially-complex-site.md)
