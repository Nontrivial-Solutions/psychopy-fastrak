---
title: 00005 Stream Data from a Fastrak
authors:
  - joe_starr
status: high 
---

## Goals

The use case models the setting of a Fastrak into streaming mode.  

### Happy Outcome

When the use case completes successfully the Fastrak state is streaming.  

### Sad Outcome

When the use case completes unsuccessfully a failure is handled.

## Preconditions

- A Fastrak device is physically connected.
- A Fastrak device is set up.

## Actors

- [Time](../actors/00002_time.md)
- An upstream actor.

## Trigger

A Fastrak needs to be set to streaming mode.  

## Scenario

1. The Fastrak is set to streaming mode
1. An error occurs:
    1. Set error state
