---
type: Calculation
title: Anonymity Protection Level (APL)
description: Measures how well a user's identity is protected
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 19
---

# Definition

APL = (vpnflag\_numeric \times 30) + (tornodecount \times 2) + (encryptmethod\_numeric \times 15) + (connpatscore \times 0.2) + \frac{brwsrunique}{20}, \text{where vpnflag\_numeric maps Yes=1, Suspected=0.5, No=0, encryptmethod\_numeric maps Standard=1, Enhanced=2, Custom=3, else=0 and higher scores indicate stronger anonymity protections.}

# Columns used

* [communication](/tables/communication.md): `tornodecount`, `vpnflag`, `brwsrunique`, `connpatscore`, `encryptmethod`

# Used by

* [Identity-Protected User](/knowledge/identity-protected-user.md)
* [Sophisticated Operational Security](/knowledge/sophisticated-operational-security.md)
* [Operational Security Index (OSI)](/knowledge/operational-security-index.md)
* [OpSec Specialist](/knowledge/opsec-specialist.md)
