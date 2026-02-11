---
title: Main Page New
render_with_liquid: false
---

__NOTOC__

1. **CTK - The Common Toolkit**
div style="float:right;"
wikiscript type="text/javascript" src="http://www.ohloh.net/p/483293/widgets/project_basic_stats.js"/wikiscript
/div

The goal of CTK is to support biomedical image computing. CTK code is licensed under [Apache 2.0](Apache 2.0)(http://www.apache.org/licenses/LICENSE-2.0.html). This means that users of CTK are allowed to use the code for academic, commercial, or other purposes without paying license fees or being restricted in their ability to redistribute their code or keep it private. 

CTK works on topics that are not covered by existing toolkits that support the mutual interest and needs of the CTK community. The main scope of current CTK efforts includes the topics *DICOM*, *DICOM Application Hosting*, *Widgets*, and *Plugin Framework*.


div style="display:table-row;"
div style="display:table-cell; max-width:450px;"
{{documentation/g-box-start|Documentation/Dicom_Overview|DICOM}}Provides high-level classes supporting query and retrieve operations from PACS and local databases. Includes Qt widgets to easily set-up a server connection and to send queries and view the results. [DCMTK](DCMTK)(http://dicom.offis.de/dcmtk) is used as the underlying toolkit.
{{documentation/g-box-links|apiurl=http://www.commontk.org/docs/html/group__Project__DICOM.html|issuelabel=DICOM}}
[ Read more...]( Read more...)(Documentation/Dicom_Overview .md)
{{documentation/g-box-end}}
/div
div style="display:table-cell; max-width:450px;"
{{documentation/g-box-start|Documentation/DicomApplicationHosting|DICOM Application Hosting}}Aims at creating a C++ reference implementation of the [ DICOM Part 19 Application Hosting specifications]( DICOM Part 19 Application Hosting specifications)(media:DicomAppHostingSpecs.pdf .md). It provides an infrastructure to create both hosts and hosted applications. The project is still in alpha status but may be useful for conformance testing and initial experimentation.
{{documentation/g-box-links|apiurl=http://www.commontk.org/docs/html/group__Project__DICOMAppHosting.html|issuelabel=DICOMApplicationHosting}}
[ Read more...]( Read more...)(Documentation/DicomApplicationHosting .md)
{{documentation/g-box-end}}
/div
/div
div style="display:table-row"
div style="display:table-cell; max-width:450px;"
{{documentation/g-box-start|Documentation/WidgetPlans|Widgets}}A collection of Qt Widgets for usage in biomedical imaging applications.
{{documentation/g-box-links|apiurl=http://www.commontk.org/docs/html/group__Project__Widgets.html|issuelabel=Widgets}}
[ Read more...]( Read more...)(Documentation/WidgetPlans .md)
{{documentation/g-box-end}}
/div
div style="display:table-cell; max-width:450px;"
{{documentation/g-box-start|Documentation/Plugin_Framework|Plugin Framework}}A dynamic component system for C++, modeled after the [OSGi](OSGi)(http://www.osgi.org) specifications. It enables a development model where applications are (dynamically) composed of many different (reusable) components following a service oriented approach.
{{documentation/g-box-links|apiurl=http://www.commontk.org/docs/html/group__PluginFramework.html|issuelabel=PluginFramework}}
[ Read more...]( Read more...)(Documentation/Plugin_Framework .md)
{{documentation/g-box-end}}
/div
/div

    1. Important Links
Although the CTK efforts are concentrated on the topics described above, there are a couple of other working areas covering topics like *[ interoperability]( interoperability)(Interoperability .md)* and *software testing* which might be of interest to the biomedical imaging community. Please see the links given below for more details.

{| border="0" align="center" width="98%" valign="top" cellspacing="7" cellpadding="2"
|-
! width="33%"|
! |
! width="33%"|
! |
! width="33%"|
|- 
|valign="top"|
span style="color: #555555; font-size: 18px; font-weight: bold;"About CTK/span
----
- [News](News)(News.md)
- [Events](Events)(Events.md)
- [Team](Team)(The)(The Team.md)
- [ CTK Roadmap Document]( CTK Roadmap Document)(CTK-Roadmap .md)
- [Interoperability](Interoperability)(Interoperability.md)
- [ Technical Documentation]( Technical Documentation)(Documentation .md)

|bgcolor="#CCCCCC"|
|valign="top"|

span style="color: #555555; font-size: 18px; font-weight: bold;"CTK Users/span
----
- [Started](Started)(Getting)(Getting Started.md)
- [Instructions](Instructions)(Build)(Build Instructions.md)
- [API Documentation](API Documentation)(http://www.commontk.org/docs/html/classes.html)
- [Launcher](Launcher)(Application)(Tools:_Application_launcher.md)

|bgcolor="#CCCCCC"|
|valign="top"|

span style="color: #555555; font-size: 18px; font-weight: bold;"CTK Developers/span
----
- [Source Code](Source Code)(http://github.com/commontk/CTK)
- [Dashboard](Dashboard)(http://my.cdash.org/index.php?project=CTK)
- [to CTK](to CTK)(Contributing)(Contributing to CTK.md)
- [Report a problem](Report a problem)(http://github.com/commontk/CTK/issues/new)
- [Ideas](Ideas)(Project)(Project Ideas.md)

|}


{|align="center"
|-
|
{|cellspacing="16px"
|-
| [x26px|link=http://github.com/commontk/CTK](x26px|link=http://github.com/commontk/CTK)(File:200px-GitHub.png.md)
| [x26px|link=Documentation/BuildSystem_Description](x26px|link=Documentation/BuildSystem_Description)(File:Cmake-logo.png.md)
| [x26px|link=http://qt.nokia.com](x26px|link=http://qt.nokia.com)(File:Qt-logo.png.md)
| [x26px|link=Documentation/Python_Scripting](x26px|link=Documentation/Python_Scripting)(File:Python-powered-w-100x40.png.md)
| [x26px|link=http://www.dcmtk.org](x26px|link=http://www.dcmtk.org)(File:Dcmtk-logo.png.md)
| [x26px|link=http://www.itk.org](x26px|link=http://www.itk.org)(File:ItkLogo med.png.md)
| [x26px|link=http://www.vtk.org](x26px|link=http://www.vtk.org)(File:VTKlogo.png.md)
|}
|}