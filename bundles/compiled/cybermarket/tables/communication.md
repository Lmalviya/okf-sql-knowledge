---
type: PostgreSQL Table
title: communication
description: '18 columns: iptally, tornodecount, vpnflag, brwsrunique, devfpscore, connpatscore, encryptmethod, commchannel, msgtally, commfreq, langpattern, sentiscore, keymatchcount, susppatscore, riskindiccount. Joins to products, transactions.'
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_schema.txt
  title: cybermarket schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_column_meaning_base.json
  title: cybermarket column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `commregistry` | character varying, primary key | Primary key (VARCHAR(30)) for a communication/log record (e.g., 'COMM-98765'). |
| `iptally` | smallint | A SMALLINT counting distinct IP addresses involved (e.g., 5). |
| `tornodecount` | smallint | A SMALLINT counting how many TOR nodes/relays were detected (e.g., 2). |
| `vpnflag` | USER-DEFINED | An enum (VpnFlag_enum) indicating VPN usage (Yes, No, Suspected). |
| `brwsrunique` | numeric | A NUMERIC(6,3) measuring browser fingerprint uniqueness (e.g., 592.223). |
| `devfpscore` | numeric | A NUMERIC(6,3) device fingerprint score (e.g., 310.502). |
| `connpatscore` | numeric | A NUMERIC(5,2) rating suspicious connection patterns (e.g., 75.50). |
| `encryptmethod` | USER-DEFINED | An enum (EncryptMethod_enum) for encryption use (Custom, Standard, Enhanced). |
| `commchannel` | USER-DEFINED | An enum (CommChannel_enum) describing the channel (Mixed, External, Internal). |
| `msgtally` | smallint | A SMALLINT total messages in the session (e.g., 45). |
| `commfreq` | USER-DEFINED | An enum (CommFreq_enum) describing communication frequency (Low, Medium, High). |
| `langpattern` | USER-DEFINED | An enum (LangPattern_enum) describing language usage (Variable, Suspicious, Consistent). |
| `sentiscore` | numeric | A NUMERIC(5,3) sentiment score (e.g., 37.125). |
| `keymatchcount` | smallint | A SMALLINT counting cryptographic or keyword matches (e.g., 3). |
| `susppatscore` | numeric | A NUMERIC(5,2) suspicious pattern rating (e.g., 82.50). |
| `riskindiccount` | smallint | A SMALLINT tally of identified risk indicators or flags (e.g., 5). |
| `txref` | character varying | FK referencing Transactions(TxRegistry) if communication is tied to a transaction. |
| `prodref` | character varying | FK referencing Products(ProdRegistry) if communication pertains to a product listing. |

# Joins

* `prodref` references `prodregistry` in [products](/tables/products.md).
* `txref` references `txregistry` in [transactions](/tables/transactions.md).

# Related knowledge

* [cybermarket|communication|vpnflag](/knowledge/cybermarket-communication-vpnflag.md)
* [cybermarket|communication|langpattern](/knowledge/cybermarket-communication-langpattern.md)
* [Communication Security Risk (CSR)](/knowledge/communication-security-risk.md)
* [Anonymity Protection Level (APL)](/knowledge/anonymity-protection-level.md)
* [Identity-Protected User](/knowledge/identity-protected-user.md)
* [Sophisticated Operational Security](/knowledge/sophisticated-operational-security.md)
* [Cross-Platform Operator](/knowledge/cross-platform-operator.md)
* [Communication Pattern Risk (CPR)](/knowledge/communication-pattern-risk.md)
* [Operational Security Index (OSI)](/knowledge/operational-security-index.md)
* [Cross-Platform Risk Amplification (CPRA)](/knowledge/cross-platform-risk-amplification.md)
* [OpSec Specialist](/knowledge/opsec-specialist.md)
