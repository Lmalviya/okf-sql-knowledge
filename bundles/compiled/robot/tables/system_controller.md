---
type: PostgreSQL Table
title: system_controller
description: '4 columns: controller_metrics. Joins to actuation_data, operation, robot_details.'
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_schema.txt
  title: robot schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_column_meaning_base.json
  title: robot column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `systemoverseeractuation` | character varying, primary key | PRIMARY KEY (VARCHAR(20)) referencing actuation_data(ActReg). Identifies this system controller record uniquely. |
| `systemoverseeroperation` | character varying | VARCHAR(20) referencing operation(OperReg). |
| `systemoverseerrobot` | character varying | VARCHAR(20) referencing robot_details(BotDetReg). |
| `controller_metrics` | jsonb | JSONB column. Aggregates performance and environmental metrics of the system controller, including load, memory usage, thermal levels, and cabinet conditions. |

# JSON fields

* `controller_metrics.load_value`: NUMERIC(4,2) measuring system or CPU load for the robot’s supervisory controller.
* `controller_metrics.memory_usage`: REAL capturing memory usage (in MB or as ratio) of the system controller.
* `controller_metrics.thermal_level`: FLOAT(5) approximate float for the controller’s internal temperature or thermal reading.
* `controller_metrics.cabinet_temperature`: DECIMAL(6,3) storing the temperature inside the controller cabinet, if applicable.
* `controller_metrics.cabinet_humidity`: NUMERIC(5,2) referencing cabinet humidity level as a percentage.

# Joins

* `systemoverseeractuation` references `actreg` in [actuation_data](/tables/actuation_data.md).
* `systemoverseeroperation` references `operreg` in [operation](/tables/operation.md).
* `systemoverseerrobot` references `botdetreg` in [robot_details](/tables/robot_details.md).

# Related knowledge

* [Controller Stress Index (CSI)](/knowledge/controller-stress-index.md)
