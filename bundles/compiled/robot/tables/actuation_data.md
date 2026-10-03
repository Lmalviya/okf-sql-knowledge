---
type: PostgreSQL Table
title: actuation_data
description: '29 columns: tcpxval, tcpyval, tcpzval, tcp_rxval, tcp_ryval, tcp_rzval, tcpspeedval, tcpaccelval, pathaccmmval, poserrmmval, orienterrdegval, payloadwval, payloadival, m1currval, m2currval, m3currval, m4currval, m5currval, m6currval, m1voltval, m2voltval, m3voltval, m4voltval, m5voltval, m6voltval. Joins to operation, robot_details, robot_record.'
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
| `actreg` | character varying, primary key | Primary key (VARCHAR(20)) for actuation data records. |
| `actoperref` | character varying | VARCHAR(20) referencing operation(OperReg). Ties actuation data to a particular operation. |
| `actdetref` | character varying | VARCHAR(20) referencing robot_details(BotDetReg). Connects to a specific robot’s details. |
| `actrecref` | character varying | VARCHAR(20) referencing robot_record(RecReg). |
| `tcpxval` | numeric | NUMERIC(7,2) storing TCP (Tool Center Point) X-coordinate in a relevant unit (mm, cm). |
| `tcpyval` | real | REAL capturing TCP Y-coordinate as a float. |
| `tcpzval` | real | FLOAT(5) approximate float for TCP Z-coordinate. |
| `tcp_rxval` | numeric | NUMERIC(6,2) rotation around X-axis for the tool center point. |
| `tcp_ryval` | real | FLOAT(6) rotation around Y-axis, approximate float. |
| `tcp_rzval` | real | REAL for rotation around Z-axis. |
| `tcpspeedval` | numeric | NUMERIC(8,2) capturing linear speed of the TCP (e.g., mm/s). |
| `tcpaccelval` | real | REAL storing acceleration at the tool center point. |
| `pathaccmmval` | numeric | NUMERIC(6,3) path accuracy in millimeters (difference from taught path). |
| `poserrmmval` | real | FLOAT(5) position error in mm. |
| `orienterrdegval` | real | REAL measuring orientation error in degrees. |
| `payloadwval` | numeric | NUMERIC(6,2) specifying payload weight in kg if relevant. |
| `payloadival` | real | FLOAT(4) capturing payload inertia or moment, if used. |
| `m1currval` | numeric | NUMERIC(6,2) motor 1 current draw in amps, for example. |
| `m2currval` | real | REAL storing motor 2 current draw. |
| `m3currval` | real | FLOAT(5) approximate float for motor 3 current. |
| `m4currval` | numeric | NUMERIC(6,2) decimal for motor 4 current. |
| `m5currval` | real | REAL capturing motor 5 current. |
| `m6currval` | real | FLOAT(4) approximate float for motor 6 current. |
| `m1voltval` | numeric | NUMERIC(5,2) voltage reading for motor 1. |
| `m2voltval` | real | REAL storing voltage of motor 2. |
| `m3voltval` | real | FLOAT(6) approximate float for motor 3 voltage. |
| `m4voltval` | numeric | NUMERIC(6,2) decimal for motor 4 voltage. |
| `m5voltval` | real | REAL capturing motor 5 voltage. |
| `m6voltval` | real | FLOAT(5) approximate float for motor 6 voltage. |

# Joins

* `actdetref` references `botdetreg` in [robot_details](/tables/robot_details.md).
* `actoperref` references `operreg` in [operation](/tables/operation.md).
* `actrecref` references `recreg` in [robot_record](/tables/robot_record.md).

# Related knowledge

* [Average Position Error (APE)](/knowledge/average-position-error.md)
* [Average TCP Speed (ATCS)](/knowledge/average-tcp-speed.md)
* [Payload Utilization Ratio (PUR)](/knowledge/payload-utilization-ratio.md)
