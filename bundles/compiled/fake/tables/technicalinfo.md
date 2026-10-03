---
type: PostgreSQL Table
title: technicalinfo
description: '13 columns: regip, iprepscore, ipcountrynum, vpnratio, proxycount, torflag, devtotal, devtypedist, browserdiv, uaconsval. Joins to messaginganalysis, networkmetrics.'
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_schema.txt
  title: fake schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_column_meaning_base.json
  title: fake column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `techkey` | character, primary key | A CHAR(12) primary key for each technical info record (e.g., 'TI1234567890'). |
| `technetref` | character | References NetworkMetrics(NetKey) (e.g., 'NE1234567890'). |
| `techmsgref` | character | References MessagingAnalysis(MsgKey) (e.g., 'MA1234567890'). |
| `regip` | inet | An INET column storing the registration IP (e.g., '192.168.0.10'). |
| `iprepscore` | numeric | A NUMERIC(6,3) rating IP reputation (e.g., '0.752'). |
| `ipcountrynum` | smallint | A SMALLINT tracking how many countries this IP is linked to (e.g., '1'). |
| `vpnratio` | numeric | A NUMERIC(7,4) fraction indicating VPN usage frequency (e.g., '0.3456'). |
| `proxycount` | smallint | A SMALLINT counting times a proxy was detected (e.g., '2'). |
| `torflag` | USER-DEFINED | An enum (TorUsageDetected_enum) (Yes, Suspected, No). |
| `devtotal` | smallint | A SMALLINT total number of devices (e.g., '3'). |
| `devtypedist` | jsonb | A JSONB describing device types (e.g., '{"mobile":2, "desktop":1}'). |
| `browserdiv` | numeric | A NUMERIC(5,3) measure of browser diversity (e.g., '1.230'). |
| `uaconsval` | numeric | A NUMERIC(6,5) capturing user-agent consistency (e.g., '0.76543'). |

# Joins

* `techmsgref` references `msgkey` in [messaginganalysis](/tables/messaginganalysis.md).
* `technetref` references `netkey` in [networkmetrics](/tables/networkmetrics.md).

# Related knowledge

* [Technical Evasion Index (TEI)](/knowledge/technical-evasion-index.md)
* [technicalinfo.iprepscore](/knowledge/technicalinfo-iprepscore.md)
* [Cross-Platform Risk Index (CPRI)](/knowledge/cross-platform-risk-index.md)
