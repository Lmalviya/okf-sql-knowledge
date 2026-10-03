---
type: Calculation
title: Showcase Environmental Stability Rating (SESR)
description: Measures how well a showcase maintains stable environmental conditions.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 5
---

# Definition

SESR = 10 - \frac{(TempVar24h + \frac{HumVar24h}{5} + LeakRate)}{3}, \text{where higher scores indicate more stable showcases}

# Columns used

* [showcases](/tables/showcases.md): `leakrate`
* [environmentalreadingscore](/tables/environmentalreadingscore.md): `tempvar24h`, `humvar24h`

# Used by

* [Artifact Exhibition Compatibility (AEC)](/knowledge/artifact-exhibition-compatibility.md)
* [Showcase Failure Risk](/knowledge/showcase-failure-risk.md)
* [Showcase Protection Adequacy (SPA)](/knowledge/showcase-protection-adequacy.md)
