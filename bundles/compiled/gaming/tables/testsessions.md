---
type: PostgreSQL Table
title: testsessions
description: '20 columns: stampmoment, devscope, cpuusepct, memusemb, driverstatus, fwupdur, wlsignal, battlevel, battcapmah, battlifeh, chgtimemin, qchgflag, usbpwrline, latms, inplagms, pollratehz, dbtimems, resptimems, clkregms.'
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
| `sessionregistry` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying each test session record. |
| `stampmoment` | timestamp without time zone | A TIMESTAMP(6) capturing the exact date/time when the session was recorded. |
| `devscope` | USER-DEFINED | An enum (DevScope_enum) indicating the tested device category (e.g., Keyboard, Headset, Gamepad, Mouse, Controller). |
| `cpuusepct` | numeric | A NUMERIC(5,2) showing CPU usage percentage during the test session. |
| `memusemb` | integer | An INTEGER specifying memory usage in megabytes at the time of the test. |
| `driverstatus` | USER-DEFINED | An enum (DriverStability_enum) describing driver stability status (Stable, Beta, or Experimental). |
| `fwupdur` | smallint | A SMALLINT indicating how many seconds/minutes it takes to complete a firmware update. |
| `wlsignal` | numeric | A NUMERIC(5,2) representing wireless signal strength (e.g., in dBm or relative scale). |
| `battlevel` | smallint | A SMALLINT showing current battery percentage (0–100). |
| `battcapmah` | integer | An INTEGER specifying battery capacity in milliamp-hours (mAh). |
| `battlifeh` | numeric | A NUMERIC(4,1) for the device’s remaining or estimated battery life in hours. |
| `chgtimemin` | numeric | A NUMERIC(5,2) indicating the number of minutes required for a full battery charge. |
| `qchgflag` | boolean | A BOOLEAN (true/false) stating whether quick charge is supported by the device. |
| `usbpwrline` | character varying | A VARCHAR(25) field describing the USB power delivery or specification (e.g., 7.5W, 5W, 10W). |
| `latms` | numeric | A NUMERIC(5,2) measuring overall latency in milliseconds from user input to system response. |
| `inplagms` | numeric | A NUMERIC(5,2) capturing input lag (in ms) between the device and the system. |
| `pollratehz` | smallint | A SMALLINT describing the device's polling rate in Hertz (times per second). |
| `dbtimems` | numeric | A NUMERIC(4,2) specifying the debounce time (in ms) for mechanical or electrical inputs. |
| `resptimems` | numeric | A NUMERIC(4,2) indicating the device’s response time (in ms) after input is detected. |
| `clkregms` | numeric | A NUMERIC(4,3) measuring how many milliseconds it takes for a click/button press to register. |

# Related knowledge

* [Battery Efficiency Ratio (BER)](/knowledge/battery-efficiency-ratio.md)
* [Input Responsiveness Score (IRS)](/knowledge/input-responsiveness-score.md)
* [Wireless Performance Rating (WPR)](/knowledge/wireless-performance-rating.md)
* [Premium Gaming Mouse](/knowledge/premium-gaming-mouse.md)
* [Tournament-Ready Keyboard](/knowledge/tournament-ready-keyboard.md)
* [Extended Battery Life Device](/knowledge/extended-battery-life-device.md)
* [Minimal Input Latency](/knowledge/minimal-input-latency.md)
* [Premium Wireless Solution](/knowledge/premium-wireless-solution.md)
* [LatMs (Latency)](/knowledge/latms.md)
* [PollRateHz (Polling Rate)](/knowledge/pollratehz.md)
* [WlSignal (Wireless Signal Strength)](/knowledge/wlsignal.md)
* [Response Accuracy Index (RAI)](/knowledge/response-accuracy-index.md)
* [Tournament Standard Device](/knowledge/tournament-standard-device.md)
* [Ultra-Responsive Gaming Device](/knowledge/ultra-responsive-gaming-device.md)
* [Extended Tournament Ready Wireless](/knowledge/extended-tournament-ready-wireless.md)
