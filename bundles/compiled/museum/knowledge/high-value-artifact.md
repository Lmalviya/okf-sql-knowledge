---
type: Business Rule
title: High-Value Artifact
description: Identifies artifacts with exceptional historical, cultural, or monetary value requiring special attention.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 11
---

# Definition

An artifact is considered high-value when its InsValueUSD exceeds $1,000,000 OR when both HistSignRating and CultScore are in the top 10% of all artifacts.

# Columns used

* [artifactratings](/tables/artifactratings.md): `histsignrating`, `cultscore`
* [artifactsecurityaccess](/tables/artifactsecurityaccess.md): `insvalueusd`

# Used by

* [Showcase Compatibility Issue](/knowledge/showcase-compatibility-issue.md)
* [High Security Priority Artifact](/knowledge/high-security-priority-artifact.md)
* [High-Value Category](/knowledge/high-value-category.md)
