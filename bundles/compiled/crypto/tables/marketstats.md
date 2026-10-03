---
type: PostgreSQL Table
title: marketstats
description: '19 columns: fundrate, fundspot, openstake, volday, tradeday, tnoverday, priceshiftday, highspotday, lowspotday, vwapday, mktsize, circtotal, totsupply, maxsupply, mkthold, traderank, liquidscore, volmeter. Joins to marketdata.'
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
| `fundrate` | numeric | A DECIMAL(6,4) funding rate for futures (e.g., '0.0100'). |
| `fundspot` | timestamp without time zone | A TIMESTAMP for next or recent funding event (e.g., '2025-05-11 08:00:00'). |
| `openstake` | numeric | A NUMERIC(15,5) open interest (e.g., '125000.50000'). |
| `volday` | double precision | A DOUBLE PRECISION showing 24h volume (e.g., 1204567.8). |
| `tradeday` | integer | An INTEGER for 24h trade count (e.g., 34567). |
| `tnoverday` | numeric | A DECIMAL(12,3) 24h turnover or notional (e.g., '356789.230'). |
| `priceshiftday` | numeric | A DECIMAL(12,3) net 24h price change (e.g., '-350.250'). |
| `highspotday` | numeric | A DECIMAL(12,3) 24h high (e.g., '28100.000'). |
| `lowspotday` | numeric | A DECIMAL(12,3) 24h low (e.g., '27200.000'). |
| `vwapday` | numeric | A DECIMAL(12,3) volume-weighted average price (e.g., '27700.125'). |
| `mktsize` | numeric | A NUMERIC(13,3) total market cap or size (e.g., '125000000.000'). |
| `circtotal` | numeric | A NUMERIC(13,3) circulating supply (e.g., '18000000.000'). |
| `totsupply` | numeric | A NUMERIC(13,3) total supply (e.g., '21000000.000'). |
| `maxsupply` | numeric | A NUMERIC(13,3) maximum supply if applicable (e.g., '21000000.000'). |
| `mkthold` | numeric | A DECIMAL(13,3) market dominance or share (e.g., '45.000'). |
| `traderank` | integer | An INTEGER rank for volume or liquidity (e.g., 2). |
| `liquidscore` | numeric | A DECIMAL(8,2) liquidity measure (e.g., '85.20'). |
| `volmeter` | numeric | A DECIMAL(8,2) volatility or fluctuation rating (e.g., '35.50'). |
| `mdlink` | bigint | A BIGINT FK to MarketData(MarketDataNode), associating stats with a snapshot. |

# Joins

* `mdlink` references `marketdatanode` in [marketdata](/tables/marketdata.md).

# Related knowledge

* [Position Value at Risk (PVaR)](/knowledge/position-value-at-risk.md)
* [Liquidity Ratio](/knowledge/liquidity-ratio.md)
* [Over-Leveraged Position](/knowledge/over-leveraged-position.md)
* [Technical Breakout](/knowledge/technical-breakout.md)
* [Volatility-Adjusted Spread](/knowledge/volatility-adjusted-spread.md)
