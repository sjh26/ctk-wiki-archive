---
title: Documentation/BuildSystem Description
---

[Back to CTK Documentation](../Documentation.html)

1. Overview
CTK is a toolkit composed of three different kinds of modules:
- Libraries
- Plugins 
- Applications

Based on set of custom CMake macros and functions, CTK buildsystem allows to make the developer easier and increase its productivity.

Each one of these modules may have specific dependencies (like VTK, Log4Qt, QtMobility, ... ). CTK buildsystem provides the ability to checkout and build these external projects only if required. 
Note also that in some case, the developer want to use a local build of a given external project, this is also possible specifying the proper variable when CMake is invoked.

In addition to external projects, libraries, applications and plugins may also have inter dependencies.

1. Specifying dependencies
Based on Superbuild, CTK is build in two steps:
- 1) Checkout and build external dependencies 
- 2) Build CTK itself using the external dependencies build at step 1

In order to checkout the expected external project, the developer need to specify which module he wants to build at "configuration time" before even executing step1.
Moreover, if application X is enabled, all dependent plugins, libraries, etc .. need to be enabled.

It means, dependencies of a given CTK module need to be done at time of step 1. To achieve that, dependencies of each module are specified within a file named *target_libraries.cmake*.

For example, the content of file CTK/Libs/Visualization/VTK/Core/target_libraries.cmake is the following:
pre
#
1. See CMake/ctkMacroGetTargetLibraries.cmake
1. 
1. This file should list the libraries required to build the current CTK libraries
#

SET(target_libraries
  VTK_LIBRARIES
  CTKCore
  )
/pre

In this example, the library codeCTKVisualizationVTKCore/code depends on codeCTKCor/code and the also external project codeVTK_LIBRARIES/code. 

On the other hand, the file allowing to specify VTK external project (CTK/CMakeExtermals/VTK.cmake) look like:
pre
superbuild_include_once()

set(proj VTK)

set(${proj}_DEPENDENCIES "")

superbuild_include_dependencies(PROJECT_VAR proj)

if(${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj})
  unset(VTK_DIR CACHE)
  find_package(VTK REQUIRED NO_MODULE)
endif()

1. Sanity checks
if(DEFINED VTK_DIR AND NOT EXISTS ${VTK_DIR})
  message(FATAL_ERROR "VTK_DIR variable is defined but corresponds to non-existing directory")
endif()

if(NOT DEFINED VTK_DIR AND NOT ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj})

  set(revision_tag v5.10.0)
  if(${proj}_REVISION_TAG)
    set(revision_tag ${${proj}_REVISION_TAG})
  endif()

  set(location_args )
  if(${proj}_URL)
    set(location_args URL ${${proj}_URL})
  elseif(${proj}_GIT_REPOSITORY)
    set(location_args GIT_REPOSITORY ${${proj}_GIT_REPOSITORY}
                      GIT_TAG ${revision_tag})
  else()
    set(location_args GIT_REPOSITORY "${git_protocol}://vtk.org/VTK.git"
                      GIT_TAG ${revision_tag})
  endif()

  set(additional_vtk_cmakevars )
  if(MINGW)
    list(APPEND additional_vtk_cmakevars -DCMAKE_USE_PTHREADS:BOOL=OFF)
  endif()

  if(CTK_LIB_Scripting/Python/Core_PYTHONQT_USE_VTK)
    list(APPEND additional_vtk_cmakevars
      -DPYTHON_EXECUTABLE:PATH=${PYTHON_EXECUTABLE}
      -DPYTHON_LIBRARIES:FILEPATH=${PYTHON_LIBRARIES}
      -DPYTHON_DEBUG_LIBRARIES:FILEPATH=${PYTHON_DEBUG_LIBRARIES}
      )
  endif()

  ExternalProject_Add(${proj}
    ${${proj}_EXTERNAL_PROJECT_ARGS}
    SOURCE_DIR ${CMAKE_BINARY_DIR}/${proj}
    BINARY_DIR ${proj}-build
    PREFIX ${proj}${ep_suffix}
    ${location_args}
    UPDATE_COMMAND ""
    INSTALL_COMMAND ""
    CMAKE_CACHE_ARGS
      ${ep_common_cache_args}
      ${additional_vtk_cmakevars}
      -DVTK_WRAP_TCL:BOOL=OFF
      -DVTK_USE_TK:BOOL=OFF
      -DVTK_WRAP_PYTHON:BOOL=${CTK_LIB_Scripting/Python/Core_PYTHONQT_USE_VTK}
      -DVTK_WRAP_JAVA:BOOL=OFF
      -DBUILD_SHARED_LIBS:BOOL=ON
      -DDESIRED_QT_VERSION:STRING=4
      -DVTK_USE_GUISUPPORT:BOOL=ON
      -DVTK_USE_QVTK_QTOPENGL:BOOL=ON
      -DVTK_USE_QT:BOOL=ON
      -DVTK_LEGACY_REMOVE:BOOL=ON
      -DQT_QMAKE_EXECUTABLE:FILEPATH=${QT_QMAKE_EXECUTABLE}
    DEPENDS
      ${${proj}_DEPENDENCIES}
    )
  set(VTK_DIR ${CMAKE_BINARY_DIR}/${proj}-build)

else()
  superbuild_add_empty_external_project(${proj} "${${proj}_DEPENDENCIES}")
endif()

mark_as_superbuild(
  VARS VTK_DIR:PATH
  LABELS "FIND_PACKAGE"
  )
/pre

1. Enabling and building dependencies
Before performing step1, the target_libraries.cmake file associated with each module is read. 
Then, the dependency graph is validated. If no errors occurred, the dependent modules and external projects are enabled.

The dependency graph is validated using a small tool named DGraph. This executable is a lightweight application also built by CTK buildsystem.

The DGraph tool helps also to:
- obtain the topological order of the different module. This is later used by the dashboard driver script to build, test, compute coverage of each module in the correct order.
- generate the project.xml file used to tell CDash what is the dependency graph.

1. Library options
As documented in CTK/CMakeLists.txt, ... 
pre
1. For CTK libraries, if the file Libs/DIR/LIBNAME/ctk_library_options.cmake exists,
1. in addition to 'CTK_LIB_DIR/LIBNAME' option, the following ones
1. will also be available in CMake configure menu:
1. CTK_LIB_DIR/LIBNAME_OPT1  (set to OFF)
1. CTK_LIB_DIR/LIBNAME_OPT2  (set to ON)
#
1. The file Libs/DIR/LIBNAME/ctk_library_options.cmake should look like:
#
1. SET(ctk_library_options
1. OPT1:OFF
1. OPT2:ON
1. )
/pre