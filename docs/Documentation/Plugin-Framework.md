---
title: Documentation/Plugin Framework
---

The CTK Plugin Framework can shortly be described as a dynamic component system for C++. It is directly based on the [OSGi](http://www.osgi.org) specifications, hence any material explaining OSGi also applies to CTK (without the Java specifics, of course).

    1. Introduction
Being based on an industry standard like OSGi brings the benefits of stabilized APIs and specifications directly to the CTK Plugin Framework. Making use of the experience and dedicated work of highly skilled architects enables us to concentrate on the implementation instead of doing tedious iterations of the API design.

Start reading the [introduction to the scope and features](../Documentation/CTK-Plugin-Framework-Introduction.html) of the Plugin Framework.

See the original [design document](../Documentation/PluginFramework-DesignDoc.html) for the initial requirements.

    1. Specifications
The original [OSGi specifications](http://www.osgi.org/Release4/Download) are a great read for detailed technical information about the plugin framework itself and the provided interfaces and implementations for the compendium services. The CTK Plugin Framework is based on OSGi Release 4 Version 4.2, with some API inspired by the upcoming Version 4.3.

    1. Documentation
If you are new to OSGi, consider reading [Neil Bartlett's free book on OSGi](http://njbartlett.name/osgibook.html) (skip the first 20 pages and read the rest of Part I). To get a quick overview how to use parts of the CTK Plugin Framework API, you can view this [Technical Introduction](../MediaCTKPluginFrameworkIntro.pdf.html).

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
- [Setting up a project using the CTK Plugin Framework](../Documentation/CTK-Plugin-Framework-Setting-up-a-project.html)
- [Embedding the CTK Plugin Framework in an existing application](../Documentation/CTK-Plugin-Framework-Embedding-the-CTK-Plugin-Framework.html)
- Starting and configuring the Framework
- [Creating a new CTK Plugin](../Documentation/CTK-Plugin-Framework-Creating-a-new-CTK-Plugin.html)
- Listen to service events
- The CTK-Plugin Framework in CAS Applications ([Tutorial](https://github.com/transbite/CTK_CAS_Tutorial/blob/master/TheCTK-PluginFrameworkinCASApplications-ATutorial.pdf), [source code](https://github.com/transbite/CTK_CAS_Tutorial))

|bgcolor="#CCCCCC"|
|valign="top"|

span style="color: #555555; font-size: 18px; font-weight: bold;"Service Implementations/span
----
OSGi Compendium Service Specifications already implemented or being worked on:
- [MetaType Service](../Documentation/CTK-Plugin-MetaType.html) `{{Done}}` [ [Chapter 105](http://www.osgi.org/Download/File?url=/download/r4v42/r4.cmpn.pdf) ]
- [Event Admin (local event bus)](../Documentation/CTK-Plugin-EventAdmin-local.html) `{{Done}}` [ [Chapter 113](http://www.osgi.org/Download/File?url=/download/r4v42/r4.cmpn.pdf) ]
- [Event Admin (remote event bus)](../Documentation/CTK-Plugin-EventAdmin-remote.html) `{{Doing}}` [ [Chapter 113](http://www.osgi.org/Download/File?url=/download/r4v42/r4.cmpn.pdf) ]
- [Config Admin](../Documentation/CTK-Plugin-ConfigAdmin.html) `{{Done}}` [ [Chapter 104](http://www.osgi.org/Download/File?url=/download/r4v42/r4.cmpn.pdf) ]
- [Log Service](../Documentation/CTK-Plugin-Log.html) `{{Doing}}` [ [Chapter 101](http://www.osgi.org/Download/File?url=/download/r4v42/r4.cmpn.pdf) ]

|bgcolor="#CCCCCC"|
|valign="top"|

span style="color: #555555; font-size: 18px; font-weight: bold;"External Documentation/span
----
- [API Documentation](http://www.commontk.org/docs/html/group__PluginFramework.html)

A free preview draft about OSGi. Skip the first 20 pages about Java class dependencies and read the rest of Part I.

- [Neil Bartlett's free book on OSGi](http://njbartlett.name/osgibook.html)

Java implementations which provide several tutorials (Java specific)

- [Equinox](http://www.eclipse.org/equinox)
- [Knopflerfish](http://www.knopflerfish.org)
- [Apache Felix](http://felix.apache.org)

|}