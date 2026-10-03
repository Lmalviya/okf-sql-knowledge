---
type: PostgreSQL Table
title: advancedbehavior
description: '6 columns: patsim, peercorr, mktcorr, secrotimp. Joins to transactionrecord.'
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_schema.txt
  title: insider schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_column_meaning_base.json
  title: insider column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `abhvreg` | character varying, primary key | VARCHAR(50). Primary key for an advanced behavioural analysis record. |
| `translink` | character varying | VARCHAR(50). Foreign‑key to TransactionRecord.TransReg. |
| `patsim` | numeric | NUMERIC(7,4). Similarity score to known illicit trading patterns (e.g., 0.8754). |
| `peercorr` | numeric | NUMERIC(7,4). Correlation of the trader’s pattern with peers (e.g., 0.6432). |
| `mktcorr` | numeric | NUMERIC(7,4). Correlation of trading activity with overall market moves (e.g., 0.5123). |
| `secrotimp` | numeric | NUMERIC(7,4). Impact of sector rotation strategies used by the trader (e.g., 0.2198). |

# Joins

* `translink` references `transreg` in [transactionrecord](/tables/transactionrecord.md).

# Related knowledge

* [Pattern Anomaly Score (PAS)](/knowledge/pattern-anomaly-score.md)
* [Pattern Similarity Score Context](/knowledge/pattern-similarity-score-context.md)
* [Market-Adjusted Pattern Anomaly (MAPA)](/knowledge/market-adjusted-pattern-anomaly.md)
* [Peer Mimicry Suspicion](/knowledge/peer-mimicry-suspicion.md)
* [Unique Pattern Deviation Ratio (UPDR)](/knowledge/unique-pattern-deviation-ratio.md)
* [Peer Correlation Z-Score](/knowledge/peer-correlation-z-score.md)
