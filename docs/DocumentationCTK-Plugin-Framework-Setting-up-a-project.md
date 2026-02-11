---
title: "Documentation/CTK Plugin Framework: Setting up a project"
---

This tutorial will show you how to set-up your own project using the CMake build system and how to integrate it with the CTK Plugin Framework.

The described set-up will allow for an arbitrary number of applications and CTK plug-ins, contained in one project.

      1. Project Layout
[1 Example Project Layout](1 Example Project Layout)(frame|Fig.)(File:CTKPluginProject_Layout.png.md)
A possible project layout is shown in Fig. 1. It contains one application (UseCTKPlugin) and one plug-in (org.mydomain.serviceeventlistener). The code for the application and different plug-ins is explained in other tutorials. We will cover only the three CMakeLists.txt files seen in Fig. 1.

      1. Top-Level CMake File
The top-level CMakeLists.txt file is in charge of finding CTK and Qt4. You can add any CMake commands you want, the only requirement for a CTK Plugin integration is the availability of CTK and Qt4 (by using FIND_PACKAGE). You can have a look at an example file by clicking on the CMakeLists.txt link below. We will discuss two important parts of this file in more detail:

[CMakeLists.txt](CMakeLists.txt)(https://github.com/saschazelzer/CTKPluginTutorials/blob/master/CMakeLists.txt)
syntaxhighlight lang="cmake" line sectionmarker="|\s*#gt;|" filtersections="Extract all" url
https://github.com/saschazelzer/CTKPluginTutorials/raw/master/CMakeLists.txt
/syntaxhighlight

To be able to take advantage of CTKs sophisticated dependency checking system inside your own build system, you need to write a small CMake macro called *GetMyTargetLibraries*. It is used as a callback inside CTKs own CMake macros and functions to distinguish between targets being build in your project and targets external to your project (e.g. targets coming from CTK). It works by taking a list of target names and filtering out the names belonging to your own project using regular expressions. You can use as many regular expressions as you want in the call to *ctkMacroListFilter*, between *_tmp_list* and *OUTPUT_VARIABLE*.

The second important part is the invocation of a special CMake macro from CTK which takes care of the heavy lifting. 

[CMakeLists.txt](CMakeLists.txt)(https://github.com/saschazelzer/CTKPluginTutorials/blob/master/CMakeLists.txt)
syntaxhighlight lang="cmake" line sectionmarker="|\s*#gt;|" filtersections="Create a list" url
https://github.com/saschazelzer/CTKPluginTutorials/raw/master/CMakeLists.txt
/syntaxhighlight

We first create a list containing one entry for each plug-in in the *Plugins* directory. Each entry consists of the directory name containing the plug-in followed by a *:* and the default build option value. This list is then passed to the *ctkFunctionSetupPlugins* function, which executes the following steps:

- Create a CMake option for each given plug-in. You can customise the option name with a prefix by supplying "BUILD_OPTION_PREFIX *MyPrefix*" as the last arguments to the function (*MyPrefix* defaults to BUILD_).
- Generate a dependency graph of your plug-ins and external dependencies (other plug-ins and libraries).
- Validate the dependencies of enabled plug-ins. If one of your own plug-ins depends on other plug-ins in your project, they will be automatically enabled. Unsatisfied external dependencies will result in a CMake configuration error.
- Add the subdirectories of enabled plug-ins.

This completes the integration of your CTK plug-ins in your CMake build system.

      1. Application Integration
The [CMakeLists.txt](CMakeLists.txt)(https://github.com/saschazelzer/CTKPluginTutorials/blob/master/Apps/CMakeLists.txt) file inside the *Apps* directory is not required to use any CTK specific CMake code. In the described set-up it just adds a build option for our *CTKUsePlugin* application and adds its directory to be parsed by CMake.

Here is an example CMake file for our *CTKUsePlugin* application which needs to call methods in the CTK Plugin Framework library:

[CMakeLists.txt](CMakeLists.txt)(https://github.com/saschazelzer/CTKPluginTutorials/blob/master/Apps/CTKUsePlugin/CMakeLists.txt)
syntaxhighlight lang="cmake" line url
https://github.com/saschazelzer/CTKPluginTutorials/raw/master/Apps/UseCTKPlugin/CMakeLists.txt
/syntaxhighlight

This is standard CMake code, adding the CTK include directories and linking the application to the CTK Plugin Framework library *CTKPluginFramework*.

      1. Plugin CMake File
Plug-ins external to CTK are build exactly the same way as plug-ins contained within the CTK project itself. An example CMakeLists.txt file for a plug-in named *org.mydomain.serviceeventlistener* is shown below:

[CMakeLists.txt](CMakeLists.txt)(https://github.com/saschazelzer/CTKPluginTutorials/blob/master/Plugins/org.mydomain.serviceeventlistener/CMakeLists.txt)
syntaxhighlight lang="cmake" line url
https://github.com/saschazelzer/CTKPluginTutorials/raw/master/Plugins/org.mydomain.serviceeventlistener/CMakeLists.txt
/syntaxhighlight

The *PROJECT* command in line one sets the name for your plugin sub-project. Additionally, this name is used as the target name for the shared library and should be globally unique. A good convention is to use the reverse domain scheme for the project name and also for the directory containing the plug-in code. Note that the project name must not contain periods.

Calling the macro *ctkMacroBuildPlugin* will do the heavy lifting and set-up all include paths and library dependencies. The definition of plug-in dependencies and the usage of this macro is covered in the [Creating a new CTK Plugin}}?action=purge Creating a new CTK Plugin](Creating a new CTK Plugin}}?action=purge Creating a new CTK Plugin)( tutorial.

      1. Related Tutorials
- [Creating a new CTK Plugin}}?action=purge Creating a new CTK Plugin](Creating a new CTK Plugin}}?action=purge Creating a new CTK Plugin)(
- [Embedding the CTK Plugin Framework}}?action=purge Embedding the CTK Plugin Framework](Embedding the CTK Plugin Framework}}?action=purge Embedding the CTK Plugin Framework)(