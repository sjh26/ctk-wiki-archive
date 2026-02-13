---
title: CTK In QtDesigner
---

1. Instructions to load CTK widgets in Qt Designer
#Set the **QT_PLUGIN_PATH** environment variable to the *.../CTK-build/CTK-build/bin* path (that should contains a *designer* folder).
#:You might also have to add into the path the CTK plugins dependencies:
#:: Set the **LD_LIBRARY_PATH** (or **PATH** on Windows) environment variable to the *.../CTK-build/CTK-build/bin* (suffixed by Release on Windows) path (that should contains files such as *libCTKCore.so* or *libCTKWidgets.so*)
#:: If you built CTK with the VTK option, then you also need to add in your **LD_LIBRARY_PATH** (or **PATH** on Windows) environment variable the path to the VTK libraries (e.g. VTKCommon.dll). Those files are typically located in *.../CTK-build/VTK-build/bin[/Release]*.
#:: And if you built CTK with QtTesting, you also need to add the QtTesting-build/bin directory into your path environment variable.
#:: Don't forget that on Windows, folders are separated using '\' and not '/'
#Then you can start QtDesigner
#:You can troubleshoot by opening the "Help - About Plugins" dialog within QtDesigner.
#:You can also troubleshoot library dependencies (- what is missing in your LD_LIBRARY_PATH or PATH) by using ldd on linux or "Dependency Walker" on Windows.

1. Instructions to load CTK widgets in Qt Creator
    1. Links
*QtCreator plugins: http://qt-project.org/doc/qtcreator-2.6/adding-plugins.html
*Dependency walker: http://www.dependencywalker.com/