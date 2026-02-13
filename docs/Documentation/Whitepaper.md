---
title: Documentation/Whitepaper
---

*This document describes thoughts as of approximately 2009.  A restatement of our plans is presented in the [CTK Roadmap Document](../CTK-Roadmap.html)*

1. Overview
*This is open for discussion!*

The purpose of this whitepaper is to provide a general framework for the development of CTK. It gives an overview of
 
- Goals
- Development strategy
- Design
- Toolkit parts
- Technical infrastructure 
- Implementation roadmap

1. Goals
(to be discussed)

The goals of the CommonTK are to:

- provide a unified set of basic features for use in medical imaging
- facilitate the exchange and combination of developments
- avoid duplicate developments
- continuously extend to new tasks within the scope of the toolkit (medical imaging) without growing source-code-wise for existing tasks
- integrate and adapt successful solutions

1. Development strategy
(to be discussed)

The development of the CommonTK has to face several challenges:

- Several large development efforts already exist.
- Research and development in medical imaging can have different foci and therefore pose different requirements on a toolkit.
- The participants in the common effort have to agree on design issues.
- When using the CommonTK, changes within existing code will be inevitable, which is not attractive for developers.

The CommonTK effort faces these challenges by defining a development strategy.

  1. Modular design with small core and loose coupling
The CommonTK will be highly modular and very loose coupling between the modules whenever possible. This will make it possible to use only small parts of it within existing developments or complement CTK code with proprietary code.

  1. Use parts of CTK within the developments of the CTK founders soon
To demonstrate (and verify) the possibility to integrate CTK code and their commitment to CTK, the founders should use parts of CTK within their software and toolkit developments soon.

In case that some functionality of an existing toolkit of a founder (e.g. the logging mechanism of toolkit Y) is provided to the CommonTK, it should be use from the CTK from then on (i.e., toolkit Y should use the logging mechanism from CTK and remove its own - which will be (almost) identical to CTKs).

  1. Interface design / review /decision process
Open question: how can we effectively agree on interfaces without getting into a cumbersome process of reviewing everything by everyone?

1. Design
(based on [Architecture](../Documentation/Architecture.html) and workshop results)

  1. BSD style license
The Common Toolkit shall have a BSD-style license to put no restrictions on the user and allow commercial use. Therefore contributed and used libraries must have a compatible license.

  1. C++
The main language of the Common Toolkit will be C++.

  1. Qt
Since all of the main contributors to the Common Toolkit already use Qt or plan to use Qt it was agreed on using it as a GUI Toolkit and also for non-GUI tasks like cross-platform database access. 

  1. CMake
CMake will be used as build automation tool.

**Proposal: Package system **

CTK should be organized in packages, like in a Linux distribution package system. This would make it possible to check out only parts of the source code: faster checkout, less code, proabably resulting in higher acceptance of the toolkit.

The packages should have well defined dependencies. The process of getting source code for the packages that are needed could be automated.

Possibly the package system can be implemented with CMake.

1. Toolkit parts
  1. Common data structures
The Common Toolkit will provide some basic data structures to allow interface design and data exchange between modules. 
One goal will be to use a common scene representation (see [wiki:ctkScene]).

Comments: (to be discussed)

The data structures have to be carefully designed to allow integration with existing toolkits. Duplication of memory should be avoided. 

It may even be possible to refrain from defining actual data classes (as a class for storing images like vtkImageData) for the DICOM-IO part: The IO module could stream the data to adaptor classes that create the actual data objects. These adaptor classes can be written by the CTK users.

In a later step CTK might define its own data classes using the same mechanism. Possible types for that could be:

- Image
- Surface
- Scene or scene graph
- Pipeline 
- Data repository (like MRML, mitk::!DataStorage)

  1. Logging
A central logging interface should be defined in the core and used throughout the toolkit.

  1. DICOM database support
The DICOM support part of the Common Toolkit will cover different aspects:

    1. WG23 implementation
The Common Toolkit will provide a C++ reference implementation of a WG23 plugin.

    1. Broad DICOM support
The Common Toolkit will support more DICOM datatypes like surfaces, segmentations etc. 

    1. DICOM GUI
GUI components like patient/study browser 

  1. Plugin support
The Common Toolkit should support different kinds of plugins to extend applications without recompile.

- IO adapters (shared object, dll): Support for special file formats could be provided by IO adapters 
- algorithms / filter (shared object, dll): Support for adding algorithms and filters
- command line plugins: Some generic command line interface to allow all kinds of plugins
- GUI modules: Complete GUI (Qt) modules which perform some end-user task and can be integrated as modules in the application

  1. Scripting engines
The Common Toolkit should support application scripting. The scripting language and the wrapping mechanism are still to be defined. Things to evaluate: Qt Script for Applications (ECMA Script), Python (!PyQt, !PythonQt) 

  1. XML files to exchange scene graphs and pipelines
To exchange scene descriptions, scene graphs and pipelines a XML file format has to defined.

  1. GUIs
The Common Toolkit will contain packages that provide widgets. GUIs should be skinnable.

The focus will be on Qt-based widgets (see WidgetPlans). 

A Qt-based GUI will *not* be mandatory for applications based on CTK. Support for other GUI toolkits might be added in a later phase.

  1. Integrated Development Environments (IDEs)
The scope of CTK will include IDEs (e.g. a visual programming environment) and tools for IDEs. Usage of these will not be required for using other CTK modules.

1. Technical infrastructure
  1. Wiki / repository / testing / cdash?
Who will be responsible for / who will pay for maintaining the basic development infrastructure?

  1. Package system
Is CMake as-it-is the adequate solution for this? Maybe some moderate extensions will be necessary, e.g. more than one level of grouping in the GUI.

1. Implementation Roadmap
**To be defined**: modules and packages to be started in the next 6 months.