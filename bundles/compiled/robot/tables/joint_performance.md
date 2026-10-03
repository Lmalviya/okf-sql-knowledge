---
type: PostgreSQL Table
title: joint_performance
description: '4 columns: joint_metrics. Joins to operation, robot_details, robot_record.'
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
| `jperfoperref` | character varying | VARCHAR(20) referencing operation(OperReg). Associates these joint performance metrics with a specific operation. |
| `jperfrecref` | character varying | VARCHAR(20) referencing robot_record(RecReg). |
| `jperfdetref` | character varying | VARCHAR(20) referencing robot_details(BotDetReg). |
| `joint_metrics` | jsonb | JSONB column. Groups performance metrics for each joint, including angle, speed, and torque, organized by joint number for easier access. |

# JSON fields

* `joint_metrics.joint1.angle`: NUMERIC(6,2) indicating the angle (degrees or radians) of Joint 1 at measurement.
* `joint_metrics.joint1.speed`: NUMERIC(4,1) speed of Joint 1. Possibly in deg/s or rad/s, depends on system config.
* `joint_metrics.joint1.torque`: NUMERIC(5,2) measuring torque for Joint 1. Possibly in Nm.
* `joint_metrics.joint2.angle`: REAL capturing the angle of Joint 2. Stored as a float with platform-specific precision.
* `joint_metrics.joint2.speed`: NUMERIC(6,3) speed of Joint 2 with up to three decimals.
* `joint_metrics.joint2.torque`: FLOAT(4) approximate float for Joint 2 torque.
* `joint_metrics.joint3.angle`: FLOAT(5) a float with approx. 5 binary digits precision for Joint 3 angle.
* `joint_metrics.joint3.speed`: REAL for speed of Joint 3.
* `joint_metrics.joint3.torque`: REAL capturing Joint 3 torque.
* `joint_metrics.joint4.angle`: NUMERIC(7,3) angle of Joint 4. More precise decimal.
* `joint_metrics.joint4.speed`: FLOAT(5) a float for Joint 4’s speed, limited precision.
* `joint_metrics.joint4.torque`: NUMERIC(6,3) decimal for Joint 4 torque.
* `joint_metrics.joint5.angle`: REAL storing angle of Joint 5.
* `joint_metrics.joint5.speed`: NUMERIC(5,2) speed of Joint 5 (e.g., deg/s).
* `joint_metrics.joint5.torque`: NUMERIC(7,4) storing Joint 5 torque with four decimal places.
* `joint_metrics.joint6.angle`: FLOAT(6) a float with approx. 6 binary digits precision for Joint 6 angle.
* `joint_metrics.joint6.speed`: REAL storing speed for Joint 6.
* `joint_metrics.joint6.torque`: FLOAT(6) approximate float for Joint 6 torque value.

# Joins

* `jperfdetref` references `botdetreg` in [robot_details](/tables/robot_details.md).
* `jperfoperref` references `operreg` in [operation](/tables/operation.md).
* `jperfrecref` references `recreg` in [robot_record](/tables/robot_record.md).

# Related knowledge

* [Joint Torque Variance (JTV)](/knowledge/joint-torque-variance.md)
