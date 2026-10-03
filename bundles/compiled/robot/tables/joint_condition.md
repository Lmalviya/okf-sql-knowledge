---
type: PostgreSQL Table
title: joint_condition
description: '21 columns: j1tempval, j2tempval, j3tempval, j4tempval, j5tempval, j6tempval, j1vibval, j2vibval, j3vibval, j4vibval, j5vibval, j6vibval, j1backval, j2backval, j3backval, j4backval, j5backval, j6backval. Joins to operation, robot_details, robot_record.'
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
| `jcondoperref` | character varying | VARCHAR(20) referencing operation(OperReg) to link these condition metrics. |
| `jcrecref` | character varying | VARCHAR(20) referencing robot_record(RecReg). |
| `jcdetref` | character varying | VARCHAR(20) referencing robot_details(BotDetReg). |
| `j1tempval` | numeric | NUMERIC(5,2) capturing the temperature of Joint 1’s motor or housing. |
| `j2tempval` | real | REAL storing Joint 2 temperature. May have platform-limited precision. |
| `j3tempval` | numeric | NUMERIC(6,3) for Joint 3 temperature with 3 decimals. |
| `j4tempval` | real | FLOAT(4) approximate float for Joint 4 temperature. |
| `j5tempval` | numeric | NUMERIC(7,2) decimal storing Joint 5 temperature. |
| `j6tempval` | real | FLOAT(6) approximate float for Joint 6 temperature. |
| `j1vibval` | numeric | NUMERIC(5,3) measuring vibration amplitude for Joint 1. |
| `j2vibval` | real | REAL storing Joint 2 vibration reading. |
| `j3vibval` | real | FLOAT(5) approximate float for Joint 3 vibration. |
| `j4vibval` | numeric | NUMERIC(5,3) decimal for Joint 4 vibration amplitude. |
| `j5vibval` | real | REAL storing Joint 5 vibration. |
| `j6vibval` | real | FLOAT(4) approximate float for Joint 6 vibration measure. |
| `j1backval` | numeric | NUMERIC(5,4) describing measured backlash in Joint 1. |
| `j2backval` | numeric | NUMERIC(6,3) backlash for Joint 2 with different precision. |
| `j3backval` | real | REAL capturing Joint 3 backlash measurement. |
| `j4backval` | real | FLOAT(5) approximate float for Joint 4 backlash. |
| `j5backval` | numeric | NUMERIC(7,4) decimal for Joint 5 backlash. |
| `j6backval` | real | FLOAT(7) approximate float for Joint 6 backlash. |

# Joins

* `jcdetref` references `botdetreg` in [robot_details](/tables/robot_details.md).
* `jcondoperref` references `operreg` in [operation](/tables/operation.md).
* `jcrecref` references `recreg` in [robot_record](/tables/robot_record.md).

# Related knowledge

* [Average Joint 1 Temperature (AJ1T)](/knowledge/average-joint-1-temperature.md)
* [Maximum Joint Temperature (MJT)](/knowledge/maximum-joint-temperature.md)
* [Joint Degradation Index (JDI)](/knowledge/joint-degradation-index.md)
