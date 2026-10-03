---
type: Business Rule
title: Networked Mimicry Risk
description: Flags traders suspected of peer mimicry who are also part of an identified potential collusion network.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 62
---

# Definition

A trader flagged for Peer Mimicry Suspicion  AND associated with a Collusion Network Indicator .

# Depends on

* [Collusion Network Indicator](/knowledge/collusion-network-indicator.md)
* [Peer Mimicry Suspicion](/knowledge/peer-mimicry-suspicion.md)
