---
type: PostgreSQL Table
title: location
description: '7 columns: Timestamp, stationname, locationtype, latitude, longitude, altitudem. Joins to equipment.'
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:09+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_schema.txt
  title: polar schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_column_meaning_base.json
  title: polar column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `loceqref` | character varying | A VARCHAR(70) foreign key referencing Equipment(EquipmentCode), linking location data to a specific piece of equipment. |
| `Timestamp` | timestamp without time zone |  |
| `stationname` | text | A TEXT field giving the name of the station, camp, or site. |
| `locationtype` | USER-DEFINED | An enum (LocationType_enum) describing if it is an 'Arctic' or 'Antarctic' location (e.g., Arctic, Antarctic). |
| `latitude` | numeric | A NUMERIC(9,6) representing the latitude of the location in decimal degrees. |
| `longitude` | numeric | A NUMERIC(9,6) representing the longitude of the location in decimal degrees. |
| `altitudem` | numeric | A DECIMAL(7,2) specifying the altitude (in meters) above sea level. |

# Joins

* `loceqref` references `equipmentcode` in [equipment](/tables/equipment.md).
