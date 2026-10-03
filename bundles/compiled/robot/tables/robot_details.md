---
type: PostgreSQL Table
title: robot_details
description: '9 columns: mfgnameval, modelseriesval, bottypeval, payloadcapkg, reachmmval, instdateval, fwversionval, ctrltypeval. Joins to robot_record.'
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
| `botdetreg` | character varying, primary key | Primary key (VARCHAR(20)) referencing robot_record(RecReg). Ties detailed specs to an existing robot record. |
| `mfgnameval` | character varying | VARCHAR(60) describing the manufacturer’s name (was 'Manufacturer') (e.g., 'FANUC', 'Yaskawa', 'KUKA', 'ABB', 'Universal Robots'). |
| `modelseriesval` | character varying | VARCHAR(40) capturing the robot’s model series/designation. |
| `bottypeval` | character | CHAR(15) labeling the broad type of robot (e.g., 'Delta', 'Collaborative', 'Cartesian', 'SCARA', 'Articulated'). |
| `payloadcapkg` | numeric | DECIMAL(9,2) specifying the maximum payload the robot can handle in kilograms (e.g., 5, 200, 100, 50, 20, 3, 10). |
| `reachmmval` | smallint | SMALLINT storing the robot’s reach in millimeters (distance from base). |
| `instdateval` | date | DATE indicating when this robot was installed (was 'InstallationDate'). |
| `fwversionval` | character varying | VARCHAR(25) logging the firmware version installed on the robot’s controller. |
| `ctrltypeval` | character varying | VARCHAR(40) referencing the type or brand of controller used (was 'ControllerType'). |

# Joins

* `botdetreg` references `recreg` in [robot_record](/tables/robot_record.md).

# Related knowledge

* [Robot Age in Years (RAY)](/knowledge/robot-age-in-years.md)
* [Payload Utilization Ratio (PUR)](/knowledge/payload-utilization-ratio.md)
* [APE Rank](/knowledge/ape-rank.md)
