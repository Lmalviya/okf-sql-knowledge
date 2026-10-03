---
type: Business Rule
title: Light Exposure Thresholds
description: Defines maximum safe light exposure levels for artifacts based on material sensitivity
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 53
---

# Definition

High sensitivity artifacts (textiles, paper) must not exceed 50 lux; Medium sensitivity (paintings, wood) must not exceed 200 lux. Based on conservation research about light-induced deterioration rates.

# Depends on

* [Light Exposure Risk (LER)](/knowledge/light-exposure-risk.md)
* [ArtifactsCore.ConserveStatus](/knowledge/artifactscore-conservestatus.md)
