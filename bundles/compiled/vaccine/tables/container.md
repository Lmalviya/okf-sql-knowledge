---
type: PostgreSQL Table
title: container
description: '15 columns: containmodel, volliters, masskg, containflag, coolkind, coolmass, coolremainpct, coolrefills, refilllatest, refillnext, batterypct, pwrfeed, pwrbackupflag. Joins to shipments.'
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_schema.txt
  title: vaccine schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_column_meaning_base.json
  title: vaccine column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `containregistry` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying each container record. |
| `containmodel` | character varying | A VARCHAR(40) naming or describing the container model/type. |
| `volliters` | integer | An INTEGER specifying the container's internal volume in liters. |
| `masskg` | real | A REAL number for the container’s mass in kilograms (when empty, if applicable). |
| `containflag` | character varying | A VARCHAR(30) field capturing a container status or classification (e.g., ‘In Transit’, ‘Active’, ‘Return’, ‘Delivered’). |
| `coolkind` | character varying | A VARCHAR(40) describing the coolant type used within the container (e.g., Dry Ice, Liquid Nitrogen, Phase Change Material). |
| `coolmass` | real | A REAL number indicating the mass (in kilograms) of the coolant present. |
| `coolremainpct` | numeric | A DECIMAL(5,2) representing the remaining percentage of coolant. |
| `coolrefills` | smallint | A SMALLINT count of how many times coolant has been refilled. |
| `refilllatest` | date | A DATE recording the most recent coolant refill date. |
| `refillnext` | date | A DATE for the scheduled or expected next refill date. |
| `batterypct` | real | A REAL percentage of the container’s internal battery level, if battery-powered components exist. |
| `pwrfeed` | character varying | A VARCHAR(40) indicating the primary power feed or source (e.g., Battery, External, Hybrid). |
| `pwrbackupflag` | character varying | A VARCHAR(40) specifying backup power availability status (e.g., Available, In Use, Not Available). |
| `shipown` | character varying | A VARCHAR(20) foreign key referencing Shipments(ShipmentRegistry). Links this container to a shipment. |

# Joins

* `shipown` references `shipmentregistry` in [shipments](/tables/shipments.md).

# Related knowledge

* [Coolant Depletion Rate (CDR)](/knowledge/coolant-depletion-rate.md)
* [Container Risk Index (CRI)](/knowledge/container-risk-index.md)
* [Storage Efficiency Ratio (SER)](/knowledge/storage-efficiency-ratio.md)
* [Logger Health Index (LHI)](/knowledge/logger-health-index.md)
* [Logger Failure Risk](/knowledge/logger-failure-risk.md)
* [Coolant Critical](/knowledge/coolant-critical.md)
* [CoolKind: 'Phase Change Material'](/knowledge/coolkind-phase-change-material.md)
* [Coolant Efficiency Index (CEI)](/knowledge/coolant-efficiency-index.md)
