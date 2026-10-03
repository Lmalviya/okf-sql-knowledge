---
type: PostgreSQL Table
title: interactionandcontrol
description: '21 columns: amblight, tempsense, accelsense, gyrosense, hapfeed, hapstr, vibmodes, forcefeed, trigres, trigtravmm, joydead, joyprec, btnspcmm, btnszmm, dpadvar, dpadacc, astickvar, driftres. Joins to deviceidentity, physicaldurability.'
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
| `interactregistry` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying each interaction/control record. |
| `interactphysref` | character varying | A VARCHAR(20) foreign key referencing PhysicalDurability(PhysRegistry), linking control features to the physical build. |
| `interactdevref` | character varying | A VARCHAR(20) foreign key referencing DeviceIdentity(DevRegistry), connecting input/interactivity data to a specific device. |
| `amblight` | boolean | A BOOLEAN showing whether ambient light sensors are present and used for adaptive brightness. |
| `tempsense` | boolean | A BOOLEAN indicating if the device has a temperature sensor to track environmental or internal heat. |
| `accelsense` | boolean | A BOOLEAN stating if accelerometers are included for motion detection. |
| `gyrosense` | boolean | A BOOLEAN indicating the presence of gyroscopes for orientation or tilt detection. |
| `hapfeed` | character varying | A VARCHAR(30) describing the haptic feedback system (e.g., Basic, Advanced). |
| `hapstr` | smallint | A SMALLINT representing the maximum intensity or strength of the haptic feedback. |
| `vibmodes` | smallint | A SMALLINT counting how many vibration patterns or modes are available. |
| `forcefeed` | character varying | A VARCHAR(35) naming the force feedback type or system (e.g., Advanced, Basic). |
| `trigres` | smallint | A SMALLINT for trigger resistance levels or steps (on controllers with adaptive triggers). |
| `trigtravmm` | numeric | A NUMERIC(3,1) describing trigger travel distance in millimeters. |
| `joydead` | numeric | A NUMERIC(4,2) specifying the joystick dead zone (as a ratio or percentage). |
| `joyprec` | numeric | A NUMERIC(4,1) measuring joystick precision or resolution (e.g., in a scale from 0-100). |
| `btnspcmm` | numeric | A NUMERIC(4,1) indicating spacing (in mm) between buttons (e.g., on a controller face). |
| `btnszmm` | numeric | A NUMERIC(4,1) describing the physical size (in mm) of face buttons or triggers. |
| `dpadvar` | character varying | A VARCHAR(30) naming the D-pad style/type (e.g., Hybrid, Standard, Floating). |
| `dpadacc` | numeric | A NUMERIC(4,1) measuring D-pad accuracy on a scale or in a test metric. |
| `astickvar` | character varying | A VARCHAR(30) describing the analog stick construction/type (e.g., Standard, Magnetic, Hall Effect). |
| `driftres` | numeric | A NUMERIC(4,1) reflecting drift resistance or detection in the analog stick, measured on a scale or percentage. |

# Joins

* `interactdevref` references `devregistry` in [deviceidentity](/tables/deviceidentity.md).
* `interactphysref` references `physregistry` in [physicaldurability](/tables/physicaldurability.md).

# Related knowledge

* [Professional Esports Controller](/knowledge/professional-esports-controller.md)
* [DriftRes (Drift Resistance)](/knowledge/driftres.md)
* [Response Accuracy Index (RAI)](/knowledge/response-accuracy-index.md)
* [Haptic Feedback Quality (HFQ)](/knowledge/haptic-feedback-quality.md)
* [Professional-Grade Control Consistency](/knowledge/professional-grade-control-consistency.md)
