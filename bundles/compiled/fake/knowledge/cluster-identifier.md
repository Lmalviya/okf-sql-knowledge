---
type: Business Rule
title: cluster identifier
description: A key used to group related accounts identified as part of the same network or cluster.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 80
---

# Definition

In this context, the platform identifier (`platident`) associated with the accounts in the potential Amplification Network is the cluster identifier.

# Columns used

* [account](/tables/account.md): `platident`

# Depends on

* [Amplification Network](/knowledge/amplification-network.md)

# Used by

* [member count](/knowledge/member-count.md)
* [maximum coordination score](/knowledge/maximum-coordination-score.md)
* [member account IDs](/knowledge/member-account-ids.md)
