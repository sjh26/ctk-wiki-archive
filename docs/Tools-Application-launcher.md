---
title: "Tools: Application launcher"
---

`{{banner`
| text = [For the latest version of this page, visit the CTkAppLauncher README on GitHub.](https://github.com/commontk/AppLauncher#readme)}}

![Application Launcher Logo](images/Commontk_applauncher.png)


    1. What is CTK Application Launcher ?
CTK Application launcher is a lightweight open-source utility allowing to set environment before starting a real application. The launcher is available on Linux, Windows and MacOSX.

    1. Getting started
You could either:
- download the [pre-built binaries](https://github.com/commontk/AppLauncher/releases) matching your operating system `{{note-with-icon-only}}`See [](unnamed.html#Why-should-I-used-the-pre-build-binaries-?)''

or 

- [build](Tools-Application-launcher/Build-Instructions.html) from the source


See also [](unnamed.html#How-to-integrate-the-launcher-in-my-existing-project-?)''

    1. How does CTK Application Launcher work ?
The launcher looks for a setting file where the path of the real application and its associated environment variable are reported. While setting the environment and loading the real application, it can also display a splash screen.

The settings file follows the format as specified here: https://doc.qt.io/qt-5/qsettings.html#Format-enum


** Settings file location **

The launcher successively looks for a setting file located either in the current directory or in *bin* and *lib* subdirectories. 
The setting file should match the following pattern *LAUNCHERNAMELauncherSettings.ini*

For example:
pre
 /home/jchris/Projects/AwesomeApp
 /home/jchris/Projects/bin/AwesomeApp-real
 /home/jchris/Projects/bin/AwesomeAppLauncherSettings.ini
 /home/jchris/Projects/lib/libFoo.so
/pre


** Setting file description **

The setting file should have the following format:
pre
[General]
launcherSplashImagePath=bin/Splash.png
launcherSplashScreenHideDelayMs=1000

[Application]
path=bin/AwesomeApp-real
arguments=--multithreading-enabled

[Paths]
1\path=./bin
size=1

[LibraryPaths]
1\path=./lib
size=1

[EnvironmentVariables]
FOO_DIRS=APPLAUNCHER_DIR/libPATHSEP/usr/local/lib
/pre

Note that the special strings **PATHSEP**, **APPLAUNCHER_NAME** and **APPLAUNCHER_DIR** will be expanded by the launcher to match the current context.


** Launcher command line arguments **

As described below, the launcher also provides a broad set of command line arguments.

pre
jchris@karakoram:~/Projects/CTK-AppLauncher-Debug/bin $ ./CTKAppLauncher --launcher-help
Usage
  CTKAppLauncher [options]

Options
  --launcher-help                Display help
  --launcher-verbose             Verbose mode
  --launch                       Specify the application to launch
  --launcher-detach              Launcher will NOT wait for the application to finish
  --launcher-no-splash           Hide launcher splash
  --launcher-timeout             Specify the time in second before the launcher kills the application. -1 means no timeout (default: -1)
  --launcher-generate-template   Generate an example of setting file
/pre

    1. Why should you use CTK Application Launcher ?
- Very easy to configure
- Standalone executable
- Available on Windows, linux and MacOSX
- Thoroughly tested


    1. How to integrate the launcher in my existing project ?
      1. Superbuild
- Integrate the [external project definition](Tools-Application-launcher/external-project-definition.html)
- Use the macro **ctkAppLauncherConfigure** as described below
pre
    INCLUDE(${CTKAPPLAUNCHER_DIR}/CMake/ctkAppLauncher.cmake)
    INCLUDE(${Slicer_CMAKE_DIR}/SlicerCTKAppLauncherSettings.cmake)

    ctkAppLauncherConfigure(

      TARGET SlicerQT-real

      APPLICATION_INSTALL_SUBDIR ${Slicer_INSTALL_BIN_DIR}
      APPLICATION_NAME Slicer

      SPLASH_IMAGE_PATH ${Slicer_SOURCE_DIR}/Applications/SlicerQT/Resources/Images/SlicerSplashScreen.png
      SPLASH_IMAGE_INSTALL_SUBDIR ${Slicer_INSTALL_BIN_DIR}
      SPLASHSCREEN_HIDE_DELAY_MS 3000

      ADDITIONAL_HELP_SHORT_ARG "-h"
      ADDITIONAL_HELP_LONG_ARG "--help"
      ADDITIONAL_NOSPLASH_LONG_ARG "--no-splash"

      DESTINATION_DIR ${Slicer_BINARY_DIR}

      LIBRARY_PATHS_BUILD "${SLICER_LIBRARY_PATHS_BUILD}"
      PATHS_BUILD "${SLICER_PATHS_BUILD}"
      ENVVARS_BUILD "${SLICER_ENVVARS_BUILD}"

      LIBRARY_PATHS_INSTALLED "${SLICER_LIBRARY_PATHS_INSTALLED}"
      PATHS_INSTALLED "${SLICER_PATHS_INSTALLED}"
      ENVVARS_INSTALLED "${SLICER_ENVVARS_INSTALLED}"
      )

    install(PROGRAMS "${Slicer_BINARY_DIR}/Slicer${CMAKE_EXECUTABLE_SUFFIX}" DESTINATION ".")

    install(
      FILES "${Slicer_SOURCE_DIR}/Applications/SlicerQT/Resources/Images/SlicerSplashScreen.png" 
      DESTINATION ${Slicer_INSTALL_BIN_DIR}
      )

    install(
      FILES "${Slicer_BINARY_DIR}/SlicerLauncherSettingsToInstall.ini" 
      DESTINATION ${Slicer_INSTALL_BIN_DIR}
      RENAME SlicerLauncherSettings.ini
      )
/pre

1. Links for Developers
{| cellspacing="20"
|- style="vertical-align:top;"
|| [![Commontk build](images/Commontk_build.png)](Tools-Application-launcher/Build-Instructions.html)
|| [![Commontk sourcecode](images/Commontk_sourcecode.png)](http://github.com/commontk/AppLauncher)
!--
|| [![Commontk dashboard](images/Commontk_dashboard.png)](http://my.cdash.org/index.php?project=CTKAppLauncher)
|| [![commontk ideas](images/Commontk_ideas.png)](Tools-Application-launcher/Project-Ideas.html)
--
|| [![Commontk bug](images/Commontk_bug.png)](http://github.com/commontk/AppLauncher/issues)
|- style="text-align:center; font-size: large"
|| [Build Instructions](Tools-Application-launcher/Build-Instructions.html)
|| [Source Code](http://github.com/commontk/AppLauncher)
!--
|| [Source Code's br/Quality Dashboard](http://my.cdash.org/index.php?project=CTKAppLauncher)
|| [Project Ideas](Tools-Application-launcher/Project-Ideas.html)
--
|| [Report a problem](http://github.com/commontk/AppLauncher/issues)
|}

!--

1. Links for Dashboard Maintainers
{| cellspacing="20"
|- style="vertical-align:top;"
|| [![Commontk dashboard setup](images/Commontk_dashboard_setup.png)](CTKAppLauncherDashboard-setup.html)
|- style="text-align:center; font-size: large"
|| [Dashboard setup](Tools-Application-launcher/Dashboard-setup.html)
|}

--

1. Known issues
- Windows: Timeout option doesn't work properly

1. Frequently Asked Questions
  1. Why should I used the pre-build binaries ?
If you distribute the AppLauncher along with your Qt application and if there is a chance that Qt libraries are not installed on the host system, you will probably also distribute Qt libraries along with your package. For that reason, you will prefer using the pre-built binaries since they are statically linked against Qt.