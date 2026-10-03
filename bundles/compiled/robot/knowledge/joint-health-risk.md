---
type: Business Rule
title: Joint Health Risk
description: Indicates robots at risk of joint failure.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 42
---

# Definition

A robot R has Joint Health Risk if JDI > 1.5 and MJT > 65.

# Depends on

* [Joint Degradation Index (JDI)](/knowledge/joint-degradation-index.md)
* [Maximum Joint Temperature (MJT)](/knowledge/maximum-joint-temperature.md)
