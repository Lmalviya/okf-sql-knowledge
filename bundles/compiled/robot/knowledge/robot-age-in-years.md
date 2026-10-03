---
type: Calculation
title: Robot Age in Years (RAY)
description: Calculates the age of the robot in years based on installation date and record timestamp.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 0
---

# Definition

For a given robot R, let D be the instdateval from robot_details where botdetreg = R, and T be the rects from robot_record where recreg = R. Then, RAY = \frac{(T - D).days}{365.25}

# Columns used

* [robot_record](/tables/robot_record.md): `recreg`, `rects`
* [robot_details](/tables/robot_details.md): `botdetreg`, `instdateval`

# Used by

* [Old Robot](/knowledge/old-robot.md)
* [Payload Utilization Ratio (PUR)](/knowledge/payload-utilization-ratio.md)
* [Escalating Maintenance Costs](/knowledge/escalating-maintenance-costs.md)
* [Overloaded Robot](/knowledge/overloaded-robot.md)
