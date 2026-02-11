---
title: Debian Packaging
render_with_liquid: false
---


1. Status
There is an experimental debian package here: http://packages.qa.debian.org/c/ctk.html

The current Debian sources for CTK are here: http://anonscm.debian.org/viewvc/debian-med/trunk/packages/ctk/trunk/debian/

Some experimental changes are published here: https://github.com/nolden/ctk-debian and https://github.com/nolden/CTK/commits/debian-patches *Update 11/05/2013:* everything from here has been merged upstream, apart from the DCMTK workarounds, see [below](below)(#DCMTK.md).


  1. Related Issues and Pull Requests on Github
[RESOLVED](RESOLVED) https://github.com/commontk/CTK/issues/65 

[RESOLVED](RESOLVED) https://github.com/commontk/CTK/pull/158

  1. Working configuration
*Updated 11/05/2013*

This is a working subset (possibly not complete) of CTK that builds with Debian Unstable, use this as an initial cache

pre
CTK_APP_ctkCommandLineModuleExplorer:BOOL=ON
CTK_APP_ctkDICOM:BOOL=ON
CTK_APP_ctkPluginBrowser:BOOL=ON
CTK_APP_ctkPluginGenerator:BOOL=ON
CTK_BUILD_QTDESIGNER_PLUGINS:BOOL=ON
CTK_ENABLE_DICOM:BOOL=ON
CTK_ENABLE_PluginFramework:BOOL=ON
CTK_ENABLE_Python_Wrapping:BOOL=ON
CTK_ENABLE_Widgets:BOOL=ON
CTK_LIB_CommandLineModules/Backend/FunctionPointer:BOOL=ON
CTK_LIB_CommandLineModules/Backend/LocalProcess:BOOL=ON
CTK_LIB_CommandLineModules/Core:BOOL=ON
CTK_LIB_CommandLineModules/Frontend/QtGui:BOOL=ON
CTK_LIB_CommandLineModules/Frontend/QtWebKit:BOOL=ON
CTK_LIB_Core:BOOL=ON
CTK_LIB_DICOM/Core:BOOL=ON
CTK_LIB_DICOM/Widgets:BOOL=ON
CTK_LIB_PluginFramework:BOOL=ON
CTK_LIB_Visualization/VTK/Core:BOOL=ON
CTK_LIB_Visualization/VTK/Widgets:BOOL=ON
CTK_LIB_Widgets:BOOL=ON
CTK_PLUGIN_org.commontk.configadmin:BOOL=ON
CTK_PLUGIN_org.commontk.eventadmin:BOOL=ON
CTK_PLUGIN_org.commontk.log:BOOL=ON
CTK_PLUGIN_org.commontk.metatype:BOOL=ON
CTK_PLUGIN_org.commontk.plugingenerator.core:BOOL=ON
CTK_PLUGIN_org.commontk.plugingenerator.ui:BOOL=ON
CTK_SUPERBUILD:BOOL=OFF
DCMTK_DIR:PATH=/usr
/pre

  1. Proposed package structure
 /usr/lib/:
   # CTK libraries
   libCTKCore.so
   libCTKDICOM.so
   ...
 /usr/lib/ctk-plugins/:
   # CTK plugin framework plugins
   liborg_commontk_eventadmin.so
   liborg_commontk_dah_core.so
   ...
 /usr/lib/x86_64-linux-gnu/qt4/plugins/designer/:
   # Qt designer plugins
   libCTKWidgetsPlugins.so
   libCTKDICOMWidgetsPlugins.so
   ...
 /usr/include/ctk/:
   # all public library headers
   ctkUtils.h
   ctkComboBox.h
   ctkDICOMDatabase.h
   ...
 /usr/include/ctk/org.commontk.dah.core/: 
   # public plugin headers
   ctkDicomAppInterface.h
   ...
 /usr/bin:
   # executables (separate package "ctk" or "ctk-utils"?)
   ctkDICOM
   ctkCommandLineModuleExplorer

  1. Open issues
- CTK side
** installation of CMake files: make CTKConfig.cmake and UseCTK.cmake relocatable (after some cleanup), see also https://github.com/commontk/CTK/pull/158#issuecomment-6955188
*** For examples, see [commontk/DCMTK@f461865d](commontk/DCMTK@f461865d)(https://github.com/commontk/DCMTK/commit/f461865d1759854db56e4c840991c81c77e45bb9) and [python-cmake-buildsystem@3f504d8b](python-cmake-buildsystem@3f504d8b)(https://github.com/davidsansome/python-cmake-buildsystem/commit/3f504d8be5b41086f615494517ddd2cf66f4d365)
*** CMake wiki page: http://www.cmake.org/Wiki/CMake/Tutorials/How_to_create_a_ProjectConfig.cmake_file
** make DGraph work for external projects without a CTK source tree
** test whether CTK CMake macros work with an installation tree depicted above
** install support for Qt plugins and CTK plugins
- Debian side
** do we want to create separate packages for the various topics? (libctk-core, libctk-dicom, libctk-cli, ... )
** currently the installation paths are changed in the debian/rules files, e.g. removing the "ctk-0.1" part of the path. Is that ok or should we try to solve this as well upstream?
** should we wait for the 3.6.1 experimental package to enter "sid" or try to create some workarounds in CTK and/or the Debian package?
** if the Debian rules map files from the install tree to a different directory layout in the Debian package, how is this going to play well together with CTKConfig.cmake?

  1. Dependencies with potential problems
    1. ITK
ITK 4 in Debian has limited architecture support:

http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=724711

The ITK package also recently [added a dependency](added a dependency)(http://anonscm.debian.org/viewvc/debian-med/trunk/packages/insighttoolkit/trunk/debian/control?r1=15674r2=15675) to an older version of DCMTK. Currently we assume CTK will use the new DCMTK package which is still in experimental.

We need ITK for the ttCTK_LIB_ImageProcessing/ITK/Core/tt setting. The options are
- disable the option and move the class to Slicer or other packages needing it
- enable the option conditionally on supported platform
- create separate packages for CTK, so most packages can be supported on all platforms

    1. DCMTK
CTK is using a recent snapshot in the superbuild, but Debian includes the latest stable release 3.6.0 . Since the Bologna Hackfest in December 2012 CTK builds (again) with DCMTK 3.6.0, using one backported class that is included conditionally (scu.cc)

*Update 11/05/2013:* 
- using CTK master and the Debian sid (3.6.0) package you need two patches that would be much more complicated to integrate upstream since the would be specific to Debian
- using the Debian experimental package (3.6.1) everything works fine, you have to provide tt-DDCMTK_DIR:PATH=/usr/tt to the initial CMake run 

    1. Log4Qt
Log4Qt is in general not used by CTK anymore. There is one plugin left using it but this is more of a technical study and can be turned of:

preCTK_PLUGIN_org.commontk.log4qt:BOOL=OFF/pre

*Update 11/05/2013:* This plugin is outdated will be removed soon, so we should probably remove all related code from the debian package rules 

    1. PythonQt
Several patches have been submitted to upstream, some are left, a summary can be found here. If this is resolved more features of CTK can be enabled for the Debian package.

*Update 11/05/2013:* one header is missing: ctkAbstractPythonManager.cpp:31:33: fatal error: PythonQt_QtBindings.h .

    1. VTK
CTK Visualization Core compiles with VTK 5.8, just missing one small functionality.

There is an issue with VTK linking which is not totally clear, see 

http://debian.2.n7.nabble.com/Bug-747436-libvtk6-Libraries-are-possibly-underlinked-td3249140.html

    1. QtSoap
There is a debian package called libqtsolutions-soap-2.7-1, but there is no development package so it's unclear if this can be useful.

*Update 11/05/2013:* libqtsolutions-soap-2.7-1 is probably not useful. In the CTK context QtSoap is currently only needed for DICOM application hosting which itself is highly experimental and should probably be omitted from an initial debian package anyway

