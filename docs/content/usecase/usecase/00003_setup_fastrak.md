---
title: 00003 Set up the Fastrak 
authors:
  - joe_starr
status: high 
---

## Goals

The use case models the initialization of the physical Fastrak.  

### Happy Outcome

When the use case completes successfully the Fastrak is set up.  

### Sad Outcome

When the use case completes unsuccessfully a failure is handled.

## Preconditions

- A Fastrak device is physically connected.

## Actors

- [Time](../actors/00002_time.md)
- An upstream actor.

## Trigger

A Fastrak needs to be set up.  

## Scenario

1. The Fastrak is set up  
1. An error occurs:
    1. Set error state
