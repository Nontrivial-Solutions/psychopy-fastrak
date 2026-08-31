---
title: 00007 Code Generation Style/Handling  
authors:
  - joe_starr
status: deprecated
date: 2026-08-31
---

## Context and Problem Statement

A Psychopy component is essentially a code generator. When an experiment is "generated" (turned into
an executable python script) the plugin supplies a string which is inserted into an experiment
outline and then generated into a python (or JS) file.

This ADR decides how to handle the code generation within the plugin.

## Decision Outcome

Write standalone Jinja2 templates.

## Decision Drivers  

- Must be easy to maintain.
- Must be easy to test.

## Considered Options

- Use python string replacement or `f` strings
- Write standalone Jinja2 templates
- Write internal Jinja2 templates
- Have a simple (one line) template that calls into a lower level component directly.  

## Use Python String Replacement or `f` Strings

This is the strategy used by built in PsychoPy components.

- Bad, because it would induce large change sets in the source files within git.  
- Bad, because the files would be unlintable.  
- Bad, because testing low level code would require generation.  

### Write Standalone Jinja2 Templates

For this option we would write a collection of standalone Jinja2 templates. One template for each
component interface. The template would contain the python code needed to call into a backend 6DOF
device.

- Good, because the files would be easy to store in git.  
- Good, because the files would be lintable.  
- Bad, because testing low level code would require generation.  

### Write Internal Jinja2 Templates

For this option we would write a Jinja2 template inline within the plugin source. The template would
contain the python code needed to call into a backend 6DOF device.

- Bad, because it would induce large change sets in the source files within git.  
- Bad, because the files would be unlintable.  
- Bad, because testing low level code would require generation.  

### Have a Simple (One Line) Template That Calls into a Lower Level Component Directly

In this option a simple one line callback would be generated. All functionality would be handled by
a submodule.

- Good, because the functional files would be plain Python.  
- Good, because the changes to backends (add/modify device) would induce no changes in the plugin
    generation code.  
- Good, because testing low level code would an easy unit test.
- Bad, because it requires python to be in a known state (must include the plugin).
