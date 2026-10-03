---
type: Business Rule
title: Streaming-Optimized Device
description: Identifies devices specifically designed for content creators and streamers with appropriate features.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 15
---

# Definition

A device with MicSenseDb < -45, MicFreqResp covering at least '50Hz-18kHz', McRespTime < 1.0, and ProfCount ≥ 5, allowing streamers to capture high-quality audio while maintaining flexible device configurations.

# Columns used

* [deviceidentity](/tables/deviceidentity.md): `profcount`, `mcresptime`
* [audioandmedia](/tables/audioandmedia.md): `micsensedb`, `micfreqresp`
