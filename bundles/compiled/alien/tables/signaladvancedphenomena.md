---
type: PostgreSQL Table
title: signaladvancedphenomena
description: '9 columns: intermedeffects, gravlens, quanteffects, encryptevid, langstruct, msgcontent, cultsig, sciimpact. Joins to signals.'
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
| `signalref` | character, primary key | Full name: 'Signal Registry Reference'. Explanation: Primary key referencing the main signal. Data type: CHAR(36). Example: 'SIG-ABC-1234'. |
| `intermedeffects` | character varying | Full name: 'Interstellar Medium Effects'. Explanation: Impact of interstellar medium on the signal. Data type: VARCHAR(40). Possible categories: Minimal, Moderate, Severe. |
| `gravlens` | character varying | Full name: 'Gravitational Lensing'. Explanation: Whether the signal is affected by gravitational lensing. Data type: VARCHAR(50). Possible categories: None, Strong, Weak. |
| `quanteffects` | character varying | Full name: 'Quantum Effects'. Explanation: Quantum-level phenomena observed in the signal. Data type: VARCHAR(85). Possible categories: None, Observed, Significant. |
| `encryptevid` | character varying | Full name: 'Encryption Evidence'. Explanation: Whether there is indication the signal is encrypted. Data type: VARCHAR(40). Possible categories: None, Possible, Strong. |
| `langstruct` | text | Full name: 'Language Structure'. Explanation: Presence of linguistic or structured patterns. Data type: TEXT. Possible categories: Complex, None, Simple. |
| `msgcontent` | text | Full name: 'Message Content'. Explanation: Indicates whether an actual message was detected. Data type: TEXT. Possible categories: Identified, None, Possible. |
| `cultsig` | character varying | Full name: 'Cultural Significance'. Explanation: The level of cultural impact or interest. Data type: VARCHAR(60). Possible categories: High, Low, None. |
| `sciimpact` | character varying | Full name: 'Scientific Impact'. Explanation: Significance of the signal to scientific research. Data type: VARCHAR(50). Possible categories: Major, Minor, Moderate. |

# Joins

* `signalref` references `signalregistry` in [signals](/tables/signals.md).

# Related knowledge

* [EncryptEvid: Strong Pattern](/knowledge/encryptevid-strong-pattern.md)
* [Quantum-Coherent Transmission](/knowledge/quantum-coherent-transmission.md)
* [Anomalous Quantum Signal](/knowledge/anomalous-quantum-signal.md)
