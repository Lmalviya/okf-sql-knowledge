---
type: PostgreSQL Table
title: engineandfluids
description: '8 columns: enginespeedrpm, engineloadpercent, enginetemperaturec, enginehours, engfluidsopmaintref, fluidmetrics. Joins to equipment, powerbattery.'
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
| `engfluidseqref` | character varying | A VARCHAR(60) foreign key referencing Equipment(EquipmentCode), linking engine data to a specific equipment unit. |
| `engfluidspbref` | integer | An INTEGER foreign key referencing PowerBattery(PowerBattRegistry), associating the engine with battery/power data if relevant. |
| `enginespeedrpm` | integer | An INT measuring engine speed in revolutions per minute (RPM). |
| `engineloadpercent` | real | A REAL value indicating the current engine load in percentage. |
| `enginetemperaturec` | double precision | A DOUBLE PRECISION value measuring overall engine temperature in Celsius. |
| `enginehours` | numeric | A DECIMAL(8,1) recording total operational hours on the engine. |
| `engfluidsopmaintref` | integer | An INTEGER optionally referencing an OperationMaintenance record if needed. |
| `fluidmetrics` | jsonb | JSONB column. Groups fluid-related metrics for fuel, oil, coolant, and hydraulic systems, including levels, pressures, and temperatures. |

# JSON fields

* `fluidmetrics.fuel.level_percent`: A REAL value specifying the current fuel tank level percentage.
* `fluidmetrics.fuel.consumption_lh`: A DECIMAL(5,2) representing fuel consumption in liters per hour.
* `fluidmetrics.fuel.pressure_kpa`: A SMALLINT measuring the fuel pressure in kilopascals.
* `fluidmetrics.fuel.temperature_c`: A FLOAT for the current fuel temperature in Celsius.
* `fluidmetrics.oil.level_percent`: A REAL value for the oil level percentage.
* `fluidmetrics.oil.pressure_kpa`: An INT indicating the oil pressure in kilopascals.
* `fluidmetrics.oil.temperature_c`: A DOUBLE PRECISION value measuring the engine oil temperature in Celsius.
* `fluidmetrics.coolant.level_percent`: A DECIMAL(5,2) for the coolant level percentage in the system.
* `fluidmetrics.coolant.temperature_c`: A REAL number denoting the coolant temperature in Celsius.
* `fluidmetrics.coolant.pressure_kpa`: An INT for the coolant pressure in kilopascals.
* `fluidmetrics.hydraulic.pressure_kpa`: A DECIMAL(7,3) specifying the hydraulic system pressure in kilopascals.
* `fluidmetrics.hydraulic.temperature_c`: A FLOAT for the hydraulic fluid temperature in Celsius.
* `fluidmetrics.hydraulic.level_percent`: A DECIMAL(5,2) indicating the hydraulic fluid level as a percentage.

# Joins

* `engfluidseqref` references `equipmentcode` in [equipment](/tables/equipment.md).
* `engfluidspbref` references `powerbattregistry` in [powerbattery](/tables/powerbattery.md).

# Related knowledge

* [Vehicle Performance Coefficient (VPC)](/knowledge/vehicle-performance-coefficient.md)
