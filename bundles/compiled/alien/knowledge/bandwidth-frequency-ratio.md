---
type: Calculation
title: Bandwidth-Frequency Ratio (BFR)
description: Measures the proportion of bandwidth to center frequency, helping identify signal type.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 4
---

# Definition

$\text{BFR} = \frac{\text{BwHz}}{\text{CenterFreqMhz} \times 10^6}$, where narrow ratios ($<0.001$) often indicate technological signals while wider ratios suggest natural phenomena.

# Columns used

* [signals](/tables/signals.md): `bwhz`, `centerfreqmhz`

# Used by

* [Technosignature](/knowledge/technosignature.md)
* [Narrowband Technological Marker (NTM)](/knowledge/narrowband-technological-marker.md)
* [SignalClass: Narrowband](/knowledge/signalclass-narrowband.md)
* [SigClassType: Broadband Transient](/knowledge/sigclasstype-broadband-transient.md)
* [NTM Classification System](/knowledge/ntm-classification-system.md)
