---
type: PostgreSQL Table
title: powerbattery
description: '7 columns: powerstatus, powersource, chargingstatus, powerconsumptionw, energyefficiencypercent, batterystatus. Joins to equipment.'
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
| `pwrbatteqref` | character varying | A VARCHAR(70) foreign key referencing Equipment(EquipmentCode), linking battery data to the equipment using it. |
| `powerstatus` | USER-DEFINED | An enum (PowerStatus_enum) showing the device power state (e.g., Sleep, Charging, On, Off). |
| `powersource` | USER-DEFINED | An enum (PowerSource_enum) describing the primary energy source (e.g., Wind, Solar, Diesel, Hybrid, Battery). |
| `chargingstatus` | USER-DEFINED | An enum (ChargingStatus_enum) showing the charging state (e.g., Error, Not Charging, Charging, Full). |
| `powerconsumptionw` | numeric | A NUMERIC(10,4) measuring the power consumption (in watts). |
| `energyefficiencypercent` | numeric | A NUMERIC(6,3) indicating overall power or energy efficiency (e.g., 95.000%). |
| `batterystatus` | jsonb | JSONB column. Combines metrics describing battery performance, health, and charging status. |

# JSON fields

* `batterystatus.level_percent`: A NUMERIC(5,2) representing the current battery level percentage.
* `batterystatus.health_percent`: A NUMERIC(4,1) indicating the battery’s health status in percentage (e.g., 90.0%).
* `batterystatus.cycles`: A SMALLINT counting the number of charge/discharge cycles for the battery.
* `batterystatus.temperature_c`: A DOUBLE PRECISION value measuring the battery’s temperature in Celsius.
* `batterystatus.current_a`: A NUMERIC(7,3) specifying the current (in amperes) used during charging.
* `batterystatus.voltage_v`: A NUMERIC(5,2) specifying the voltage (in volts) used during charging.

# Joins

* `pwrbatteqref` references `equipmentcode` in [equipment](/tables/equipment.md).

# Related knowledge

* [Energy Sustainability Index (ESI)](/knowledge/energy-sustainability-index.md)
* [powerconsumptionw](/knowledge/powerconsumptionw.md)
* [energyefficiencypercent](/knowledge/energyefficiencypercent.md)
* [Emergency Response Readiness Status (ERRS)](/knowledge/emergency-response-readiness-status.md)
* [Polar Base Energy Security Status (PBESS)](/knowledge/polar-base-energy-security-status.md)
