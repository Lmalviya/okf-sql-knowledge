---
type: PostgreSQL Table
title: disasterevents
description: '9 columns: timemark, haztype, hazlevel, affectedarea, regiontag, latcoord, loncoord, impactmetrics.'
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_schema.txt
  title: disaster schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_column_meaning_base.json
  title: disaster column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `distregistry` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying each disaster record (e.g., 'DIST0001'). |
| `timemark` | timestamp without time zone | A TIMESTAMP indicating when this disaster event record was created (e.g., '2025-04-15 10:30:00'). |
| `haztype` | USER-DEFINED | An enum (HazType_enum) describing the primary hazard type; possible values include 'Wildfire', 'Earthquake', 'Tsunami', 'Flood', 'Hurricane'. |
| `hazlevel` | USER-DEFINED | An enum (HazLevel_enum) specifying the hazard’s severity level; possible values include 'Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5'. |
| `affectedarea` | character varying | A VARCHAR(100) naming the geographic area impacted by the disaster (e.g., 'Coastal Region'). |
| `regiontag` | character | A CHAR(10) tagging the region code (e.g., 'REG001'). |
| `latcoord` | numeric | A NUMERIC(9,6) capturing the latitude coordinate of the affected area (e.g., 34.052235). |
| `loncoord` | numeric | A DECIMAL(10,7) capturing the longitude coordinate (e.g., -118.243683). |
| `impactmetrics` | jsonb | JSONB column. Consolidates impact-related metrics of the disaster including population effects, infrastructure damage, and communication status. |

# JSON fields

* `impactmetrics.population.affected`: An INTEGER counting how many people are affected (e.g., 150000).
* `impactmetrics.population.displaced`: An INTEGER indicating the number of displaced individuals (e.g., 10000).
* `impactmetrics.population.casualties`: An INTEGER representing the total number of fatalities (e.g., 50).
* `impactmetrics.population.injured`: An INT logging how many were injured (e.g., 200).
* `impactmetrics.population.missing`: An INT showing how many persons are missing (e.g., 25).
* `impactmetrics.infrastructure.damage_percent`: A DECIMAL(5,2) measuring infrastructure damage as a percentage (e.g., 45.30).
* `impactmetrics.infrastructure.power_outage_percent`: A DECIMAL(7,3) capturing the percentage of power outages (e.g., 75.200).
* `impactmetrics.infrastructure.water_damage_percent`: An INT indicating the water system damage percentage (e.g., 60).
* `impactmetrics.communication`: An enum (CommNetState_enum) for communication network status; possible values: 'Limited', 'Operational', 'Down'.
* `impactmetrics.transportation`: An enum (TransportAccess_enum) describing transportation accessibility; possible values: 'Full', 'Limited', 'Minimal'.
* `impactmetrics.damage_level`: An enum (DamageReport_enum) labeling the damage severity; possible values: 'Severe', 'Moderate', 'Minor', 'Catastrophic'.

# Related knowledge

* [hazlevel](/knowledge/hazlevel.md)
* [impactMetrics.communication](/knowledge/impactmetrics-communication.md)
* [impactMetrics.damage_level](/knowledge/impactmetrics-damage-level.md)
* [Communication Resilience Factor (CRF)](/knowledge/communication-resilience-factor.md)
* [Staffing to Need Ratio (SNR)](/knowledge/staffing-to-need-ratio.md)
* [Health System Capacity Index (HSCI)](/knowledge/health-system-capacity-index.md)
* [High-Impact Communication Failure](/knowledge/high-impact-communication-failure.md)
