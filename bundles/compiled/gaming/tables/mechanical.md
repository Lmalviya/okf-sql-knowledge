---
type: PostgreSQL Table
title: mechanical
description: '25 columns: keyforceg, keytravmm, swtchvar, swtchdur, ghostkeys, keyrollo, swtchcons, ghosteff, keychatter, actpointmm, respointmm, tacbumpmm, tottravmm, stabrattle, stabtype, capthkmm, capmat, caplegmeth, kbdangle, wristflag, palmangle, ergorate. Joins to deviceidentity, performance.'
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
| `mechregistry` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying the mechanical properties record. |
| `mechperfref` | character varying | A VARCHAR(20) foreign key referencing Performance(PerfRegistry), linking mechanical specs to performance metrics. |
| `mechdevref` | character varying | A VARCHAR(20) foreign key referencing DeviceIdentity(DevRegistry), associating mechanical data with a specific device. |
| `keyforceg` | numeric | A NUMERIC(5,2) describing actuation force (in grams) for keys or switches. |
| `keytravmm` | numeric | A NUMERIC(3,1) showing total travel distance (in mm) for keys or buttons. |
| `swtchvar` | character varying | A VARCHAR(40) naming the specific switch variant (e.g., Membrane, Mechanical, Optical, Magnetic). |
| `swtchdur` | bigint | A BIGINT indicating the rated switch durability (e.g., total actuations). |
| `ghostkeys` | smallint | A SMALLINT counting how many keys might exhibit ‘ghosting’ if pressed simultaneously. |
| `keyrollo` | character varying | A VARCHAR(35) describing the rollover spec (e.g., 2KRO, 6KRO, NKRO). |
| `swtchcons` | numeric | A NUMERIC(4,1) measuring the consistency in switch actuation force or performance. |
| `ghosteff` | numeric | A NUMERIC(4,1) quantifying the effective impact of ghosting (on a scale or percentage). |
| `keychatter` | numeric | A NUMERIC(3,2) indicating key chatter or bounce (in ms or a relative measure). |
| `actpointmm` | numeric | A NUMERIC(3,1) showing at what point (in mm) the key actuates from the top of its travel. |
| `respointmm` | numeric | A NUMERIC(3,1) specifying the reset point (in mm) where the switch deactivates on release. |
| `tacbumpmm` | numeric | A NUMERIC(3,1) measuring the tactile bump position (in mm) in a tactile switch. |
| `tottravmm` | numeric | A NUMERIC(3,1) for the total travel distance (in mm) if fully bottomed out. |
| `stabrattle` | USER-DEFINED | An enum (StabRattle_enum) indicating stabilizer rattle level (None, Minimal, Moderate). |
| `stabtype` | character varying | A VARCHAR(30) naming the stabilizer type (e.g., PCB Mount, Screw-in, Plate Mount). |
| `capthkmm` | numeric | A NUMERIC(3,1) for the keycap thickness (in mm). |
| `capmat` | character varying | A VARCHAR(35) specifying the keycap material (ABS, PBT, etc.). |
| `caplegmeth` | character varying | A VARCHAR(40) describing how the legends are applied (e.g., Double Shot, Dye Sub, Laser Etched). |
| `kbdangle` | smallint | A SMALLINT indicating the built-in keyboard angle or tilt (in degrees). |
| `wristflag` | boolean | A BOOLEAN stating whether a wrist rest is integrated or included. |
| `palmangle` | smallint | A SMALLINT measuring the palm rest angle (in degrees), if applicable. |
| `ergorate` | smallint | A SMALLINT providing an ergonomic rating (on a defined scale). |

# Joins

* `mechdevref` references `devregistry` in [deviceidentity](/tables/deviceidentity.md).
* `mechperfref` references `perfregistry` in [performance](/tables/performance.md).

# Related knowledge

* [Comfort Index (CI)](/knowledge/comfort-index.md)
* [Switch Performance Rating (SPR)](/knowledge/switch-performance-rating.md)
* [SwtchDur (Switch Durability)](/knowledge/swtchdur.md)
* [ErgoRate (Ergonomic Rating)](/knowledge/ergorate.md)
* [Ergonomic Sustainability Factor (ESF)](/knowledge/ergonomic-sustainability-factor.md)
* [Ergonomic Excellence Certification](/knowledge/ergonomic-excellence-certification.md)
* [Professional-Grade Control Consistency](/knowledge/professional-grade-control-consistency.md)
