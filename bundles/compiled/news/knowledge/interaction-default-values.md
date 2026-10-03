---
type: Value Illustration
title: Interaction Default Values
description: A standardized set of initial values assigned to interaction behavior metrics when a new interaction record is created.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 60
---

# Definition

A JSON structure: jsonb_build_object('scroll', jsonb_build_object('depth', 0, 'speed', 0.0, 'percentage', 0), 'exit_type', 'Natural', 'conversion', jsonb_build_object('value', 0, 'status', 'None'), 'time_spent', jsonb_build_object('viewport_time', 0, 'attention_time', 0, 'reading_seconds', 0, 'duration_seconds', 0), 'next_action', 'None', 'bounce_status', 'No', 'click_seconds', 0)
