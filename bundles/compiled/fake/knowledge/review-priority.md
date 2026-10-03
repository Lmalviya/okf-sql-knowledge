---
type: Value Illustration
title: review priority
description: A flag or status assigned to an account to indicate the need or priority level for manual review.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 85
---

# Definition

A field in the `account` table set to a specific value like 'Review_Inactive_Trusted' to signal that an otherwise trusted account requires review due to prolonged inactivity.

# Depends on

* [Trusted Account](/knowledge/trusted-account.md)
* [last activity proxy time](/knowledge/last-activity-proxy-time.md)
