---
type: PostgreSQL Table
title: profile
description: '3 columns: profile_composition. Joins to account.'
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
| `profkey` | character, primary key | A CHAR(12) primary key uniquely identifying each profile record (e.g., 'PF1234567890'). |
| `profaccref` | character | A CHAR(12) referencing Account(AccIndex), linking this profile to a single account (e.g., 'AC1234567890'). |
| `profile_composition` | jsonb | JSONB column. Consolidates username, picture, bio, location, and contact‑credibility attributes to streamline profile‑quality checks and downstream ML feature extraction. |

# JSON fields

* `profile_composition.completeness`: NUMERIC(3,2) reflecting how complete the profile is (e.g., '0.85').
* `profile_composition.username.profnametag`: An enum (ProfileNamePattern_enum) describing the profile’s name style (Sequential, Template, Random, Natural).
* `profile_composition.username.usrentval`: NUMERIC(5,4) capturing username entropy (e.g., '0.2549').
* `profile_composition.username.usrlen`: A SMALLINT indicating how many characters are in the username (e.g., '12').
* `profile_composition.username.usrpatn`: An enum (UsernamePattern_enum) storing the username pattern (Random, Generated, Meaningful, AlphaNum).
* `profile_composition.display_name.dispnameshift`: A SMALLINT counting how many times the display name changed (e.g., '3').
* `profile_composition.picture.picformat`: An enum (ProfilePictureType_enum) describing the profile picture type (Stock, AI Generated, Real, Celebrity).
* `profile_composition.picture.picscval`: NUMERIC(4,1) scoring the authenticity/quality of the picture (e.g., '7.5').
* `profile_composition.bio.biospan`: A SMALLINT measuring bio length in characters (e.g., '160').
* `profile_composition.bio.biolang`: An enum (BioLanguage_enum) for the bio’s language code (en, multiple, mixed, unknown).
* `profile_composition.bio.biolinknum`: An enum (BioLinkCount_enum) for the number of links (0 through 5).
* `profile_composition.bio.biokeycheck`: An enum (BioKeywordMatch_enum) flagging suspicious or notable keywords (Suspicious, Normal, Spam, Promo).
* `profile_composition.location.locgiven`: An enum (LocationProvided_enum) describing location provisioning (Fake, No, Yes, Multiple).
* `profile_composition.location.locshiftnum`: A SMALLINT showing how many times the stated location changed (e.g., '2').
* `profile_composition.contact.maildomainfmt`: An enum (EmailDomainType_enum) describing the email domain (Free, Unknown, Custom, Disposable).
* `profile_composition.contact.phnumstate`: An enum (PhoneNumberStatus_enum) describing phone number status (Invalid, VOIP, Valid).

# Joins

* `profaccref` references `accindex` in [account](/tables/account.md).

# Related knowledge

* [profile_composition.completeness](/knowledge/profile-composition-completeness.md)
* [Session Count (SC)](/knowledge/session-count.md)
* [Total Post Frequency (TPF)](/knowledge/total-post-frequency.md)
