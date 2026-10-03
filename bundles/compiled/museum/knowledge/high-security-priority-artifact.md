---
type: Business Rule
title: High Security Priority Artifact
description: Identifies artifacts requiring enhanced security measures.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 48
---

# Definition

An artifact that is classified as High-Value AND has an SRE > 5.

# Depends on

* [High-Value Artifact](/knowledge/high-value-artifact.md)
* [Security Risk Exposure (SRE)](/knowledge/security-risk-exposure.md)
