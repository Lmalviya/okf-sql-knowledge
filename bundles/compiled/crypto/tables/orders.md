---
type: PostgreSQL Table
title: orders
description: '17 columns: recordvault, timecode, exchspot, mktnote, orderstamp, ordertune, dealedge, dealquote, dealcount, notionsum, orderflow, timespan, orderbase, clientmark, createspot, updatespot. Joins to users.'
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_schema.txt
  title: crypto schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_column_meaning_base.json
  title: crypto column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `recordvault` | character | A CHAR(36) unique order reference (e.g., '58d9c141-7f13-4cd3-ba93-f520bf922f7c'). |
| `timecode` | timestamp without time zone | A TIMESTAMP recording order creation (e.g., '2025-05-10 13:45:00'). |
| `exchspot` | character | A CHAR(10) referencing the exchange ID (e.g., 'BINANCE'). |
| `mktnote` | character varying | A VARCHAR(30) naming the market pair or trading symbol (e.g., 'BTC/USDT'). |
| `orderstamp` | character | A CHAR(36) external or client order ID (e.g., 'CL-3c4a8f89-9aed'). |
| `userlink` | character | A CHAR(36) FK to Users(UserStamp), linking this order to its owner. |
| `ordertune` | USER-DEFINED | An enum (OrderTune_enum) describing order type (Stop, Market, Limit, StopLimit). |
| `dealedge` | USER-DEFINED | An enum (DealEdge_enum) indicating side (Sell, Buy). |
| `dealquote` | numeric | A DECIMAL(12,3) capturing the limit or stop price (e.g., '27800.500'). |
| `dealcount` | numeric | A NUMERIC(12,4) for the order quantity (e.g., '0.1250'). |
| `notionsum` | numeric | A DECIMAL(12,3) notional value (price × quantity) (e.g., '3475.063'). |
| `orderflow` | USER-DEFINED | An enum (OrderFlow_enum) describing the status (New, PartiallyFilled, Cancelled, Filled). |
| `timespan` | USER-DEFINED | An enum (TimeSpan_enum) for time-in-force (IOC, GTC, GTD, FOK). |
| `orderbase` | USER-DEFINED | An enum (OrderBase_enum) indicating how the order was placed (API, Web, Mobile, Bot). |
| `clientmark` | character varying | A VARCHAR(80) holding an optional client-supplied tag (e.g., 'myXtrOrder001'). |
| `createspot` | timestamp without time zone | A TIMESTAMP showing when the order was first persisted (e.g., '2025-05-10 13:45:00'). |
| `updatespot` | timestamp without time zone | A TIMESTAMP noting the last update to this order (e.g., '2025-05-10 14:02:15'). |

# Joins

* `userlink` references `userstamp` in [users](/tables/users.md).

# Related knowledge

* [Slippage Impact](/knowledge/slippage-impact.md)
* [Market Impact Cost (MIC)](/knowledge/market-impact-cost.md)
* [Order Fill Rate](/knowledge/order-fill-rate.md)
* [Whale Order](/knowledge/whale-order.md)
* [dealedge](/knowledge/dealedge.md)
* [orderflow](/knowledge/orderflow.md)
* [timespan](/knowledge/timespan.md)
* [True Cost of Execution](/knowledge/true-cost-of-execution.md)
* [Arbitrage ROI](/knowledge/arbitrage-roi.md)
* [Market Depth Ratio](/knowledge/market-depth-ratio.md)
