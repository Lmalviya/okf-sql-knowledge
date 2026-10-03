---
type: PostgreSQL Table
title: operation
description: '10 columns: totopshrval, apptypeval, opermodeval, currprogval, progcyclecount, cycletimesecval, axiscountval. Joins to robot_details, robot_record.'
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
| `operreg` | character varying, primary key | Primary key (VARCHAR(20)) for an operation record (previously 'OperationRegistry'). |
| `operbotdetref` | character varying | VARCHAR(20) referencing robot_details(BotDetReg). Links this operation record to a specific robot’s details. |
| `operrecref` | character varying | VARCHAR(20) referencing robot_record(RecReg), tying the operation to the main robot record. |
| `totopshrval` | numeric | DECIMAL(9,2) capturing total operating hours for the robot in this operation context. |
| `apptypeval` | character varying | VARCHAR(40) describing the application type (e.g., 'Assembly', 'Painting', 'Palletizing', 'Material Handling', 'Welding'). |
| `opermodeval` | character | CHAR(25) indicating the operation mode (e.g., 'Programming', 'Maintenance', 'Auto', 'Manual'). |
| `currprogval` | character varying | VARCHAR(40) naming the current program loaded or running on the robot. |
| `progcyclecount` | integer | INT counting how many times the program cycle has executed. |
| `cycletimesecval` | numeric | DECIMAL(8,3) measuring cycle time in seconds (precision to three decimals). |
| `axiscountval` | smallint | SMALLINT storing how many axes (joints) the robot uses in this operation environment (e.g., 7, 6, 5, 4). |

# Joins

* `operbotdetref` references `botdetreg` in [robot_details](/tables/robot_details.md).
* `operrecref` references `recreg` in [robot_record](/tables/robot_record.md).

# Related knowledge

* [Total Operating Hours (TOH)](/knowledge/total-operating-hours.md)
* [Number of Operations (NO)](/knowledge/number-of-operations.md)
* [Total Program Cycles (TPC)](/knowledge/total-program-cycles.md)
* [Operation Cycle Efficiency (OCE)](/knowledge/operation-cycle-efficiency.md)
* [Average Cycle Time](/knowledge/average-cycle-time.md)
* [EER Rank](/knowledge/eer-rank.md)
* [Efficiency Metrics](/knowledge/efficiency-metrics.md)
