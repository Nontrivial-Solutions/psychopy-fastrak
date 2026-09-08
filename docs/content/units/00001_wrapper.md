---
title: Fastrak Component Hardware Wrapper 
authors:
  - joe_starr
date: 2026-07-13
---

## Description

This unit describes the functionality of the Fastrak component hardware wrapper. The class offers a
simple interface for the Fastrak hardware device to be used in an experiment.

### Members

#### Public Data

##### Status

The `status` is an expected interface for all components in an experiment. The status is essentially
an enum of possible states a component can be in. The status is essentially an enum of possible
states a component can be in. Unfortunately, PsychoPy doesn't use an actual enum for this purpose
but instead a [SimpleNamespace](https://docs.python.org/3/library/types.html#types.SimpleNamespace).

##### Is Streaming

The `is_streaming` memeber indicates if the wrapped hardware device is streaming.

#### Private Data

- device: A reference to the hardware device that is being wrapped.
- outputPath: The path where the collected data will be stored.  
- hasDeviceLock: Indicates if this component wrapper instance holds the lock on the hardware
    device. Allows multiple components to interact with the same hardware device.
- counter: Counts the number of data collection sessions this component has completed.  

### Interfaces

#### Constructor

The constructor method takes in a collection of data:

- device: The hardware device to wrap.
- outputDir: The output directory for data collected by this wrapper.

##### State Machine

```mermaid
stateDiagram-v2
    state "Initalize members" as im
    state "Set state to not started" as ss 
    [*] --> im
    im --> ss
    ss --> [*]

```

#### Reset

Since wrapper instances are reused between routine instances ([ADR 00004](../../madr/00004_reuse/))
to simplify how this works we reset the state of the wrapper instead of recreate the wrapper.

Takes an optional `outputDir` as an argument allowing for the wrapper to save to a different
location.

##### State Machine

```mermaid
stateDiagram-v2
    state "Clear buffer" as ss 
    state "Set does not have lock" as unl 
    state "Emit error" as err 
    state is_streaming <<choice>> 
    state has_lock <<choice>> 
    state hardware_ulock <<choice>> 
    [*] --> has_lock
    has_lock --> is_streaming: Has device lock
    has_lock --> err: Does not have device lock
    is_streaming --> ss: Is not streaming
    is_streaming --> err: Is streaming
    ss --> hardware_ulock
    hardware_ulock --> unl: Hardware lock released 
    hardware_ulock --> err: Hardware lock not released
    unl --> [*]
    err --> [*]

```

#### Dispatch Messages

PsychoPy has a built-in hardware component messaging service. These services must be polled to
publish state to the "bus".

##### State Machine

```mermaid
stateDiagram-v2
    state "Dispatch messages in hardware" as ss 
    [*] --> ss 
    ss --> [*]
```

#### Startup

The `startup` method sets the state of the wrapped hardware device to the correct settings.
Additionally, acquires a lock on the wrapped device.

##### State Machine

```mermaid
stateDiagram-v2
    state "Run hardware setup" as ss 
    state "Set does have lock" as unl 
    state "Emit error" as err 
    state has_lock <<choice>> 
    state hardware_lock <<choice>> 
    [*] --> has_lock
    has_lock --> hardware_lock: Does not have device lock
    has_lock --> err: Has device lock
    hardware_lock --> ss: Hardware lock acquired 
    hardware_lock --> err: Hardware lock not acquired 
    ss --> unl
    unl --> [*]
    err --> [*]

```

#### Start Stream

The `startStream` method commands the wrapped hardware device to enter streaming mode.

##### State Machine

```mermaid
stateDiagram-v2
    state "Start stream" as ss 
    state "Emit error" as err 
    state is_streaming <<choice>> 
    state has_lock <<choice>> 
    [*] --> has_lock
    has_lock --> is_streaming: Has device lock
    has_lock --> err: Does not have device lock
    is_streaming --> ss: Is not streaming
    is_streaming --> err: Is streaming
    ss --> [*]
    err --> [*]
```

#### End Stream

The `endStream` method commands the wrapped hardware device to exit streaming mode.

##### State Machine

```mermaid
stateDiagram-v2
    state "End stream" as ss 
    state "Await end of stream" as  aeos 
    state "Emit error" as err 
    state is_streaming <<choice>> 
    state has_lock <<choice>> 
    [*] --> has_lock
    has_lock --> is_streaming: Has device lock
    has_lock --> err: Does not have device lock
    is_streaming --> ss: Is streaming
    is_streaming --> err: Is not streaming
    ss --> aeos
    aeos --> [*]
    err --> [*]
```

#### Save Stream

The `saveRecording` method ends the current streaming session (if active) and saves the last
streaming session data to the configured file.  

Takes two optional arguments with types:

- `Experiment`: Metadata object containing the context of the current experiment. If present we
    use the `dataFileName` attribute for naming the output file.
- `Path`: An output base directory. Defaults to the `./data` directory.

> [!note]
> 
> Output path attribute determines where the file should be stored. The data file name is controlled
> by the stream session counter attribute as well as any naming data from the experiment reference
> passed to the save `saveRecording` method.

##### State Machine

```mermaid
stateDiagram-v2
    state "Create ouput file name" as ss 
    state "End stream"as es 
    state "Save data" as sd 
    state "Increment counter" as ic 
    state "Emit error" as err 
    state is_streaming <<choice>> 
    state has_lock <<choice>> 
    [*] --> has_lock
    has_lock --> is_streaming: Has device lock
    has_lock --> err: Does not have device lock
    is_streaming --> ss: Is not streaming
    is_streaming --> es: Is streaming
    es --> ss
    ss --> sd
    sd --> ic
    ic --> [*]
    err --> [*]
```

