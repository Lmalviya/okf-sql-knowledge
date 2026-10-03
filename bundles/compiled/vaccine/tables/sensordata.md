---
type: PostgreSQL Table
title: sensordata
description: '22 columns: storetempc, temptolc, tempnowc, tempdevcount, tempmaxc, tempminc, tempstabidx, humiditypct, presskpa, shockflag, tiltflag, impactflag, vibelvlmms, lightlux, acceldata, handleevents, critevents, alerts, alerttime, alertkind. Joins to container, transportinfo.'
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_schema.txt
  title: vaccine schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_column_meaning_base.json
  title: vaccine column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `storetempc` | real | A REAL value indicating the recommended or target storage temperature in Celsius. |
| `temptolc` | numeric | A DECIMAL(4,1) specifying allowable temperature deviation (±°C). |
| `tempnowc` | real | A REAL number for the current actual temperature reading in Celsius. |
| `tempdevcount` | smallint | A SMALLINT counting how many times the temperature has deviated beyond the allowed tolerance. |
| `tempmaxc` | numeric | A DECIMAL(5,2) representing the maximum temperature recorded (in °C). |
| `tempminc` | numeric | A DECIMAL(5,2) representing the minimum temperature recorded (in °C). |
| `tempstabidx` | real | A REAL value indicating a temperature stability index or coefficient. |
| `humiditypct` | numeric | A DECIMAL(4,1) showing the percentage of humidity inside or around the container. |
| `presskpa` | real | A REAL number representing the recorded pressure in kilopascals (kPa). |
| `shockflag` | character varying | An enum (SensorStatus_enum) describing the shock sensor status (e.g., Normal, Malfunction, Triggered). |
| `tiltflag` | character varying | An enum (SensorStatus_enum) describing the tilt sensor status (e.g., Normal, Triggered, Malfunction). |
| `impactflag` | character varying | An enum (SensorStatus_enum) describing the impact sensor status (e.g., Normal, Triggered, Malfunction). |
| `vibelvlmms` | numeric | A DECIMAL(6,2) measuring vibration level in mm/s (millimeters per second). |
| `lightlux` | integer | An INTEGER for the current or last known light level in lux. |
| `acceldata` | real | A REAL value capturing acceleration data (e.g., in m/s²) from the sensor. |
| `handleevents` | smallint | A SMALLINT counting non-critical handling events (minor jolts, slight tilts). |
| `critevents` | smallint | A SMALLINT recording critical events (major shocks, severe impacts). |
| `alerts` | smallint | A SMALLINT tally of all sensor alerts triggered within a specific timeframe. |
| `alerttime` | timestamp without time zone | A TIMESTAMP marking the most recent alert event time. |
| `alertkind` | character varying | A VARCHAR(50) describing the kind or category of the last triggered alert. |
| `containlink` | character varying | A VARCHAR(20) foreign key referencing Container(ContainRegistry). Associates sensor data with a specific container. |
| `vehsenseref` | character varying | A VARCHAR(20) foreign key referencing TransportInfo(VehicleReg). Links sensor data to a particular vehicle. |

# Joins

* `containlink` references `containregistry` in [container](/tables/container.md).
* `vehsenseref` references `vehiclereg` in [transportinfo](/tables/transportinfo.md).

# Related knowledge

* [Temperature Stability Score (TSS)](/knowledge/temperature-stability-score.md)
* [Handling Quality Index (HQI)](/knowledge/handling-quality-index.md)
* [Temperature Breach Severity (TBS)](/knowledge/temperature-breach-severity.md)
* [Temperature Alert](/knowledge/temperature-alert.md)
* [TempNowC Value](/knowledge/tempnowc-value.md)
* [LightLux Value](/knowledge/lightlux-value.md)
* [Thermal Stability Coefficient (TSC)](/knowledge/thermal-stability-coefficient.md)
* [Environmental Stress Factor (ESF)](/knowledge/environmental-stress-factor.md)
* [Predictive Degradation Alert](/knowledge/predictive-degradation-alert.md)
