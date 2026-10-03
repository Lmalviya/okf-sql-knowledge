---
type: PostgreSQL Table
title: equipment
description: '11 columns: equipmenttype, equipmentmodel, manufacturer, servicelifeyears, equipmentutilizationpercent, reliabilityindex, performanceindex, efficiencyindex, safetyindex, environmentalimpactindex.'
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
| `equipmentcode` | character varying, primary key | A VARCHAR(50) primary key uniquely identifying each equipment record. |
| `equipmenttype` | USER-DEFINED | An enum (EquipmentType_enum) specifying the category of equipment (e.g., Shelter, Scientific, Safety, Vehicle, Generator, Communication). |
| `equipmentmodel` | character varying | A VARCHAR(80) describing the model name/number of the equipment. |
| `manufacturer` | character varying | A VARCHAR(120) naming the manufacturer or brand of the equipment. |
| `servicelifeyears` | smallint | A SMALLINT indicating the expected or recommended service life (in years). |
| `equipmentutilizationpercent` | numeric | A NUMERIC(5,2) showing the approximate utilization percentage (e.g., 75.00%). |
| `reliabilityindex` | numeric | A NUMERIC(6,3) representing a reliability metric or score for the equipment. |
| `performanceindex` | numeric | A NUMERIC(7,2) measuring the performance level of the equipment. |
| `efficiencyindex` | real | A REAL value indicating the efficiency rating or ratio. |
| `safetyindex` | numeric | A DECIMAL(5,3) capturing the safety rating index for the equipment. |
| `environmentalimpactindex` | double precision | A DOUBLE PRECISION value denoting the environmental impact rating. |

# Related knowledge

* [Equipment Efficiency Rating (EER)](/knowledge/equipment-efficiency-rating.md)
* [Vehicle Operational Safety Threshold](/knowledge/vehicle-operational-safety-threshold.md)
* [reliabilityindex](/knowledge/reliabilityindex.md)
* [safetyindex](/knowledge/safetyindex.md)
* [Overall Safety Performance Index (OSPI)](/knowledge/overall-safety-performance-index.md)
* [Sustainable Polar Operations (SPO)](/knowledge/sustainable-polar-operations.md)
* [Polar Vehicle Safe Operation Conditions (PVSOC)](/knowledge/polar-vehicle-safe-operation-conditions.md)
