---
title: 00006 Conclude Streaming of Data from a Fastrak
authors:
  - joe_starr
status: high 
---

## Goals

The use case models the bringing a Fastrak out of streaming mode.  

### Happy Outcome

When the use case completes successfully the Fastrak state is not streaming.  

### Sad Outcome

When the use case completes unsuccessfully a failure is handled.

## Preconditions

- A Fastrak device is physically connected.
- A Fastrak device is set up.

## Actors

- [Time](../actors/00002_time.md)
- An upstream actor.

## Trigger

A Fastrak needs to end streaming mode.  

## Scenario

1. The Fastrak streaming mode is deactivated
1. An error occurs:
    1. Set error state
