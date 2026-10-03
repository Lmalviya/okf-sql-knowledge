---
type: Calculation
title: Resource Self-Sufficiency Index (RSSI)
description: Measures a polar site's self-sufficiency in terms of resources
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 35
---

# Definition

RSSI = 0.6 × REC + 0.4 × WRMI

# Depends on

* [Water Resource Management Index (WRMI)](/knowledge/water-resource-management-index.md)
* [Renewable Energy Contribution (REC)](/knowledge/renewable-energy-contribution.md)

# Used by

* [Sustainable Polar Operations (SPO)](/knowledge/sustainable-polar-operations.md)
* [Polar Base Energy Security Status (PBESS)](/knowledge/polar-base-energy-security-status.md)
