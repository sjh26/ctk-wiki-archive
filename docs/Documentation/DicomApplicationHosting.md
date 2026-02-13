---
title: Documentation/DicomApplicationHosting
---

1. DICOM Application Hosting
  1. Introduction
The goal is to create a C++ implementation of an application host and and a hosted application conforming to the DICOM Part 19 specifications.

  1. Status
Usable code is available in the master branch of the CTK repository. Current development happens in the [dah branch](http://github.com/commontk/CTK/tree/dah).

Basic message passing between the CTK Host and the application works (state changes, screen area exchange). Basic interoperability with the XIP implementations also works (in both directions: XIP host - ctk app, as well as ctk host - XIP simple app), but there is no exchange of image data yet. (Note: the current version of the XIP host (v0.3.0) works only on Windows without problems).

Data exchange is being worked on at the moment. First we will exchange data files, not models. To bring you up to date with the current progress and shortcomings of the data exchange part of the implementation, see [DicomApplicationHosting:DataExchangeDevelopment](../Documentation/DicomApplicationHostingDataExchangeDevelopment.html)

  1. Build / Usage
Two applications can be turned on in the CMake configuration: ctkExampleHost and ctkExampleHostedApp . Make sure you also turn on all CMake variables starting with CTK_PLUGIN_org.commontk.dah .

The ctkExampleHost is a Qt application . Press the Load button to choose the application to host. Press Start to invoke the application and Run to start processing. 

  1. Architecture
See the diagram below for an overview of the architecture used for the implementation

![Dah architecture](../images/Dah_architecture.png)

  1. Testing
Some initial work has been done during the [Sophia-Antipolis Hackfest](../CTK-Hackfest-Nov-2011.html) regarding conformance and functional tests. See [DICOM_Application_Hosting_Testing](../DICOM-Application-Hosting-Testing.html).

  1. Links
[XIP@caBIG](https://cabig.nci.nih.gov/tools/XIP) 

[General information about DICOM application hosting](http://support.dcmtk.org/wiki/dicom/application-hosting)

  1. Reference
![DicomAppHostingSpecs](../images/DicomAppHostingSpecs.pdf)

[DicomApplicationHostingReference](../Documentation/DicomApplicationHostingReference.html)

WSDL, XSD, and RNC files: ![wsdl ft](../images/wsdl_ft.zip)