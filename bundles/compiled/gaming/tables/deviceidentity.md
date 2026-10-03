---
type: PostgreSQL Table
title: deviceidentity
description: '22 columns: makername, modnum, fwver, conntype, wlrangem, wlinterf, wlchanhop, wllatvar, pwridlemw, pwractmw, pwrrgbmw, brdmemmb, profcount, mcresptime, mcexecspeed, mctimacc, dpires, dpisteps, senstype, sensres. Joins to testsessions.'
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
| `devregistry` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying the device identity record. |
| `devsessionref` | character varying | A VARCHAR(20) foreign key referencing TestSessions(SessionRegistry), linking the device to its test session. |
| `makername` | character varying | A VARCHAR(50) naming the manufacturer or brand of the device. |
| `modnum` | character varying | A VARCHAR(50) specifying the model name or number of the device. |
| `fwver` | character varying | A VARCHAR(50) denoting the firmware version running on the device. |
| `conntype` | character varying | A VARCHAR(35) indicating how the device connects (e.g., Wireless 2.4GHz, Wired, Bluetooth, Hybrid). |
| `wlrangem` | numeric | A NUMERIC(4,1) measuring the device’s wireless range in meters (if applicable). |
| `wlinterf` | character varying | A VARCHAR(35) describing interference or constraints on the wireless connection (e.g., Low, High, Medium). |
| `wlchanhop` | boolean | A BOOLEAN stating if the device automatically hops channels to avoid interference. |
| `wllatvar` | numeric | A NUMERIC(4,2) capturing variation in wireless latency (e.g., standard deviation). |
| `pwridlemw` | integer | An INTEGER specifying power consumption (in mW) when the device is idle. |
| `pwractmw` | integer | An INTEGER indicating power consumption (in mW) under active usage. |
| `pwrrgbmw` | integer | An INTEGER showing additional power draw (in mW) attributed to any RGB lighting. |
| `brdmemmb` | smallint | A SMALLINT for onboard memory size (in MB) for storing profiles/macros. |
| `profcount` | smallint | A SMALLINT specifying how many user profiles can be stored on the device. |
| `mcresptime` | numeric | A NUMERIC(4,2) measuring the microcontroller’s response time (in ms) to inputs. |
| `mcexecspeed` | numeric | A NUMERIC(4,2) describing microcontroller execution speed or frequency (possibly in MHz). |
| `mctimacc` | numeric | A NUMERIC(5,2) representing microcontroller timing accuracy (in percent or a relevant unit). |
| `dpires` | integer | An INTEGER for the sensor’s primary DPI resolution. |
| `dpisteps` | smallint | A SMALLINT listing how many DPI step increments the device supports. |
| `senstype` | character varying | A VARCHAR(50) describing the sensor type (e.g., PMW3389, Optical, Laser, PAW3399). |
| `sensres` | integer | An INTEGER indicating a secondary sensor resolution or specification (if distinct from DPI). |

# Joins

* `devsessionref` references `sessionregistry` in [testsessions](/tables/testsessions.md).

# Related knowledge

* [Sensor Performance Index (SPI)](/knowledge/sensor-performance-index.md)
* [Battery Efficiency Ratio (BER)](/knowledge/battery-efficiency-ratio.md)
* [Wireless Performance Rating (WPR)](/knowledge/wireless-performance-rating.md)
* [Premium Gaming Mouse](/knowledge/premium-gaming-mouse.md)
* [Extended Battery Life Device](/knowledge/extended-battery-life-device.md)
* [Streaming-Optimized Device](/knowledge/streaming-optimized-device.md)
* [Premium Wireless Solution](/knowledge/premium-wireless-solution.md)
* [DpiRes (DPI Resolution)](/knowledge/dpires.md)
* [BrdMemMB (Onboard Memory)](/knowledge/brdmemmb.md)
* [Wireless Performance Efficiency (WPE)](/knowledge/wireless-performance-efficiency.md)
* [Gaming Versatility Score (GVS)](/knowledge/gaming-versatility-score.md)
* [Professional Adoption Rating (PAR)](/knowledge/professional-adoption-rating.md)
* [Tournament Standard Device](/knowledge/tournament-standard-device.md)
* [Professional Multi-Genre Setup](/knowledge/professional-multi-genre-setup.md)
