---
title: Project Ideas
---

1. Qt Help File
Create a .qch file from the CTK doxygen documentation and include it in QtCreator for enabling "F1" (Context Help) on CTK classes and methods.

      1. CMake support in Doxygen `{{done}}`
Write a doxygen extension to be able to parse CMake files and generate HTML documentation from it. See

- http://www.stack.nl/~dimitri/doxygen/faq.html #12
- http://www.stack.nl/~dimitri/doxygen/helpers.html

Done, see [CMakeDoxygenFilter](https://github.com/saschazelzer/CMakeDoxygenFilter)