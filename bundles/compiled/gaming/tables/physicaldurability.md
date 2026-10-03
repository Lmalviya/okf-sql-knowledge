---
type: PostgreSQL Table
title: physicaldurability
description: '27 columns: wgtgram, wgtdist, cablegram, cabledrag, feetmat, feetthkmm, glidecons, fricstatic, frickinetic, surfcompat, gripsty, gripcoat, gripdur, sweatres, tempres, humidres, dustres, waterres, impres, drophtm, bendforce, twistdeg, cablebend, usbconndur. Joins to performance, rgb.'
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
| `physregistry` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying each physical durability record. |
| `physrgbref` | character varying | A VARCHAR(20) foreign key referencing RGB(RgbRegistry), linking durability data to RGB hardware (often in keyboards or mice). |
| `physperfref` | character varying | A VARCHAR(20) foreign key referencing Performance(PerfRegistry), associating physical durability with overall performance metrics. |
| `wgtgram` | smallint | A SMALLINT specifying the device’s weight in grams. |
| `wgtdist` | character varying | A VARCHAR(30) describing weight distribution (e.g., 'Front Heavy', 'Back Heavy', 'Balanced'). |
| `cablegram` | smallint | A SMALLINT measuring the cable’s weight in grams (if relevant). |
| `cabledrag` | character varying | A VARCHAR(25) characterizing the cable’s drag or friction level (e.g., 'Moderate', 'Minimal', 'Significant'). |
| `feetmat` | character varying | A VARCHAR(25) naming the material of the device’s feet/skates (e.g., Glass, Virgin PTFE, PTFE, Ceramic). |
| `feetthkmm` | numeric | A NUMERIC(3,1) indicating thickness (in mm) of the device’s feet/skates. |
| `glidecons` | numeric | A NUMERIC(4,1) measuring gliding consistency or friction uniformity (relative scale). |
| `fricstatic` | numeric | A NUMERIC(3,2) specifying static friction coefficient or rating. |
| `frickinetic` | numeric | A NUMERIC(3,2) specifying kinetic friction coefficient or rating. |
| `surfcompat` | character varying | A VARCHAR(25) indicating the recommended or tested surface compatibility (e.g., Cloth Preferred, Hard Pad Preferred, Universal). |
| `gripsty` | character varying | A VARCHAR(30) describing the handle/grip style (e.g., Palm, Hybrid, Fingertip, Claw). |
| `gripcoat` | character varying | A VARCHAR(30) naming the grip coating type (must match GripCoat_enum if relevant). |
| `gripdur` | smallint | A SMALLINT specifying approximate grip durability or rating (e.g., hours or a scale). |
| `sweatres` | character varying | A VARCHAR(30) detailing sweat resistance or finish claim (e.g., Low, Medium, High). |
| `tempres` | USER-DEFINED | An enum (TempRes_enum) describing the temperature resistance level (Standard, Premium, Enhanced). |
| `humidres` | USER-DEFINED | An enum (HumidRes_enum) indicating humidity resistance level (Standard, Premium, Enhanced). |
| `dustres` | character varying | A VARCHAR(30) referencing dust ingress rating or claim (e.g., IPX1, IPX2, IPX3, IPX0). |
| `waterres` | character varying | A VARCHAR(35) referencing water ingress protection (e.g., IPX1, IPX3, IPX0, IPX2). |
| `impres` | character varying | A VARCHAR(30) describing impact resistance (e.g., Standard, Military Grade, Enhanced). |
| `drophtm` | numeric | A NUMERIC(3,1) measuring the tested or guaranteed drop height in meters. |
| `bendforce` | smallint | A SMALLINT indicating how much force (in N or a relative scale) is needed for noticeable bending. |
| `twistdeg` | smallint | A SMALLINT specifying the angle (in degrees) at which twisting becomes significant or detrimental. |
| `cablebend` | integer | An INTEGER showing the tested cable bend cycles or durability count. |
| `usbconndur` | integer | An INTEGER representing how many connect-disconnect cycles the USB port can handle before failure. |

# Joins

* `physperfref` references `perfregistry` in [performance](/tables/performance.md).
* `physrgbref` references `rgbregistry` in [rgb](/tables/rgb.md).

# Related knowledge

* [Durability Score (DS)](/knowledge/durability-score.md)
* [Competitive-Grade Durability](/knowledge/competitive-grade-durability.md)
* [Physical Endurance Rating (PER)](/knowledge/physical-endurance-rating.md)
* [Ultra-Durable Tournament Device](/knowledge/ultra-durable-tournament-device.md)
