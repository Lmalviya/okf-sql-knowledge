---
type: PostgreSQL Table
title: communication
description: '7 columns: radiofrequencymhz, antennastatus, bluetoothstatus, commopmaintref, signalmetrics. Joins to equipment, location.'
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:09+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_schema.txt
  title: polar schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_column_meaning_base.json
  title: polar column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `commeqref` | character varying | A VARCHAR(70) foreign key referencing Equipment(EquipmentCode), linking communication data to a specific piece of equipment. |
| `commlocref` | integer | An INTEGER foreign key referencing Location(LocationRegistry) for associating the communication system with a location (e.g., a station). |
| `radiofrequencymhz` | real | A REAL value specifying the radio communication frequency in MHz. |
| `antennastatus` | USER-DEFINED | An enum (AntennaStatus_enum) indicating the antenna’s operational state (e.g., Error, Normal, Warning). |
| `bluetoothstatus` | USER-DEFINED | An enum (BluetoothStatus_enum) indicating the Bluetooth status (e.g., On, Error, Off, Pairing). |
| `commopmaintref` | integer | An INTEGER optionally referencing OperationMaintenance(OpMaintRegistry) for maintenance or operational records tied to communication gear. |
| `signalmetrics` | jsonb | JSONB column. Combines signal strength and performance metrics for various communication systems. |

# JSON fields

* `signalmetrics.gps_strength`: An enum (GPSSignalStrength_enum) for GPS signal quality (e.g., Strong, Weak, Medium).
* `signalmetrics.satellite_status`: An enum (SatelliteConnectionStatus_enum) specifying the satellite connection state (e.g., Limited, Connected, Disconnected).
* `signalmetrics.radio_strength_dbm`: A DECIMAL(7,3) measuring radio signal strength in dBm.
* `signalmetrics.wifi_strength_dbm`: A FLOAT specifying the WiFi signal strength in dBm.
* `signalmetrics.latency_ms`: A NUMERIC(6,2) for the measured network latency in milliseconds.
* `signalmetrics.data_rate_kbps`: A DOUBLE PRECISION value showing the data transmission rate in kilobits per second.

# Joins

* `commeqref` references `equipmentcode` in [equipment](/tables/equipment.md).
* `commlocref` references `locationregistry` in [location](/tables/location.md).

# Related knowledge

* [Communication Reliability Index (CRI)](/knowledge/communication-reliability-index.md)
* [Communication Zone Status](/knowledge/communication-zone-status.md)
* [Base Station Communication Stability Index (BSCSI)](/knowledge/base-station-communication-stability-index.md)
