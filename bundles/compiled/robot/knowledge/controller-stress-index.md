---
type: Calculation
title: Controller Stress Index (CSI)
description: Measures controller stress based on load and thermal metrics.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 36
---

# Definition

For a given robot R, CSI = \frac{\sum_{sc \in \text{system_controller} \mid \text{systemoverseerrobot = R}} (controller_metrics->>'load_value'::float + controller_metrics->>'thermal_level'::float)}{\text{|}\{sc \in \text{system_controller} \mid \text{systemoverseerrobot = R}\}|}, \text{where JSONB fields load_value and thermal_level are averaged.}

# Columns used

* [system_controller](/tables/system_controller.md): `systemoverseerrobot`, `controller_metrics`

# Used by

* [Controller Overload Risk](/knowledge/controller-overload-risk.md)
