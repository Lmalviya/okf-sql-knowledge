---
type: Business Rule
title: Deceptive Communication Pattern
description: Identifies communication exhibiting signs of deliberate deception
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 43
---

# Definition

A communication with CPR > 70, 'Suspicious' language patterns as defined in the language pattern classification, high CSR values (CSR > 80), and frequently changing connection parameters. These patterns suggest deliberate attempts to obfuscate identity and intentions.

# Depends on

* [cybermarket|communication|langpattern](/knowledge/cybermarket-communication-langpattern.md)
* [Communication Security Risk (CSR)](/knowledge/communication-security-risk.md)
* [Communication Pattern Risk (CPR)](/knowledge/communication-pattern-risk.md)
