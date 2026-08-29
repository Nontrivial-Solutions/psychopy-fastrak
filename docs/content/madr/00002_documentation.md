---
title: 00002 Decide on How to Document the Plugin 
authors:
  - joe_starr
status: accepted
date: 2026-06-18
---

## Context and Problem Statement

Based on [ADR 00001](./00001_architecture.md) we know the plugin will follow the general
architecture found in the existing PsychoPy Buttonbox and microphone plugins. This makes detailed
use case and unit documentation somewhat redundant.

This ADR decides how and where we will omit detained documentation.

## Decision Outcome

A mixed full and code unit and use case documentation.

We will document all the code fully. The only unit that will be documented fully is the "wrapper".
This object is the most important during an [experiment][DD_EXP] which is the primary goal.

For use cases only a block diagram will be presented.

## Decision Drivers  

- Must be fast to complete
- Must be understandable
- Must assist readers in understanding
- Must be easy to maintain

## Additional Information

We will define as follows for units similar definitions can be phrased for Use Cases:

>[!definition] "Full Unit Documentation"
>
> A complete collection of the following:
>
> - A class diagram
> - A description for each data member
> - Documentation for each data method
>     - A description for the method
>     - A state machine for the method
>     - (Optional) A collection of submachines
>     - (Optional) A sequence diagram
> - Unit test cards for each public method
> - Code context documentation

>[!definition] "Public Unit Documentation"
>
> A complete collection of the following:
>
> - A class diagram
> - A description for each public data member
> - Documentation for each public data method
>     - A description for the method
>     - A state machine for the method
>     - (Optional) A collection of submachines
>     - (Optional) A sequence diagram
> - Unit test cards for each public method
> - Code context documentation
>

>[!definition] "Code Context Documentation"
>
> - A full documentation for each unit and use case. No supplemental documentation.
> Inline source code comments for the unit and each of its methods and members.

## Considered Options

- A full documentation for each unit and use case.
- Public documentation for unit and use case
- A mixed full and public unit and use case documentation.
- A mixed full and code unit and use case documentation.

### A Full Documentation for Each Unit and Use Case

- Good, because it gives full context for all units and use cases
- Bad, because it is hard and time-consuming to maintain
- Bad, because it is time-consuming to complete

### Public Documentation for Unit and Use Case

- Good, because it gives interface context for all units and use cases
- Bad, because it is hard and time-consuming to maintain
- Bad, because it is time-consuming to complete

### A Mixed Full and Public Unit and Use Case Documentation

Some units and use cases are documented at the `full` level and some at the `public` level.

- Good, because it gives interface context for all units and use cases where deemed important
- Bad, because it is time-consuming to maintain since many units and use cases aren't used.
- Bad, because it is time-consuming to complete since many units and use cases aren't used.

### A Mixed Full and Code Unit and Use Case Documentation

Some components are documented at the `full` level and some at the `code` level.

- Good, because it gives interface context for all units and use cases where deemed important
- Good, because it is efficient to maintain since many units and use cases aren't used.
- Good, because it is efficient to complete since many units and use cases aren't used.
