---
type: PostgreSQL Table
title: signalprobabilities
description: '10 columns: falseposprob, sigunique, simindex, corrscore, anomscore, techsigprob, biosigprob, natsrcprob, artsrcprob. Joins to signals.'
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
| `signalref` | character, primary key | Full name: 'Signal Registry Reference'. Explanation: Primary key referencing the main signal record. Data type: CHAR(36). Example: 'SIG-XYZ-9876'. |
| `falseposprob` | numeric | Full name: 'False Positive Probability'. Explanation: Probability that the signal is falsely detected. Data type: DECIMAL(5,4). Example: '0.0135'. |
| `sigunique` | numeric | Full name: 'Signal Uniqueness'. Explanation: A measure of how unique the signal is compared to others. Data type: DECIMAL(7,4). Example: '99.1234'. |
| `simindex` | numeric | Full name: 'Similarity Index'. Explanation: Compares the signal to known references. Data type: NUMERIC(5,4). Example: '0.8222'. |
| `corrscore` | numeric | Full name: 'Correlation Score'. Explanation: How well the signal aligns with expected patterns. Data type: DECIMAL(5,4). Example: '0.9950'. |
| `anomscore` | double precision | Full name: 'Anomaly Score'. Explanation: How unusual or unexpected the signal is. Data type: FLOAT. Example: '1.23'. |
| `techsigprob` | numeric | Full name: 'Technosignature Probability'. Explanation: Probability that the signal is of artificial technological origin. Data type: DECIMAL(5,4). Example: '0.6789'. |
| `biosigprob` | numeric | Full name: 'Biosignature Probability'. Explanation: Probability that the signal indicates a biological origin. Data type: DECIMAL(6,2). Example: '45.21'. |
| `natsrcprob` | numeric | Full name: 'Natural Source Probability'. Explanation: Probability the signal is from a natural source. Data type: NUMERIC(7,3). Example: '98.761'. |
| `artsrcprob` | numeric | Full name: 'Artificial Source Probability'. Explanation: Probability the signal is from an artificial source. Data type: NUMERIC(3,1). Example: '3.4'. |

# Joins

* `signalref` references `signalregistry` in [signals](/tables/signals.md).

# Related knowledge

* [Technological Origin Likelihood Score (TOLS)](/knowledge/technological-origin-likelihood-score.md)
* [Research Priority Index (RPI)](/knowledge/research-priority-index.md)
* [Technosignature](/knowledge/technosignature.md)
* [Target of Opportunity (TOO)](/knowledge/target-of-opportunity.md)
* [Potential Biosignature](/knowledge/potential-biosignature.md)
* [FalsePosProb: <0.01](/knowledge/falseposprob-0-01.md)
* [Artificial Intelligence Detection Probability (AIDP)](/knowledge/artificial-intelligence-detection-probability.md)
* [Information Entropy Ratio (IER)](/knowledge/information-entropy-ratio.md)
* [Confirmation Confidence Score (CCS)](/knowledge/confirmation-confidence-score.md)
* [CCS Approximation](/knowledge/ccs-approximation.md)
* [Anomalous Quantum Signal](/knowledge/anomalous-quantum-signal.md)
