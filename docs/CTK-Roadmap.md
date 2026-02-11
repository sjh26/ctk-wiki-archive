---
title: CTK-Roadmap
render_with_liquid: false
---


This page contains the roadmap for the core CTK effort. It is intended as a guideline for participants to decide whether their intended contributions fit into the CTK core. Beginning in 2012, CTK events are open to all who are willing to comply with the following two conditions:

*Participate for the entire event (no one-day stands)
*Qualifications and intent to write code for the CTK core roadmap (code writers only).


  1. Background
*This roadmap was developed during the [Antipolis 2011 Hackfest](Antipolis 2011 Hackfest)(Sophia)(CTK-Hackfest-Nov-2011.md)
*The roadmap is based on an earlier version which can be found [here](here)(Documentation/Whitepaper.md) and ideas for an overview which can be found in the [ CTK Integration Levels Table]( CTK Integration Levels Table)(CTK_Integration_Levels_Overview.md).

  1. Overview
The goal of CTK is to support biomedical image computing.  Other application areas can benefit from CTK, but the needs of other domains will not guide the selection of CTK priorities (efforts to sway development in support of more generalized goals will be resisted).

The tools used in CTK are Qt, DCMTK, CMake, C++, and Python.  C++, Qt, and CMake are essential in all CTK uses, and DCMTK is essential for all DICOM uses.  Python wrapping can optionally be applied on top of CTK code.  Other relevant technologies will be considered but are unlikely to be included.  Some support for ITK, VTK, OpenInventor, and related toolkits is optionally supported in terms of adapters and interfaces but CTK is not a place to house, for example, a set of algorithms implemented in ITK.

CTK code is licensed under [Apache 2.0](Apache 2.0)(http://www.apache.org/licenses/LICENSE-2.0.html). This means that users of CTK are allowed use the code for academic, commercial, or other purposes without paying license fees or being restricted in their ability to redistribute their code or keep it private.  Absolutely no GPL, academic-use-only, non-free, or patented code belongs in CTK, but CTK can be used in projects that also include this kind of code.
 
CTK works on topics that are not covered by existing toolkits that support the mutual interest and needs of the CTK community.  The scope of current CTK efforts includes:
- Biomedical, Medical and visualization customizations of Qt in the form of widgets, testing, and support code
- DICOM Networking including Qt wrappers around DCMTK classes 
- DICOM Application Hosting
- Build system to support CTK
- PythonQt and related support
- Plugin Framework
- EventBus

Topics other than those listed above may be considered in the future if they meet the 'mutual interest and need' criterion -- anything that is too specialized or too application specific does not belong in CTK.

The scope of CTK does **not** include:
- CTK does not do GPU computing
- CTK does not implement image processing algorithms
- CTK only supports the technologies explicitly called out above -- some of us may love ObjectiveC or Lua, but they have no place in CTK
- CTK cannot commit to implementing all or even a majority of the DICOM specification -- priorities will be defined by the needs and abilities of the CTK participants.

  1. Short Term Action Items
The community can expect the following from CTK:

CTK will deliver an integrated set of DICOM Networking and Application Hosting widgets, libraries, demo programs and related support to developers of biomedical image computer applications using tools that are compatible with the CTK technologies and usable from C++ or Python.

During 2012, CTK expects to deliver a series of 0.x releases for use in applications.  Because the API and technology will continue to evolve, these will not be considered 1.x releases but will be stable and tested enough for use in application level code and inclusion in, for example, OS distributions such as debian.

Consistent with the technical targets, CTK software is expected to evolve in terms of API and structure.  Some unused or little used dependencies will be removed (such as log4qt) and other CTK elements may be split into sub libraries.  For example the Qt widgets that are not visualization or biomedical imaging specific may be split into a distinct repository so that they can be used in non-biomedical applications with minimal dependencies and excess source code.

  1. Five Year Goals
Likely deliverables over 5 years given current efforts:
- Enable code sharing at a variety of levels
- Become a mechanism (for example through DICOM Application Hosting) for interoperability of algorithms across applications.
- Become the standard mechanism for solving problems in our domain, meaning that if a developer were to implement a Qt application that needed DICOM support it would be unthinkable not to use CTK.
- Be professional in our software development:
** CTK will be tested
** CTK will be documented
** CTK developers will provide community minded and participatory support
** CTK's web site and communication efforts will give a clear picture of our goals and status

Possible developments over the 5 years if sufficient support is available:
- Extension of CTK to related biomedical standards (such as a clearly defined subset of IHE)
- Support for scene data interchange beyond dicom images (surface models, colors, transformations, annotations) 

  1. Getting in Touch
Additional details are available on the [commontk.org](commontk.org)(http://commontk.org) site.

Feel free to contact ctk-developers@commontk.org for more information.  Your feedback is welcome.

