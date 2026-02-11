---
title: "Documentation/CTK Plugin Framework: Embedding the CTK Plugin Framework"
---

This tutorial explains how to embed the CTK Plugin Framework into your existing application/infrastructure.

If you want to know more about how to set-up your CMake build system to integrate CTK, have a look at [Setting up a project}}?action=purge Setting up a project using the CTK Plugin Framework](Setting up a project}}?action=purge Setting up a project using the CTK Plugin Framework)(.

    1. Example Code
Below is a minimal code sample demonstrating how to use the CTK Plugin Framework to get a specific service (we will use the [ctkEventAdmin](ctkEventAdmin)(http://www.commontk.org/docs/html/structctkEventAdmin.html) service in this example):

[UseCTKPluginMain.cpp](UseCTKPluginMain.cpp)(https://github.com/saschazelzer/CTKPluginTutorials/blob/master/Apps/UseCTKPlugin/UseCTKPluginMain.cpp)
syntaxhighlight lang="cpp" filtersections="Main" line url
https://github.com/saschazelzer/CTKPluginTutorials/raw/master/Apps/UseCTKPlugin/UseCTKPluginMain.cpp
/syntaxhighlight

The code makes use of the helper class [ctkPluginFrameworkLauncher](ctkPluginFrameworkLauncher)(http://www.commontk.org/docs/html/classctkPluginFrameworkLauncher.html) to initialize and start the framework. See its documentation to get an overview how to customize this process (you may always initialize and start the framework directly by using the [ctkPluginFrameworkFactory](ctkPluginFrameworkFactory)(http://www.commontk.org/docs/html/classctkPluginFrameworkFactory.html) class and supplying custom framework properties).

We will discuss the code step by step:

; Line 5-7
: The CTK Plugin Framework needs a directory in the local file system for persistent configuration data. By default, the framework uses the organization and application information from the QCoreApplication object to construct a directory name. You can provide a custom path using the framework property [FRAMEWORK_STORAGE](FRAMEWORK_STORAGE)(http://www.commontk.org/docs/html/structctkPluginConstants.html#1f2d6ba0864d0d51d875f8c21e2cc7a6).
; Line 9
: This method call starts the Plugin Framework and installs (if not already installed) and starts the plugin with the given symbolic name. We assume that the plugin is available, otherwise we would have to check the return type of the called method.
; Line 11-13
: The [ctkPluginFrameworkLauncher](ctkPluginFrameworkLauncher)(http://www.commontk.org/docs/html/classctkPluginFrameworkLauncher.html) can be used to get a [ctkPluginContext](ctkPluginContext)(http://www.commontk.org/docs/html/classctkPluginContext.html) which is the only way to interact with the running framework. It allows for example to get a registered service.
; Line 15
: The retrieved service which was registerd by the "org.commontk.eventadmin" plugin during start-up is used by calling a method on it.

    1. Discussion
The [ctkPluginFrameworkLauncher](ctkPluginFrameworkLauncher)(http://www.commontk.org/docs/html/classctkPluginFrameworkLauncher.html) is a useful utility class to start the CTK Plugin Framework. It also allows to get a plugin context (actually the context from the framework itself). However, using this context globally in your application is strongly discouraged. It counteracts the idea of a modularized, service oriented design. You should consider writing your own CTK plugins which will have their own unique context. See [Creating a new CTK Plugin}}?action=purge Creating a new CTK Plugin](Creating a new CTK Plugin}}?action=purge Creating a new CTK Plugin)( for more information.