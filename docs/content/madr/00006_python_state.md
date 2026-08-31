---
title: 00006 Python State
authors:
  - joe_starr
status: accepted
date: 2026-08-31
---

## Context and Problem Statement

At experiment runtime the hardware portion of the plugin requires that the python environment have
drivers on the PATH. Additionally, at runtime PsychoPy requires that the Python environment has the
plugin itself on the PATH. This ADR answers how we will ensure that the plugin is on the PATH.

## Decision Outcome

We will take no positive action to install the plugin into the Python environment. We will assume
that the current Python environment has the plugin and fail by exception otherwise. We assume that
the user is competent and able to debug the missing package error.

## Decision Drivers  

- Must not squash Python state.

## Considered Options

No other options considered.
