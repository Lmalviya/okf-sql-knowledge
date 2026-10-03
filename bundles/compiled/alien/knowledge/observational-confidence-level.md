---
type: Business Rule
title: Observational Confidence Level (OCL)
description: Rates the reliability of observations based on conditions and equipment.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 16
---

# Definition

A classification system with three tiers: 'High' ($\text{AOI} > 0.8$, $\text{EquipStatus} = \text{'Operational'}$, $\text{CalibrStatus} = \text{'Current'}$), 'Medium' ($\text{AOI}$ 0.5-0.8, minor equipment issues), and 'Low' ($\text{AOI} < 0.5$ or significant equipment problems).

# Columns used

* [telescopes](/tables/telescopes.md): `equipstatus`, `calibrstatus`

# Depends on

* [Atmospheric Observability Index (AOI)](/knowledge/atmospheric-observability-index.md)
