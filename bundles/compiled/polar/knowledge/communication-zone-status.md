---
type: Business Rule
title: Communication Zone Status
description: Evaluates the communication coverage and reliability in different operational zones.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 14
---

# Definition

A zone is classified as having 'Reliable Coverage' when equipment within it maintains a CRI > 7, has active satellite connections (signalmetrics.satellite_status = 'Connected'), and supports emergency beacon functionality (emergencybeaconstatus != 'Inactive').

# Columns used

* [communication](/tables/communication.md): `signalmetrics`
* [cabinenvironment](/tables/cabinenvironment.md): `emergencybeaconstatus`

# Depends on

* [Communication Reliability Index (CRI)](/knowledge/communication-reliability-index.md)
