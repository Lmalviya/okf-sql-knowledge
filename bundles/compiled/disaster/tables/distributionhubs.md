---
type: PostgreSQL Table
title: distributionhubs
description: '11 columns: hubcaptons, hubutilpct, storecapm3, storeavailm3, coldstorecapm3, coldstoretempc, warehousestate, invaccpct, stockturnrate. Joins to disasterevents.'
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
| `hubregistry` | character varying, primary key | A VARCHAR(20) primary key identifying each distribution hub record (e.g., 'HUB0001'). |
| `disteventref` | character varying | A VARCHAR(20) referencing DisasterEvents(DistRegistry), linking this hub to a specific disaster event (e.g., 'DIST0001'). |
| `hubcaptons` | numeric | A DECIMAL(11,2) for the hub’s maximum capacity in tons (e.g., 350.00). |
| `hubutilpct` | numeric | A DECIMAL(7,3) showing the percentage of hub capacity currently utilized (e.g., 85.300). |
| `storecapm3` | numeric | A NUMERIC(9,2) representing total storage capacity in cubic meters (e.g., 2000.00). |
| `storeavailm3` | numeric | A DECIMAL(8,3) specifying how many cubic meters of storage remain available (e.g., 450.750). |
| `coldstorecapm3` | numeric | A DECIMAL(10,3) indicating cold-storage capacity in cubic meters (e.g., 150.300). |
| `coldstoretempc` | numeric | A NUMERIC(4,1) for the temperature in the cold storage facility (e.g., -5.0). |
| `warehousestate` | USER-DEFINED | An enum (WarehouseState_enum) describing the warehouse’s condition; values: 'Fair', 'Excellent', 'Good', 'Poor'. |
| `invaccpct` | numeric | A DECIMAL(5,2) representing inventory accuracy as a percentage (e.g., 98.50). |
| `stockturnrate` | numeric | A DECIMAL(5,2) measuring how often inventory is turned over during a specific period (e.g., 5.20). |

# Joins

* `disteventref` references `distregistry` in [disasterevents](/tables/disasterevents.md).

# Related knowledge

* [Resource Utilization Ratio (RUR)](/knowledge/resource-utilization-ratio.md)
* [Logistics Performance Metric (LPM)](/knowledge/logistics-performance-metric.md)
* [Critical Resource Shortage](/knowledge/critical-resource-shortage.md)
* [Resource Optimization Opportunity](/knowledge/resource-optimization-opportunity.md)
* [Operational Excellence](/knowledge/operational-excellence.md)
* [available storage percentage](/knowledge/available-storage-percentage.md)
