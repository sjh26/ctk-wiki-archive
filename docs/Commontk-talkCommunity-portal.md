---
title: "Commontk talk:Community portal"
---

hello
I'm trying to install ctk and there is a bug that I would like to solve. Wanting to run CTK-BUILD_EXAMPLE, after that I have configured and generated and doing a make. I get as error:
CMake Error at Utilities / CMake / FindDCMTK.cmake: 47 (find_package):
   Could not find a package configuration file provided by "DCMTK" with any of
   Following the names:

     DCMTKConfig.cmake
     dcmtk-config.cmake

   Add the install prefix of "DCMTK" to CMAKE_PREFIX_PATH gold set
   "DCMTK_DIR" to a directory Containing one of the above files. If "DCMTK"
   Provides a separate development package or SDK, be safe it has-beens
   installed.
Call Stack (most recent call first):
   CMakeLists.txt: 858 (find_package)


- Configuring incomplete, errors occurred!
make [2]: *** [CTK-Configure-prefix/src/CTK-Configure-stamp/CTK-Configure-configure] Error 1
make [1]: *** [CMakeFiles / CTK-Configure.dir / all] Error 2
make: *** [all] Error 2.

(I am very sure to install DCMTK).
Does someone could help me?thanks