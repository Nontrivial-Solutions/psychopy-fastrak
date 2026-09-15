---
title: 00002 Publish Position 
authors:
  - joe_starr
status: high 
---

## Goals

The use case models the publishing of the Fastrak's current position to any subscribed components.  

### Happy Outcome

When the use case completes successfully a position is published.  

### Sad Outcome

When the use case completes unsuccessfully a failure is handled.

## Preconditions

- A Fastrak device is physically connected.

## Actors

- [Time](../actors/00002_time.md)
- An upstream actor.

## Trigger

A new frame is processed in the event loop.  

## Scenario

1. The position is retrieved from the Fastrak
1. The position is published
1. An error occurs:
    1. Set error state
