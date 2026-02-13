---
title: "Documentation/CTK Plugin Framework: Getting Started"
---

**This page is not updated anymore. Please go to [Plugin_Framework](../Documentation/Plugin-Framework.html)**

The CTK Plugin Framework is directly based on the OSGi specifications, hence any material explaining OSGi also applies to CTK (without the Java specifics, of course). You may want to read the [Introduction](../Documentation/CTK-Plugin-Framework-Introduction.html) to get a high-level overiew about the framework.

    1. CTK Plugin Tutorials
This is a list of existing (or planned) tutorials:

- [ Setting up a project using the CTK Plugin Framework]
- [ Embedding the CTK Plugin Framework in an existing application]
- Starting and configuring the Framework
- [Creating a new CTK Plugin](../Documentation/CTK-Plugin-Framework-Creating-a-new-CTK-Plugin.html)
- Listen to service events

    1. CTK Plugin Documentation
CTK provides default implementations for some OSGi specifications and other functionality.

The following list points to the sub-projects inside the CTK Plugin Framework. Sub-projects are either implementations of certain functionality in plug-ins (e.g. OSGi Compendium Service Specifications) or distinct functionality inside the CTK Plugin Framework library.

      1. OSGi Compendium Services
- [MetaType Service](../Documentation/CTK-Plugin-MetaType.html) `{{Done}}` [ [Chapter 105, Service Compendium Version 4.2](http://www.osgi.org/Download/File?url=/download/r4v42/r4.cmpn.pdf) ]
- [Event Admin (local event bus)](../Documentation/CTK-Plugin-EventAdmin-local.html) `{{Done}}` [ [Chapter 113, Service Compendium Version 4.2](http://www.osgi.org/Download/File?url=/download/r4v42/r4.cmpn.pdf) ]
- [Event Admin (remote event bus)](../Documentation/CTK-Plugin-EventAdmin-remote.html) `{{Doing}}` [ [Chapter 113, Service Compendium Version 4.2](http://www.osgi.org/Download/File?url=/download/r4v42/r4.cmpn.pdf) ]
- [Config Admin](../Documentation/CTK-Plugin-ConfigAdmin.html) `{{Done}}` [ [Chapter 104, Service Compendium Version 4.2](http://www.osgi.org/Download/File?url=/download/r4v42/r4.cmpn.pdf) ]
- [Log Service](../Documentation/CTK-Plugin-Log.html) `{{Doing}}` [ [Chapter 101, Service Compendium Version 4.2](http://www.osgi.org/Download/File?url=/download/r4v42/r4.cmpn.pdf) ]

    1. API Documentation
The [API documentation](http://www.commontk.org/docs/html/group__PluginFramework.html) is also a good place to learn more about the CTK Plugin Framework capabilities.

    1. OSGi Tutorials
There are many OSGi tutorials for the major OSGi frameworks ([Equinox](http://www.eclipse.org/equinox), [Knopflerfish](http://www.knopflerfish.org), and [Apache Felix](http://felix.apache.org)) on the web. The principles are the same and can be applied to CTK.

You may also want to read [Neil Bartlett's free book on OSGi](http://njbartlett.name/osgibook.html), which is available as a preview draft. You can skip the first 20 pages about Java class dependencies and read the rest of Part I. Basically everything described in Part I applies to the CTK Plugin Framework.

    1. Specifications
The original [OSGi specifications](http://www.osgi.org/Release4/Download) are a great read for detailed technical information about the plugin framework itself and the provided interfaces and implementations for the compendium services. The CTK Plugin Framework is based on OSGi Release 4 Version 4.2, with some API inspired by the upcoming Version 4.3.