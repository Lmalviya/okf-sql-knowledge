---
type: PostgreSQL Table
title: datalogger
description: '19 columns: logflag, loginterval, transmitflag, datauptime, datapct, batteryswap, firmvers, softupdate, syshealth, memusepct, storecapmb, storeremainmb, netsignal, commproto, syncflag, syncfreqhr. Joins to container, shipments.'
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
| `loggerreg` | character varying, primary key | A VARCHAR(20) primary key uniquely identifying each data logger record. |
| `logflag` | USER-DEFINED | An enum (DataLoggerStatus_enum) indicating the logger’s status (e.g., 'Malfunction', 'Battery Low', 'Active'). |
| `loginterval` | smallint | A SMALLINT specifying the frequency (in minutes) at which the logger records or transmits data. |
| `transmitflag` | USER-DEFINED | An enum (TransmissionStatus_enum) indicating the data transmission status (e.g., 'Failed', 'Real-time', 'Delayed'). |
| `datauptime` | timestamp without time zone | A TIMESTAMP showing the logger’s current or last recorded operational uptime reading. |
| `datapct` | real | A REAL value reflecting the logger’s used data capacity or data completeness in percentage. |
| `batteryswap` | date | A DATE noting when the data logger battery was last replaced or swapped. |
| `firmvers` | character varying | A VARCHAR(50) naming the firmware version installed on the data logger. |
| `softupdate` | text | A TEXT field for recording any software update notes or logs. |
| `syshealth` | USER-DEFINED | An enum (SystemHealth_enum) describing the logger’s system health (e.g., 'Poor', 'Fair', 'Good'). |
| `memusepct` | smallint | A SMALLINT for the percentage of the logger’s internal memory currently in use. |
| `storecapmb` | integer | An INTEGER representing the logger’s total storage capacity in megabytes. |
| `storeremainmb` | integer | An INTEGER indicating remaining/free storage in megabytes. |
| `netsignal` | USER-DEFINED | An enum (NetworkSignal_enum) representing network signal strength (e.g., 'Poor', 'Good', 'Excellent'). |
| `commproto` | character varying | A VARCHAR(20) naming the communication protocol (e.g., RF, Bluetooth, Satellite, GSM). |
| `syncflag` | character varying | A VARCHAR(20) describing synchronization status (e.g., 'Pending', 'Success', 'Failed'). |
| `syncfreqhr` | smallint | A SMALLINT indicating how often (in hours) synchronization is attempted or performed. |
| `containlog` | character varying | A VARCHAR(20) foreign key referencing Container(ContainRegistry). Connects the data logger to a container. |
| `shiplog` | character varying | A VARCHAR(20) foreign key referencing Shipments(ShipmentRegistry). Optionally links the data logger to a shipment. |

# Joins

* `containlog` references `containregistry` in [container](/tables/container.md).
* `shiplog` references `shipmentregistry` in [shipments](/tables/shipments.md).

# Related knowledge

* [Logger Health Index (LHI)](/knowledge/logger-health-index.md)
* [CommProto: 'RF'](/knowledge/commproto-rf.md)
* [TransmitFlag: 'Real-time'](/knowledge/transmitflag-real-time.md)
* [CommProto: 'Satellite'](/knowledge/commproto-satellite.md)
