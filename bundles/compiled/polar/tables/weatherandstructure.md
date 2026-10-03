---
type: PostgreSQL Table
title: weatherandstructure
description: '17 columns: externaltemperaturec, windspeedms, winddirectiondegrees, barometricpressurehpa, solarradiationwm2, snowdepthcm, icethicknesscm, visibilitykm, precipitationtype, precipitationratemmh, snowloadkgm2, structuralloadpercent, structuralintegritystatus, vibrationlevelmms2, noiseleveldb. Joins to location, operationmaintenance.'
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
| `weatherlocref` | integer | An INTEGER foreign key referencing Location(LocationRegistry), tying weather data to a specific location. |
| `externaltemperaturec` | real | A REAL value for the external ambient temperature in Celsius. |
| `windspeedms` | double precision | A FLOAT indicating wind speed in meters per second. |
| `winddirectiondegrees` | numeric | A DECIMAL(5,1) specifying the wind direction in degrees (0–359.9). |
| `barometricpressurehpa` | numeric | A NUMERIC(7,2) showing atmospheric pressure in hectopascals (hPa). |
| `solarradiationwm2` | numeric | A DECIMAL(8,3) measuring solar radiation in watts per square meter. |
| `snowdepthcm` | smallint | A SMALLINT for current snow depth in centimeters. |
| `icethicknesscm` | numeric | A DECIMAL(5,2) representing ice thickness in centimeters. |
| `visibilitykm` | real | A REAL value indicating visibility in kilometers. |
| `precipitationtype` | USER-DEFINED | An enum (PrecipitationType_enum) specifying the type of precipitation (e.g., Blowing Snow, Ice, Snow). |
| `precipitationratemmh` | numeric | A DECIMAL(7,3) measuring precipitation rate in millimeters per hour. |
| `snowloadkgm2` | integer | An INT indicating the snow load on structures in kg/m². |
| `structuralloadpercent` | real | A REAL showing structural load as a percentage of maximum capacity. |
| `structuralintegritystatus` | USER-DEFINED | An enum (StructuralIntegrityStatus_enum) describing the building/structure condition (e.g., Warning, Critical, Normal). |
| `vibrationlevelmms2` | double precision | A FLOAT recording vibration level in mm/s². |
| `noiseleveldb` | numeric | A DECIMAL(7,2) specifying noise level in decibels (dB). |
| `weatheropmaintref` | integer | An INTEGER foreign key referencing OperationMaintenance(OpMaintRegistry), linking weather/structural data to operation/maintenance records if needed. |

# Joins

* `weatherlocref` references `locationregistry` in [location](/tables/location.md).
* `weatheropmaintref` references `opmaintregistry` in [operationmaintenance](/tables/operationmaintenance.md).

# Related knowledge

* [Structural Safety Factor (SSF)](/knowledge/structural-safety-factor.md)
* [Critical Equipment](/knowledge/critical-equipment.md)
* [externaltemperaturec](/knowledge/externaltemperaturec.md)
* [windspeedms](/knowledge/windspeedms.md)
* [Extreme Climate Adaptation Coefficient (ECAC)](/knowledge/extreme-climate-adaptation-coefficient.md)
