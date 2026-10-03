---
type: PostgreSQL Table
title: supplies
description: '4 columns: resourceinventory. Joins to disasterevents, distributionhubs.'
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
| `supplyregistry` | character varying, primary key | A VARCHAR(20) primary key identifying each supplies record (e.g., 'SUP0001'). |
| `supplydistref` | character varying | A VARCHAR(20) referencing DisasterEvents(DistRegistry) to link supplies to an event (e.g., 'DIST0001'). |
| `supplyhubref` | character varying | A VARCHAR(20) referencing DistributionHubs(HubRegistry), tying supplies to a particular hub (e.g., 'HUB0001'). |
| `resourceinventory` | jsonb | JSONB column. Provides a comprehensive view of all supply resources available for disaster response, including food, water, shelter, medical, and power-related supplies. |

# JSON fields

* `resourceinventory.essentials.food_tons`: A DECIMAL(11,3) denoting the quantity of food in tons (e.g., 12.500).
* `resourceinventory.essentials.water_liters`: A NUMERIC(12,3) specifying the water supply in liters (e.g., 25000.000).
* `resourceinventory.medical`: An INT counting medical supply units (e.g., 500).
* `resourceinventory.shelter.units`: An INT showing how many shelter kits or tents (e.g., 200).
* `resourceinventory.shelter.blankets`: An INTEGER storing the total number of blankets (e.g., 1000).
* `resourceinventory.hygiene_kits`: An INT measuring the quantity of hygiene kits (e.g., 300).
* `resourceinventory.power.generators`: An INT for how many power generators are available (e.g., 10).
* `resourceinventory.power.fuel_liters`: A DECIMAL(9,1) specifying the liters of fuel reserve (e.g., 5000.0).

# Joins

* `supplydistref` references `distregistry` in [disasterevents](/tables/disasterevents.md).
* `supplyhubref` references `hubregistry` in [distributionhubs](/tables/distributionhubs.md).
