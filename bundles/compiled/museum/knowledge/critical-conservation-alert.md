---
type: Business Rule
title: Critical Conservation Alert
description: Identifies artifacts in critical condition requiring immediate intervention.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 41
---

# Definition

An artifact that meets both the Conservation Emergency criteria AND has an AVS > 8.

# Depends on

* [Conservation Emergency](/knowledge/conservation-emergency.md)
* [Artifact Vulnerability Score (AVS)](/knowledge/artifact-vulnerability-score.md)
