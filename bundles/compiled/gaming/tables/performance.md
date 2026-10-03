---
type: PostgreSQL Table
title: performance
description: '12 columns: accelmax, speedips, liftdistmm, angsnap, btntens, clklat, clkdur, screnctyp, scrsteps, scraccy. Joins to testsessions.'
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
| `perfregistry` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying each performance record. |
| `perfsessionref` | character varying | A VARCHAR(20) foreign key referencing TestSessions(SessionRegistry) to link performance metrics to a specific session. |
| `accelmax` | smallint | A SMALLINT indicating the maximum acceleration (in G or m/s²) the device sensor can handle. |
| `speedips` | smallint | A SMALLINT for maximum tracking speed in inches per second (IPS) for pointing devices. |
| `liftdistmm` | numeric | A NUMERIC(3,1) describing the lift-off distance in millimeters, often relevant for mouse sensors. |
| `angsnap` | boolean | A BOOLEAN stating whether angle snapping (prediction or correction) is enabled. |
| `btntens` | USER-DEFINED | An enum (BtnTens_enum) describing button tension (Light, Medium, or Heavy). |
| `clklat` | numeric | A NUMERIC(3,2) measuring click latency (in ms) from actuation to system registration. |
| `clkdur` | bigint | A BIGINT noting the rated click durability (e.g., number of clicks before failure). |
| `screnctyp` | USER-DEFINED | An enum (ScrollEncoder_enum) for the scroll wheel mechanism type (Mechanical, Optical, Magnetic). |
| `scrsteps` | smallint | A SMALLINT for how many discrete 'clicks' or steps a full scroll wheel rotation has. |
| `scraccy` | numeric | A NUMERIC(4,1) reflecting the scroll wheel’s accuracy or consistency (on a relative scale). |

# Joins

* `perfsessionref` references `sessionregistry` in [testsessions](/tables/testsessions.md).

# Related knowledge

* [Tournament-Ready Keyboard](/knowledge/tournament-ready-keyboard.md)
* [Minimal Input Latency](/knowledge/minimal-input-latency.md)
* [Ultra-Responsive Gaming Device](/knowledge/ultra-responsive-gaming-device.md)
