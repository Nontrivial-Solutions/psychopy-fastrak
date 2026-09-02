---
title: 00004 Reset the Fastrak 
authors:
  - joe_starr
status: high 
---

## Goals

The use case models the resetting of the state of a physical Fastrak.  

### Happy Outcome

When the use case completes successfully the Fastrak state is reset.  

### Sad Outcome

When the use case completes unsuccessfully a failure is handled.

## Preconditions

- A Fastrak device is physically connected.

## Actors

- [Time](../actors/00002_time.md)
- An upstream actor.

## Trigger

A Fastrak needs to be reset.  

## Scenario

1. The Fastrak is reset
1. An error occurs:
    1. Set error state
