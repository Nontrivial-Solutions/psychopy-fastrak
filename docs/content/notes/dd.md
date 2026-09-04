---
title: Data Dictionary 
authors:
  - joe_starr
---

## PsychoPy

### Development

> [!definition] "Routine[](){#DD_RTN}"
>
> A named discrete collection of stimuli and responses over a fixed time frame.

> [!definition] "Stimulus Component[](){#DD_STMCOMP}"
>
> A stimulus component outputs a stimulus (text, sound, light, etc.) to a participant.  

> [!definition] "Response Component[](){#DD_RSPCOMP}"
>
> A response component retrieves a response (keypress, microphone, camera, etc.) from a participant.  
>

> [!definition] "Hardware Device Response[](){#DD_HWDEV}"
>
> A response is an event, formatted data and context, exposed by a [device][DD_DEVICE] and
> subscribed to by components.

> [!definition] "Device[](){#DD_DEVICE}"
>
> A device is a PsychoPy abstraction of a physical hardware device (microphone, keyboard, Fastrak,
> etc.). Device objects (in the programming sense) have two logical flows.
>
> 1. A logical flow used by a [configurator][DD_CFG] to generate an [experiment file][DD_EXPPY].
> 1. A logical flow used during an [experiment][DD_EXP] to control/communicate with the connected hardware.  

> [!definition] "Frame[](){#DD_FRM}"
>
> In a PsychoPy [routine][DD_RTN] components are polled and triggered within an event loop. Steps in
> this even loop are called "frames".

### GUI/Building Experiments

> [!definition] "Configurator[](){#DD_CFG}"
>
> Also called a ["builder"](https://psychopy.org/builder/index.html), used for configuring
> [experiments][DD_TRIAL].

> [!definition] "Component[](){#DD_COMP}"
>
> A [component](https://psychopy.org/builder/components/index.html) is the basic building block of a
> [Routine][DD_RTN].

> [!definition] "Experiment Python File[](){#DD_EXPPY}"
>
> A Python file generated from a [configurator][DD_CFG] containing the executable
> [experiment][DD_EXP].

> [!definition] "Experiment[](){#DD_EXP}"
>
> A collection of ordered and/or [looped](https://psychopy.org/builder/flow.html#loops) routines.

## General

> [!definition] "Wrapper[](){#DD_WRAP}"
>
> A collection of code that exposes other code with new interfaces.
> [See Wikipedia](https://en.wikipedia.org/wiki/Wrapper_function).

> [!definition] "Driver[](){#DD_ID_008}"
> 
> A computer program that defines how to control physical hardware.
> [See Wikipedia](https://en.wikipedia.org/wiki/Device_driver)
