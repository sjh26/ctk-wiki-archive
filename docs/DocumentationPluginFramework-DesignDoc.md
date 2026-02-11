---
title: Documentation/PluginFramework DesignDoc
---

pre style="font-size:large;color:red"Attention: This document is unfinished!/pre

1. Introduction
In the course of previous discussions and workshops ([link](link)(http://www.commontk.org/index.php/Events)) the CTK group agreed on providing a general plugin/component system. This system should allow for loose coupling between plugins and should provide well designed means of exchanging functionality and data. Further, it should not a priori impose restrictions on the plugins, such that it will be easy to embed existing plugin-infrastructures from existing toolkits/partners.

  1. Purpose of this Document
This document serves as a software design document for the proposed CTK Plugin Framework. CTK members are welcome to add their comments directly on this page or post to ctk-developers@commontk.org.

  1. Scope of this Document
This document describes the architecture of the proposed CTK Plugin Framework and explains the design decisions taken. It also points out features which may be important in the future.

  1. Intended Audience
The intended audience are CTK developers, and to a certain degree CTK users which want to gain more insight into the framework.


1. System Overview
The proposed plugin framework is based on the Qt plugin systemref name="qtpluginsys"[Qt Plugin System](Qt Plugin System)(http://doc.trolltech.com/4.6/plugins-howto.html)/ref and the Service Framework API from Qt Mobility.ref name="qtmob"[Qt Mobility (Service Framework)](Qt Mobility (Service Framework))(http://doc.qt.nokia.com/qtmobility-1.0/index.html)/ref It augments these two systems by adding the following features:

- Plugin meta-data
- A well-defined plugin lifecycle and context
- Integrated service discovery and registration

The plugin framework is developed as a CTK Library ([code](code)(http://github.com/commontk/CTK/tree/master/Libs/PluginFramework/)).

Documentation created from the code can be found here:

- Doxygen generated documentation for the [public API](public API)(http://www.commontk.org/docs/html/classes.html)
- Doxygen generated documentation for [public and internal classes](public and internal classes)(http://docs.mitk.org/ctk-pluginfw-dev/classes.html)

Bleeding edge development concerning the plugin framework happens [here](here)(http://github.com/saschazelzer/CTK). Newly developed features will be merged into the main CTK git repository when they are ready.


1. Design Considerations
The following points should be considered when designing a plugin system for CTK (please comment and/or add points!):

- The system must not impose functional restrictions on plugins.
- Plugins should communicate via well-defined means (services, interfaces, etc.).
- Dependencies between plugins must be handled.
- Plugins should be loadable at runtime

Before writing any new library/framework, it is beneficial to closely look at already existing solutions. One well established modular system for Java applications is specified by the OSGi group.ref name="osgi"[OSGi Service Platform Release 4 Version 4.2 Core Specification](OSGi Service Platform Release 4 Version 4.2 Core Specification)(http://www.osgi.org/Download/Release4V42)/ref Other, more complex solutions like CORBA look interesting at first, but impose too much overhead and add a lot of complexity for the target audience of CTK (in my opinion). On the other hand, Qt Creator uses an elegant, yet simple approach to achieve extensibility.ref name="qtcreator-extensions"[Qt Creator Extensions System](Qt Creator Extensions System)(http://qt.gitorious.org/qt-creator/qt-creator/trees/master/src/libs/extensionsystem)/ref

Other solutions developed independently by members of the CTK consortium handle extensibility very well in the context of their respective applications. However, they usually require the implementation of a specialized interface which may not be suitable in a general context (please add comments or corrections!).

Therefore, general plugin systems (frameworks) like OSGiref name="osgi"/ and to a certain degree the Qt Creator extension system[4](4) seem most suitable as guidelines. They add meta data to plugins (Java archives or shared libraries) by using embedded text files (for example a [.pluginspec](.pluginspec)(http://qt.gitorious.org/qt-creator/qt-creator/blobs/master/src/plugins/cppeditor/CppEditor.pluginspec) file), which may provide the following information about a plugin:

- Name
- Vendor
- License
- Version
- Dependencies

Further, communication between plugins is done by declaring interfaces or providing services rather than using implementation classes directly. The OSGi specifications provide a central service registry which can be used by all plugins to register or discover services. Qt Creator uses a common QObject pool to make implementations for certain interfaces available.

Due to the more general approach of the OSGi module system and its proven reliability and extensibility in large scale and distributed applications (Apache Sling, Eclipse, GlassFish, JBoss, NetBeans, etc.) the design of the proposed CTK plugin framework closely follows those specifications where it makes sense. Hence the system will benefit from ten years of experience gained in the OSGi community and it will be relatively easy for OSGi developers to understand the API of the CTK plugin framework.

The plugin system must also be designed to be able to handle a large amount of plugins. Loading a lot of (potentially) large shared libraries which may execute arbitrary code at load time can impact the initial start of an application drastically. Loading plugins on demand (lazy loading) reduces the start time. However, the system then needs to be able to access the plugin meta-data without loading the plugin itself.


1. Architectural Strategies
The architecture of the proposed plugin framework can be broken up in two main components, the Plugin System itself and the Service Registry. However, those two components are related to each other and their combination at the API level results in a comprehensive and flexible system.

  1. Plugin System
The CTK Core already depends on the QtCore library, hence the CTK plugin framework will be based on the Qt Plugin System.ref name="qtpluginsys"/ The Qt API allows for loading and unloading of plugins at runtime, however, this capability needs to be augmented to enable transparent lazy loading and resolving of dependencies. The meta-data for a plugin could either be distributed as a textfile together with the plugin or be compiled into it. The proposed plugin framework favors the second solution because it avoids the problem of distributing multiple files by using the Qt Resource System. This system makes it easy to embed arbitrary data in a shared library and extract it via a filesystem like API. However, the Qt resources can only be accessed if the plugin is loaded into memory, hence the meta-data should be cached to avoid application load time issues. 

Additionally, the plugin framework should directly support the use of services via a central registry.

  1. Service Registry
The Qt Mobilityref name="qtmob"/ project recently released a Service Framework API as a Qt solution. This service framework allows for [declarative services](declarative services)(http://www.eclipsezone.com/eclipse/forums/t96740.html) and loads the service implementations on demand. To also enable dynamic (non-persistent) services, the Qt Mobility service framework should be used together with a service registry similar to the one described in the OSGi Core Specifications.ref name="osgi"/ Using the Qt API will also enable future out-of-process services (a release for an out-of-process service framework is scheduled for H2 2010 by Nokia).

  1. Memory Management and Binary Compatibility
Due to the direct use of Qt classes in the proposed plugin framework, the Qt architecture and coding style should be used. In detail, this means making use of private implementations to ensure binary compatibility once the API is stable. Further, memory management should be done by using the Qt object hierarchy, smart pointers, or implicit sharing. In the case of using the Qt object hierarchy or raw pointers (if the classes don't inherit from QObject), the class member documentation must clearly state if the caller is responsible for any allocated memory.


1. System Architecture
The proposed CTK plugin framework is designed quite analogous to the OSGi specifications. For application developers, the main entry point is the [PluginFrameworkFactory](PluginFrameworkFactory)(#The PluginFrameworkFactory.md). Plugin developers need to understand the [Plugin*](Plugin*)(#The PluginActivator and PluginContext.md) classes as well as the [ServiceRegistry](ServiceRegistry)(#The ServiceRegistry and related classes.md) and its related classes.

  1. The PluginFrameworkFactory
The [PluginFrameworkFactory](PluginFrameworkFactory)(http://www.commontk.org/docs/html/classctkPluginFrameworkFactory.html) is the main entry point for CTK application developers who want to make use of the plugin framework. It can be used to create a [PluginFramework](PluginFramework)(http://www.commontk.org/docs/html/classctkPluginFramework.html) instance which derives from the [Plugin](Plugin)(http://www.commontk.org/docs/html/classctkPlugin.html) class (see next section). In this sense, the framework itself is a plugin, known as the *System Plugin*.

  1. The PluginActivator and PluginContext
The [PluginActivator](PluginActivator)(http://www.commontk.org/docs/html/classctkPluginActivator.html), [PluginContext](PluginContext)(http://www.commontk.org/docs/html/classctkPluginContext.html), and [Plugin](Plugin)(http://www.commontk.org/docs/html/classctkPlugin.html) classes are the main entry points for plugin developers to the API provided by the framework.

The *PluginActivator* is a Qt interface which must be implemented by each plugin. It is used to customize the starting and stopping of the plugin and to get access to the *PluginContext*.

The *PluginContext* is the execution context for a plugin within the framework. The context allows a plugin to

- Subscribe to events published by the plugin framework
- Register service objects
- Discover and retrieve service objects
- Install new plugins
- Get a list of installed plugins
- Get the *Plugin* object for a plugin

Having such a well defined interface to the framework API for each plugin allows the framework adapting its actions depending on the calling context. In the future this would also allow the implementation of a security model restricting the access to certain framework objects, depending on the access rights of the calling plugin.

  1. The ServiceRegistry and related classes
To be written.

  1. The Plugin Meta-Data Cache
As described in [Strategies / Plugin System](Strategies / Plugin System)(Architectural)(#Plugin System.md) the meta data for a plugin needs to be cached when the data is embedded in the plugin itself. The proposed plugin framework uses a SQLite database via the Qt API to store a modification time stamp for each plugin. When a plugin is installed the first time, it will be loaded and the modification time and its meta data will be added to the database. Additionally, all Qt resources which are accessible under a plugin specific prefix (the plugin symbolic name) are extracted and inserted into the database. Subsequent installations of the same plugin will only load the shared library if the modification time stamp differs.

The meta data can be later on be accessed by using the "getHeaders()" and "getResource*()" methods of the [Plugin](Plugin)(http://www.commontk.org/docs/html/classctkPlugin.html) class.

1. References
references/