---
type: Business Rule
title: Dynasty Value Artifact
description: Identifies artifacts from historically significant dynasties with higher research and cultural value.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 18
---

# Definition

Artifacts from 'Ming', 'Han', or 'Tang' dynasties that also have ResearchValRating > 8.

# Columns used

* [artifactratings](/tables/artifactratings.md): `researchvalrating`

# Used by

* [Dynasty Artifact at Risk](/knowledge/dynasty-artifact-at-risk.md)
