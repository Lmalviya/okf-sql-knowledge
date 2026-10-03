---
type: PostgreSQL Table
title: mechanical_status
description: '27 columns: brk1statval, brk2statval, brk3statval, brk4statval, brk5statval, brk6statval, enc1statval, enc2statval, enc3statval, enc4statval, enc5statval, enc6statval, gb1tempval, gb2tempval, gb3tempval, gb4tempval, gb5tempval, gb6tempval, gb1vibval, gb2vibval, gb3vibval, gb4vibval, gb5vibval, gb6vibval. Joins to actuation_data, operation, robot_details.'
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
| `mechactref` | character varying | VARCHAR(20) referencing actuation_data(ActReg). Relates mechanical status to actuation context. |
| `mechoperref` | character varying | VARCHAR(20) referencing operation(OperReg). |
| `mechdetref` | character varying | VARCHAR(20) referencing robot_details(BotDetReg). |
| `brk1statval` | character varying | VARCHAR(20) capturing brake 1 status (e.g., 'Normal', 'Warning', 'Error'). |
| `brk2statval` | character varying | VARCHAR(30) for brake 2 status (e.g., 'Error', 'Warning', 'Normal'). |
| `brk3statval` | character varying | VARCHAR(25) storing brake 3 status (e.g., 'Normal', 'Error', 'Warning'). |
| `brk4statval` | character varying | VARCHAR(25) describing brake 4 status (e.g., 'Warning', 'Normal', 'Error'). |
| `brk5statval` | character varying | VARCHAR(55) capturing brake 5 status (e.g., 'Warning', 'Error', 'Normal'). |
| `brk6statval` | character varying | VARCHAR(25) referencing brake 6 status (e.g., 'Normal', 'Warning', 'Error'). |
| `enc1statval` | character varying | VARCHAR(35) summarizing encoder 1 status (e.g., 'Warning', 'Normal', 'Error'). |
| `enc2statval` | character varying | VARCHAR(20) capturing encoder 2 status (e.g., 'Error', 'Warning', 'Normal'). |
| `enc3statval` | character varying | VARCHAR(40) referencing encoder 3 status string (e.g., 'Normal', 'Error', 'Warning'). |
| `enc4statval` | character varying | VARCHAR(45) describing encoder 4 condition (e.g., 'Normal', 'Error', 'Warning'). |
| `enc5statval` | character varying | VARCHAR(25) for encoder 5 status (e.g., 'Normal', 'Warning', 'Error'). |
| `enc6statval` | character varying | VARCHAR(20) storing encoder 6 status string (e.g., 'Normal', 'Warning', 'Error'). |
| `gb1tempval` | numeric | NUMERIC(6,2) gearbox 1 temperature reading. |
| `gb2tempval` | real | REAL capturing gearbox 2 temperature as a float. |
| `gb3tempval` | real | FLOAT(5) approximate float for gearbox 3 temperature. |
| `gb4tempval` | numeric | NUMERIC(7,3) gearbox 4 temperature with 3 decimals. |
| `gb5tempval` | real | REAL storing gearbox 5 temperature. |
| `gb6tempval` | real | FLOAT(5) approximate float for gearbox 6 temperature. |
| `gb1vibval` | numeric | NUMERIC(6,3) gearbox 1 vibration measure. |
| `gb2vibval` | real | REAL capturing gearbox 2 vibration amplitude. |
| `gb3vibval` | real | FLOAT(4) approximate float for gearbox 3 vibration. |
| `gb4vibval` | numeric | NUMERIC(5,3) gearbox 4 vibration measure. |
| `gb5vibval` | real | REAL storing gearbox 5 vibration level. |
| `gb6vibval` | real | FLOAT(5) approximate float for gearbox 6 vibration. |

# Joins

* `mechactref` references `actreg` in [actuation_data](/tables/actuation_data.md).
* `mechdetref` references `botdetreg` in [robot_details](/tables/robot_details.md).
* `mechoperref` references `operreg` in [operation](/tables/operation.md).
