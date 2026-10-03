---
type: Business Rule
title: Extended Battery Life Device
description: Identifies devices with exceptionally efficient battery performance for extended gaming sessions.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 13
---

# Definition

A device with BER > 7.5, BattLifeH > 30, QChgFlag = true, and PwrIdleMw < 100, enabling marathon gaming sessions with minimal charging interruptions.

# Columns used

* [testsessions](/tables/testsessions.md): `battlifeh`, `qchgflag`
* [deviceidentity](/tables/deviceidentity.md): `pwridlemw`

# Depends on

* [Battery Efficiency Ratio (BER)](/knowledge/battery-efficiency-ratio.md)
