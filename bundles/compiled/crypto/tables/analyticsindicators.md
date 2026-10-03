---
type: PostgreSQL Table
title: analyticsindicators
description: '3 columns: market_sentiment_indicators. Joins to marketdata, marketstats.'
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
| `mdataref` | bigint | A BIGINT FK referencing MarketData(MarketDataNode). |
| `mstatsref` | bigint | A BIGINT FK referencing MarketStats(MarketStatsMark). |
| `market_sentiment_indicators` | jsonb | JSONB column. Aggregates order‑book walls, momentum gauges, technical oscillators, flow imbalances, large‑player activity, and arbitrage signals to streamline advanced analytics and back‑testing. |

# JSON fields

* `market_sentiment_indicators.walls.buywallband`: A DECIMAL(10,3) measuring buy wall distance (e.g., '450.500').
* `market_sentiment_indicators.walls.sellwallband`: A DECIMAL(10,3) measuring sell wall distance (e.g., '480.250').
* `market_sentiment_indicators.momentum.buyforce`: A REAL indicating buy momentum (e.g., 35.7).
* `market_sentiment_indicators.momentum.sellforce`: A REAL indicating sell momentum (e.g., 25.4).
* `market_sentiment_indicators.momentum.mktfeel`: An enum (MktFeel_enum) for overall sentiment (Bearish, Bullish, Neutral).
* `market_sentiment_indicators.momentum.techmeter`: An enum (TechMeter_enum) summarizing technical signals (Buy, Sell, Hold).
* `market_sentiment_indicators.oscillators.rsi14spot`: A NUMERIC(13,3) storing RSI(14) (e.g., '45.123').
* `market_sentiment_indicators.oscillators.macdtrail`: A NUMERIC(12,3) capturing MACD line (e.g., '1.234').
* `market_sentiment_indicators.oscillators.bbandspan`: A NUMERIC(12,3) Bollinger Band width (e.g., '150.250').
* `market_sentiment_indicators.flow.flowimbal`: A DOUBLE PRECISION for order-flow imbalance (e.g., 12.5).
* `market_sentiment_indicators.flow.tradeimbal`: A DOUBLE PRECISION for trade-flow imbalance (e.g., -8.75).
* `market_sentiment_indicators.flow.largeflowrate`: A DECIMAL(12,3) fraction of large orders (e.g., '0.125').
* `market_sentiment_indicators.flow.smartforce`: A REAL capturing 'smart money' flows (e.g., 10.2).
* `market_sentiment_indicators.flow.retailflow`: A REAL capturing retail flows (e.g., 5.3).
* `market_sentiment_indicators.flow.instflow`: A REAL capturing institutional flows (e.g., 7.9).
* `market_sentiment_indicators.big_players.whalemotion`: An enum (WhaleMotion_enum) for large trader activity (Low, Medium, High).
* `market_sentiment_indicators.big_players.makermotion`: An enum (MakerMotion_enum) for market maker activity (Low, Medium, High).
* `market_sentiment_indicators.arbitrage.arbpotential`: A NUMERIC(10,4) arbitrage potential (e.g., '0.0575').
* `market_sentiment_indicators.arbitrage.xexchband`: A NUMERIC(10,4) cross-exchange spread (e.g., '0.0125').
* `market_sentiment_indicators.arbitrage.fundgap`: A NUMERIC(10,4) funding arbitrage difference (e.g., '0.0050').
* `market_sentiment_indicators.arbitrage.basisgap`: A NUMERIC(10,4) basis spread (futures vs spot) (e.g., '0.0300').

# Joins

* `mdataref` references `marketdatanode` in [marketdata](/tables/marketdata.md).
* `mstatsref` references `marketstatsmark` in [marketstats](/tables/marketstats.md).
