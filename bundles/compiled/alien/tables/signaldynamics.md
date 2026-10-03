---
type: PostgreSQL Table
title: signaldynamics
description: '13 columns: sigintegrity, sigrecurr, sigevolve, tempstab, spatstab, freqstab, phasestab, ampstab, modstab, sigcoherence, sigdisp, sigscint. Joins to signals.'
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
| `signalref` | character, primary key | Full name: 'Signal Registry Reference'. Explanation: Foreign key referencing the main signal. Data type: CHAR(36). Example: 'SIG-JKL-3456'. |
| `sigintegrity` | character varying | Full name: 'Signal Integrity'. Explanation: Rating of how intact or uncorrupted the signal is. Data type: VARCHAR(30). If no fixed categories, example: 'HighIntegrity'. |
| `sigrecurr` | character varying | Full name: 'Signal Recurrence'. Explanation: Whether the signal recurs over time. Data type: VARCHAR(25). Possible categories: None, Regular, Sporadic. |
| `sigevolve` | character varying | Full name: 'Signal Evolution'. Explanation: Indicates if the signal changes/evolves during observation. Data type: VARCHAR(25). Possible categories: Dynamic, Static, Unknown. |
| `tempstab` | character varying | Full name: 'Temporal Stability'. Explanation: How stable the signal remains over time. Data type: VARCHAR(20). If no fixed categories, example: 'Stable'. |
| `spatstab` | character varying | Full name: 'Spatial Stability'. Explanation: How stable the signal is spatially (e.g., consistent direction). Data type: VARCHAR(20). If no fixed categories, example: 'Moderate'. |
| `freqstab` | character varying | Full name: 'Frequency Stability'. Explanation: How stable the signal’s frequency is. Data type: VARCHAR(35). If no fixed categories, example: 'HighlyStable'. |
| `phasestab` | character varying | Full name: 'Phase Stability'. Explanation: Any variation in signal phase. Data type: VARCHAR(35). If no fixed categories, example: 'VaryingPhase'. |
| `ampstab` | character varying | Full name: 'Amplitude Stability'. Explanation: Consistency of signal amplitude. Data type: VARCHAR(20). If no fixed categories, example: 'Unstable'. |
| `modstab` | character varying | Full name: 'Modulation Stability'. Explanation: Consistency in the signal’s modulation scheme. Data type: VARCHAR(30). If no fixed categories, example: 'Consistent'. |
| `sigcoherence` | character varying | Full name: 'Signal Coherence'. Explanation: How coherent the signal remains over its duration. Data type: VARCHAR(25). If no fixed categories, example: 'HighCoherence'. |
| `sigdisp` | character varying | Full name: 'Signal Dispersion'. Explanation: The degree to which the signal is dispersed (time/frequency smearing). Data type: VARCHAR(25). If no fixed categories, example: 'SignificantDisp'. |
| `sigscint` | character varying | Full name: 'Signal Scintillation'. Explanation: Fluctuation in signal amplitude due to propagation effects. Data type: VARCHAR(45). If no fixed categories, example: 'MildScintillation'. |

# Joins

* `signalref` references `signalregistry` in [signals](/tables/signals.md).

# Related knowledge

* [Directed Transmission](/knowledge/directed-transmission.md)
