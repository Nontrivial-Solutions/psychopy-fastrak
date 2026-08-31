---
title: 00003 Decide on Testing Strategy
authors:
  - joe_starr
status: accepted
date: 2026-06-18
---

## Context and Problem Statement

Based on [ADR 00001](./00001_architecture.md) and [ADR 00002](./00002_documentation.md) we will be
reusing the architecture from PsychoPy and omitting documentation where reasonable. This combined
with the PsychoPy runtime makes traditional unit testing difficult. This ADR decides how we will
handle testing.

## Decision Outcome

Due to the difficulty of unit testing components in PsychoPy we will only conduct integration tests.
Test plans will be outlined in individual Markdown files in the `docs/content/tests` directory.

## Decision Drivers  

No drivers considered.

## Considered Options

No other options considered.
