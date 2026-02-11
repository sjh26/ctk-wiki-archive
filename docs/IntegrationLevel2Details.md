---
title: IntegrationLevel2Details
---

[File:CTK-Level2.png](File:CTK-Level2.png)(File:CTK-Level2.png.md)

  1. Scenario 2a
I have an image processing module that I want to run in the Slicer, MITK or GIMIAS application. The parameters of the module shall be adjustable in the application, e.g. with a generated GUI.

    1. Solution
I use the CTK command line interface module which helps me to publish my parameters, parse command line calls and on the host to communicate the processing parameters between my module and the application.

    1. Limitation
You do not have access to application features or other modules from inside your module.

  1. Scenario 2b
I have an application, e.g. a PACS/DICOM viewer, that I want to extend with the possibility to run command line modules following the CTK standard / parameter conventions.

    1. Solution
You use the command line interface support module for parsing parameter descriptions. If your application is using Qt you can optinally use the GUI generator for creating a GUI for the module parameters.