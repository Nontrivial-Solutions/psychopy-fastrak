---
title: 00001 Use a Fastrak in an Experiment
authors:
  - joe_starr
status: high
---

## Goals

The use case models the use of Fastrak device during a [routine][DD_RTN].

### Happy Outcome

When the use case completes successfully a streaming session is completed with the Fastrak.

#### Sad Outcome

When the use case completes unsuccessfully a failure is handled.

### Preconditions

- A Fastrak device is physically connected.

### Actors

- [User](../actors/00001_user.md)
- [Time](../actors/00002_time.md)

### Trigger

A user begins an experiment containing a [routine][DD_RTN] which uses a Fastrak.

### Scenario

1. The Fastrak is connected
1. The Fastrak is set up
1. Fastrak stream is begun
1. Fastrak stream is concluded
1. Fastrak stream is saved
1. The Fastrak is reset
1. An error occurs:
    1. Set error state
