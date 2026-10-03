---
type: PostgreSQL Table
title: surfaceandphysicalreadings
description: '26 columns: vibralvlmms2, noisedb, dustaccummgm2, microbialcountcfu, moldriskidx, pestactivitylvl, pesttrapcount, pestspeciesdetected, surfaceph, matmoistcontent, saltcrystalrisk, metalcorroderate, organicdegradidx, colorchangedeltae, surfacetempc, surfacerh, condenserisk, thermalimgstatus, structstability, crackmonitor, deformmm, wtchangepct, surfdustcoverage, o2concentration, n2concentration. Joins to environmentalreadingscore.'
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
| `envreadref` | bigint | BIGINT FOREIGN KEY referencing EnvironmentalReadingsCore(EnvReadRegistry). Ties surface data to a general environment reading. |
| `vibralvlmms2` | real | REAL measuring vibration level in mm/s² (millimeters per second squared). |
| `noisedb` | smallint | SMALLINT capturing noise level in decibels (dB). |
| `dustaccummgm2` | numeric | NUMERIC(5,2) for dust accumulation in milligrams per square meter (mg/m²). |
| `microbialcountcfu` | integer | INT counting colony-forming units (CFU) of microbes on surfaces. |
| `moldriskidx` | numeric | NUMERIC(4,2) representing a calculated mold risk index (e.g., 0–10). |
| `pestactivitylvl` | character varying | VARCHAR(50) noting observed pest activity (could be enumerations like 'Medium', 'Low', 'High'). |
| `pesttrapcount` | smallint | SMALLINT indicating how many pests were caught in traps (if applicable). |
| `pestspeciesdetected` | text | TEXT listing pest species observed or identified (e.g., 'Beetles', 'Booklice', 'Moths', 'Silverfish'). |
| `surfaceph` | numeric | NUMERIC(3,1) measuring pH on the artifact’s surface. |
| `matmoistcontent` | numeric | NUMERIC(4,2) for the material’s moisture content in percentage (0–100%). |
| `saltcrystalrisk` | character | CHAR(20) describing risk of salt crystallization (possible values: 'High', 'Low', 'Medium'). |
| `metalcorroderate` | numeric | NUMERIC(4,2) capturing corrosion rate for metal surfaces, e.g., mg/cm² per day. |
| `organicdegradidx` | numeric | NUMERIC(4,2) measuring potential organic degradation (e.g., 0–10 scale). |
| `colorchangedeltae` | real | REAL indicating color change (Delta E) measurement. |
| `surfacetempc` | numeric | NUMERIC(5,2) temperature of the surface in Celsius. |
| `surfacerh` | numeric | NUMERIC(4,1) relative humidity at the surface (percentage). |
| `condenserisk` | character varying | VARCHAR(60) describing condensation risk level (possible values: 'Medium', 'High', 'Low'). |
| `thermalimgstatus` | character | CHAR(15) summarizing thermal imaging results (possible values: 'Normal', 'Critical', 'Attention Required'). |
| `structstability` | character varying | VARCHAR(50) describing structural stability (possible values: 'Stable', 'Minor Issues', 'Major Issues'). |
| `crackmonitor` | text | TEXT field noting crack monitoring details (possible values: 'Significant Changes', 'Minor Changes', 'No Changes'). |
| `deformmm` | numeric | NUMERIC(5,2) measuring any deformation in millimeters. |
| `wtchangepct` | numeric | NUMERIC(6,5) capturing weight change in percentage (e.g., 0.00001–99.99999). |
| `surfdustcoverage` | smallint | SMALLINT representing the percentage of surface area covered by dust (0–100%). |
| `o2concentration` | numeric | NUMERIC(4,2) measuring oxygen concentration (e.g., 21.00% for normal air). |
| `n2concentration` | numeric | NUMERIC(4,2) measuring nitrogen concentration (often ~78.00% in air). |

# Joins

* `envreadref` references `envreadregistry` in [environmentalreadingscore](/tables/environmentalreadingscore.md).
