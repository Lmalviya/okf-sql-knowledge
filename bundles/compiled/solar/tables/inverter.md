---
type: PostgreSQL Table
title: inverter
description: '8 columns: invertmoment, inverttempc, gridvolt, gridfreqhz, pwrqualidx, power_metrics. Joins to plant.'
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
| `invertregistry` | character varying, primary key | VARCHAR(50) PRIMARY KEY uniquely identifying each inverter record. |
| `siteref` | uuid | UUID REFERENCES Plant(GrowRegistry), indicating which plant’s inverter we are tracking. |
| `invertmoment` | timestamp without time zone | TIMESTAMP noting when this inverter reading was taken (e.g., '2023-07-15 10:40:00'). |
| `inverttempc` | numeric | DECIMAL(7,3) inverter operating temperature in °C (was 'InverterOperatingTempC') (e.g., 45.250). |
| `gridvolt` | numeric | NUMERIC(7,3) the AC grid voltage in volts (was 'GridVoltageV') (e.g., 400.000). |
| `gridfreqhz` | numeric | DECIMAL(7,3) the AC grid frequency in Hz (was 'GridFrequencyHz') (e.g., 50.050). |
| `pwrqualidx` | numeric | DECIMAL(7,3) power quality index (was 'PowerQualityIndex') (e.g., 0.980). |
| `power_metrics` | jsonb | JSONB column. Stores key performance metrics related to the inverter's power output and quality, including efficiency, power factor, and harmonic distortion. |

# JSON fields

* `power_metrics.inverteffpct`: DECIMAL(7,3) the inverter efficiency percentage (was 'InverterEfficiencyPercent') (e.g., 98.500).
* `power_metrics.invertpowfac`: NUMERIC(7,3) the inverter’s power factor (was 'InverterPowerFactor') (e.g., 0.990).
* `power_metrics.harmdistpct`: DECIMAL(7,3) total harmonic distortion in percent (was 'HarmonicDistortionPercent') (e.g., 3.500).
* `power_metrics.reacpwrkvar`: DECIMAL(7,2) reactive power output in kVAR (was 'ReactivePowerKVAR') (e.g., 10.00).

# Joins

* `siteref` references `growregistry` in [plant](/tables/plant.md).

# Related knowledge

* [Inverter Efficiency Loss (IEL)](/knowledge/inverter-efficiency-loss.md)
* [Grid Integration Quality (GIQ)](/knowledge/grid-integration-quality.md)
