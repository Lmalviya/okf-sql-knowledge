---
type: PostgreSQL Table
title: cabinenvironment
description: '13 columns: emergencybeaconstatus, ventilationstatus, ventilationspeedpercent, heaterstatus, heatertemperaturec, defrosterstatus, windowstatus, doorstatus, hatchstatus, cabinclimate. Joins to communication, equipment, location.'
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
| `cabineqref` | character varying | A VARCHAR(70) foreign key referencing Equipment(EquipmentCode), linking cabin environment data to a specific piece of equipment. |
| `cabinlocref` | integer | An INTEGER foreign key referencing Location(LocationRegistry), associating this cabin environment with a location or station. |
| `emergencybeaconstatus` | USER-DEFINED | An enum (EmergencyBeaconStatus_enum) indicating the beacon’s mode (e.g., Active, Standby, Testing). |
| `ventilationstatus` | USER-DEFINED | An enum (VentilationStatus_enum) (e.g., On, Auto, Off). |
| `ventilationspeedpercent` | numeric | A DECIMAL(5,2) specifying the current ventilation speed or fan power as a percentage. |
| `heaterstatus` | USER-DEFINED | An enum (HeaterStatus_enum) indicating if the heater is On, Off, or in Auto mode (e.g., Off, On, Auto). |
| `heatertemperaturec` | double precision | A DOUBLE PRECISION value denoting the set or measured heater output temperature in Celsius. |
| `defrosterstatus` | USER-DEFINED | An enum (DefrosterStatus_enum) describing the defroster’s state (e.g., On, Auto, Off). |
| `windowstatus` | USER-DEFINED | An enum (WindowStatus_enum) specifying if windows are Open, Closed, or Partial (e.g., Partial, Closed, Open). |
| `doorstatus` | USER-DEFINED | An enum (DoorStatus_enum) indicating if doors are Locked, Open, or Closed (e.g., Closed, Locked, Open). |
| `hatchstatus` | USER-DEFINED | An enum (HatchStatus_enum) describing the status of any hatches (e.g., Closed, Open, Locked). |
| `cabincommref` | integer | An INTEGER foreign key referencing Communication(CommRegistry), linking the cabin environment to a communication record if relevant. |
| `cabinclimate` | jsonb | JSONB column. Aggregates environmental metrics for the cabin, including temperature, humidity, pressure, and air quality indicators. |

# JSON fields

* `cabinclimate.temperature_c`: A REAL value representing the cabin’s internal temperature in Celsius.
* `cabinclimate.humidity_percent`: A DECIMAL(4,1) measuring the relative humidity in the cabin as a percentage.
* `cabinclimate.pressure_kpa`: An INT specifying the internal cabin pressure in kilopascals.
* `cabinclimate.co2_ppm`: A DECIMAL(7,1) describing the CO₂ concentration in parts per million (ppm).
* `cabinclimate.o2_percent`: A NUMERIC(5,2) indicating the oxygen percentage inside the cabin.
* `cabinclimate.air_quality_index`: A REAL value summarizing the cabin air quality (e.g., 0–500 index).

# Joins

* `cabincommref` references `commregistry` in [communication](/tables/communication.md).
* `cabineqref` references `equipmentcode` in [equipment](/tables/equipment.md).
* `cabinlocref` references `locationregistry` in [location](/tables/location.md).

# Related knowledge

* [Extreme Weather Readiness (EWR)](/knowledge/extreme-weather-readiness.md)
* [Communication Zone Status](/knowledge/communication-zone-status.md)
* [Cabin Habitability Standard](/knowledge/cabin-habitability-standard.md)
* [cabinclimate.co2_ppm](/knowledge/cabinclimate-co2-ppm.md)
* [Energy-Water Resource Integration Index (EWRII)](/knowledge/energy-water-resource-integration-index.md)
* [Extreme Weather Readiness Status (EWRS)](/knowledge/extreme-weather-readiness-status.md)
