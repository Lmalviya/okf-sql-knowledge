---
type: PostgreSQL Table
title: signaldecoding
description: '13 columns: encodetype, compressratio, errcorrlvl, decodeconf, decodemethod, decodestat, decodeiters, proctimehrs, compresources, analysisdp, veriflvl, confirmstat. Joins to signals.'
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
| `signalref` | character, primary key | Full name: 'Signal Registry Reference'. Explanation: Foreign key referencing the main signal entry. Data type: CHAR(36). Example: 'SIG-GHI-9012'. |
| `encodetype` | character varying | Full name: 'Encoding Type'. Explanation: The type of signal encoding used (e.g., Binary). Data type: VARCHAR(40). Possible categories: Binary, Complex, Tertiary, Unknown. |
| `compressratio` | numeric | Full name: 'Compression Ratio'. Explanation: Factor by which the raw signal data was compressed. Data type: DECIMAL(6,3). Example: '2.500'. |
| `errcorrlvl` | character varying | Full name: 'Error Correction Level'. Explanation: Degree of error correction applied. Data type: VARCHAR(35). Possible categories: High, Low, Medium, None. |
| `decodeconf` | numeric | Full name: 'Decoding Confidence (%)'. Explanation: Confidence level that the decoding is correct. Data type: DECIMAL(5,2). Example: '88.75'. |
| `decodemethod` | character varying | Full name: 'Decoding Method'. Explanation: Method used to decode the signal. Data type: VARCHAR(35). Possible categories: FFT, Neural Network, Quantum, Wavelet. |
| `decodestat` | character varying | Full name: 'Decoding Status'. Explanation: Status of the decoding process. Data type: VARCHAR(25). Possible categories: Completed, Failed, In Progress. |
| `decodeiters` | smallint | Full name: 'Decoding Iterations'. Explanation: Number of algorithmic passes attempted. Data type: SMALLINT. Example: '7'. |
| `proctimehrs` | numeric | Full name: 'Processing Time (hours)'. Explanation: Total hours spent decoding. Data type: DECIMAL(6,2). Example: '3.50'. |
| `compresources` | character varying | Full name: 'Computational Resources'. Explanation: Level of computing power used. Data type: VARCHAR(50). Possible categories: Extreme, High, Low, Medium. |
| `analysisdp` | character varying | Full name: 'Analysis Depth'. Explanation: How thoroughly the signal was analyzed. Data type: VARCHAR(25). Possible categories: Comprehensive, Detailed, Preliminary. |
| `veriflvl` | character varying | Full name: 'Verification Level'. Explanation: Extent to which decoding has been verified. Data type: VARCHAR(30). Possible categories: Partially, Unverified, Verified. |
| `confirmstat` | character varying | Full name: 'Confirmation Status'. Explanation: Whether the decoding results have been confirmed. Data type: VARCHAR(30). Possible categories: Confirmed, Pending, Rejected. |

# Joins

* `signalref` references `signalregistry` in [signals](/tables/signals.md).

# Related knowledge

* [Encoding Complexity Index (ECI)](/knowledge/encoding-complexity-index.md)
* [EncodeType: Frequency Hopping](/knowledge/encodetype-frequency-hopping.md)
* [Signal Processing Efficiency Index (SPEI)](/knowledge/signal-processing-efficiency-index.md)
* [Confirmation Confidence Score (CCS)](/knowledge/confirmation-confidence-score.md)
* [CCS Approximation](/knowledge/ccs-approximation.md)
