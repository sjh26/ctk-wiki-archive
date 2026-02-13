---
title: Documentation/MigrationGuide/ExternalProject
---

__TOC__


1. Transitioning to ExternalProject following cb4e2c9
Commits: [jcfr/CTK@cb4e2c9](https://github.com/jcfr/CTK/commit/cb4e2c9), [jcfr/ExternalProjectsContrib@8b62614](https://github.com/jcfr/ExternalProjectsContrib/commit/8b62614)


1. At the top, change 'ctk_include_once()' into 'superbuild_include_once()'


1. Transitioning to ExternalProject following 0c423189d
Commits: [jcfr/CTK@0c423189](https://github.com/jcfr/CTK/commit/0c423189d41ea79943085189e2f4698d345c20f6), [jcfr/ExternalProjectsContrib@f83bb40](https://github.com/jcfr/ExternalProjectsContrib/commit/f83bb40601cae94c5dc50f3f4cde01dda6637e1f)


1. Add 'ctk_include_once()' at the top


2. Remove 'ctkMacroShouldAddExternalproject' call and associated if/endif statement
  
Before:

  ctkMacroShouldAddExternalproject(QUAZIP_LIBRARIES add_project) # --------- REMOVE THIS
  if(${add_project})                                             # --------- REMOVE THIS
    [...]                                                        # Keep this block and fix indentation
  endif()                                                        # --------- REMOVE THIS
  
After:

  [...]


3. Remove 'if(CTK_SUPERBUILD)/endif()' statement

Before:

  if(CTK_SUPERBUILD) # --------- REMOVE THIS
    [...]            # Keep this block and fix indentation
  endif()            # --------- REMOVE THIS

After:

  [...]


4. Remove 'CTK_DEPENDENCIES' update statement:

Before:
 
  [...]
  
  set(proj_DEPENDENCIES)
  
  list(APPEND CTK_DEPENDENCIES ${proj})  # --------- REMOVE THIS
  
  set(${QuaZip_enabling_variable}_LIBRARY_DIRS QUAZIP_LIBRARY_DIRS)
  
  [...]


After:

  [...]
  
  set(proj_DEPENDENCIES)
  
  set(${QuaZip_enabling_variable}_LIBRARY_DIRS QUAZIP_LIBRARY_DIRS)
  
  [...]


5. Move 'Sanity Checks' before 'if(DEFINED ...' test 

Before:

  ctk_include_once()
  
  # Sanity checks                                                                                    # --------- CUT HERE
  if(DEFINED QuaZip_DIR AND NOT EXISTS ${QuaZip_DIR})                                                # --------- CUT HERE
    message(FATAL_ERROR "QuaZip_DIR variable is defined but corresponds to non-existing directory")  # --------- CUT HERE
  endif()                                                                                            # --------- CUT HERE
  
  set(QuaZip_enabling_variable QUAZIP_LIBRARIES)
  
  [...]
  
  if(NOT DEFINED QuaZip_DIR)

After:

  ctk_include_once()
  
  set(QuaZip_enabling_variable QUAZIP_LIBRARIES)
  
  [...]
  
  # Sanity checks                                                                                    # --------- PASTE HERE
  if(DEFINED QuaZip_DIR AND NOT EXISTS ${QuaZip_DIR})                                                # --------- PASTE HERE
    message(FATAL_ERROR "QuaZip_DIR variable is defined but corresponds to non-existing directory")  # --------- PASTE HERE
  endif()                                                                                            # --------- PASTE HERE
  
  if(NOT DEFINED QuaZip_DIR)


6. Add call to 'ctkMacroCheckExternalProjectDependency' macro

Before:

  ctk_include_once()
  
  set(QuaZip_enabling_variable QUAZIP_LIBRARIES)
                                                          # --------- REMOVE THIS
  set(proj QuaZip)                                        # --------- REMOVE THIS
  set(proj_DEPENDENCIES)                                  # --------- REMOVE THIS
                                                          # --------- REMOVE THIS
  set(${QuaZip_enabling_variable}_LIBRARY_DIRS QUAZIP_LIBRARY_DIRS)
  set(${QuaZip_enabling_variable}_INCLUDE_DIRS QUAZIP_INCLUDE_DIRS)
  set(${QuaZip_enabling_variable}_FIND_PACKAGE_CMD QuaZip)
  
  # Sanity checks
  
  [...]

After:

  ctk_include_once()
  
  set(QuaZip_enabling_variable QUAZIP_LIBRARIES)
  set(${QuaZip_enabling_variable}_LIBRARY_DIRS QUAZIP_LIBRARY_DIRS)
  set(${QuaZip_enabling_variable}_INCLUDE_DIRS QUAZIP_INCLUDE_DIRS)
  set(${QuaZip_enabling_variable}_FIND_PACKAGE_CMD QuaZip)
  
  set(QuaZip_DEPENDENCIES "")                            # --------- ADD THIS
                                                         # --------- ADD THIS
  ctkMacroCheckExternalProjectDependency(QuaZip)         # --------- ADD THIS
  set(proj QuaZip)                                       # --------- ADD THIS
  
  # Sanity checks
  
  [...]

7. Add check for 'CTK_USE_SYSTEM_..' variable

Before:

  [...]
  
  ctkMacroCheckExternalProjectDependency(QuaZip)
  set(proj QuaZip)
  
  # Sanity checks
  
  [...]

After:

  [...]
  
  ctkMacroCheckExternalProjectDependency(QuaZip)
  set(proj QuaZip)
  
  if(${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj})
    message(FATAL_ERROR "Enabling ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj} is not supported !")
  endif()
  
  # Sanity checks
  
  [...]