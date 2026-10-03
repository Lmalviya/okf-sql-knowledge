---
type: PostgreSQL Table
title: scientific
description: '6 columns: scientificequipmentstatus, dataloggingstatus, sensorstatus, calibrationstatus, measurementaccuracypercent. Joins to equipment.'
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
| `scieqref` | character varying | A VARCHAR(70) foreign key referencing Equipment(EquipmentCode), linking scientific data to a specific piece of equipment. |
| `scientificequipmentstatus` | USER-DEFINED | An enum (ScientificEquipmentStatus_enum) describing the operating state of scientific instruments (e.g., Standby, Operating, Fault). |
| `dataloggingstatus` | USER-DEFINED | An enum (DataLoggingStatus_enum) indicating the data logging status (e.g., Active, Paused, Error). |
| `sensorstatus` | USER-DEFINED | An enum (SensorStatus_enum) noting sensor integrity (e.g., Error, Warning, Normal). |
| `calibrationstatus` | USER-DEFINED | An enum (CalibrationStatus_enum) specifying calibration validity (e.g., Expired, Valid, Due). |
| `measurementaccuracypercent` | real | A REAL value reflecting the measurement accuracy (e.g., 98.5%). |

# Joins

* `scieqref` references `equipmentcode` in [equipment](/tables/equipment.md).

# Related knowledge

* [Scientific Equipment Reliability (SER)](/knowledge/scientific-equipment-reliability.md)
* [Long-term Scientific Mission Viability (LSMV)](/knowledge/long-term-scientific-mission-viability.md)
