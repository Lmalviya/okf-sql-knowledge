---
type: Business Rule
title: High-Value Category
description: Classification system for categorizing high-value artifacts based on their monetary or cultural/historical significance.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 51
---

# Definition

An artifact falls into 'Monetary High-Value' category when its InsValueUSD exceeds $1,000,000. It qualifies as 'Cultural/Historical High-Value' when both its HistSignRating and CultScore are in the top 10% of all artifacts (percentile rank = 1). Otherwise 'Other'.

# Columns used

* [artifactratings](/tables/artifactratings.md): `histsignrating`, `cultscore`
* [artifactsecurityaccess](/tables/artifactsecurityaccess.md): `insvalueusd`

# Depends on

* [High-Value Artifact](/knowledge/high-value-artifact.md)
