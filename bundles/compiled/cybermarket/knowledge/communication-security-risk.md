---
type: Calculation
title: Communication Security Risk (CSR)
description: Evaluates the security risk of a communication channel
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 13
---

# Definition

CSR = (iptally \times 5) + (tornodecount \times 2) + (vpnflag\_numeric \times 30) + \frac{brwsrunique}{10} + (susppatscore \times 3) + (riskindiccount \times 4), \text{where vpnflag\_numeric maps Yes=1, Suspected=0.5, No=0, and higher scores indicate greater security concerns.}

# Columns used

* [communication](/tables/communication.md): `iptally`, `tornodecount`, `vpnflag`, `brwsrunique`, `susppatscore`, `riskindiccount`

# Used by

* [Communication Pattern Risk (CPR)](/knowledge/communication-pattern-risk.md)
* [Deceptive Communication Pattern](/knowledge/deceptive-communication-pattern.md)
