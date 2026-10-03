---
type: PostgreSQL Table
title: performance_and_safety
description: '12 columns: conditionindexval, effectivenessindexval, qualitymeasureval, energyusekwhval, pwrfactorval, airpressval, toolchangecount, toolwearpct, safety_metrics. Joins to actuation_data, operation, robot_details.'
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
| `effectivenessactuation` | character varying, primary key | PRIMARY KEY (VARCHAR(20)) referencing actuation_data(ActReg). |
| `effectivenessoperation` | character varying | VARCHAR(20) referencing operation(OperReg). |
| `effectivenessrobot` | character varying | VARCHAR(20) referencing robot_details(BotDetReg). |
| `conditionindexval` | numeric | DECIMAL(6,4) summarizing an index of overall robot condition (health). |
| `effectivenessindexval` | numeric | NUMERIC(4,2) capturing how effectively the robot is performing (could be throughput or success rate). |
| `qualitymeasureval` | real | FLOAT(5) approximate float for quality measurement or pass rate. |
| `energyusekwhval` | numeric | NUMERIC(7,2) referencing energy used in kWh over a certain period. |
| `pwrfactorval` | real | FLOAT(4) a float for power factor if the robot system uses AC power. |
| `airpressval` | numeric | DECIMAL(6,3) measuring compressed air pressure if pneumatic components are used. |
| `toolchangecount` | integer | INT referencing how many times a tool was changed on the robot. |
| `toolwearpct` | real | REAL storing estimated tool wear percentage. |
| `safety_metrics` | jsonb | JSONB column. Captures safety-related metrics and events, such as safety state, zone violations, emergency stops, collisions, overloads, speed violations, and calibration status. |

# JSON fields

* `safety_metrics.safety_state`: VARCHAR(25) describing current safety state (e.g., 'Emergency', 'Normal', 'Warning').
* `safety_metrics.zone_violations`: SMALLINT counting how many times the robot violated safe zones.
* `safety_metrics.emergency_stops`: SMALLINT logging how many e-stop (emergency stop) events occurred (e.g., 0, 1, 2, 3, 4, 5).
* `safety_metrics.collisions`: INT referencing collisions or crash incidents (e.g., 0, 1, 2, 3).
* `safety_metrics.overloads`: SMALLINT enumerating overload events (payload, torque) (e.g., 0, 1, 2, 3, 4, 5).
* `safety_metrics.speed_violations`: INT counting overspeed or velocity-limit violations.
* `safety_metrics.calibration_state`: CHAR(20) summarizing calibration state (e.g., 'Valid', 'Due', 'Invalid').

# Joins

* `effectivenessactuation` references `actreg` in [actuation_data](/tables/actuation_data.md).
* `effectivenessoperation` references `operreg` in [operation](/tables/operation.md).
* `effectivenessrobot` references `botdetreg` in [robot_details](/tables/robot_details.md).

# Related knowledge

* [Energy Efficiency Ratio (EER)](/knowledge/energy-efficiency-ratio.md)
* [Safety Incident Score (SIS)](/knowledge/safety-incident-score.md)
* [Tool Wear Rate (TWR)](/knowledge/tool-wear-rate.md)
