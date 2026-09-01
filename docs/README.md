---
title: Fastrak PsychoPy Plugin 
authors:
  - joe_starr
---

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![White Logo image](https://brainmade.org/white-logo.svg){width=10%}](https://brainmade.org)

![hero](./infra/assets/logo.svg){width=100%}

/// caption

///

## Note to Reader

### What Am I?

This repository contains [PsychoPy](https://psychopy.org) plugin tooling to enable use of the
[Polhemus Fastrak](https://polhemus.com/all-trackers/fastrak) in experiments.

### About the Documentation

The following document describes the "rules" and expectation for development. The
["API Reference"](./reference//) page contains the technical context descriptions found in the
source files. The ["Use Cases"](./content/usecase/usecase) page contains a collection of use cases
and a use case diagram for the tool. The ["Decisions"](./content/madr/) page contains a collection
of [architectural decision records](https://adr.github.io/madr/) [@Kopp2018] giving context on why
this tool is the way it is.

### Issues

If you discover an issue with this repository or have a question, please feel free to open an issue.
I've included templates for the following issues:

- 🖋️ Spelling and Grammar: Found some language that is incorrect?
- 🤷 Clarity: Found a section that just makes no sense?
- ❓ Question: Do you have a general question?
- 🐞 Bug: Found an error in the code?
- 🚀 Enhancement: Have a suggestion for improving the toolchain?

[:fontawesome-solid-paper-plane: Open Issue!](https://github.com/Joecstarr/itt_2_plpath_converter/issues/new/choose){ .md-button }

## 📃 Cite Me

## ⚖️ License

## Planning and Administration

### Tasks

Tasks are tracked as GitHub issues.

### Version Control

The toolchain shall be kept under Git versioning. Development shall take place on branches with
`main` on GitHub as a source of truth. GitHub pull requests shall serve as the arbiter for inclusion
on main with the following quality gates:

- Running and passing the unit test suite.
- Running and passing linting and style enforcers.
- Successful generation of documentation.

#### Release Tagging

The project shall be tagged when a new feature or bug fix is merged into main. The tag shall follow
[semantic versioning](https://semver.org) for labels.

```text
vMAJOR.MINOR.PATCH
```

### Project Structure

Files and directories shall be lower case, where capital is not required by a tool, and contain no
`' '`.

```text
📁 .
├── 📁 .github
│   ├── 📁 ISSUE_TEMPLATE
│   ├── 📁 PULL_REQUEST_TEMPLATE
│   ├── 📁 workflows
│   └── 📝 pull_request_template.md
├── 📁 .vscode
│   └── ⚙️ launch.json
├── 📁 docs
│   ├── 📁 content
│   │   ├── 📁 madr
│   │   └── 📁 units
│   ├── 📁 infra
│   └── 📖 README.md
├── 📁 psychopy_fastrak 
│   ├── 📁 component 
│   ├── 📁 hardware 
│   ├── 📁 wrapper 
│   └── 🐍 __init__.py
├── 📁 test 
│   ├── 📁 component 
│   ├── 📁 hardware 
│   ├── 📁 wrapper 
│   ├── 🐍 test_<unit>.py 
│   └── 🐍 __init__.py
├── ⚙️ .editorconfig
├── 🙈 .gitignore
├── 🛠️ .pre-commit-config.yaml
├── ⚙️ .rumdl.toml
├── ❄️ flake.lock
├── ❄️ flake.nix
├── 🛠️ Justfile
├── 📜 LICENSE
├── 📄 mkdocs.yml
├── 🐍 pyproject.toml
└── 🔒 uv.lock
```

### Directories of Interest

- docs: This directory contains the high level documentation for the tool.
- psychopy_fastrak : This directory contains the source code of the tool.
- test: This directory contains the test code of the tool.
- .github: This directory contains the GitHub infrastructure.  
- .vscode: This directory contains the debugger configuration.  

### Define a Unit

A unit shall be a Python module.

### Quality

The tool and its units shall fail-safe, that is the tool and its units can fail, but the failure
must be detectable. A segfault is okay, an off by one error that computes the wrong value is not.

#### Unit Testing

Each internal unit shall have a unit test suite.

#### Integration Testing

The plugin shall have manual integration testing.

### Requirements

Each internal unit shall have a unit test suite.

#### Use Cases

Requirements are documented by [ADR](./content/madr/index.md). Use cases are omitted as they follow
the PsychoPy plugin design requirements.

##### Architectural Decisions

Architectural decisions [MADR](<https://github.com/adr/madr>) [@Kopp2018] serve as the primary
documentation for architectural decisions.

The following is the order of operations for the proposal of a MADR:

1. Create a branch for a proposal with the name:

    ```text
    proposal-{{short title}}
    ```

1. Create a pull request with this template.
1. In the branch create a Markdown file based on the
    [MADR Template](https://github.com/adr/madr/blob/4.0.0/template/adr-template.md). Name the
    Markdown file:

    ```text
    {{issue# padded to five digits}}-{{title}}
    ```

1. When a decision is made change the status to:
    - "accepted" and pull the branch into main branch
    - "rejected" and pull the branch into main branch

#### Nonfunctional Requirements

##### Colors

Diagrams included in documentation for features (use case and unit descriptions) are expected to use
the [COLORS](https://clrs.cc) color palette.

##### Technologies

###### Languages and Frameworks

- git
- Python
- PsychoPy
- mermaid.js
- prek
- tombi
- rumdl
- ruff
- uv
- MADR[@Kopp2018]

###### Documentation of Implementation

###### Code Style Guide

Python code shall be formatted with ruff using the included style settings. Markdown files shall be
formatted with rumdl using the included style settings. TOML files shall be formatted with tombi
using the included style settings.

## Design and Documentation

### System

#### Block Diagram

```mermaid
flowchart LR
    subgraph External
    fsd@{ shape: paper-tape, label: "Fastrak Serial Driver"}
    psy@{ shape: paper-tape, label: "PsychoPy Core Configurator"}
    psyr@{ shape: paper-tape, label: "PsychoPy Core Runner"}
    ec@{ shape: paper-tape, label: "External Component"}
    gen@{ shape: docs, label: "Generated Code"}
    gen---|*..1|psyr
    end

    subgraph Internal 
    subgraph Component 
    cm["PsychoPy Component"]
    db["Device Backend"]
    cm -- uses -->db
    cm -- creates -->gen
    end
    subgraph Hardware 
    bhd["Base Hardware Device"]
    res["Device Response"]
    bhd-- uses -->res
    ec-- consumes -->res
    bhd-- uses -->fsd
    end
    subgraph Wrapper 
    dw["Device Wrapper"]
    dw-- uses -->bhd
    end

    cm---|*..1|psy
    db---|*..1|psy
    bhd---|*..1|psyr
    dw---|*..1|gen
    end



```

#### Class Diagram

```mermaid
classDiagram

BaseDeviceComponent <|-- FastrakComponent
DeviceBackend <|-- FastrakDeviceBackend
BaseResponse <|-- FastrakResponse
BaseResponseDevice <|-- FastrakHardwareDevice
FastrakWrapper --> FastrakHardwareDevice 
FastrakResponse--> FastrakHardwareDevice 
FastrakDeviceBackend --> FastrakComponent 
FastrakComponent --> FastrakWrapper


class FastrakWrapper {
+ int status
+ bool is\_streaming
- init(device, outputDir) 
+ reset(outputDir) 
+ dispatchMessages() 
+ startup() 
+ startStream() 
+ endStream() 
+ saveRecording(thisExp, baseDir)
}

class FastrakHardwareDevice {
+ bool is\_locked
- init() 
- getStation(station) 
- getBaud(baud)
+ isSameDevice(other) 
+ getAvailableDevices()
+ dispatchMessages(clear)
+ startup() 
+ clearBuffer() 
+ startStream() 
+ endStream() 
+ lock() 
+ unlock() 
}

class FastrakResponse {
}

class FastrakDeviceBackend {
- init(profile) 
+ writeDeviceCode(buff) 
}

class FastrakComponent {
- init(exp, parentName, name, startType, startVal, stopType, stopVal, deviceLabel)
- writeJinjaCode(buff , params, tmpltSource) 
- blockComment(buff , content) 
+ writeStartCode(buff)
+ writeInitCode(buff) 
+ writeRoutineStartCode(buff) 
+ writeFrameCode(buff) 
+ writeRoutineEndCode(buff) 
}

```
