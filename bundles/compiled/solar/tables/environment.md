---
type: PostgreSQL Table
title: environment
description: '18 columns: envmoment, celltempc, ambtempc, soillosspct, dustdengm2, cleancycledays, lastcleandt, relhumpct, windspdms, winddirdeg, preciptmm, airpresshpa, uv_idx, cloudcovpct, snowcovpct, irradiance_conditions. Joins to plant.'
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_schema.txt
  title: solar schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_column_meaning_base.json
  title: solar column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `envregistry` | character varying, primary key | VARCHAR(50) PRIMARY KEY uniquely identifying each environment record. |
| `arearegistry` | uuid | UUID REFERENCES Plant(GrowRegistry), referencing which plant area is monitored. |
| `envmoment` | timestamp without time zone | TIMESTAMP noting when these environmental readings were taken (e.g., '2023-07-15 10:30:00'). |
| `celltempc` | numeric | DECIMAL(7,3) measuring the cell temperature in °C (was 'CellTemperatureC') (e.g., 55.120). |
| `ambtempc` | numeric | NUMERIC(7,3) ambient temperature in °C (was 'AmbientTemperatureC') (e.g., 35.600). |
| `soillosspct` | numeric | NUMERIC(7,3) soiling loss percentage (was 'SoilingLossPercent') (e.g., 2.500). |
| `dustdengm2` | numeric | DECIMAL(7,3) dust density in g/m² (was 'DustDensityGM2') (e.g., 0.100). |
| `cleancycledays` | smallint | SMALLINT indicating the scheduled cleaning cycle in days (was 'CleaningCycleDays') (e.g., 30). |
| `lastcleandt` | date | DATE for when the last cleaning happened (was 'LastCleaningDate') (e.g., '2023-06-01'). |
| `relhumpct` | numeric | DECIMAL(7,3) relative humidity percentage (was 'RelativeHumidityPercent') (e.g., 35.500). |
| `windspdms` | numeric | NUMERIC(7,3) wind speed in m/s (was 'WindSpeedMS') (e.g., 3.200). |
| `winddirdeg` | numeric | DECIMAL(7,3) wind direction in degrees (was 'WindDirectionDegrees') (e.g., 180.000). |
| `preciptmm` | numeric | NUMERIC(6,2) precipitation in mm (was 'PrecipitationMM') (e.g., 12.50). |
| `airpresshpa` | numeric | DECIMAL(6,2) air pressure in hPa (was 'AirPressureHPA') (e.g., 1013.25). |
| `uv_idx` | numeric | NUMERIC(7,3) UV index reading (was 'UVIndex') (e.g., 7.500). |
| `cloudcovpct` | numeric | DECIMAL(7,3) cloud coverage percentage (was 'CloudCoveragePercent') (e.g., 20.250). |
| `snowcovpct` | numeric | NUMERIC(7,3) snow coverage percentage (was 'SnowCoveragePercent') (e.g., 0.000). |
| `irradiance_conditions` | jsonb | JSONB column. Groups irradiance-related environmental measurements, including global, direct, diffuse, and plane-of-array irradiance, along with spectral mismatch. |

# JSON fields

* `irradiance_conditions.irradiance_types`: ["DECIMAL(6,2) global solar irradiance in W/m² (was 'SolarIrradianceWM2') (e.g., 950.50).", "NUMERIC(5,1) direct normal irradiance in W/m² (was 'DirectIrradianceWM2') (e.g., 800.2).", "DECIMAL(7,3) diffuse irradiance in W/m² (was 'DiffuseIrradianceWM2') (e.g., 150.300).", "NUMERIC(7,3) plane-of-array irradiance in W/m² (was 'POAIrradianceWM2') (e.g., 980.450)."]
* `irradiance_conditions.specmisfac`: DECIMAL(7,3) spectral mismatch factor (was 'SpectralMismatchFactor') (e.g., 1.020).

# Joins

* `arearegistry` references `growregistry` in [plant](/tables/plant.md).

# Related knowledge

* [Temperature Performance Coefficient Impact (TPCI)](/knowledge/temperature-performance-coefficient-impact.md)
* [Irradiance Utilization Ratio (IUR)](/knowledge/irradiance-utilization-ratio.md)
* [CellTempC (Cell Temperature)](/knowledge/celltempc.md)
* [Weather Corrected Efficiency (WCE)](/knowledge/weather-corrected-efficiency.md)
