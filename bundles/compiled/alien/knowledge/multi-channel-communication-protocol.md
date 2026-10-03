---
type: Business Rule
title: Multi-Channel Communication Protocol
description: Identifies signal patterns consistent with sophisticated communication protocols.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 42
---

# Definition

Signal exhibiting Coherent Information Pattern (CIP) characteristics across multiple frequency channels with coordinated timing ($\text{RepeatCount} > 3$, $\text{PeriodSec}$ consistent across observations) and $\text{ECI} > 2.0$, suggesting a designed communication system.

# Columns used

* [signalclassification](/tables/signalclassification.md): `repeatcount`, `periodsec`

# Depends on

* [Coherent Information Pattern (CIP)](/knowledge/coherent-information-pattern.md)
* [Encoding Complexity Index (ECI)](/knowledge/encoding-complexity-index.md)
