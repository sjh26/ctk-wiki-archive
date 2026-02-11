---
title: Documentation/Plugin Framework
render_with_liquid: false
---

The CTK Plugin Framework can shortly be described as a dynamic component system for C++. It is directly based on the [OSGi](OSGi)(http://www.osgi.org) specifications, hence any material explaining OSGi also applies to CTK (without the Java specifics, of course).

    1. Introduction
Being based on an industry standard like OSGi brings the benefits of stabilized APIs and specifications directly to the CTK Plugin Framework. Making use of the experience and dedicated work of highly skilled architects enables us to concentrate on the implementation instead of doing tedious iterations of the API design.

Start reading the [ introduction to the scope and features]( introduction to the scope and features)(Documentation/CTK_Plugin_Framework:_Introduction .md) of the Plugin Framework.

See the original [ design document]( design document)(Documentation/PluginFramework_DesignDoc .md) for the initial requirements.

    1. Specifications
The original [OSGi specifications](OSGi specifications)(http://www.osgi.org/Release4/Download) are a great read for detailed technical information about the plugin framework itself and the provided interfaces and implementations for the compendium services. The CTK Plugin Framework is based on OSGi Release 4 Version 4.2, with some API inspired by the upcoming Version 4.3.

    1. Documentation
If you are new to OSGi, consider reading [Neil Bartlett's free book on OSGi](Neil Bartlett's free book on OSGi)(http://njbartlett.name/osgibook.html) (skip the first 20 pages and read the rest of Part I). To get a quick overview how to use parts of the CTK Plugin Framework API, you can view this [ Technical Introduction]( Technical Introduction)(Media:CTKPluginFrameworkIntro.pdf .md).

Below you will find more information about specific topics.

{| border="0" align="center" width="98%" valign="top" cellspacing="7" cellpadding="2"
|-
! width="33%"|
! |
! width="33%"|
! |
! width="33%"|
|- 
|valign="top"|
span style="color: #555555; font-size: 18px; font-weight: bold;"Tutorials/span
----
This is a list of available or planned tutorials:
- [up a project using the CTK Plugin Framework](up a project using the CTK Plugin Framework)(Setting)(Documentation/CTK_Plugin_Framework: Setting up a project.md)
- [the CTK Plugin Framework in an existing application](the CTK Plugin Framework in an existing application)(Embedding)(Documentation/CTK_Plugin_Framework: Embedding the CTK Plugin Framework.md)
- Starting and configuring the Framework
- [ Creating a new CTK Plugin]( Creating a new CTK Plugin)(Documentation/CTK_Plugin_Framework: Creating a new CTK Plugin .md)
- Listen to service events
- The CTK-Plugin Framework in CAS Applications ([Tutorial](Tutorial)(https://github.com/transbite/CTK_CAS_Tutorial/blob/master/TheCTK-PluginFrameworkinCASApplications-ATutorial.pdf), [source code](source code)(https://github.com/transbite/CTK_CAS_Tutorial))

|bgcolor="#CCCCCC"|
|valign="top"|

span style="color: #555555; font-size: 18px; font-weight: bold;"Service Implementations/span
----
OSGi Compendium Service Specifications already implemented or being worked on:
- [ MetaType Service]( MetaType Service)(Documentation/CTK_Plugin_MetaType .md) {{Done}} [ [Chapter 105]( [Chapter 105)(http://www.osgi.org/Download/File?url=/download/r4v42/r4.cmpn.pdf) ]
- [ Event Admin (local event bus)]( Event Admin (local event bus))(Documentation/CTK_Plugin_EventAdmin_local .md) {{Done}} [ [Chapter 113]( [Chapter 113)(http://www.osgi.org/Download/File?url=/download/r4v42/r4.cmpn.pdf) ]
- [ Event Admin (remote event bus)]( Event Admin (remote event bus))(Documentation/CTK_Plugin_EventAdmin_remote .md) {{Doing}} [ [Chapter 113]( [Chapter 113)(http://www.osgi.org/Download/File?url=/download/r4v42/r4.cmpn.pdf) ]
- [ Config Admin]( Config Admin)(Documentation/CTK_Plugin_ConfigAdmin .md) {{Done}} [ [Chapter 104]( [Chapter 104)(http://www.osgi.org/Download/File?url=/download/r4v42/r4.cmpn.pdf) ]
- [ Log Service]( Log Service)(Documentation/CTK_Plugin_Log .md) {{Doing}} [ [Chapter 101]( [Chapter 101)(http://www.osgi.org/Download/File?url=/download/r4v42/r4.cmpn.pdf) ]

|bgcolor="#CCCCCC"|
|valign="top"|

span style="color: #555555; font-size: 18px; font-weight: bold;"External Documentation/span
----
- [API Documentation](API Documentation)(http://www.commontk.org/docs/html/group__PluginFramework.html)

A free preview draft about OSGi. Skip the first 20 pages about Java class dependencies and read the rest of Part I.

- [Neil Bartlett's free book on OSGi](Neil Bartlett's free book on OSGi)(http://njbartlett.name/osgibook.html)

Java implementations which provide several tutorials (Java specific)

- [Equinox](Equinox)(http://www.eclipse.org/equinox)
- [Knopflerfish](Knopflerfish)(http://www.knopflerfish.org)
- [Apache Felix](Apache Felix)(http://felix.apache.org)

|}