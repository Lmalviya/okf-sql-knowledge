---
type: PostgreSQL Table
title: chassisandvehicle
description: '14 columns: brakepadwearpercent, brakefluidlevelpercent, brakepressurekpa, tracktensionkn, trackwearpercent, suspensionheightmm, vehiclespeedkmh, vehicleloadkg, vehicleangledegrees, vehicleheadingdegrees, tiremetrics. Joins to engineandfluids, equipment, transmission.'
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
| `chassiseqref` | character varying | A VARCHAR(70) foreign key referencing Equipment(EquipmentCode), linking chassis or vehicle details to a specific piece of equipment. |
| `chassistransref` | integer | An INTEGER foreign key referencing Transmission(TransRegistry), relating this chassis to its transmission record. |
| `brakepadwearpercent` | real | A REAL value measuring the brake pad wear as a percentage of expected lifespan used. |
| `brakefluidlevelpercent` | numeric | A DECIMAL(5,2) specifying brake fluid level as a percentage. |
| `brakepressurekpa` | integer | An INT indicating brake line pressure in kilopascals. |
| `tracktensionkn` | numeric | A NUMERIC(7,3) for tracked vehicles, indicating track tension in kilonewtons. |
| `trackwearpercent` | double precision | A FLOAT representing wear on the tracks (if applicable) as a percentage. |
| `suspensionheightmm` | numeric | A NUMERIC(6,1) describing the current suspension height in millimeters. |
| `vehiclespeedkmh` | real | A REAL number for the vehicle’s current speed in kilometers per hour. |
| `vehicleloadkg` | numeric | A DECIMAL(9,2) showing the current load (cargo + passengers) in kilograms. |
| `vehicleangledegrees` | numeric | A DECIMAL(6,2) specifying the vehicle’s pitch/tilt angle in degrees. |
| `vehicleheadingdegrees` | numeric | A NUMERIC(5,1) describing the vehicle’s heading or direction in degrees. |
| `chassisengref` | integer | An INTEGER foreign key referencing EngineAndFluids(EngineRegistry), linking the chassis record to engine data. |
| `tiremetrics` | jsonb | JSONB column. Captures tire-related data, including pressure, temperature, and tread condition. |

# JSON fields

* `tiremetrics.pressure_kpa`: A SMALLINT for the tires’ pressure in kilopascals.
* `tiremetrics.temperature_c`: A DOUBLE PRECISION value representing the tires’ temperature in Celsius.
* `tiremetrics.tread_depth_mm`: A DECIMAL(6,2) showing the depth of the tire tread in millimeters.

# Joins

* `chassisengref` references `engineregistry` in [engineandfluids](/tables/engineandfluids.md).
* `chassiseqref` references `equipmentcode` in [equipment](/tables/equipment.md).
* `chassistransref` references `transregistry` in [transmission](/tables/transmission.md).

# Related knowledge

* [Vehicle Performance Coefficient (VPC)](/knowledge/vehicle-performance-coefficient.md)
* [Vehicle Operational Safety Threshold](/knowledge/vehicle-operational-safety-threshold.md)
