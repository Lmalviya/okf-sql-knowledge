---
type: Calculation
title: Communication Pattern Risk (CPR)
description: Evaluates how suspicious a communication pattern is based on multiple factors
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 33
---

# Definition

CPR = (langpattern_numeric \times 15) + (CSR \times 0.2) + (msgtally \times 0.5) - (1 - vpnflag_numeric) \times 20, \text{where langpattern_numeric maps Consistent=1, Variable=2, Suspicious=3 as explained in the language pattern classification, and higher scores represent more suspicious communication behavior.}

# Columns used

* [communication](/tables/communication.md): `msgtally`

# Depends on

* [cybermarket|communication|langpattern](/knowledge/cybermarket-communication-langpattern.md)
* [Communication Security Risk (CSR)](/knowledge/communication-security-risk.md)

# Used by

* [Deceptive Communication Pattern](/knowledge/deceptive-communication-pattern.md)
