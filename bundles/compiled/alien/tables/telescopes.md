---
type: PostgreSQL Table
title: telescopes
description: '14 columns: equipstatus, calibrstatus, pointaccarc, trackaccarc, focusquality, detecttempk, coolsysstatus, powerstatus, datastorstatus, netstatus, bandusagepct, procqueuestatus. Joins to observatories.'
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
| `telescregistry` | character, primary key | Full name: 'Telescope Registry'. Explanation: A unique identifier for the telescope. Data type: CHAR(20). Example: 'TELESC_0001'. |
| `observstation` | character | Full name: 'Observatory Name Reference'. Explanation: Foreign key linking to the observatory station. Data type: CHAR(60). Example: 'OBS_STATION_ALPHA'. |
| `equipstatus` | character varying | Full name: 'Equipment Status'. Explanation: Operational state of the telescope. Data type: VARCHAR(35). Possible categories: Degraded, Maintenance, Operational. |
| `calibrstatus` | character varying | Full name: 'Calibration Status'. Explanation: Status of telescope’s calibration. Data type: VARCHAR(50). Possible categories: Current, Due, Overdue. |
| `pointaccarc` | numeric | Full name: 'Pointing Accuracy (arcsec)'. Explanation: How precise the telescope can point, in arcseconds. Data type: NUMERIC(6,2). Example: '0.45'. |
| `trackaccarc` | numeric | Full name: 'Tracking Accuracy (arcsec)'. Explanation: How accurately the telescope can track a target, in arcseconds. Data type: NUMERIC(6,2). Example: '1.20'. |
| `focusquality` | character varying | Full name: 'Focus Quality'. Explanation: Quality of the telescope’s focusing system. Data type: VARCHAR(25). Possible categories: Excellent, Good, Poor. |
| `detecttempk` | numeric | Full name: 'Detector Temperature (K)'. Explanation: Temperature of the telescope’s primary detector in Kelvin. Data type: DECIMAL(7,2). Example: '123.45'. |
| `coolsysstatus` | character varying | Full name: 'Cooling System Status'. Explanation: Status of the telescope’s cooling system. Data type: VARCHAR(35). Possible categories: Critical, Normal, Warning. |
| `powerstatus` | character varying | Full name: 'Power Supply Status'. Explanation: Indicates which power source or level is in use. Data type: VARCHAR(30). Possible categories: Backup, Critical, Main. |
| `datastorstatus` | character varying | Full name: 'Data Storage Status'. Explanation: Capacity and status of local data storage. Data type: VARCHAR(35). Possible categories: Available, Critical, Low. |
| `netstatus` | character varying | Full name: 'Network Status'. Explanation: Status of the network connection for telescope data transfer. Data type: VARCHAR(40). Possible categories: Connected, Disconnected, Limited. |
| `bandusagepct` | numeric | Full name: 'Bandwidth Usage (%)'. Explanation: Network bandwidth usage as a percentage. Data type: NUMERIC(5,2). Example: '73.25'. |
| `procqueuestatus` | character varying | Full name: 'Processing Queue Status'. Explanation: Indicates how full the processing queue is. Data type: VARCHAR(40). Possible categories: Empty, Full, Normal. |

# Joins

* `observstation` references `observstation` in [observatories](/tables/observatories.md).

# Related knowledge

* [Observational Confidence Level (OCL)](/knowledge/observational-confidence-level.md)
* [Observation Quality Factor (OQF)](/knowledge/observation-quality-factor.md)
