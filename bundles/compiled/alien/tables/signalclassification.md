---
type: PostgreSQL Table
title: signalclassification
description: '9 columns: sigclasstype, sigpattern, repeatcount, periodsec, complexidx, entropyval, infodense, classconf. Joins to signals.'
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_schema.txt
  title: alien schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_column_meaning_base.json
  title: alien column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `signalref` | character, primary key | Full name: 'Signal Registry Reference'. Explanation: Foreign key referencing the main signal. Data type: CHAR(36). Example: 'SIG-DEF-5678'. |
| `sigclasstype` | character varying | Full name: 'Classification Type'. Explanation: High-level category for the signal. Data type: VARCHAR(40). Possible categories: Artificial, Candidate, Natural, Unknown. |
| `sigpattern` | character varying | Full name: 'Signal Pattern'. Explanation: Pattern observed in the signal. Data type: VARCHAR(60). Possible categories: Periodic, Random, Structured, Unknown. |
| `repeatcount` | smallint | Full name: 'Repetition Count'. Explanation: Number of times the signal has repeated. Data type: SMALLINT. Example: '3'. |
| `periodsec` | numeric | Full name: 'Period (s)'. Explanation: Duration of each cycle if periodic. Data type: NUMERIC(7,3). Example: '12.345'. |
| `complexidx` | numeric | Full name: 'Complexity Index'. Explanation: Numeric measure of the signal’s complexity. Data type: DECIMAL(6,3). Example: '5.678'. |
| `entropyval` | numeric | Full name: 'Entropy'. Explanation: Entropy measurement of the signal. Data type: DECIMAL(6,2). Example: '3.45'. |
| `infodense` | numeric | Full name: 'Information Density'. Explanation: Estimated information per unit time/frequency. Data type: DECIMAL(6,3). Example: '2.345'. |
| `classconf` | numeric | Full name: 'Classification Confidence (%)'. Explanation: How confident we are in the assigned signal class. Data type: DECIMAL(5,2). Example: '92.50'. |

# Joins

* `signalref` references `signalregistry` in [signals](/tables/signals.md).

# Related knowledge

* [Signal Complexity Ratio (SCR)](/knowledge/signal-complexity-ratio.md)
* [Encoding Complexity Index (ECI)](/knowledge/encoding-complexity-index.md)
* [Technosignature](/knowledge/technosignature.md)
* [Coherent Information Pattern (CIP)](/knowledge/coherent-information-pattern.md)
* [Encoded Information Transfer (EIT)](/knowledge/encoded-information-transfer.md)
* [Fast Radio Transient (FRT)](/knowledge/fast-radio-transient.md)
* [CIP Classification Label](/knowledge/cip-classification-label.md)
* [SigClassType: Broadband Transient](/knowledge/sigclasstype-broadband-transient.md)
* [EncryptEvid: Strong Pattern](/knowledge/encryptevid-strong-pattern.md)
* [Information Entropy Ratio (IER)](/knowledge/information-entropy-ratio.md)
* [Signal Processing Efficiency Index (SPEI)](/knowledge/signal-processing-efficiency-index.md)
* [Confirmation Confidence Score (CCS)](/knowledge/confirmation-confidence-score.md)
* [Pattern Recognition Confidence (PRC)](/knowledge/pattern-recognition-confidence.md)
* [Multi-Channel Communication Protocol](/knowledge/multi-channel-communication-protocol.md)
* [Quantum-Coherent Transmission](/knowledge/quantum-coherent-transmission.md)
