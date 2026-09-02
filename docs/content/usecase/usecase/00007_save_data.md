---
title: 00007 Save Data from Previous Streaming Session
authors:
  - joe_starr
status: high 
---

## Goals

The use case models the saving of data from a streaming session is saved.

### Happy Outcome

When the use case completes successfully the Fastrak data is stored.  

### Sad Outcome

When the use case completes unsuccessfully a failure is handled.

## Preconditions

- A Fastrak device is physically connected.
- A Fastrak device is set up.

## Actors

- [Time](../actors/00002_time.md)
- An upstream actor.

## Trigger

A Fastrak data needs to be stored.  

## Scenario

1. The Fastrak data is processed
1. The Fastrak output file is identified
1. The Fastrak data is stored
1. An error occurs:
    1. Set error state
