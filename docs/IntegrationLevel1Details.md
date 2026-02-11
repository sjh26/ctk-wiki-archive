---
title: IntegrationLevel1Details
---

1. Scenarios for integration on the DICOM Application Hosting level
[File:CTK-Level1.png](File:CTK-Level1.png)(File:CTK-Level1.png.md)

  1. Scenario 1a
I have an application that I want to run integrated in an existing DICOM Application Host, e.g. a PACS viewer supporting DICOM Supplement 118.

    1. Solution
I use the CTK Dicom Application Hosting Module in my application to add intraoperability with a DICOM Application Host. My application gets started by the host, data are passed according to DICOM Supplement 118.

    1. Limitation
You cannot pass parameters to your application, so it either needs a GUI or has to do fully automatic parameterless processing.


  1. Scenario 1b
I have an application, e.g. a PACS/DICOM viewer, that I want to extend with DICOM Application Hosting support.

    1. Solution
I use the CTK Dicom Application Hosting Module in my application to add intraoperability with a processing module available as a DICOM Hosted Application.

[to overview ...](to overview ...)(Back)(CTKUsageScenarios.md)
[File:Example.jpg](File:Example.jpg)(File:Example.jpg.md)