---
type: PostgreSQL Table
title: distributionhubs
description: One row per disaster-relief distribution hub, with its capacity, storage space, cold storage, warehouse condition and inventory measures.
tags: [disaster, logistics]
generated: { by: human:your-name, at: 2026-10-02T17:00:00+05:30 }
sources:
  - id: schema
    resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_schema.txt
    title: disaster schema (LiveSQLBench)
  - id: column-meanings
    resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_column_meaning_base.json
    title: disaster column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `hubregistry` | varchar, primary key | Hub ID, for example `HUB_HS0I`. |
| `disteventref` | varchar | The disaster event this hub serves. |
| `hubcaptons` | numeric | Maximum capacity of the hub, in tons. |
| `hubutilpct` | numeric | Percentage of the hub's capacity currently in use. |
| `storecapm3` | numeric | Total storage capacity, in cubic meters. |
| `storeavailm3` | numeric | Storage still available, in cubic meters. |
| `coldstorecapm3` | numeric | Cold-storage capacity, in cubic meters. |
| `coldstoretempc` | numeric | Temperature of the cold storage, in °C. |
| `warehousestate` | enum | Warehouse condition: `Fair`, `Excellent`, `Good` or `Poor`. |
| `invaccpct` | numeric | Inventory accuracy, as a percentage. |
| `stockturnrate` | numeric | How often the inventory is turned over in a period. |

# Joins

`disteventref` references `distregistry` in [disasterevents](/tables/disasterevents.md).

# Related knowledge

* [Resource Utilization Ratio (RUR)](/knowledge/resource-utilization-ratio.md) is computed from `hubutilpct`, `storecapm3` and `storeavailm3`.