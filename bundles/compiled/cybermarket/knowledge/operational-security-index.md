---
type: Calculation
title: Operational Security Index (OSI)
description: Quantifies an entity's operational security practices
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 36
---

# Definition

OSI = (APL \times 0.5) + (SPS \times 0.2) + (tornodecount \times 2) + (CASE WHEN encryptmethod = 'Standard' THEN 1 WHEN encryptmethod = 'Enhanced' THEN 2 WHEN encryptmethod = 'Custom' THEN 3 ELSE 0 END \times 5) - (iptally \times 0.5), \text{where APL and SPS are defined by the Anonymity Protection Level and Security Posture Score respectively, and higher scores indicate stronger operational security.}

# Columns used

* [communication](/tables/communication.md): `iptally`, `tornodecount`, `encryptmethod`

# Depends on

* [Security Posture Score (SPS)](/knowledge/security-posture-score.md)
* [Anonymity Protection Level (APL)](/knowledge/anonymity-protection-level.md)

# Used by

* [OpSec Specialist](/knowledge/opsec-specialist.md)
