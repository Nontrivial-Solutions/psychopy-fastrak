---
title: 00001 Decide on Plugin Architecture 
authors:
  - joe_starr
status: accepted
date: 2026-06-18
---

## Context and Problem Statement

The general architecture of the plugin determines what and how downstream tasks (documentation,
implementation, and testing) are approached. This ADR determines how we will approach the
architecture of the system.

## Decision Outcome

Use parts of the architecture of existing flows. This lets us leverage existing PsychoPy designs we
know work without the heavy reverse engineering load of scratch work.

We will match the:

- ButtonBox flow
- Microphone flow

## Decision Drivers  

- Must be usable in PsychoPy
- Must be straight forward to design and implement
- Must be fast to design and implement
- Must be easy to test

## Considered Options

- A custom architecture
- Match the architecture of an existing flow
- Use parts of the architecture of existing flows

### A Custom Architecture

Define a custom architecture (file structure, design methodology, etc.) for the plugin.

- Good, because it allows for the most flexibility in implementation.  
- Good, because it allows for easy to unit test
- Good, because it allows for easy to integration test
- Bad, because it will take a long time to reverse engineer PsychoPy architecture
- Bad, because it may not work with PsychoPy very easily

### Match the Architecture of an Existing Flow

Use an existing PsychoPy hardware $\to$ experiment architecture for the plugin.

- Neutral, because it locks us into a potentially "suboptimal" architecture
- Good, because it reduces a need for unit testing
- Good, because it allows for easy to integration test
- Good, because it will be quick to design and implement
- Good, because it WILL work with PsychoPy

### Use Parts of the Architecture of Existing Flows

Use ideas from a number of existing PsychoPy hardware $\to$ experiment architectures for the plugin.

- Good, because it lets us build a more "optimal" architecture
- Good, because it reduces a need for unit testing
- Good, because it allows for easy to integration test
- Good, because it will be quick to design and implement
- Good, because it WILL work with PsychoPy
