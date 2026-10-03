---
type: Business Rule
title: Showcase Compatibility Issue
description: Identifies incompatible artifact-showcase pairings requiring adjustment.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 44
---

# Definition

Occurs when SPA < 0 AND the artifact is classified as having High-Value.

# Depends on

* [Showcase Protection Adequacy (SPA)](/knowledge/showcase-protection-adequacy.md)
* [High-Value Artifact](/knowledge/high-value-artifact.md)
