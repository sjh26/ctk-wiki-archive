---
title: Documentation/CTK Plugin Framework: Introduction
---

The CTK Plugin Framework can shortly be described as a dynamic component system for C++.

  1. Design
The design of the CTK Plugin Framework (see also the [Document](Document)(Design)(Documentation/PluginFramework_DesignDoc.md)) is heavily inspired by [OSGi](OSGi)(http://www.osgi.org) (a dynamic component system for Java) and enables
a development model where applications are (dynamically) composed of many different (reusable) components. This model
allows to communicate through *services*, which are objects that are specifically shared between components.

The framework's layered model is illustrated in Figure 1, containing:
[1: Layered Model of the CTK Plugin Framework](1: Layered Model of the CTK Plugin Framework)(frame|Figure)(File:PluginFWLayering.png.md)
- Plugins - Plugins are the CTK components created by the developers.
- Services Layer - Connects plugins in a dynamic way by offering a publish-find-bind model for C++ objects.
- Life Cycle Layer - The API to install, start, stop, update, and uninstall plugins.
- Security - Handles security aspects (not available yet)
A more detailed explanation of these concepts can be found below.

  1. Plugins
A CTK Plugin is, at it's core, a shared library based on the [Qt Plugin](Qt Plugin)(http://doc.qt.nokia.com/latest/plugins-howto.html) system.
Additionally, symbols in CTK libraries are by default hidden across all platforms. This is the first step towards *modularity*,
which is about keeping things local and not shared. The less things you share, the less wrong assumptions can be made. However, without
sharing there can be no collaboration. CTK Plugins usually only share symbols (classes and functions) to support the CTK *services* model.

  1. Services
A collaborative model in C++ is usually realized with the use of factory patterns. Different toolkits use different patterns and API
to access such a factory. Very often, influencing the decision about which implementation is used by the factory is non-trivial. Further, the
implementation code can usually not advertise its availability, nor can the user list the possible implementations and pick the most suitable
one. Factories are also in general not dynamic, once an instance of an implementation is registered, it can not be withdrawn. Finally, if
many different factories are in use, there is no centralized overview of the implementations to which your code is bound.

One solution to these issues is the CTK *service registry*. A plugin can create an object and register it with the CTK service registry under
one or more *interfaces* (an interface is a C++ class with usually only pure virtual methods). Other plugins can ask the registry to list all services (objects)
that are registered under a specific interface. A plugin may even wait for a specific service to appear and then get a call back.

A plugin can therefore *register* a service, it can *get* a service, and it can *listen* for a service to appear or disappear.
An arbitrary number of plugins can register services under the same interface, and any number of plugins can get the same service, see Figure 2.
[2: Registering and getting a service](2: Registering and getting a service)(frame|100px|Figure)(File:CTKService.png.md)
If multiple plugins register objects under the same interface, they can be distinguished by their *properties*. Each service registration has a set of
standard and custom properties. You can use an expressive filter language to select only the services in which you are interested. Properties can
also be used for other roles at the application level.

Since services are dynamic, a plugin can decide to withdraw its service from the registry while other plugins are still using it. Plugins using such
a service must then ensure that they no longer use the service object and drop any pointers to it. This may sound like a significant
additional complexity at first, but using helper classes like [ctkServiceTracker](ctkServiceTracker)(http://www.commontk.org/docs/html/classctkServiceTracker.html) and a
framework like Declarative Services (to be developed) can make this process straight-forward and the gained advantages are quite large.
The dynamic nature of services allows to install and uninstall plugins on the fly while other plugins stay functional. It also models real world
problems closer because most often, such problems are not static. For example in a distributed environment a service could model a connection end-point
and if the connection to the remote machine is gone, the service can be withdrawn. Further, the dynamics solve the initialization problem. Applications
using CTK Plugins do not require a specific start ordering in their plugins.

Though the service registry accepts any QObject-based object as a service, the best way to achieve reuse is to register these objects under (standard)
interfaces to decouple the implementation from the client code. Hence the CTK Plugin Framework provides a number of standard interfaces which are
designed closely to the service specifications published in the [OSGi Service Platform Release 4 Compendium Specification](OSGi Service Platform Release 4 Compendium Specification)(http://www.osgi.org/Specifications/HomePage).
These standard services are described in detail in the specification and on this Wiki.

  1. Deployment
The CTK Plugin Framework can be used as the main container for all your application logic, but it can also be embedded in your existing framework.
The management of the framework is standardized by providing a simple API allowing plugins to install, start, stop, and update other plugins,
as well as enumerating the plugins and their service usage. This API
can be used by so-called *management agents* to control the Plugin Framework. Management agents can be as diverse as command shells, rich
graphical desktop applications, or an AJAX-application.

  1. Benefits
The CTK Plugin Framework is based on OSGi principles and APIs. As such, it inherits a very mature and thoroughly designed component system that
is used in the Java world to build highly complex applications. It brings those benefits to native (Qt based) C++ applications. The following list
is taken from [Benefits of Using OSGi](Benefits of Using OSGi)(http://www.osgi.org/About/WhyOSGi) and adapted to the CTK context.

; Reduced Complexity
: Developing with the CTK Plugin Framework means developing plugins. They hide their internals from other plugins and communicate through well defined *services*. Hiding internals means more freedom to change later. This not only reduces the number of bugs, it also makes plugins simpler to develop because correctly sized plugins implement a piece of functionality through well defined interfaces.
; Reuse
: The standardized component model makes it very easy to use third party components in an application.
; Real World
: The CTK Plugin Framework is dynamic. It can update plugins on the fly and services can come and go. There are a surprising number of real world scenarios that match this dynamic service model. Applications can therefore reuse the powerful primitives of the service registry (register, get, list with an expressive filter language, and waiting for services to appear and disappear) in their own domain. This not only saves writing code, it also provides global visibility, debugging tools, and more functionality than would have implemented for a dedicated solution. Writing code in such a dynamic environment sounds like a nightmare, but fortunately, there are support classes and frameworks that take most, if not all, of the pain out of it. 
; Easy Deployment
: The CTK Plugin Framework is not just a standard for components. It also specifies how components are installed and managed. This API can be used by plugins to provide a management agent. This management agent can be as simple as a command shell, a graphical desktop application, a cloud computing interface for Amazon's EC2, or an IBM Tivoli management system. The standardized management API makes it very easy to integrate the CTK Plugin Framework in existing and future systems. 
; Dynamic Updates
: The used OSGi component model is a dynamic model. Plugins can be installed, started, stopped, updated, and uninstalled without bringing down the whole system. 
; Adaptive
: The used OSGi component model is designed from the ground up to allow the mixing and matching of components. This requires that the dependencies of components need to be specified and it requires components to live in an environment where their optional dependencies are not always available. The service registry is a dynamic registry where plugins can register, get, and listen to services. This dynamic service model allows plugins to find out what capabilities are available on the system and adapt the functionality they can provide. This makes code more flexible and resilient to changes.
; Transparency
: Plugins and services are first class citizens in the CTK Plugin environment. The management API provides access to the internal state of a plugin as well as how it is connected to other plugins. Parts of the applications can be stopped to debug a certain problem, or diagnostic plugins can be brought in.
; Versioning
: In the CTK Plugin Framework, all plugins are carefully versioned and only plugins that can collaborate are wired together.
; Simple
: The CTK Plugin API is surprisingly simple. The core API is less than 25 classes. This core API is sufficient to write plugins, install them, start, stop, update, and uninstall them and includes all listener classes. 
; Lazy
: Lazy in software is good and the used OSGi technology has many mechanisms in place to do things only when they are really needed. For example, plugins can be started eagerly, but they can also be configured to only start when another plugin is using them. Services can be registered but only created when they are used. These kind of lazy scenarios can save tremendous runtime costs. 
; Humble
: The CTK Plugin Framework does not take over your whole application. You can choose to expose the provided functionality to just parts of your application, or even run multiple instances of the framework inside the same process.
; Non Intrusive
: Applications (plugins) in a CTK Plugin environment are left to their own. They can use any facilities without the framework restricting them. There is no special interface required for CTK services, every QObject can act as a service and every class (also non-QObject based) can act as an interface.