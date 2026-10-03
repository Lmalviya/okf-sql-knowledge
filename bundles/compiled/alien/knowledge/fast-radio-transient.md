---
type: Business Rule
title: Fast Radio Transient (FRT)
description: Defines a specific class of brief, high-energy radio emissions.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 19
---

# Definition

Signals with extremely short duration ($\text{SigDurSec} < 0.1$), high signal strength ($\text{SigStrDb} > 15$), broad bandwidth ($\text{BwHz} > 1000000$), and no periodicity ($\text{RepeatCount} = 1$).

# Columns used

* [signals](/tables/signals.md): `sigstrdb`, `bwhz`, `sigdursec`
* [signalclassification](/tables/signalclassification.md): `repeatcount`
