---
type: PostgreSQL Table
title: signals
description: '25 columns: timemark, detectinstr, signalclass, sigstrdb, freqmhz, bwhz, centerfreqmhz, freqdrifthzs, doppshifthz, sigdursec, pulsepersec, pulsewidms, modtype, modindex, carrierfreqmhz, phaseshiftdeg, polarmode, polarangledeg, snrratio, noisefloordbm, interflvl, rfistat, atmointerf. Joins to telescopes.'
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
| `signalregistry` | character, primary key | Full name: 'Signal Registry'. Explanation: Unique ID for each signal record. Data type: CHAR(36). Example: 'SIG-123E4567-E89B'. |
| `timemark` | timestamp with time zone | Full name: 'Timestamp'. Explanation: The moment of signal detection. In some CSVs, it may be stored as an Excel serial date/time (e.g., '44302.55648' ≈ 2021-05-16 13:20:20 UTC). Data type: TIMESTAMPTZ. Example: '2025-08-01 13:45:00+00'. |
| `telescref` | character | Full name: 'Telescope Reference'. Explanation: Foreign key to the telescope used for detection. Data type: CHAR(20). Example: 'TELESC_0001'. |
| `detectinstr` | character varying | Full name: 'Detection Instrument'. Explanation: The instrument type employed for detecting the signal. Data type: VARCHAR(50). Possible categories: Infrared Array, Optical Telescope, Quantum Detector, Radio Telescope. |
| `signalclass` | character varying | Full name: 'Signal Type'. Explanation: Broad classification of the detected signal. Data type: VARCHAR(50). Possible categories: Broadband, Continuous, Modulated, Narrowband, Pulsed. |
| `sigstrdb` | numeric | Full name: 'Signal Strength (dB)'. Explanation: Measured strength of the signal in decibels. Data type: NUMERIC(7,2). Example: '12.35'. |
| `freqmhz` | numeric | Full name: 'Frequency (MHz)'. Explanation: Signal’s nominal frequency in MHz. Data type: DECIMAL(9,3). Example: '1420.405'. |
| `bwhz` | numeric | Full name: 'Bandwidth (Hz)'. Explanation: Signal’s bandwidth in Hertz. Data type: DECIMAL(10,3). Example: '500000.000'. |
| `centerfreqmhz` | numeric | Full name: 'Center Frequency (MHz)'. Explanation: Center frequency of the detected signal in MHz. Data type: NUMERIC(8,3). Example: '1420.500'. |
| `freqdrifthzs` | numeric | Full name: 'Frequency Drift (Hz/s)'. Explanation: How fast the signal drifts in frequency over time. Data type: NUMERIC(9,3). Example: '0.123'. |
| `doppshifthz` | double precision | Full name: 'Doppler Shift (Hz)'. Explanation: Measured Doppler shift of the signal in Hertz. Data type: DOUBLE PRECISION. Example: '142.75'. |
| `sigdursec` | numeric | Full name: 'Signal Duration (s)'. Explanation: Total duration of the signal in seconds. Data type: NUMERIC(6,2). Example: '12.50'. |
| `pulsepersec` | numeric | Full name: 'Pulse Rate (pulses/sec)'. Explanation: Rate of pulse repetition in the signal. Data type: NUMERIC(6,3). Example: '4.500'. |
| `pulsewidms` | numeric | Full name: 'Pulse Width (ms)'. Explanation: Duration of each pulse in milliseconds. Data type: NUMERIC(6,3). Example: '2.300'. |
| `modtype` | character varying | Full name: 'Modulation Type'. Explanation: The method of signal modulation. Data type: VARCHAR(30). Possible categories: AM, FM, PM, QAM, Unknown. |
| `modindex` | numeric | Full name: 'Modulation Index'. Explanation: Numerical index describing modulation depth. Data type: DECIMAL(6,4). Example: '0.2875'. |
| `carrierfreqmhz` | numeric | Full name: 'Carrier Frequency (MHz)'. Explanation: Frequency of the carrier wave in MHz. Data type: DECIMAL(9,3). Example: '1000.000'. |
| `phaseshiftdeg` | numeric | Full name: 'Phase Shift (°)'. Explanation: Phase shift in degrees for the signal. Data type: NUMERIC(6,2). Example: '45.00'. |
| `polarmode` | character varying | Full name: 'Polarization Mode'. Explanation: Type of signal polarization. Data type: VARCHAR(30). Possible categories: Circular, Elliptical, Linear, Unknown. |
| `polarangledeg` | numeric | Full name: 'Polarization Angle (°)'. Explanation: Angle of polarization in degrees. Data type: DECIMAL(5,1). Example: '90.0'. |
| `snrratio` | numeric | Full name: 'Signal-to-Noise Ratio'. Explanation: SNR measured for the signal. Data type: DECIMAL(6,2). Example: '18.75'. |
| `noisefloordbm` | double precision | Full name: 'Noise Floor (dBm)'. Explanation: Measured noise floor in dBm. Data type: DOUBLE PRECISION. Example: '-85.3'. |
| `interflvl` | character varying | Full name: 'Interference Level'. Explanation: Degree of interference around the signal. Data type: VARCHAR(30). Possible categories: High, Low, Medium, None. |
| `rfistat` | character varying | Full name: 'RFI Status'. Explanation: Radio Frequency Interference status. Data type: VARCHAR(30). Possible categories: Clean, Contaminated, Unknown. |
| `atmointerf` | character varying | Full name: 'Atmospheric Interference'. Explanation: Impact of atmospheric conditions on signal. Data type: VARCHAR(30). Possible categories: Minimal, Moderate, Severe. |

# Joins

* `telescref` references `telescregistry` in [telescopes](/tables/telescopes.md).

# Related knowledge

* [Signal-to-Noise Quality Indicator (SNQI)](/knowledge/signal-to-noise-quality-indicator.md)
* [Signal Complexity Ratio (SCR)](/knowledge/signal-complexity-ratio.md)
* [Bandwidth-Frequency Ratio (BFR)](/knowledge/bandwidth-frequency-ratio.md)
* [Signal Stability Metric (SSM)](/knowledge/signal-stability-metric.md)
* [Coherent Information Pattern (CIP)](/knowledge/coherent-information-pattern.md)
* [Narrowband Technological Marker (NTM)](/knowledge/narrowband-technological-marker.md)
* [Fast Radio Transient (FRT)](/knowledge/fast-radio-transient.md)
* [SignalClass: Narrowband](/knowledge/signalclass-narrowband.md)
* [CIP Classification Label](/knowledge/cip-classification-label.md)
* [SigClassType: Broadband Transient](/knowledge/sigclasstype-broadband-transient.md)
* [PolarMode: Circular](/knowledge/polarmode-circular.md)
* [FalsePosProb: <0.01](/knowledge/falseposprob-0-01.md)
* [Modulation Complexity Score (MCS)](/knowledge/modulation-complexity-score.md)
* [NTM Classification System](/knowledge/ntm-classification-system.md)
* [Directed Transmission](/knowledge/directed-transmission.md)
* [CCS Approximation](/knowledge/ccs-approximation.md)
* [Bandwidth-to-Frequency Ratio (BFR)](/knowledge/bandwidth-to-frequency-ratio.md)
