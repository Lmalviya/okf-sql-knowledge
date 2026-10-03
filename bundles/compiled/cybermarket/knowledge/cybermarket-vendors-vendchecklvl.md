---
type: Value Illustration
title: cybermarket|vendors|vendchecklvl
description: Illustrates the vendor verification system and trustworthiness indicators
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 7
---

# Definition

'Basic' vendors have completed minimal verification steps, typically only email and captcha verification with limited platform history; 'Advanced' vendors have undergone additional verification including identification consistency checks and longer positive platform history; 'Premium' vendors represent the highest verification tier, having submitted verifiable identity elements and maintained extended positive transaction records with minimal disputes.

# Columns used

* [vendors](/tables/vendors.md): `vendchecklvl`

# Used by

* [Trusted Vendor](/knowledge/trusted-vendor.md)
* [Vendor Relationship Strength (VRS)](/knowledge/vendor-relationship-strength.md)
* [Market Kingpin](/knowledge/market-kingpin.md)
* [Customer Loyalty Network](/knowledge/customer-loyalty-network.md)
