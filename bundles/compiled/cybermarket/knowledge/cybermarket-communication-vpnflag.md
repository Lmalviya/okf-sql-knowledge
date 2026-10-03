---
type: Value Illustration
title: cybermarket|communication|vpnflag
description: Explains the significance of VPN detection in communication analysis
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 5
---

# Definition

'Yes' indicates confirmed VPN usage, demonstrating deliberate attempts to mask true location and identity; 'No' suggests direct connections potentially revealing actual user locations; 'Suspected' indicates communication patterns consistent with VPN usage but lacking definitive confirmation, requiring further investigation to determine the true level of identity obfuscation.

# Columns used

* [communication](/tables/communication.md): `vpnflag`
