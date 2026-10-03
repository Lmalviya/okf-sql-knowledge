---
type: Calculation
title: Payload Utilization Ratio (PUR)
description: Measures how close the robot operates to its payload capacity.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 39
---

# Definition

For a given robot R, PUR = \frac{\sum_{ad \in \text{actuation_data} \mid \text{actdetref = R}} payloadwval}{\text{(robot_details.payloadcapkg where botdetref = R)} \cdot \text{|}\{ad \in \text{actuation_data} \mid \text{actdetref = R}\}|}, \text{where RAY adjusts for age-related capacity changes if applicable.}

# Columns used

* [robot_details](/tables/robot_details.md): `payloadcapkg`
* [actuation_data](/tables/actuation_data.md): `actdetref`, `payloadwval`

# Depends on

* [Robot Age in Years (RAY)](/knowledge/robot-age-in-years.md)

# Used by

* [Overloaded Robot](/knowledge/overloaded-robot.md)
