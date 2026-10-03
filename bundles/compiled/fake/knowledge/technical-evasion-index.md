---
type: Calculation
title: Technical Evasion Index (TEI)
description: Quantifies attempts to evade detection.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 7
---

# Definition

TEI = 0.4 \times \text{vpnratio} + 0.3 \times \frac{\text{proxycount}}{10} + 0.3 \times \frac{\text{ipcountrynum}}{20}

# Columns used

* [technicalinfo](/tables/technicalinfo.md): `ipcountrynum`, `vpnratio`, `proxycount`

# Used by

* [VPN Abuser](/knowledge/vpn-abuser.md)
* [Automated Behavior Score (ABS)](/knowledge/automated-behavior-score.md)
* [Authentication Risk Score (ARS)](/knowledge/authentication-risk-score.md)
* [Advanced Persistent Threat](/knowledge/advanced-persistent-threat.md)
* [Authentication Pattern Score (APS)](/knowledge/authentication-pattern-score.md)
* [TEI quartile](/knowledge/tei-quartile.md)
