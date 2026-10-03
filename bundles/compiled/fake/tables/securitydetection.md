---
type: PostgreSQL Table
title: securitydetection
description: '7 columns: detecttime, detectsource, lastupd, updfreqhrs, detection_score_profile. Joins to technicalinfo.'
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_schema.txt
  title: fake schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_column_meaning_base.json
  title: fake column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `secdetkey` | character, primary key | A CHAR(12) primary key uniquely identifying each security detection (e.g., 'SD1234567890'). |
| `sectechref` | character | A CHAR(12) referencing TechnicalInfo(TechKey) (e.g., 'TI1234567890'). |
| `detecttime` | timestamp without time zone | A TIMESTAMP noting when the security event was detected (e.g., '2025-03-14 10:15:00'). |
| `detectsource` | USER-DEFINED | An enum (DetectionSource_enum) for how detection was triggered (Manual Review, User Report, Pattern Match, Algorithm). |
| `lastupd` | timestamp without time zone | A TIMESTAMP indicating the last update (e.g., '2025-03-15 05:20:00'). |
| `updfreqhrs` | smallint | A SMALLINT for how often (in hours) re-evaluation occurs (e.g., '24'). |
| `detection_score_profile` | jsonb | JSONB column. Aggregates all granular detection scores, risk indicators, and model‑reliability attributes so the full threat posture of a security event can be inspected with a single JSONB read. |

# JSON fields

* `detection_score_profile.overall.detectconf`: A NUMERIC(3,2) confidence level (e.g., '0.93').
* `detection_score_profile.overall.riskval`: NUMERIC(4,2) overall risk rating (e.g., '0.93').
* `detection_score_profile.overall.threatlvl`: An enum (ThreatLevel_enum) describing threat priority (Critical, High, Low, Medium).
* `detection_score_profile.overall.confval`: NUMERIC(6,5) confidence in the final detection verdict (e.g., '0.98765').
* `detection_score_profile.overall.fposprob`: NUMERIC(5,4) false positive probability (e.g., '0.0345').
* `detection_score_profile.behavior_scores.autobehavscore`: NUMERIC(5,3) rating how automated the user’s behavior is (e.g., '0.754').
* `detection_score_profile.behavior_scores.botlikscore`: NUMERIC(6,3) capturing the likelihood of bot behavior (e.g., '0.784').
* `detection_score_profile.behavior_scores.spambehavscore`: NUMERIC(4,2) measuring spam-related behavior (e.g., '0.87').
* `detection_score_profile.behavior_scores.commintscore`: NUMERIC(6,4) rating commercial/spam intent (e.g., '0.1234').
* `detection_score_profile.pattern_scores.behavpatscore`: NUMERIC(5,2) capturing overall suspicious patterns (e.g., '0.75').
* `detection_score_profile.pattern_scores.temppatscore`: NUMERIC(6,3) measuring irregularities in temporal patterns (e.g., '1.234').
* `detection_score_profile.pattern_scores.netpatscore`: NUMERIC(4,2) capturing suspicious network-level patterns (e.g., '0.85').
* `detection_score_profile.pattern_scores.contpatscore`: NUMERIC(5,3) capturing suspicious content patterns (e.g., '0.642').
* `detection_score_profile.pattern_scores.profpatscore`: NUMERIC(4,3) suspicious profile patterns (e.g., '0.632').
* `detection_score_profile.pattern_scores.techpatscore`: NUMERIC(4,3) suspicious technical patterns (e.g., '0.872').
* `detection_score_profile.detection_reliability.detmethrel`: NUMERIC(4,3) detection method reliability (e.g., '0.855').
* `detection_score_profile.detection_reliability.modelver`: A VARCHAR(12) labeling the detection model version (e.g., 'mdl_v1.3').
* `detection_score_profile.detection_reliability.featver`: A VARCHAR(12) labeling the detection feature set version (e.g., 'feat_set2').

# Joins

* `sectechref` references `techkey` in [technicalinfo](/tables/technicalinfo.md).

# Related knowledge

* [detection_score_profile.overall.confval](/knowledge/detection-score-profile-overall-confval.md)
* [detection_score_profile.behavior_scores.botlikscore](/knowledge/detection-score-profile-behavior-scores-botlikscore.md)
* [Latest Bot Likelihood Score (LBS)](/knowledge/latest-bot-likelihood-score.md)
* [last activity proxy time](/knowledge/last-activity-proxy-time.md)
