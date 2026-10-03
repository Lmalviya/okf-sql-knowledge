---
type: Business Rule
title: Mesh Quality Classification
description: A standardized system for categorizing archaeological site documentation based on the presence and quality of 3D mesh models.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 53
---

# Definition

A three-tier classification where 'Has High-Fidelity Meshes' indicates sites with at least one mesh meeting high-fidelity criteria, 'Standard Mesh Quality' indicates sites with meshes that don't meet high-fidelity standards, and 'No Mesh Data' indicates sites lacking 3D mesh documentation entirely. This classification helps prioritize additional documentation efforts and determines appropriate analytical approaches for different sites.

# Depends on

* [High Fidelity Mesh](/knowledge/high-fidelity-mesh.md)
