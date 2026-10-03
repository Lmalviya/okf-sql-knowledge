---
type: PostgreSQL Table
title: riskandmargin
description: '2 columns: risk_margin_profile. Joins to orders.'
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
| `ordervault` | character | A CHAR(36) FK referencing Orders(RecordVault). |
| `risk_margin_profile` | jsonb | JSONB column. Bundles leverage settings, margin thresholds, liquidation levels, iceberg layout, multifaceted risk labels, position sizing, margin‑call figures, and collateral details into one field for rapid risk evaluation. |

# JSON fields

* `risk_margin_profile.leverage.margform`: An enum (MargForm_enum) for margin mode (Isolated, Cross).
* `risk_margin_profile.leverage.levscale`: An enum (LevScale_enum) for leverage (1, 2, 3, 5, 10, 20, 50, 100).
* `risk_margin_profile.margin_thresholds.inithold`: A DECIMAL(12,3) initial margin required (e.g., '500.250').
* `risk_margin_profile.margin_thresholds.mainthold`: A DECIMAL(12,3) maintenance margin threshold (e.g., '300.125').
* `risk_margin_profile.price_levels.liqquote`: A NUMERIC(12,3) liquidation price estimate (e.g., '25000.750').
* `risk_margin_profile.price_levels.stopquote`: A NUMERIC(12,3) stop price (e.g., '27000.000').
* `risk_margin_profile.price_levels.trigquote`: A DECIMAL(12,3) advanced trigger price (e.g., '26950.250').
* `risk_margin_profile.price_levels.traildiff`: A DECIMAL(12,3) trailing delta (e.g., '150.500').
* `risk_margin_profile.iceberg.icebcount`: A DOUBLE PRECISION iceberg hidden portion (e.g., 3.25).
* `risk_margin_profile.iceberg.viscount`: A DOUBLE PRECISION visible portion (e.g., 1.75).
* `risk_margin_profile.risk_factors.liqfactor`: A VARCHAR(20) label for liquidation risk (e.g., 'HighRisk').
* `risk_margin_profile.risk_factors.cpfactor`: A VARCHAR(30) label for counterparty risk (e.g., 'Tier2Counterparty').
* `risk_margin_profile.risk_factors.setfactor`: A VARCHAR(30) settlement risk label (e.g., 'DailySettle').
* `risk_margin_profile.risk_factors.custfactor`: A VARCHAR(30) custody risk label (e.g., 'ColdStorage').
* `risk_margin_profile.risk_factors.netfactor`: A VARCHAR(30) network risk label (e.g., 'ChainCongestion').
* `risk_margin_profile.risk_factors.regfactor`: A VARCHAR(30) regulatory risk label (e.g., 'RestrictedRegion').
* `risk_margin_profile.position.poscount`: A DECIMAL(12,3) position size in base units (e.g., '0.300').
* `risk_margin_profile.position.possum`: A DECIMAL(12,3) notional value of position (e.g., '8100.000').
* `risk_margin_profile.position.posedge`: An enum (PosEdge_enum) for position direction (Short, Long).
* `risk_margin_profile.position.posmagn`: An enum (PosMagn_enum) representing position leverage (1, 2, 3, 5, 10, 20, 50, 100).
* `risk_margin_profile.position.posriskrate`: A DECIMAL(5,3) position risk ratio (e.g., '0.455').
* `risk_margin_profile.margin_rates.margrate`: A DECIMAL(5,3) margin ratio (e.g., '0.300').
* `risk_margin_profile.margin_rates.margcallquote`: A DECIMAL(12,3) margin-call trigger price (e.g., '25500.250').
* `risk_margin_profile.margin_rates.bkptquote`: A DECIMAL(12,3) bankruptcy or forced liquidation price (e.g., '25000.000').
* `risk_margin_profile.collateral.collrate`: A DECIMAL(5,3) collateral ratio (e.g., '0.600').
* `risk_margin_profile.collateral.collsum`: A DECIMAL(12,3) collateral amount posted (e.g., '5000.000').
* `risk_margin_profile.collateral.collcoin`: An enum (CollCoin_enum) referencing collateral currency (USDT, USDC, BTC, ETH).
* `risk_margin_profile.collateral.insfundshare`: A DECIMAL(12,3) portion allocated from the insurance fund (e.g., '50.000').

# Joins

* `ordervault` references `recordvault` in [orders](/tables/orders.md).
