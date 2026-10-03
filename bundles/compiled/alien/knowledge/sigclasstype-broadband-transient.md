---
type: Value Illustration
title: 'SigClassType: Broadband Transient'
description: Illustrates a class of brief signals covering wide frequency ranges.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 25
---

# Definition

Describes short-duration signals ($\text{SigDurSec}$ typically $< 5$) that span a large portion of the spectrum ($\text{BFR} > 0.1$). Examples include solar radio bursts, lightning discharges, and certain types of cosmic explosions like Fast Radio Bursts (FRBs).

# Columns used

* [signals](/tables/signals.md): `sigdursec`
* [signalclassification](/tables/signalclassification.md): `sigclasstype`

# Depends on

* [Bandwidth-Frequency Ratio (BFR)](/knowledge/bandwidth-frequency-ratio.md)
