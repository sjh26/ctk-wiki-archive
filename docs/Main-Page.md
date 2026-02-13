---
title: Main Page
---

__NOTOC__

1. **CTK - The Common Toolkit**
The goal of CTK is to support biomedical image computing. CTK code is licensed under [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html). This means that users of CTK are allowed to use the code for academic, commercial, or other purposes without paying license fees or being restricted in their ability to redistribute their code or keep it private. 

CTK works on topics that are not covered by existing toolkits that support the mutual interest and needs of the CTK community. The main scope of current CTK efforts includes the topics *DICOM*, *DICOM Application Hosting*, *Widgets*, and *Plugin Framework*.


<center>
<div style="display:table-row;">
<div style="display:table-cell; max-width:450px;">
{{documentation/g-box-start|Documentation/Dicom_Overview|DICOM}}Provides high-level classes supporting query and retrieve operations from PACS and local databases. Includes Qt widgets to easily set-up a server connection and to send queries and view the results. [DCMTK](http://dicom.offis.de/dcmtk) is used as the underlying toolkit.
{{documentation/g-box-links|imggalurl=|apiurl=http://www.commontk.org/docs/html/group__Project__DICOM.html|issuelabel=DICOM}}. 
[Read more...](Documentation/Dicom-Overview.html)
CTK is also the home of [dcmjs](http://dcmjs.org).
`{{documentation/g-box-end}}`
</div>
<div style="display:table-cell; max-width:450px;">
{{documentation/g-box-start|Documentation/DicomApplicationHosting|DICOM Application Hosting}}Aims at creating a C++ reference implementation of the [DICOM Part 19 Application Hosting specifications](mediaDicomAppHostingSpecs.pdf.html). It provides an infrastructure to create both hosts and hosted applications. The project is still in alpha status but may be useful for conformance testing and initial experimentation.
{{documentation/g-box-links|imggalurl=|apiurl=http://www.commontk.org/docs/html/group__Project__DICOMAppHosting.html|issuelabel=DICOMApplicationHosting}}
[Read more...](Documentation/DicomApplicationHosting.html)
`{{documentation/g-box-end}}`
</div>
</div>
<div style="display:table-row">
<div style="display:table-cell; max-width:450px;">
{{documentation/g-box-start|Documentation/Widgets|Widgets}}A collection of Qt Widgets for usage in biomedical imaging applications.
{{documentation/g-box-links|imggalurl=Documentation/ImageGallery|apiurl=http://www.commontk.org/docs/html/group__Project__Widgets.html|issuelabel=Widgets}}
[Read more...](Documentation/Widgets.html)
`{{documentation/g-box-end}}`
</div>
<div style="display:table-cell; max-width:450px;">
{{documentation/g-box-start|Documentation/Plugin_Framework|Plugin Framework}}A dynamic component system for C++, modeled after the [OSGi](http://www.osgi.org) specifications. It enables a development model where applications are (dynamically) composed of many different (reusable) components following a service oriented approach.
{{documentation/g-box-links|imggalurl=|apiurl=http://www.commontk.org/docs/html/group__PluginFramework.html|issuelabel=PluginFramework}}
[Read more...](Documentation/Plugin-Framework.html)
`{{documentation/g-box-end}}`
</div>
</div>
<div style="display:table-row">
<div style="display:table-cell; max-width:450px;">
{{documentation/g-box-start|Documentation/Command_Line_Interface|Command Line Interfaces}}A technology that allows the algorithms written as self-contained executables to be used in multiple end-user application environments without modifications.
{{documentation/g-box-links|imggalurl=|apiurl=http://www.commontk.org/docs/html/group__CommandLineModules__Group.html|issuelabel=CmdLineModules}}
[Read more...](Documentation/Command-Line-Interface.html)
`{{documentation/g-box-end}}`
</div>
</div>
</center>
    1. Important Links
Although the CTK efforts are concentrated on the topics described above, there are a couple of other working areas covering topics like *[interoperability](Interoperability.html)* and *software testing* which might be of interest to the biomedical imaging community. Please see the links given below for more details.

{| border="0" align="center" width="98%" valign="top" cellspacing="7" cellpadding="2"
|-
! width="33%"|
! |
! width="33%"|
! |
! width="33%"|
|- 
|valign="top"|
<span style="color: #555555; font-size: 18px; font-weight: bold;">About CTK</span>
----
- [News](News.html)
- [Events](Events.html)
- [The Team](The-Team.html)
- [CTK Roadmap Document](CTK-Roadmap.html)
- [Interoperability](Interoperability.html)
- [Technical Documentation](Documentation.html)


|bgcolor="#CCCCCC"|
|valign="top"|

<span style="color: #555555; font-size: 18px; font-weight: bold;">CTK Users</span>
----
- [Getting Started](Getting-Started.html)
- [Build Instructions](Build-Instructions.html)
- [API Documentation](http://www.commontk.org/docs/html/classes.html)
- [Application Launcher](https://github.com/commontk/AppLauncher#readme)

|bgcolor="#CCCCCC"|
|valign="top"|

<span style="color: #555555; font-size: 18px; font-weight: bold;">CTK Developers</span>
----
- [Getting Started](Getting-Started.html)
- [Source Code](http://github.com/commontk/CTK)
- [Dashboard](http://my.cdash.org/index.php?project=CTK)
- [Contributing to CTK](Contributing-to-CTK.html)
- [Report a problem](http://github.com/commontk/CTK/issues/new)
- [Project Ideas](Project-Ideas.html)
- [Making a Release](Making-a-Release.html)


|}


{|align="center"
|-
|-
| 
{|cellspacing="16px"
|-
|CTK builds on some awesome technology: 
| [![200px GitHub](images/200px-GitHub.png)](http://github.com/commontk/CTK)
| [![Cmake logo](images/Cmake-logo.png)](Documentation/BuildSystem-Description.html)
| [![Qt logo](images/Qt-logo.png)](http://qt.nokia.com)
| [![Python powered w 100x40](images/Python-powered-w-100x40.png)](Documentation/Python-Scripting.html)
| [![Dcmtk logo](images/Dcmtk-logo.png)](http://www.dcmtk.org)
| [![ItkLogo med](images/ItkLogo_med.png)](http://www.itk.org)
| [![VTKlogo](images/VTKlogo.png)](http://www.vtk.org)
|}
|}