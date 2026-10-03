---
type: PostgreSQL Table
title: audioandmedia
description: '24 columns: sndleveldb, sndsig, noiseisodb, audlatms, micsensedb, micfreqresp, spkimpohm, spksensedb, thdpct, freqresp, drvszmm, surrsnd, eqcount, micmon, noisecanc, btversion, btrangem, btlatms, multidev, autoslpmin, wakems. Joins to deviceidentity, performance.'
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_schema.txt
  title: gaming schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_column_meaning_base.json
  title: gaming column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `audregistry` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying the audio/media properties record. |
| `auddevref` | character varying | A VARCHAR(20) foreign key referencing DeviceIdentity(DevRegistry), linking these audio/media specs to a device. |
| `audperfref` | character varying | A VARCHAR(20) foreign key referencing Performance(PerfRegistry), associating audio/media data with performance metrics. |
| `sndleveldb` | numeric | A NUMERIC(4,1) measuring sound output level in decibels from the device. |
| `sndsig` | character varying | A VARCHAR(30) describing the sound signature (e.g., Silent, Thocky, Clicky, Linear). |
| `noiseisodb` | smallint | A SMALLINT for how many dB of noise isolation the device provides. |
| `audlatms` | numeric | A NUMERIC(4,1) capturing audio latency (in ms) from signal to output. |
| `micsensedb` | numeric | A NUMERIC(5,2) measuring microphone sensitivity in dB (e.g., dBV). |
| `micfreqresp` | character varying | A VARCHAR(50) specifying the microphone frequency response range (e.g., 20Hz–20kHz). |
| `spkimpohm` | smallint | A SMALLINT indicating the speaker or driver impedance in ohms. |
| `spksensedb` | smallint | A SMALLINT specifying speaker sensitivity in decibels (dB SPL @ 1kHz). |
| `thdpct` | numeric | A NUMERIC(3,2) for total harmonic distortion (THD) as a percentage. |
| `freqresp` | character varying | A VARCHAR(50) describing the device’s frequency response specification (e.g., 20Hz–20kHz). |
| `drvszmm` | smallint | A SMALLINT measuring the diameter (in mm) of the speaker or audio driver. |
| `surrsnd` | character varying | A VARCHAR(30) naming any surround sound technology (e.g., Stereo, 5.1, 7.1). |
| `eqcount` | smallint | A SMALLINT counting available EQ profiles or presets. |
| `micmon` | boolean | A BOOLEAN indicating if mic monitoring (sidetone) is supported. |
| `noisecanc` | USER-DEFINED | An enum (NoiseCanc_enum) denoting the noise cancellation type (None, Passive, Active). |
| `btversion` | character varying | A VARCHAR(35) referencing Bluetooth version (e.g., 4.0, 5.0, 5.1, 5.2) if applicable. |
| `btrangem` | smallint | A SMALLINT specifying typical Bluetooth range in meters. |
| `btlatms` | numeric | A NUMERIC(5,2) measuring Bluetooth audio latency (in ms). |
| `multidev` | boolean | A BOOLEAN stating whether the device can connect to multiple endpoints simultaneously. |
| `autoslpmin` | smallint | A SMALLINT specifying how many minutes pass before the device goes into auto-sleep mode. |
| `wakems` | numeric | A NUMERIC(5,1) representing how many milliseconds it takes for the device to wake from sleep. |

# Joins

* `auddevref` references `devregistry` in [deviceidentity](/tables/deviceidentity.md).
* `audperfref` references `perfregistry` in [performance](/tables/performance.md).

# Related knowledge

* [Audio Quality Index (AQI)](/knowledge/audio-quality-index.md)
* [Audiophile Gaming Headset](/knowledge/audiophile-gaming-headset.md)
* [Streaming-Optimized Device](/knowledge/streaming-optimized-device.md)
* [ThdPct (Total Harmonic Distortion)](/knowledge/thdpct.md)
* [Subpar Audio Device Identification](/knowledge/subpar-audio-device-identification.md)
