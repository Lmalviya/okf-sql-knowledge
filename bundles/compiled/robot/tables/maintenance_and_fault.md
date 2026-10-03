---
type: PostgreSQL Table
title: maintenance_and_fault
description: '11 columns: faultcodeval, issuecategoryval, issuelevelval, faultpredscore, faulttypeestimation, rulhours, upkeepduedays, upkeepcostest. Joins to actuation_data, operation, robot_details.'
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
| `upkeepactuation` | character varying, primary key | PRIMARY KEY (VARCHAR(20)) referencing actuation_data(ActReg). Ties maintenance/fault record to actuation data. |
| `upkeepoperation` | character varying | VARCHAR(20) referencing operation(OperReg). |
| `upkeeprobot` | character varying | VARCHAR(20) referencing robot_details(BotDetReg). |
| `faultcodeval` | character varying | VARCHAR(25) storing a code for the specific fault (e.g., 'F1234'). |
| `issuecategoryval` | character varying | VARCHAR(22) labeling the fault or issue category (e.g., 'Communication', 'Electrical', 'Mechanical', 'Software'). |
| `issuelevelval` | character varying | VARCHAR(18) describing severity or priority (e.g., 'Low', 'High', 'Medium', 'Critical'). |
| `faultpredscore` | real | FLOAT(5) approximate float rating the probability or severity of fault. |
| `faulttypeestimation` | character varying | VARCHAR(20) referencing the likely fault type (e.g., 'Motor', 'Joint', 'Gearbox', 'Controller'). |
| `rulhours` | integer | INT storing Remaining Useful Life in hours if predicted. |
| `upkeepduedays` | smallint | SMALLINT capturing days until next scheduled maintenance is due. |
| `upkeepcostest` | numeric | DECIMAL(9,3) estimated cost for upcoming maintenance or repair. |

# Joins

* `upkeepactuation` references `actreg` in [actuation_data](/tables/actuation_data.md).
* `upkeepoperation` references `operreg` in [operation](/tables/operation.md).
* `upkeeprobot` references `botdetreg` in [robot_details](/tables/robot_details.md).

# Related knowledge

* [Recent Fault Prediction Score (RFPS)](/knowledge/recent-fault-prediction-score.md)
* [Minimum Remaining Useful Life (MRUL)](/knowledge/minimum-remaining-useful-life.md)
* [Weighted Fault Prediction Score (WFPS)](/knowledge/weighted-fault-prediction-score.md)
* [Maintenance Cost Trend (MCT)](/knowledge/maintenance-cost-trend.md)
