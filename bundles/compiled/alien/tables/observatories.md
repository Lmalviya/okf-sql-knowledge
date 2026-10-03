---
type: PostgreSQL Table
title: observatories
description: '13 columns: weathprofile, seeingprofile, atmostransparency, lunarstage, lunardistdeg, solarstatus, geomagstatus, sidereallocal, airtempc, humidityrate, windspeedms, presshpa.'
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_schema.txt
  title: alien schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_column_meaning_base.json
  title: alien column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `observstation` | character, primary key | Full name: 'Observatory Name'. Explanation: This field holds the name or unique identifier for the observatory station. Data type: CHAR(60). Example: 'OBS_STATION_ALPHA'. |
| `weathprofile` | character varying | Full name: 'Weather Profile'. Explanation: A short description of weather conditions during observation. Data type: VARCHAR(40). Possible categories: Clear, Cloudy, Partially Cloudy. |
| `seeingprofile` | character varying | Full name: 'Seeing Profile'. Explanation: Assessment of sky seeing conditions (atmospheric steadiness). Data type: VARCHAR(50). Possible categories: Excellent, Good, Poor. |
| `atmostransparency` | numeric | Full name: 'Atmospheric Transparency'. Explanation: A numeric measure of how transparent the atmosphere is. Data type: NUMERIC(5,3). Example: '0.867'. |
| `lunarstage` | character varying | Full name: 'Lunar Phase'. Explanation: The current phase of the Moon during observation. Data type: VARCHAR(25). Possible categories: First Quarter, Full, Last Quarter, New. |
| `lunardistdeg` | numeric | Full name: 'Moon Distance (Degrees)'. Explanation: Angular distance to the Moon in degrees. Data type: DECIMAL(7,2). Example: '97.52'. |
| `solarstatus` | character varying | Full name: 'Solar Activity'. Explanation: The level of solar activity at the time of observation. Data type: VARCHAR(35). Possible categories: High, Low, Moderate. |
| `geomagstatus` | character varying | Full name: 'Geomagnetic Activity'. Explanation: The level of geomagnetic activity during observation. Data type: VARCHAR(35). Possible categories: Active, Quiet, Storm. |
| `sidereallocal` | character | Full name: 'Local Sidereal Time'. Explanation: Sidereal time at the observatory in HH:MM:SS format. Data type: CHAR(8). Example: '12:34:56'. |
| `airtempc` | numeric | Full name: 'Air Temperature (°C)'. Explanation: Ambient temperature in Celsius. Data type: NUMERIC(5,2). Example: '18.45'. |
| `humidityrate` | numeric | Full name: 'Humidity (%)'. Explanation: Relative humidity as a percentage. Data type: NUMERIC(6,3). Example: '62.300'. |
| `windspeedms` | numeric | Full name: 'Wind Speed (m/s)'. Explanation: Wind speed in meters per second. Data type: NUMERIC(4,2). Example: '3.45'. |
| `presshpa` | numeric | Full name: 'Pressure (hPa)'. Explanation: Atmospheric pressure in hectopascals. Data type: DECIMAL(6,1). Example: '1013.2'. |

# Related knowledge

* [Atmospheric Observability Index (AOI)](/knowledge/atmospheric-observability-index.md)
* [Detection Instrument Sensitivity Factor (DISF)](/knowledge/detection-instrument-sensitivity-factor.md)
* [Lunar Interference Factor (LIF)](/knowledge/lunar-interference-factor.md)
* [Optimal Observing Window (OOW)](/knowledge/optimal-observing-window.md)
* [Signal Degradation Scenario (SDS)](/knowledge/signal-degradation-scenario.md)
* [WeathProfile: Clear](/knowledge/weathprofile-clear.md)
* [SeeingProfile: Excellent](/knowledge/seeingprofile-excellent.md)
* [GeomagStatus: Major Storm](/knowledge/geomagstatus-major-storm.md)
