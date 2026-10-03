---
type: Calculation
title: JDI-TOH Regression Slope
description: Measures the linear relationship between Joint Degradation Index and Total Operating Hours using regression.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 50
---

# Definition

For a set of robots meeting JDI > 1.5, MJT > 65, and TOH > 5000, the JDI-TOH Regression Slope is given by \[ \text{slope} = \frac{n \sum (x_i y_i) - \sum x_i \sum y_i}{n \sum x_i^2 - (\sum x_i)^2} \] where \( y_i = \text{JDI} \) (Joint Degradation Index for robot \( i \)), \( x_i = \text{TOH} \) (Total Operating Hours for robot \( i \)), \( n \) is the number of qualifying robots, and sums are over all qualifying robots.

# Depends on

* [Joint Degradation Index (JDI)](/knowledge/joint-degradation-index.md)
* [Total Operating Hours (TOH)](/knowledge/total-operating-hours.md)
