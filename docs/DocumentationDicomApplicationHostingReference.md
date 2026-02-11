---
title: Documentation/DicomApplicationHostingReference
---

center**Digital Imaging and Communications in Medicine (DICOM)**/center


center*Supplement 118 Application Hosting*/center


**DICOM Standards Committee, Working Group 23**

1300 N. 17th Street, Suite 1752

Rosslyn, Virginia 22209 USA


VERSION: Final Text, 2010/09/30

Developed pursuant to DICOM Work Item 2004-09-E


1. Scope and Field of Application
This Supplement defines an interface between two software applications. One application, the Hosting System, provides the second application with data, such as a set of images and related data. The second application, the Hosted Application, analyzes that data, potentially returning the results of that analysis, for example in the form of another set of images and/or a structured report, to the first application. Such an Application Program Interface (API) differs in scope from other portions of the DICOM Standard in that it standardizes the data interchange between software components on the same system, instead of data interchange between different systems.

This Supplement describes the APIs shared by a Hosting System and one or more Hosted Applications.

The Hosted Application API covers the following functions:

control the lifecycle of a Hosted Application (e.g. initialize, terminate)

interact with a Hosted Application (e.g. launch a job, pass input data, get job status, communicate results)

This Supplement adds PS3.19, Application Hosting, to the DICOM Standard.

  1. Relationship to Other Standards
The API description is intended to be technology neutral. In other words, the description should not limit the technology a vendor might use to implement the API (e.g. Java, Microsoft� .NET). 

The API is specified using WSDL (Web Services Definition Language), and utilizes concepts from XML Infosets, and their representation in XML. The API also utilizes XPath as a mechanism to describe a selection path (query) into the content of an XML Infoset that represents an object.


1. Changes to NEMA Standards Publication PS3.1-2009
*Add the following text to PS3.1 Introduction and Overview:*


  1. 6.19PS3.19: Application Hosting
PS3.19 of the DICOM Standard specifies an Application Programming Interface (API) to a DICOM-based medical computing system into which programs written to that standardized interface can plug-in (see Figure 6.19-1). A Hosting System implementer only needs to create the standardized API once to support a wide variety of add-on Hosted Applications. 

center/center

center**Figure 6.19-1. Interface between a Hosted Application and a Hosting System**/center

In the traditional plug-in model, the plug-in is dedicated to a particular host system (e.g. a web browsing program), and might not run under other host systems (e.g. other web browsing programs). PS3.19 defines an API that may be implemented by any Hosting System. A plug-in Hosted Application written to the API would be able run in any environment provided by a Hosting System that implements that API (see Figure 6.19-2). 

[Image:](Image:)(Image:.md)

center**Figure 6.19-2. Illustration of platform independence via the Hosted Application architecture.**/center

PS3.19 specifies both the interactions and the Application Programming Interfaces (API) between Hosting Systems and Hosted Applications. PS3.19 also defines the data models that are used by the API.

1. Changes to NEMA Standards Publication PS3.1-2009 through PS3.18-2009
*Add to the Foreword of PS3.1 through PS3.18:*

PS3.18: Web Access to DICOM Persistent Objects (WADO)

**PS3.19: Application Hosting**

These Parts are related but independent documents. Their development level and approval status may differ. 


1. Changes to NEMA Standards Publication PS3.6-2009
*Add the following rows to Table A-1 in PS3.6 Data Dictionary:*

center**Table A-1UID VALUES**/center


{| style="border-spacing:0;"
| style="border-top:0.0153in double #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| **UID Value**
| style="border-top:0.0153in double #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| **UID NAME**
| style="border-top:0.0153in double #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| **UID TYPE**
| style="border-top:0.0153in double #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| **Part**

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| 1.2.840.10008.7.1.1
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| Native DICOM Model
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| Application Hosting Model
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| PS 3.19

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| 1.2.840.10008.7.1.2
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| Abstract Multi-Dimensional Image Model
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| Application Hosting Model
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| PS 3.19

|}
*Add the following rows to Table A-3 in PS3.6 Data Dictionary:*

center**Table A-3CONTEXT GROUP UID VALUES**/center


{| style="border-spacing:0;"
| style="border-top:0.0153in double #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| **Context UID **
| style="border-top:0.0153in double #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| center**Context Identifier**/center
| style="border-top:0.0153in double #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| **Context Group Name**

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| 1.2.840.10008.6.1.916
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| center7180/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| Abstract Multi-Dimensional Image Model Component Semantics

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| 1.2.840.10008.6.1.917
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| center7181/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| Abstract Multi-Dimensional Image Model Component Units

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| 1.2.840.10008.6.1.918
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| center7182/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| Abstract Multi-Dimensional Image Model Dimension Semantics

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| 1.2.840.10008.6.1.919
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| center7183/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| Abstract Multi-Dimensional Image Model Dimension Units

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| 1.2.840.10008.6.1.920
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| center7184/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| Abstract Multi-Dimensional Image Model Axis Direction

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| 1.2.840.10008.6.1.921
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| center7185/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| Abstract Multi-Dimensional Image Model Axis Orientation

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| 1.2.840.10008.6.1.922
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| center7186/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.0597in;padding-right:0.0597in;"| Abstract Multi-Dimensional Image Model Qualitative Dimension Sample Semantics

|}
1. Changes to NEMA Standards Publication PS3.17-2009
**PS3.17: Add the following Annex:**

1. Annex ZX Use Cases for Application Hosting
  1. ZX.1Agent-Specific Post Processing
Many metabolic/contrast agents require more than just simple imaging to provide data for decision making. Rather than just detecting the presence or absence of the metabolic/contrast agents, calculations based on relative uptake rates, or decay rates, comparisons with previous or neighboring data, fusion of data from multiple sources or time points, etc. may be necessary to properly evaluate image data with these metabolic/contrast agents. Often the nature of this processing is closely related to the type of agent, the anatomy, and the disease process being targeted. The processing may be so specific that the general-purpose image processing features found on medical imaging workstations are inadequate to properly perform the procedure. The effective use of a particular agent for a particular procedure may depend on having properly tuned, targeted post-processing. Both the algorithms used, as well as the workflow in performing the analysis, may be customized for performing procedures with a particular agent.

The stakeholders interested in developing such agent- and exam-specific post-processing applications may have a vested interest in insuring that such post-processing applications can run on a wide variety of systems. The standard post-processing software API outlined in PS3.19 could simplify the distribution of such agent-specific analysis applications. Rather than creating multiple versions of the same application, each version targeted to a particular medical imaging vendors system, the application developer need only create a single version of the application, which would run on any system that implemented the standard API. 

Differences in physical characteristics, acquisition technique and equipment, and user preference affect image quality and processing requirements. By allowing the sharing of applications based on device-independent (or conversely, device-specific) procedures, the Hosted Application technology will reduce these differences to a minimum.

  1. ZX.2Support for Multi-Site Collaborative Research
A common API for Application Hosting facilitates multi-site research.

**Site-specific problems**: The development of molecular imaging applications can be accelerated with multiple site cooperation in the validation of new algorithms and software. However, the run-time environment and tools available at one site typically are not matched identically at other sites, hampering the sharing of applications between sites. Using the same tools allows them to share applications. One cannot simply take an application written at one of these sites, and make it run on the other site without major software work involving the installation and configuration of multiple tool packages. Even after installing the needed tools and libraries, software developed at one site may be trying to access facilities that are unavailable at the other site, for example, facilities to store, access, and organize the image data. Often the data formats applications from one site are expecting are incompatible with the data formats available at other sites. Having a standard API could help minimize these data incompatibilities.

**Gap between research and clinical environments**: The initial versions of agent-specific applications are typically created in a research environment, and are not easily accessible in the clinical environment. The early experimental work generally is done by exporting the image data out of the clinical environment to research workstations, and then importing the results back into the clinical system once the analysis is done. While exporting and importing the images may be sufficient for the early research work, clinical acceptance of an application can be significant enhanced if that application could run in the same clinical environment where the images are collected, in order to better fit into the clinical workflow.

The problem of mismatched run time environments becomes even more acute when attempting to run the typical research application on a production clinical workstation. Due to a variety of legal and commercial concerns, vendors of the systems utilized in the clinical environment generally do not support running unknown software, nor do most commercial vendors have the time or resources to assist the hundreds of researchers who may wish to port a particular application to that vendor's system. Even if researchers manage to load an experimental program onto a clinical system, the experimental program rarely has direct access to the data stored on that clinical system, nor can it directly store results back into the systems clinical database. Without a single standard interface, users have to resort to the cumbersome and time-consuming export and input routines to be able to run research programs on clinical data. It is expected that the constrained environment that a standard API provides would be simpler to validate, particularly if it is universally deployed by multiple vendors, and could lessen the burden on any individual system vendor.

  1. ZX.3Screening Applications
Computer Aided Diagnosis and Decision Making (CAD) is becoming more prevalent in radiology departments. Many classes of exams now routinely go through a computer screening process prior to reading. One potential barrier to more widespread use of CAD screening is that the various vendors of CAD applications typically only allow their applications to run on servers or workstations provided by those companies. A clinical site that wishes to utilize, for example, mammo CAD from one vendor and lung CAD from another often is forced to acquire two different servers or workstations from the two different vendors.

The Hosted Application concept described in PS3.19 could be used to facilitate the running of multiple CAD applications from multiple vendors on the same computer system. 

  1. ZX.4Modality-Specific Post Processing
As medical imaging technology progresses, new modalities are added to the standard. For example, vessel wall detection in intravascular ultrasound is often easier if the images are left in radial form. Unfortunately, most DICOM workstations would not know how to deal with images in such a strange format even though the workstation might recognize that it is an image.

One possible solution is for a workstation to seek out an appropriate Hosted Application for handling Modalities or SOP classes that it does not recognize. This would allow for automatic handling of all image types by a generic imaging platform. Similarly, SOP Classes, even private SOP Classes, could be created that depend on particular Hosted Applications to prepare data for display.

  1. ZX.5Measurement/Evidence Document Creation
Another natural use for such a standardized API is the creation of exam-specific analysis and measurement programs for the creation of Evidence Documents (Structured Reports). The standardized API would allow the same analysis program to run on a variety of host systems, reducing the amount of development needed to support multiple platforms.

  1. ZX.6CAD Rendering
Often the regulatory approval for CAD systems includes the method by which the CAD marks are presented to the user. Providers of CAD systems have used dedicated workstations for such display in the past in order to insure that the CAD marks are presented as intended. If there were a suitable standardized API for launching hosted applications, a Hosted Application could handle the display of CAD results on any workstation that supports that standardized API.

1. Creation of NEMA Standards Publication PS3.19
**Create PS3.19 and add the following contents:**

1. FOREWORD
The DICOM Standard is structured as a multi-part document using the guidelines established in the following document:

ISO/IEC Directives, 1989 Part 3 : Drafting and Presentation of International Standards.

This document is one part of the DICOM Standard, which consists of the following parts:

PS3.1: Introduction and Overview

PS3.2: Conformance

PS3.3: Information Object Definitions

PS3.4: Service Class Specifications

PS3.5: Data Structures and Encoding

PS3.6: Data Dictionary

PS3.7: Message Exchange

PS3.8: Network Communication Support for Message Exchange

PS3.9: Retired

PS3.10: Media Storage and File Format for Media Interchange

PS3.11: Media Storage Application Profiles

PS3.12: Formats and Physical Media

PS3.13: Retired

PS3.14: Grayscale Standard Display Function

PS3.15: Security and System Management Profiles

PS3.16: Content Mapping Resource

PS3.17: Explanatory Information

PS3.18: Web Access to DICOM Persistent Objects (WADO)

PS3.19: Application Hosting

These parts are related but independent documents. Their development level and approval status may differ. Additional parts may be added to this multi-part standard. PS3.1 should be used as the base reference for the current parts of this standard.

1. 1Scope and field of application
This Part of the DICOM Standard defines an interface between two software applications. One application, the Hosting System, provides the second application with data, such as a set of images and related data. The second application, the Hosted Application, analyzes that data, potentially returning the results of that analysis, for example in the form of another set of images and/or structured reports, to the first application. Such an Application Program Interface (API) differs in scope from other portions of the DICOM Standard in that it standardizes the data interchange between software components on the same system, instead of data interchange between different systems. Hosted Application programs written to that standardized interface can plug-into (see Figure 1-1) Hosting Systems. The notion of software add-ons or plug-ins is quite common in the computing world, and has been successfully employed to extend the capabilities of web browsers, media players, graphical editors, publishing programs, etc. A Hosting System implementer needs only to create the standardized API once in order to support a wide variety of add-on Hosted Applications. 

center/center

center**Figure 1-1. Interface between Hosted Application and Hosting System**/center

In the traditional plug-in model, the plug-in is dedicated to a particular host system (e.g. a web browsing program), and might not run under other host systems (e.g. other web browsing programs). PS3.19 defines a standardized API that may be implemented by any Hosting System. A plug-in Hosted Application written to the standardized API would be able to run on any Hosting System that implements that standardized API (see Figure 1-2). 

[Image:](Image:)(Image:.md)

center**Figure 1-2. Illustration of platform independence via Hosted Application architecture.**/center

The design goals and assumptions for the API include:

-Language independence  the API is defined in such a way that programs written in any common programming language could utilize it.

-Platform independence  the API is defined in such a way that it is not dependent on any particular computing platform or operating system.

-Extensible  the API can be extended in a backward compatible fashion. Old applications still work even with new extensions in place, while new applications that are aware of the extensions can gain access to a richer set of functionality.

-Protected  the API design is consistent with later additions of mechanisms to protect intellectual property rights, and mechanisms that assure appropriate permissions and licenses are in place. The API should not interfere with common licensing systems.

-Secure  the Hosted Applications access to data on the Hosting System would be controlled via the API by the Hosting System. The Hosting System would be responsible for access controls and audit logging, since it is the one providing the data to the Hosted Application.

-Leverage Existing Technology  the API definition utilizes existing technology in common use, as far as practical, and does not define new methodologies.

-Simultaneous Launching  the Hosting System will be able to launch several instances of the same or of different Hosted Applications at the same time.

-Distributed Execution  although the API is designed for local execution, it does not prevent remote execution, where the Application is running on a different system from the Host. 

PS3.19 specifies both the interactions and the Application Programming Interfaces (API) between Hosting Systems and Hosted Applications. PS3.19 also includes Normative and Informative Annexes that define the data models that are used by the API defined in this part. 

The API does not directly address workflow management, which is addressed by other DICOM Services.

1. 2Normative references
The following standards contain provisions that, through reference in this text, constitute provisions of this Standard. At the time of publication, the editions indicated were valid. All standards are subject to revision, and parties to agreements based on this Standard are encouraged to investigate the possibilities of applying the most recent editions of the standards indicated below.

IETF RFC 2045,2046,2048MIME Multipurpose Internet Mail Extension

IETF RFC 2396Uniform Resource Identifiers (URI): Generic Syntax

IETF RFC 3240application/dicom MIME Sub-type Registration

ISO 8822:1988Information processing systems -- Open Systems Interconnection - Connection oriented presentation service definition

ISO/IEC 19757DSDL Document Schema Definition Languages (DSDL)

ITU-T Recommendation X.667UUID (also IETF RFC 4122)

W3C RecommendationWeb Services Description Language (WSDL) 1.1

Note:The WSDL W3C Recommendation can be found at [http://www.w3.org/TR/wsdl](http://www.w3.org/TR/wsdl)(http://www.w3.org/TR/wsdl)

W3C RecommendationXML Path Language (XPath) 2.0 

Note:The XPath W3C Recommendation can be found at [http://www.w3.org/TR/2007/REC-xpath20-20070123/](http://www.w3.org/TR/2007/REC-xpath20-20070123/)(http://www.w3.org/TR/2007/REC-xpath20-20070123/))

W3C Recommendation XML Information Set 

Note:The XML Information Set W3C Recommendation can be found at [http://www.w3.org/TR/xml-infoset/](http://www.w3.org/TR/xml-infoset/)(http://www.w3.org/TR/xml-infoset/) 

1. 3Definitions
For the purposes of this Standard the following definitions apply.

  1. 3.1Presentation service definitions
This part of the standard makes use of the following terms defined in ISO 8822:

a.Transfer Syntax

b.Transfer Syntax Name

  1. 3.2XML Infoset definitions
This part of the standard makes use of the following terms defined in W3C Recommendation XML Information Set:

a.Infoset or XML Infoset

b.Element or XML Element

c.Attribute or XML Attribute

Notes:1. The concept of an XML Attribute is quite distinct from that of a DICOM Attribute. 

2. To avoid confusion with the DICOM terms with similar names, the text of the DICOM Standard will use XML Element and XML Attribute when referring to these XML Infoset concepts. The appearance of Element or Attribute without the term XML in front of them generally refers to the DICOM concepts instead of the XML Infoset concepts.

  1. 3.3DICOM introduction and overview definitions
This Part of the Standard makes use of the following terms defined in PS3.1:

a. Attribute

  1. 3.4DICOM Information object definition
This part of the standard makes use of the following term defined in PS3.3:

a. Attribute Tag

  1. 3.5DICOM data structures and encoding
This Part of the Standard makes use of the following terms defined in PS3.5:

a. Data Element

b.Data Element Tag

c. Data Element Type

d.Data Set

e.Defined Term

f.Enumerated Value

g.Sequence of Items

h.Unique Identifier (UID) 

i.Value Multiplicity (VM)

j.Value Representation (VR)


  1. 3.6Codes and Controlled Terminology Definitions:
This Part of the Standard makes use of the following terms defined in PS3.16:

a.Baseline Context Group Identifier (BCID)

b.Defined Context Group Identifier (DCID)

c.Context Group

d.Context Group Version

e.Context ID (CID)

f.Mapping Resource

g.DICOM Content Mapping Resource (DCMR)

h.Value Set

i.Coding schemes

  1. 3.7Application Hosting Definitions
The following definitions are commonly used in this part of the Standard:

**Application Programming Interface:** A set of interface methods that Hosted Applications and Hosting Systems use to communicate with each other. 

**Hosted Application:** An application launched and controlled by a Hosting System. The Hosted Application may utilize services offered by the Hosting System. 

**Hosting System:** The application used to launch and control Hosted Applications. The Hosting System provides a variety of services such as DICOM object retrieval and storage for the Hosted Application. The Hosting System provides the infrastructure in which the Hosted Application runs and interacts with the external environment. This includes network access, database and security.


1. 4Symbols and abbreviations
The following symbols and abbreviations are used in this Part of the Standard.

**ACR**American College of Radiology

**ASCII**American Standard Code for Information Interchange

**ANSI**American National Standards Institute

**API **Application Programming Interface

**BCID**Baseline Context Group Identifier

**CID**Context ID

**DCID**Defined Context Group Identifier

**DCMR**DICOM Content Mapping Resource

**DICOM**Digital Imaging and Communications in Medicine

**DSDL**Document Schema Definition Languages** **

**IEC**International Electrotechnical Commission

**IOD**Information Object Definition

**IANA**Internet Assigned Numbers Authority

**ISO**International Standards Organization

**LUT**Lookup Table

**MIME**Multipurpose Internet Mail Extensions

**NEMA**National Electrical Manufacturers Association

**OID**Object Identifier (ISO 8824)

**ROI**Region of interest

**SOP**Service-Object Pair

**SR**Structured Reporting

**UID**Unique Identifier

**UUID**Universal Unique Identifier (ISO/IEC 11578)

**URL/URI**Uniform Resource Locator / Identifier

**VM**Value Multiplicity

**VR**Value Representation

**WSDL **Web Services Description Language

**XSD **XML Schema Definition

**XML **eXtensible Markup Language

**XPath**XML Path Language

1. Conventions
Terms listed in Section 3 Definitions are capitalized throughout the document.

1. 6Application Hosting Overview
This section describes the capabilities of the API, gives an example of the sequence of operations, and summarizes the remaining sections of this Part.

The APIs are shared by a Hosting System and one or more Hosted Applications.

The API is agnostic to the hardware platform, the operating system, and the GUI. The API supports requesting space in the GUI, if available. The API supports headless operation (i.e., no GUI).

The APIs are defined using Web Services Definition Language (WSDL) to be programming language, platform, and technology neutral. The APIs are designed to maximize language independence while minimizing the impact on efficiency of utilizing web services technology. The interfaces support both a networked file-based and a shared-memory interaction model. The API supports manual configuration, but not discovery.

The API can provide DICOM Data Sets and other data to the Hosted Application and can accept DICOM Data Sets and other data created by the Hosted Application, incrementally or upon completion. The Hosted Application has granular access to data provided by the Hosting System (e.g., single attributes, a subset of the pixel data, etc.) and only that data. The API utilizes DICOM semantics, but not necessarily DICOM network transfer syntax. The Hosting System provides a mechanism to the Hosted Application for generating UIDs.

The API allows the Hosting System to suspend and/or cancel the operation of the Hosted Application and regain user interface control. The API supports returning status information from the Hosted Application to the Hosting System and tracking the state of the Hosted Application.

The Hosting System has a mechanism to launch or connect to one or more Hosted Applications, verify that the Hosted Application has started successfully, and then pass the initial data objects. All interactions start in the Hosting System. A typical sequence of events is as follows:

1. The Hosting System identifies and locates the Hosted Application appropriate to the task and data using host-specific methods. Often the desired application is selected by the user of the system or is identified in a work list entry.
1. The Hosting System launches the application, essentially issuing a run or exec command, passing parameters that the Hosted Application uses to establish bilateral communications between the two.
1. The Hosting System uses the API to initiate a processing task in the Hosted Application and notifies it of its input data.
1. The Hosted Application uses the API to pull information from the Hosting System about the input data, including the location of the bulk pixel data.
1. The Hosted Application may use file I/O, memory mapping, or any other appropriate method to gain access to the bulk pixel data.
1. The Hosted Application may also use the API to inform the Hosting System of the status of the processing, for example progress, any warnings or errors encountered.
1. The Hosting System might use the API to suspend or cancel processing in the Hosted Application.
1. If the Hosting System suspended processing in the Hosted Application, it may use the API to instruct the Hosted Application to resume processing.
1. The Hosted Application, as it processes the input data, might create output objects, and use the API to inform the Hosting System of their existence.
1. The Hosting System uses the API to pull information about the output objects from the Hosted Application, including the location of the bulk data.
1. The Hosting system might use file I/O, memory mapping, or any other appropriate method to gain access to the output bulk data, if needed.
1. Once the Hosting System has pulled the output data from the Hosted Application, it uses the API to instruct the Hosted Application to wait for the next processing task (i.e., tells the Hosted Application to idle).
1. If the Hosting System has another task for the Hosted Application to perform, it may use the API to start that task, following this sequence of events beginning at Step 3.
1. When the Hosting System no longer needs the Hosted Application, it may use the API to request that the Hosted Application exit.

Section 7 describes in greater detail the Hosted Application Life Cycle.

Section 8 describes the base interfaces between the Hosting System and the Hosted Application.

Section 9 describes the custom data types and data structures used by the interfaces.

Section 10 describes the general form of models used by the model-based interfaces, and the conventions used in defining those models. The models defined by this Standard are described in the Annexes.

1. 7Hosted Application Life Cycle
  1. 7.1 Initialization
The Hosting System initializes a Hosted Application by issuing a run command or its equivalent (e.g exec function in the C language) with command line parameters to specify the end point references (URLs) to be used for the interfaces. One end point reference is used by the Hosted Application to access the Host interface provided by the Hosting System. The second end point reference is where the Hosting System will look for the Application interface provided by the Hosted Application. The Host and Application interfaces are described in Section 8. If issued from a command prompt or shell, the run command may appear as:

*app* -hostURL *url1* -applicationURL *url2*

Notes:1. In this startup methodology, it is the Hosting System, not the Hosted Application that specifies both URLs. The Hosted Application must respond at the URL assigned to it by the Hosting System.

2. A Hosted Application implementation where the Hosted Application runs remotely or on an application server might utilize a startup or proxy application to appropriately map between the URL provided by the Hosting System and the actual URL that the Hosted Application is using.

Figure 7.1-1 shows a sequence diagram of Hosted Application initialization. Once the Hosted Application has initialized and is ready to begin processing data, it changes its state to IDLE and notifies the Hosting System of the state change using a call to the notifyStateChanged() method, thus informing the Hosting System that the Hosted Application is ready to go.

center[Image:](Image:)(Image:.md)/center

center**Figure 7.1-1 Hosted Application Initialization Sequence**/center

  1. 7.2 States
Figure 7.2-1 shows the state diagram for a Hosted Application. The following states are defined:


{| style="border-spacing:0;"
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**State**/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Description**/center

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| IDLE
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| In IDLE state the Hosted Application is waiting for a new task assignment from the Hosting System. This is the initial state when the Hosted Application starts.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| INPROGRESS
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The Hosted Application is performing the assigned task.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| SUSPENDED
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The Hosted Application is stopping processing and is releasing as many resources as it can, while still preserving enough state to be able to resume processing.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| COMPLETED
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The Hosted Application has completed processing, and is waiting for the Hosting System to access and release any output data from Hosted Application.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CANCELED
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The Hosted Application is stopping processing, and is releasing all resources with no chance to resume processing.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| EXIT
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The terminal state of the Hosted Application.

|}
The transitions between states are:


{| style="border-spacing:0;"
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**State**/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Trigger**/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**New State**/center

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| not started
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Hosting System launches the Hosted Application (e.g. run, exec).
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| IDLE

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| IDLE
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Hosting System calls Application.setState (EXIT).
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| EXIT

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| IDLE
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Hosting System calls Application.setState (INPROGRESS).
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| INPROGRESS

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| INPROGRESS
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Hosting System calls Application.setState (SUSPENDED).
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| SUSPENDED

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| INPROGRESS
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Hosting System calls Application.setState (CANCELED).
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CANCELED

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| INPROGRESS
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Hosted Application encounters an error that prevents further processing, but is still healthy enough to perhaps start another task. The Hosted Application shall report this error through a call to notifyStatus() with a statusType of FATALERROR prior to transitioning to the CANCELED state.
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CANCELED

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| INPROGRESS
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Hosted Application finishes its processing.
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| COMPLETED

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| SUSPENDED
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Hosting System calls Application.setState (INPROGRESS).
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| INPROGRESS

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| SUSPENDED
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Hosted Application encounters an error (e.g. during suspension) that prevents further processing, but is still healthy enough to perhaps start another task. The Hosted Application shall report this error through a call to notifyStatus() with a statusType of FATALERROR prior to transitioning to the CANCELED state.
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CANCELED

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| SUSPENDED
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Hosting System calls Application.setState (CANCELED).
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CANCELED

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| COMPLETED
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Hosting System calls Application.setState (IDLE), after capturing all pertinent output data from the Hosted Application.
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| IDLE

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CANCELED
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Hosted Application releases all resources and is ready for the next task.
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| IDLE

|}
The Hosted Application notifies the Hosting System of all state transitions by calling the notifyStateChanged() method.

Note:If a Hosted Application does not respond to state change requests made by the Hosting System, the Hosting System may hard abort the Hosted Application in some implementation specific manner, such as by killing the process in which the Hosted Application is executing.

center[Image:](Image:)(Image:.md)/center

center**Figure 7.2-1 State Diagram of Hosted Applications.**/center

1. 8Interfaces
There are three base interfaces defined in this supplement, as shown in Figure 8-1. One, named Application, represents the Hosted Application, and is utilized by the Hosting System to control the Hosted Application. The second, named Host, represents the Hosting System, and is utilized by the Hosted Application to request services from and to notify the Hosting System of events during the execution of the Hosted Application. The third, named DataExchange is an interface used by both the Hosting System and the Hosted Application to communicate information about the data to be exchanged. Thus, the entire Hosted Application (ApplicationService) implementation consists of the combination of the Application and DataExchange base interfaces, while the entire Hosting System (HostService) implementation consists of the combination of the Host and DataExchange base interfaces.

The interfaces are defined as a set of methods using Web Services Description Language (WSDL). The implementers shall change the end point references (i.e., the location XML Attribute within the address XML Element within the port XML Elements of a service XML Element) in the WSDL specification as needed to deploy Hosted Applications and Hosting Systems that utilize these interfaces. 

Note:The major (non-backward compatible) versions of the interfaces are reflected in the values of the name and targetNamespace XML Attributes of the definitions XML Element in the WSDL specification of the interfaces. Any changes to the interfaces that are not backward compatible will utilize new values for name and targetNamespace XML Attributes of the definitions XML Element.

Minor (backward compatible) versions of the interfaces may be reflected in the values of the targetNamespace XML Attribute of any new schema XML Element where new input or output data types are defined in the WSDL specifications, and/or in the values of the name XML Attributes of the portType and service XML Elements where new messages and operations are associated as new services in the WSDL specifications of the interfaces. To maintain backward compatibility, the names of existing elements, messages, and operations in the WSDL specification of the interfaces remain the same.

These methods utilize a set of basic data types and more complex data structures to communicate parameters, which are defined using XML Schemas. Later sections of this document provide more detailed descriptions of the interfaces and data structures, along with sequence diagrams illustrating how the interfaces are used. 

The actual WSDL code and XML Schemas that specify this interface are defined in Annex B.

Notes:1. WSDL is a platform and programming language independent means of specifying an interface between two cooperating applications. The applications need not be written in the same programming language.

2. The interfaces do not directly address reporting of SOAP communications problems. If a problem occurs in the communications between the Hosting System and a Hosting Application during the execution of a WSDL interface call, this should be reported by the SOAP libraries utilized by an implementation, e.g., thrown as an exception.

[Image:](Image:)(Image:.md)

center**Figure 8-1 Diagram of the Interface Between the Hosting System and the Hosted Application**/center

  1. 8.1Application Interface
The following sections describe the methods of the Application interface.

    1. 8.1.1getState() : State
The Hosted Application returns its current state to the caller. 

This method may be called at any time.

Note:1. A Hosting System may use this method as an alternative to tracking Hosted Application state changes reported by the notifyStateChanged() method call.

2. A Hosting System may use this method to determine if a Hosted Application is still in operation (i.e., did not die without calling the notifyStateChanged() method with an EXIT state).

    1. 8.1.2setState(newState : State) : boolean
The Hosting System requests that the Hosted Application switch to the newState. 

The Hosted Application returns TRUE from the method if the Hosted Application received the request, and the requested state change is allowed in the state diagram. Otherwise, the method returns FALSE. A return value of TRUE does not indicate that the state of the Hosted Application has changed to the newState; it merely indicates that the requested state change is valid, and will be made at the soonest opportunity. Once the Hosted Application switches to the requested state, it shall inform the Hosting System through the notifyStateChanged() method of the Host interface.

Note:The asynchronous response to a state change is intended to minimize blocking the Hosting System while waiting for a potentially time-consuming state change in the application.

The Hosted Application shall ignore any setState() and return TRUE when the Hosted Application is already in requested state (i.e., this is a repeated call with the same state).

If the Hosted Application receives a second setState() request for a different state prior to completing a previous request, then the Hosted Application shall abort or ignore the previous request, and begin processing the latest request.

This method may be called at any time, however may not have any effect (other than a return of FALSE) if the requested new state is not an allowed transition from the current state.

    1. 8.1.3bringToFront(requestedScreenArea : Rectangle) : boolean
By calling this method, the Hosting System is asking the Hosted Application to take whatever steps are needed to make its GUI visible as the topmost window, and to gain focus. 

If possible, the Hosted Application shall resize and reposition itself to the requestedScreenArea. If requestedScreenArea is missing or null, the Hosted Application may retain its current size and location on the screen.

The method returns TRUE if the Hosted Application received the request and will act on it. Otherwise it returns FALSE.

A Hosted Application shall act on this method if the Hosted Application is in the IDLE or INPROGRESS state. A Hosted Application is not required to act on this method if the Hosted Application is not in the IDLE or INPROGRESS state. 

A Hosted Application that has no GUI (e.g. a headless analysis application), where becoming visible and gaining focus has no meaning, shall always return TRUE from this method. 

  1. 8.2Host Interface
The following sections describe the methods of the Host interface.

    1. 8.2.1generateUID() : UID
Returns a newly created DICOM UID that the Hosted Application might use, e.g., to create new data objects and structures.

This method may be called at any time.

    1. 8.2.2getAvailableScreen(appPreferredScreen : Rectangle) : Rectangle
The Hosted Application supplies its preferred screen size in the appPreferredScreen parameter. The Hosting System may utilize this information as a hint, but may return a window location and size that best suits the Hosting Systems GUI.

The method returns the window location and size that the Hosting System would prefer that the Hosted Application utilize. However, there are no requirements that the Hosted Application act on that information.

This method may be called at any time.

    1. 8.2.3getOutputLocation(preferredProtocols: ArrayOfString) : String
The method returns a URI that a Hosted Application may use to store output that it may provide back to the Hosting System (e.g. in response to a getData() call). 

The Hosted Application indicates, in order of preference, the protocols it can use to store data. The Hosted Application shall at least support both the http: and the file: protocols. The Hosting System selects the most appropriate protocol, potentially taking into account system or security considerations as well as the order of preference. The Hosting System uses the selected protocol in setting up the resources and generating the URI returned to the Hosted Application.

Notes:1. There may be limitations when using the http: protocol when compared to the file: protocol. Some functions that might work with a file: protocol such as seek, rewrite, and delete, may not work with the http: protocol. The Hosted Application should assume that it can only write once in sequential order when the returned output location uses the http: protocol.

2. If any authentication information is needed in order to access the data, this authentication information may be included in the URI.

The Hosting System shall keep the URI active while the Hosted Application is in any state other than IDLE or EXIT, or until such time that the Hosted Application returns the URI to the Hosting System (e.g. in an ObjectLocator returned to the Hosting System in response to a getData() call). The disposition of the data that the Hosted Application sends to this URI is the responsibility of the Hosting System after the Hosted Application transitions to the IDLE state or after the Hosted Application returns the URI to the Hosting System (e.g. in an ObjectLocator returned to the Hosting System in response to a getData() call). After the Hosted Application transitions to IDLE state, the Hosting System need not keep the URI active.

The Hosted Application shall only call this method if the Hosted Application is at the INPROGRESS or COMPLETED states.

    1. 8.2.4notifyStateChanged(state : State) : void
The Hosted Application shall invoke this method each time the Hosted Application successfully transitions to a new state. The new state is passed in the state parameter. 

Note:While all Hosting Systems need to accept this interface call method, they may track the current Application State in other ways, such as by polling for the state using the Application getState() method.

    1. 8.2.5notifyStatus(status : Status) : void
The Hosted Application may inform the Hosting System of notable events that occur during execution by invoking this method, passing the information in the status parameter. 

Note:The Hosting System typically would log these events to facilitate debugging. It may, at its discretion, display the information to the user.

This method may be called at any time.

  1. 8.3DataExchange Interface
The interface used to exchange information about data being transferred between a source and a recipient is the same for both the Hosting System and the Hosted Application. Implementations of the Application interface shall also include the DataExchange interface. Implementations of the Host interface shall also include the DataExchange interface. In other words, the DataExchange interface is symmetric with respect to the Hosting System and Hosting Application.

The data being exchanged between the Hosting System and the Hosted Application can either be passed as files, or may be described in models that might be queried by the recipient. 

Recipients that can parse DICOM objects are able to request the file-based methods. The sequence diagram in Figure 8.3-1 illustrates one potential exchange using the file-based methods.

[Image:](Image:)(Image:.md)

center**Figure 8.3-1 Example File-based Data Exchange Sequence**/center


The advantage of using the model-based methods is that the recipient need not know how to parse the data formats, but instead can use commonly available tools for manipulating XML Infosets to extract data from the models. 

The model-based interfaces can work with a variety of models. Particular models are identified by a UID. The models can either be an abstraction of the data, or can be a model of some native format. Models defined by the DICOM Standard are described in Annex A. Models are described as XML Infosets, even though the original data might never be actually represented in XML form. The source providing the data handles the mapping from the models back to the original data format.

Abstract models allow a recipient to work with data without regard to what its native form is. For example, data from a variety of image formats, such as DICOM, TIFF, JPEG, NIfTI, or Analyze, could be included in an abstract image model. The recipient can then work with the data even though the recipient has no knowledge of how the data was natively represented. Abstract models may have been derived from data referenced in multiple ObjectDescriptors (e.g. multiple CT slices combined into a single volume).

Abstract models generally do not include the full richness of data that is available in native representations. For example, an abstract image model derived from DICOM data normally would include references to cooked' pixel data and its spatial organization, but might not include many of the modality-specific Attributes. To allow recipients to access such details the supplier of an abstract model can provide references to the ObjectDescriptors, in the form of UUIDs, from which that abstract model was derived. The recipient may gain access to any attribute of the original data formats through the source ObjectDescriptors.

The sequence diagram in Figure 8.3-2 illustrates one potential exchange using the model-based methods. It also illustrates the Hosted Application returning partial outputs, one potential way a Hosted Application might use the getOutputLocation() method, and potential uses of the releaseModel() and releaseData() methods.

[Image:](Image:)(Image:.md)

(Continued on next page)

center**Figure 8.3-2 Example Model-based Data Exchange Sequence**/center

(Continued from previous page)

[Image:](Image:)(Image:.md)

Hosting Systems shall support both the file-based and model-based interfaces, both as a data source as well as a data recipient. 

Hosted Applications shall support at least one of the file-based or model-based interfaces, as either a data source or as a data recipient, as needed by the Hosted Application. If a Hosted Application supports the model-based interfaces, it shall support at least one of the models defined in Annex A. Hosted Applications may choose to implement only those portions of those interfaces that the Hosted Application actually uses; however, all interface methods that a Hosting System may call must be available for the Hosting System to call, even if the Hosted Application does not do anything but return appropriately.

The following sections describe the methods of the DataExchange interface.

    1. 8.3.1notifyDataAvailable(data : AvailableData, lastData : boolean) : boolean
The source of the data calls this method with descriptions of the available data that it can provide to the recipient. If the source of the data expects that additional data will become available, it shall pass FALSE in the lastData parameter. Otherwise, it shall pass TRUE in the lastData parameter, and shall not make any further calls to notifyDataAvailable until after it has transitioned through the IDLE state once more. 

The source of the data shall be able to provide the data in the form identified in the AvailableData structure. 

A Hosting System uses this method to inform a Hosted Application of input data that the Hosted Application should work with. A Hosted Application uses this method to inform the Hosting System of outputs produced by the Hosted Application.

This method returns TRUE if the recipient of the data successfully received the AvailableData list. Otherwise this method returns FALSE. 

Note:A Hosted Application that is recipient of this call, but that was unsuccessful in receiving the AvailableData list might report a reason for the failure in a notifyStatus method call.

The source of the data shall not include in AvailableData any references to data that were sent in a previous successful notifyDataAvailable call (i.e., one where the method call returned TRUE).

A Hosted Application shall not transition into the COMPLETED state if it has received or sent a notifyDataAvailable() call with a lastData indicator of FALSE. 

The source of the data may call notifyDataAvailable() with an empty data list.

Notes:Calling notifyDataAvailable() with an empty list is useful for setting the lastData indicator to TRUE.

This method shall only be called if the Hosted Application is at the INPROGRESS state.

    1. 8.3.2getData(objectUUIDs : ArrayOfUUID, acceptableTransferSyntaxUIDs : ArrayOfUID, includeBulkData : boolean) : ArrayOfObjectLocator
The recipient of data invokes this method to gain access to binary data provided by the source of the data. The source of the data provides a URI that the recipient may open as a byte stream to retrieve the data. 

Note:The provider of the data may delay the actual preparation of binary data until the recipient actually requests it.

The objectUUIDs array provides the UUIDs of the binary data that the source wishes to retrieve. Each of the UUIDs in that array are drawn either from the ObjectDescriptors provided in the AvailableData structure received by the recipient in one or more notifyDataAvailable() method calls, or from bulk data pointers in models accessed by the recipient. 

If the UUID came from an ObjectDescriptor, the source returns ObjectLocators of the binary objects using the MIME content type and class UID listed in the ObjectDescriptor within the AvailableData structure associated with each UUID. If the UUID came from a Data Exchange Model, then the source returns the binary bulk data described within the model.

The recipient lists the desired Transfer Syntax for the bulk data via the acceptableTransferSyntaxUIDs parameter. The recipient shall list in order of preference in the acceptableTransferSyntaxUIDs parameter the UIDs of the Transfer Syntaxes that it will accept for the data represented by objectUUIDs. The provider of the data shall select and use the first transfer syntax in the list that it supports. For DICOM data, the provider of data shall as a minimum support the Explicit VR Little Endian transfer syntax. The acceptableTransferSyntaxUIDs may be empty for those MIME content types where Transfer Syntax has no meaning. 

When retrieving binary data identified by a UUID from an ObjectDescriptor, if the recipient sets the includeBulkData flag to TRUE, then the source shall supply the bulk data within the data stream. Otherwise, the source may, but is not required to, omit bulk data such as pixel data.

Note:The includeBulkData flag is useful, for example, when the recipient wishes to work with the description of the pixel data in binary DICOM form, in order to decide whether or not to retrieve the pixel data itself.

The method returns one ObjectLocator for each UUID passed into the method within the objectUUIDs array. The ObjectLocator describes a file where the recipient can read in the data referred to by that particular objects UUID. 

When the recipient is finished with data referred to by an ObjectLocator URI, it may call the releaseData() method to free up the resources being consumed to provide those URIs. Any data references not explicitly released by the recipient of the data are released implicitly when the Hosted Application enters the IDLE state.

The recipient may call getData() multiple times for data referenced by a given ObjectDescriptor or bulk data UUID. Each call to getData() shall be matched by either an explicit or implicit call to releaseData().

This method shall only be called if the Hosted Application is at the INPROGRESS or COMPLETED states. A Hosting System may also call this method when the Hosted Application is in the SUSPENDED state.

    1. 8.3.3getAsModels(objectUUIDs : ArrayOfUUID, classUID : UID, supportedInfosetTypes : ArrayOfMimeType) : ModelSetDescriptor
The recipient of data invokes this method to ask that the source of the data provide the data referenced by objectUUIDs array as models of the type referenced by classUID. The objectUUIDs are drawn from the ObjectDescriptors passed to the recipient of the data in one or more notifyDataAvailable() calls.

The recipient of the data shall list in supportedInfosetTypes in order of preference the MIME types that the recipient can process as Infosets. Recipients of data shall support the text\xml MIME type, which shall always be included in the supportedInfosetTypes array. The provider of data shall select the first entry in that array that it supports.

The ModelSetDescriptor returned by this method contains the UUIDs of the models provided by the source, as well as the UUIDs of data objects referred to by the objectUUIDs array that could not be represented in the requested model.

The recipient may call getAsModels() multiple times for data referenced by a given UUID. Each successful call returns a different model UUID.

When the recipient is finished with a set of models, it may call the releaseModels() method to free up the resources being consumed to provide those models. Any models not explicitly released by the recipient of the data are released implicitly when the Hosted Application enters the IDLE state.

This method shall only be called if the Hosted Application is at the INPROGRESS or COMPLETED states. A Hosting System may also call this method when the Hosted Application is in the SUSPENDED state.

    1. 8.3.4queryModel(models : ArrayOfUUID, xpaths : ArrayOfString) : ArrayOfQueryResult
The recipient of data invokes this method to request that the source of the data return the subset of data referred to in each of the XPath query strings passed in the xpath parameter from each of the models identified by the UUIDs passed in the model array. Each of the XPath query strings is applied to each of the models referred to in the model array. 

The UUIDs passed in the model array shall be chosen from those returned by one or more getAsModels() method calls. 

The results of the query are returned by the method as XML Infosets, encoded in XML returned as a string. Each result from a particular model UUID is returned as a QueryResult element in the returned array for each xpath string. In other words, the number of QueryResults returned is the number of UUIDs in the model array times the number of XPath queries strings in the xpath array.

Note:This method is principally used when the infoset type is text\xml.

This method shall only be called if the Hosted Application is at the INPROGRESS or COMPLETED states. A Hosting System may also call this method when the Hosted Application is in the SUSPENDED state.

    1. 8.3.5queryInfoset(models : ArrayOfUUID, xpaths : ArrayOfString) : ArrayOfQueryResultInfoset
The recipient of data invokes this method to request that the source of the data return the subset of data referred to in each of the XPath query strings passed in the xpath parameter from each of the models identified by the UUIDs passed in the model array. Each of the XPath query strings is applied to each of the models referred to in the model array. 

The UUIDs passed in the model array shall be chosen from those returned by one or more getAsModels() method calls. 

The results of the query are returned by the method as XML Infosets, encoded in XML, returned as a byte array encoded in the form negotiated during the getAsModel() call.. Each result from a particular model UUID is returned as a QueryResultInfoset element in the returned array for each xpath string. In other words, the number of QueryResultInfoset structures returned is the number of UUIDs in the model array times the number of XPath queries strings in the xpath array.

Note:This method is principally used when the infoset type is not string based, for example a application\fastinfoset. If called on a model using the text\xml infoset type, a conversion from a byte array to a string would be needed.

This method shall only be called if the Hosted Application is at the INPROGRESS or COMPLETED states. A Hosting System may also call this method when the Hosted Application is in the SUSPENDED state.

    1. 8.3.6releaseData(objectUUIDs : ArrayOfUUID): void
The recipient of data invokes this method to release access to binary data provided by the source of the data through a getData() call. The ArrayOfUUID identifies the data streams that the recipient is releasing. The UUIDs in this array shall be drawn from the locator fields in ObjectLocators returned by calls to getData().

    1. 8.3.7releaseModels(objectUUIDs : ArrayOfUUID): void
The recipient of data invokes this method to release access to models provided by the source of the data. The ArrayOfUUID identifies the models that the recipient is releasing. The UUIDs in this array shall be drawn from the models fields in ModelSetDescriptors returned by calls to getAsModels().

1. 9 Data Types and Structures
  1. 9.1ArrayOf[Type](Type)
A wrapper object representing the encapsulation of an array of a specific type. Used in parameters to and return values from API functions to enable cross-platform compatibility. The wrapper contains a single field, which is an array of the type being stored. The field name is the Type name with the first letter in lowercase instead of uppercase.

Note:This construct was needed to support Microsoft� .NET language bindings even though it looks ugly in Java.

  1. 9.2AvailableData
A data structure that communicates what data is available to the recipient. The data is organized in a hierarchical fashion, communicating patients, studies, series, and finally ObjectDescriptors which identify available data objects. The fields in the data structure are:

- nowikiObjectDescriptors : ObjectDescriptor[]  An array of ObjectDescriptor data structures listing data which either applies to multiple patients, or does not fit into the patient / study / series hierarchy./nowiki
- nowikiPatients : Patient[]  An array of Patient data structures./nowiki

    1. 9.2.1ObjectDescriptor
A data structure with the following fields:

- DescriptorUUID : UUID  the UUID that the interface utilizes to track this particular data object.
- MimeType : MimeType  the MIME content type of this particular data object, in its most natural form available from the source. The most natural form is typically the form in which the source maintains the data in its database, for example a DICOM file.
- ClassUID : UID  the UID that represents the class of this data object in the form described by mimeType. For objects whose mimeType refers to a data exchange model such as those defined in Annex A, this is the UID of that model. For objects whose mimeType is application:dicom, this is the SOP Class UID of the DICOM object. This may be empty for those objects whose MIME content types have no additional classes.
- TransferSyntaxUID : UID  the UID that represents the Transfer Syntax of this data object in the form described by mimeType. This may be empty for those objects of a MIME content type where Transfer Syntax has no meaning.
- Modality : String  the modality that best represents where this data originated from. Standard values are drawn from the Defined Terms listed for the Modality (0008,0060) Attribute in the PS3.3 General Series Module (section C.7.3.1.1.1).

    1. 9.2.2Patient
A data structure that communicates data for a particular patient. The fields in the data structure are:

- Name : String  The name of the patient, formatted as described for the PN VR in PS3.5.. For DICOM SOP Instances this is the value of the Patients Name (0010,0010) Attribute.
- ID : String  A string used as the identifier for a particular patient, formatted as described for the LO VR in PS3.5. For DICOM SOP Instances this is the value of the Patient ID (0010,0020) Attribute.
- AssigningAuthority : String  The organization who assigned the id to the patient, formatted as described for the LO VR in PS3.5. For DICOM SOP Instances this is the value of the Issuer of Patient ID (0010,0021) Attribute.
- Sex : String  The sex of the patient. For DICOM SOP Instances this is the value of the Patients Sex (0010,0040) Attribute. In all other cases it shall take on the values permissible for the DICOM Sex (0010,0040) Attribute.
- BirthDate: String The birth date of the patient, formatted as described for the DA VR in PS3.5. For DICOM SOP Instances this is the value of the Patients Birth Date (0010,0030) Attribute.
- nowikiObjectDescriptors : ObjectDescriptor[]  An array of ObjectDescriptor data structures listing data which applies to this patient, but which do not apply to any particular study of this patient./nowiki
- nowikiStudies : Study[]  An array of Study data structures./nowiki

At least one of objectDescriptors or studies shall be present.

    1. 9.2.3Study
A data structure that communicates data for a particular study. The fields in the data structure are:

- StudyUID : UID  The UID of the study. For DICOM SOP Instances this is the value of the Study Instance UID (0020,000D) Attribute.
- nowikiObjectDescriptors : ObjectDescriptor[]  An array of ObjectDescriptor data structures listing data which applies to this study (within the enclosing patient), but which do not apply to any particular series within this study./nowiki
- nowikiSeries : Series[]  An array of Series data structures./nowiki

    1. 9.2.4Series
A data structure that communicates data for a particular series. The fields in the data structure are:

- SeriesUID : UID  The UID of the series. For DICOM SOP Instances this is the value of the Series Instance UID (0020,000E) Attribute.
- ObjectDescriptors : ObjectDescriptor  An array of ObjectDescriptor data structures listing data existing in this series (within the enclosing Study, within the enclosing Patient).

Note:Most DICOM Composite SOP Instances would be identified by objectDescriptors at the Series level.

  1. 9.3MimeType
A data type whose values are Defined Terms that identify particular MIME content types. The syntax of the string defining a MIME content type is defined in IETF RFC 2045. Top level MIME content types are defined in IETF RFC 2046. MIME content types are drawn from the list managed by the Internet Assigned Numbers Authority (IANA) whose web site is at [http://www.iana.org/assignments/media-types/](http://www.iana.org/assignments/media-types/)(http://www.iana.org/assignments/media-types/), as described in IETF RFC 2048. 

  1. 9.4ModelSetDescriptor
A data structure returned from the getAsModels() method with the following fields:

- InfosetType : MimeType  the MIME type of the infoset, selected by the source of the data from the list passed to it by the recipient in a getAsModels() call.
- nowikiModels : UUID[]  an array of UUIDs referring to models that have been created from the set of data objects referred to by the array of UUIDs passed into the getAsModels() call./nowiki
- nowikiFailedSourceObjects : UUID[]  an array of UUIDs designating data objects referred to the array of UUIDs passed into the getAsModels() call that could not be represented in the requested model class./nowiki

Note:For example, if the array of UUIDs passed into the getAsModels() call includes 100 CT slices from the same frame of reference (i.e., a volume stack), plus 1 GSPS object, and if the caller requested an Abstract Multi-Dimensional Image model, then the ModelSetDescriptor returned by GetAsModels() would include one UUID in the models array, identifying the CT volume image data created from the 100 CT slices, and one UUID in the failedSourceObjects array, specifying the UUID for the GSPS object.

  1. 9.5ObjectLocator
A data structure that represents the location from which the recipient of a data object can retrieve that object. It consists of the following fields:

- Locator : UUID  the UUID that the interface utilizes to track this particular ObjectLocator.
- Source : UUID  the UUID of the source that is supplying data for this ObjectLocator. This UUID matches the UUID in the ObjectDescriptor if trying to retrieve the data in its natural form (e.g., as a file or byte stream). This UUID matches the UUID in a bulk data pointer when retrieving bulk data from a model.

- TransferSyntax : UID  the transfer syntax in which this data is encoded, selected by source of the data from the list passed in by the recipient of the data in the acceptableTransferSyntaxUIDs parameter of the getData() call. This may be empty for those objects of a MIME content type where Transfer Syntax has no meaning.
- Length: long  the length of the data object referred to by the UUID.
- Offset: long  the offset within the file or byte stream where the data object begins.
- URI: URI  the URI that identifies the resource from which the recipient might retrieve the data object, typically but not limited to a file on the local file system. The recipient shall be able to access the data within the object using file IO or memory mapping.

  1. 9.6QueryResult
A data structure that holds the results from an XPath query of a model. It consists of the following fields:

- Model : UUID  the UUID of the model from which this result came.
- XPath : String  the XPath query string that led to this result.
- nowikiResults : XPathNode[]  an array of XPathNodes holding the query results./nowiki

  1. 9.7QueryResultInfoset
A data structure that holds the results from an XPath query of a model. It consists of the following fields:

- Model : UUID  the UUID of the model from which this result came.
- XPath : String  the XPath query string that led to this result.
- nowikiResults : XPathNodeInfoset[]  an array of XPathNodeInfoset structures holding the query results./nowiki

  1. 9.8Rectangle
A data structure that defines a rectangular region on a display screen. The fields in the data structure are:

- RefPointX : int
- RefPointY : int

that define the location of the top left corner of the region in screen coordinates, and

- Width : int
- Height : int

that specify the extents of the region. Screen coordinates are defined starting from an origin of 0,0 in the upper left corner of the screen, and extend in the positive direction down and to the right.

  1. 9.9State
State is an enumerated data type with the following values:

- IDLE
- INPROGRESS
- COMPLETED
- SUSPENDED
- CANCELED
- EXIT

The interpretation of these enumerated values is defined in section 7.2 States.

  1. 9.10Status
A data structure with the following fields:

- StatusType : StatusType  the severity level of this status message. 
- CodingSchemeDesignator : String  the coding scheme in which the codeValues are defined. The use of codeValue shall be consistent with the use of the DICOM Code Value (0008,0100) Attribute as specified in PS3.3.
- CodeValue : String  the particular code value within the designated coding scheme that represents the nature of this status message. The use of message shall be consistent with the use of the DICOM Code Meaning (0008,0104) Attribute as specified in PS3.3.
- CodeMeaning : String  a displayable string for the code value. The use of message shall be consistent with the use of the DICOM Code Meaning (0008,0104) Attribute as specified in PS3.3.
- Any other field from the Coded Terminology macro defined in Section 10.1.

    1. 9.10.1StatusType
An enumerated data type with the following values and definitions:

- INFORMATION  the status is for informational purposes only.
- WARNING  indicates a condition that might impact the speed or quality of the work done by the Hosted Application, but that does not prevent the Hosted Application from completing its task.
- ERROR  indicates a condition that might prevent the Hosted Application from correctly completing its task. The Hosted Application will attempt to continue.
- FATALERROR  indicates a condition that prevents the Hosted Application from completing its task. The Hosted Application will not attempt to continue, and will transition automatically to the CANCELED state.

  1. 9.11UID
A string of period-separated digits representing a Unique Identifier (see PS3.5), formatted as described for the UI VR in PS3.5.

  1. 9.12UUID
A string representing a Universally Unique Identifier as defined in ITU-T Recommendation X.667, using the hexadecimal representation form.

  1. 9.13XPathNode
A data structure with the following fields, which represents the output from an XPath query of a model, returned in a string-based representation.

- NodeType : XPathNodeType
- Value : String

  1. 9.14XPathNodeInfoset
A data structure with the following fields, which represents the output from an XPath query of a model returned in a byte array representation.

- NodeType : XPathNodeType
- nowikiInfosetValue : byte[] /nowiki

  1. 9.15XPathNodeType
An enumeration of the types of results that may come back from an XPath query.

Note:This enumeration is compatible with a similar enumeration utilized in the Microsoft .NET framework.

- Root  the result is the top level node of the XML Infoset (i.e., the result is the entire XML Infoset).
- Element  the result is an XML Element within the XML Infoset (i.e., the result is a subset of the XML Infoset).
- Attribute  the result is an XML Attribute of an XML Element within the XML Infoset.
- Text  the result is the textual content of an XML Element within the XML Infoset. Equivalent to the Document Object Model (DOM) Text and CDATA node types. Contains at least one character.
- SignificantWhitespace  the result is the content of an XML Element within the XML Infoset, where the content consists only of significant whitespace (e.g., xml:space was set to preserve). White space code points are SPACE (U0020), TAB (U0009), CARRIAGE RETURN (U000D), or LINE FEED (U000A) of ISO 10646 (Unicode).
- Whitespace  the result is the content of an XML Element within the XML Infoset, where the content consists only of whitespace. White space code points are SPACE (U0020), TAB (U0009), CARRIAGE RETURN (U000D), or LINE FEED (U000A) of ISO 10646 (Unicode).
- Comment  the result is a comment within the XML Infoset.
- Namespace  the result is a namespace directive within the XML Infoset.
- ProcessingInstruction  the result is a processing instruction within the XML Infoset.
- All  the result may contain any of the types defined in XPathNodeType.

1. 10Data Exchange Model Conventions
Models that can be used by the model-based DataExchange interface methods are defined in Annex A. These models are defined in the form of XML Schemas written in Relax NG Compact form of DSDL as specified by ISO/IEC 19757. 

Note:An implementer may translate the Relax NG Compact form to other forms for use within their implementation as long as the exchanged XML Infosets will validate against the schema specified by the standard. For example, a particular implementation may internally utilize a schema with stronger validation rules (e.g. using Schematron rules as specified in ISO/IEC 19757, or using XSDL with assertion rules) as long as the XML produced for exchange over the interface can be parsed with the schema specified in the standard, and that XML from well-formed DICOM objects produced by the schema specified in the standard can still be utilized by the implementation's internal schema.

Actual instances of the models are XML Infosets. Annex A follows the following conventions in describing models.

Notes:1. The models are defined via XML schemas to allow the use of commonly available tools to manipulate and navigate the model. For example, an XPath statement can be used to identify portions of interest within the model such as a particular DICOM Attribute and extract it.

2. Some implementations may parse directly from the incoming object, which may not be in XML form, into an internal representation, such as the domain object model (DOM) without ever having converted the object to XML.

Within each model description is a table of XML Elements and XML Attributes used to describe an XML Infoset of that model. These tables utilize the following conventions:

XML Element names (listed in the first column) are in CamelCase, with the first letter capitalized.

XML Attribute names (listed in the first column) are in camelCase with the first letter in lower case.

XML Element and XML Attribute names with a set of  characters in front of them are nested within the first preceding XML Element with one fewer  characters in front of its name. A nested XML Attribute is associated with the immediately enclosing XML Element.

The entries in the Optionality column have the following interpretations:

R indicates that the XML Element or XML Attribute is required in all models.

C indicates that the XML Element or XML Attribute is required in all models if the condition stated in the Description is met.

O indicates that the XML Element or XML Attribute is optional.

If the XML Element or XML Attribute is nested inside another XML Element, and that enclosing XML Element is not present (i.e. it is defined with an Optionality of O and is not present in the XML Infoset, or it is defined with an Optionality of RC and is not included in the XML Infoset because the condition was not met), then the nested XML Element or XML Attribute shall not be present in the XML Infoset irrespective of its optionality.

The entries in the Cardinality column have the following interpretations:

A indicates that this is represented as an XML Attribute instead of an XML Element, hence has a cardinality of 1 by definition.

1 indicates that only a single instance of this XML Element is included inside the immediately enclosing XML Element, or at the top level if this XML Element is not nested inside another XML Element.

0-n indicates that zero to n instances of this XML Element are included inside the immediately enclosing XML Element, or at the top level if this XML Element is not nested inside another XML Element.

1-n indicates that one to n instances of this XML Element are included inside the immediately enclosing XML Element, or at the top level if this XML Element is not nested inside another XML Element.

Sets of XML Elements and XML Attributes that are often repeated within models may be defined as macros. Macros that may have general applicability are defined in this section. Macros that are unique to a particular model may be defined in the Annex specific that model. When a macro is included within a table, it is as if the contents of the Macros table were inserted within the table referencing the macro. Any set of  characters in front of the directive to include a Macro in the table are prepended to the XML Element and XML Attribute names listed in the Macros table.


  1. 10.1Coded Terminology
Models may make use of coded terminology. The representation of coded terminology in DICOM is described in PS3.3. Specific terminology of interest, organized in Context Groups in PS3.16, can be referenced using the following macro.

center**Table 10.1-1 Coded Terminology Macro**/center


{| style="border-spacing:0;"
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Name**/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Optionality**/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Cardinality**/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Description**/center

|-
| colspan="4"  style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *BASIC CODED ENTRY ATTRIBUTES*

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CodeValue
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The particular code value identifying the referenced term or concept. See PS3.3 Section 8.1.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CodingSchemeDesignator
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Designates the coding scheme in which the codeValue is defined. See PS3.3 Section 8.2.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CodingSchemeVersion
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| See PS3.3 Section 8.2. Required if the codingSchemeDesignator is not sufficient to identify the codeValue.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CodeMeaning
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 0-1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A brief human readable description of what the coded value means. See PS3.3 Section 8.3.

|-
| colspan="4"  style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *ENHANCED ENCODING MODE*

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| ContextIdentifier
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 0-1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Identifies a Context Group defined within a Mapping Resource from which the values of codeValue and codeMeaning were selected or have been added as a Private Context Group extension See PS3.3 Sections 8.6 and 8.7.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| MappingResource
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| See PS3.3 Section 8.4. Required if the contextIdentifier XML Attribute is present.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| ContextGroupVersion
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| See PS3.3 Section 8.5. Required if the contextIdentifier XML Attribute is present.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| ContextGroupExtensionFlag
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 0-1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Indicates whether the codeValue/codingScheme/codeMeaning is selected from a private extension of the Context Group identified in the contextIdentifier XML Attribute. (See PS3.3 Section 8.7. 

Enumerated Values: Y, N.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| ContextGroupLocalVersion
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| See PS3.3 Section 8.7.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| ContextGroupExtensionCreatorUID
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Identifies the person or organization who created an extension to the Context Group. See PS3.3 Section 8.7.

Required if the value of contextGroupExtensionFlag is "Y".

|}
  1. 10.2Person Name Components
The Person Name Components follow the definitions given in PS3.5 of the DICOM Standard. The PS3.5 description of the usage of Person Name Components also applies to this macro.

center**Table 10.2-1 Person Name Components Macro**/center


{| style="border-spacing:0;"
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Name**/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Optionality**/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Cardinality**/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Description**/center

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| FamilyName
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 0-1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The persons family or last name. See the description of the PN VR in DICOM PS3.5.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| GivenName
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 0-1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The persons given or first names. See the description of the PN VR in DICOM PS3.5.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| MiddleName
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 0-1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The persons middle names. See the description of the PN VR in DICOM PS3.5.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| NamePrefix
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 0-1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The persons name prefix. See the description of the PN VR in DICOM PS3.5.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| NameSuffix
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 0-1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The persons name suffix. See the description of the PN VR in DICOM PS3.5.

|}
1. Annex A Data Exchange Models
  1. A.1Native DICOM Model
    1. A.1.1Usage
The Native DICOM Model defines a representation of binary-encoded DICOM SOP Instances as XML Infosets that allows a recipient of data to navigate through a binary DICOM data set using XML-based tools instead of relying on toolkits that understand the binary encoding of DICOM. 

Note:It is not the intention that this form be utilized as the basis for other uses. This form does not take advantage of the self-validation features that could be possible with a pure XML representation of the data.

With the exception of padding, a data source that is creating a new instance of a native DICOM Model (e.g. the result from some analysis application) shall follow the DICOM encoding rules (e.g. the handling of character sets) in creating Values for the DicomAttributes within the instance of the DICOM Native Model.

A data recipient that converts data from an instance of the Native DICOM Model back into a binary encoded DICOM object shall adjust the padding as necessary to meet the encoding rules specified in DICOM PS3.5.

    1. A.1.2Identification
The ObjectDescriptors MIME content type for the Native DICOM Model shall be application/x-dicom.native.

The ObjectDescriptors class UID for the Native DICOM Model shall be 1.2.840.10008.7.1.1.

    1. A.1.3Support
Support of the Native DICOM Model as both a data source and a data recipient shall be required of all Hosting Systems implementing the interface.

Support of the Native DICOM Model as either a data source or a data recipient shall be optional for all Hosted Applications implementing the interface. 

    1. A.1.4Information Model
A diagram of the Native DICOM Model appears in Figure A.1.4-1.

[Image:](Image:)(Image:.md)

center**Figure A.1.4-1 Native DICOM Model**/center

    1. A.1.5Description
center**Table A.1.5-1 Native DICOM Model**/center


{| style="border-spacing:0;"
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Name**/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Optionality**/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Cardinality**/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Description**/center

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| NativeDicomModel
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| An Infoset (as defined in W3C Recommendation XML Information Set http://www.w3.org/TR/xml-infoset/) representing the content of a DICOM Data Set (as defined in PS3.5), which may be either:

- the contents of an entire DICOM Composite Instance (as defined in PS3.3) in response to a native model request, or

- the contents of part of a DICOM Composite Instance in response to a query on a native model, or

- the contents of a Sequence Item (as defined in PS3.5), recursively included within an Infoset Value element.

The directive xml:space=preserve shall be included.

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *Include DICOM DataSet Macro Table A.1.5-2*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 

|}
center**Table A.1.5-2 DICOM Data Set Macro**/center


{| style="border-spacing:0;"
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Name**/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Optionality**/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Cardinality**/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Description**/center

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| DicomAttribute
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 0-n
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| An Infoset element corresponding to each DICOM Attribute.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| keyword
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The keyword as defined in PS3.6.

Required unless the DICOM Data Element is unknown to the host.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| tag
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The four-digit zero-padded hexadecimal values of the Group and Element Numbers of the Data Element Tag, concatenated as a single string without a delimiter. E.g., Data Element (0010,0020) would have a tag of 00100020.

For Private Data Elements, the two most significant hexadecimal characters of the Element Number shall be 00, since the Private Creator is explicitly conveyed and the block used in the DICOM encoding shall not be sent (i.e., a Private Data Element has the form gggg00ee).

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| vr
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The Value Representation of this element, represented as a two character uppercase string, as defined in PS3.5 and specified for this Data Element in PS3.6. 

Note:Implementations may utilize the Value Representation to validate data values, if desired.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| privateCreator
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The value of the Private Creator Data Element corresponding to the block in which this Private Data Element is used.

Required for Private Data Elements. Shall not be present otherwise (i.e., for Data Elements defined by the DICOM Standard).

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Value
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1-n
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A Value from the Value Field of the DICOM Data Element. There is one Infoset Value element for each DICOM Value or Sequence Item.

Required if the DICOM Data Element represented is not zero length and an Item, PersonName, or BulkData XML element is not present. Shall not be used if the VR of the enclosing Attribute is either SQ or PN. 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| number
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The order in which the Value occurs within the DICOM Value Field, as a number monotonically increasing starting from 1 by 1.

Note:The Number XML Attribute is used to preserve the original order.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *plain character data*
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A single DICOM value encoded as plain character data.

E.g., a DICOM Decimal String Value Field that contained two delimiter-separated values, e.g., 0.5\0.4 would be encoded as two Infoset Value elements: nowikiValue number="1"0.5/Value /nowiki nowikiValue number="2"0.4/Value/nowikiA Code String Value Field that containing three delimiter-separated values, the second of which was zero length, MPG\\XR3, would be encoded as:  nowikiValue number="1MPG/Value /nowiki nowikiValue number=2/Value /nowiki nowikiValue number=3XR3/Value/nowikiContrast the latter example with a zero length Value Field, in which case there would be no Infoset Value elements at all.

The character encoding is that declared for the Infoset, regardless of any DICOM Specific Character Set, and any necessary translation from the DICOM Specific Character Set to the Infoset character encoding shall have been performed.

Note:This translation might not be completely lossless, particularly with Asian character sets.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Item
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1-n
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A DICOM sequence item, in other words a nested DICOM Data Set.

Required if the DICOM Data Element represented is a Sequence (has a VR of SQ) and is not zero length. Not allowed otherwise.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| number
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The order in which the Item occurs within a Sequence of Items, as a number monotonically increasing from 1 by 1.

Note:The Number XML Attribute is used to preserve the original order.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *Include Include DICOM Data Set Macro Table A.1.5-2*
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Recursively includes the Data Set corresponding to a Sequence Item.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| PersonName
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1-n
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A parsed representation in XML of a DICOM Data Element containing a name (i.e., whose VR is PN). 

Note:Parsing Attributes with a VR of PN into an XML representation of the name groups and components simplifies the creation of XPath statements to pull only portions of names out of the DICOM data.

Required if the DICOM Data Element represented has a VR of PN and is not zero length. Not allowed otherwise.

The rules defined in DICOM PS3.5 on the usage of the Alphabetic, Ideographic, and Phonetic groups of name components within a DICOM Attribute with a Value Representation of PN apply.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| number
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The order in which the PersonName occurs within the DICOM Value Field, as a number monotonically increasing from 1 by 1.

Note:The Number XML Attribute is used to preserve the original order.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Alphabetic
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 0-1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A group of name components that are represented in alphabetical characters. (See the definition for the Value Representation of PN in DICOM PS3.5.)

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| * Include Person Name Component Macro Table 10.2-1*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Ideographic
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 0-1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A group of name components that are represented in ideographic characters. (See the definition for the Value Representation of PN in DICOM PS3.5.)

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| * Include Person Name Component Macro Table 10.2-1*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Phonetic
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 0-1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A group of name components that are represented in phonetic characters. (See the definition for the Value Representation of PN in DICOM PS3.5.)

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| * Include Person Name Component Macro Table 10.2-1*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| BulkData
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A reference to a blob of data that the recipient may retrieve through use of the GetData() method. 

Required if the DICOM Data Element represented is not zero length and an XML Infoset Value, Item, or PersonName element is not present.

The provider of the data may use a BulkData reference at its discretion to avoid encoding a large DICOM Value Field as text by value in the Infoset. For example, a provider may include large binary values such as pixel data or look up tables, which typically would be located in a file, as BulkData references.

Note that there is a single BulkData Infoset element representing the entire Value Field, and not one per Value in the case where the Value Multiplicity is greater than one. E.g., a LUT with 4096 16 bit entries that may be encoded in DICOM with a Value Representation of OW, with a VL of 8192 and a VM of 1, or a US VR with a VL of 8192 and a VM of 4096 would both be represented as a single BulkData element.

All rules (e.g. byte ordering and swapping) in DICOM PS3.5 apply. 

Note:Implementers should in particular pay attention the PS3.5 rules regarding the value representations of OW and OF.

If the BulkData has a string or text Value Representation, the value(s) of the DICOM Specific Character Set Data Element, if present, might be necessary to determine its encoding.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| UUID
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| An identifier of this bulk data reference formatted as a UUID using the hexadecimal representation defined in ITU-T Recommendation X.667,..

|}
    1. A.1.6Schema
The Normative version of the XML Schema for the Native DICOM Model follows:

default namespace="http://dicom.nema.org/PS3.19/models/NativeDICOM"


nowiki# This schema was created as an intermediary, a means of describing/nowiki

nowiki# native binary encoded DICOM objects as XML Infosets, thus allowing /nowiki

nowiki# one to manipulate binary DICOM objects using familiar XML tools. /nowiki

nowiki# As such, the schema is designed to facilitate a simple, mechanical,/nowiki

nowiki# bi-directional translation between binary encoded DICOM and XML-like /nowiki

nowiki# constructs without constraints, and to simplify identifying portions /nowiki

nowiki# of a DICOM object using XPath statements./nowiki

nowiki#/nowiki

nowiki# Since this schema has minimal type checking, it is neither intended /nowiki

nowiki# to be used for any operation that involves hand coding, nor to /nowiki

nowiki# describe a definitive, fully validating encoding of DICOM concepts/nowiki

nowiki# into XML, as what one might use, for example, in a robust XML /nowiki

nowiki# database system or in XML-based forms, though it may be used/nowiki

nowiki# as a means for translating binary DICOM Objects into such a form/nowiki

nowiki# (e.g. through an XSLT script)./nowiki


start = element NativeDicomModel { DicomDataSet }


nowiki# A DICOM Data Set is as defined in PS3.5. /nowikiIt does not appear 

nowiki# as an XML Element, since it does not appear in the binary encoded /nowiki

nowiki# DICOM objects. /nowikiIt exists here merely as a documentation aid. 

DicomDataSet = DicomAttribute*


DicomAttribute = element DicomAttribute {

Tag, VR, Keyword?, PrivateCreator?, 

( BulkData | Value+ | Item+ | PersonName+ )? 

} 

BulkData = element BulkData{ UUID } 

Value = element Value { Number, xsd:string }

Item = element Item { Number, DicomDataSet }

PersonName = element PersonName {

Number,

element SingleByte { NameComponents }?,

element Ideographic { NameComponents }?,

element Phonetic { NameComponents }?

}


NameComponents =

element FamilyName {xsd:string}?,

element GivenName {xsd:string}?,

element MiddleName {xsd:string}?,

element NamePrefix {xsd:string}?,

element NameSuffix {xsd:string}?


nowiki# keyword is the attribute tag from PS3.6 /nowiki

nowiki# (derived from the DICOM Attribute's name)/nowiki

Keyword = attribute keyword { xsd:token }

nowiki# canonical XML definition of Hex, with lowercase letters disallowed/nowiki

nowikiTag = attribute tag { xsd:string{ minLength="8" maxLength="8" pattern="[0-9A-F](0-9A-F){8}" } } /nowiki

VR = attribute vr { "AE" | "AS" | "AT"| "CS" | "DA" | "DS" | "DT" | "FL" | "FD" 

| "IS" | "LO" | "LT" | "OB" | "OF" | "OW" | "PN" | "SH" | "SL" 

| "SQ" | "SS" | "ST" | "TM" | "UI" | "UL" | "UN" | "US" | "UT" }

PrivateCreator = attribute privateCreator{ xsd:string }

UUID = attribute uuid { xsd:string }

Number = attribute number { xsd:positiveInteger } 


    1. A.1.7Examples
Here is an example XPath query to extract the code meaning of the first item in the View Code Sequence:

nowiki/DicomNativeModel/DicomAttribute[@keyword=ViewCodeSequence](@keyword=ViewCodeSequence)/Item[@number=1](@number=1)/ /nowikinowiki/DicomAttribute[@keyword=CodeMeaning](@keyword=CodeMeaning)/Value[@number=1](@number=1)/nowiki

  1. A.2Abstract Multi-Dimensional Image Model
    1. A.2.1Usage
The Abstract Multi-Dimensional Image Model can be used to refer to a discretely-sampled, multi-dimensional image data. The sample values may either be single-valued (a scalar) or a vector of values (a vector). An example would be a time varying series of three dimensional images set at multiple energy levels. The Abstract Multi-Dimensional Image Model is patterned after the Enhanced Multi-frame family of DICOM objects. In mathematical terms, this is any data set that is defined by a function *I (x,y,z,t,)*, where *(x,y,z,t,)* are the dimensions, and the sample value of *I* is either a vector of components or a scalar (i.e., a single component). The primary purpose of this model is to allow applications to process image data without concern as to the underlying format of the data.

When converting DICOM SOP Instances into Abstract Multi-Dimensional Image Models, a provider of data shall follow these rules as closely as it practically can:

Note:Deterministic behavior is not expected nor guaranteed when making conversions between DICOM SOP Instances and Abstract Multi-Dimensional Image Models. For example, given the same DICOM SOP Instances, different Hosting Systems may create Abstract Multi-Dimensional Image Models that differ in some details, such as the Units of the Component values or in the Dimensions.

1. Multiple DICOM SOP Instances from the same series that have the same Frame of Reference UID shall be combined into a single instance of the Abstract Multi-Dimensional Image Model. DICOM SOP Instances from multiple series that have the same Frame of Reference UUID may be combined into a single instance of the Abstract Multi-Dimensional Image Model, if appropriate.
1. A single DICOM SOP Instance shall not be divided into multiple instances of the Abstract Multi-Dimensional Image Model.
1. The coordinate system utilized within the Abstract Multi-Dimensional Image Model shall use the coordinate system defined by the DICOM objects utilized in the creation of the Abstract Multi-Dimensional Image Model instance if applicable. Where practical, the coordinate system and Dimension definitions utilized within the Abstract Multi-Dimensional Image Model shall be chosen such that interpolation is not required to covert the source data into the Abstract Multi-Dimensional Image Model.

Note:Interpolation may be necessary if the source data is not laid out on a frame-based Cartesian coordinate grid.

1. Spatial coordinates, such as Image Position (Patient) (0020,0032), shall be transformed into the coordinate system utilized within the Abstract Multi-Dimensional Image Model instance.
1. The Pixel Data shall be spatially transformed as needed to match the Semantics and Units of the Dimensions of the Abstract Multi-Dimensional Image Model into which the pixels values are being placed.
1. Any embedded overlays within the Pixel Data (7FE0,0010) Attribute shall be stripped out of the pixel values and the pixel values sign extended or converted as needed to match the Datatype of the Component of the Abstract Multi-Dimensional Image Model into which the pixels values are being placed.
1. The pixel values of the Pixel Data shall be transformed as needed to match the Semantics and Units of the Component of the Abstract Multi-Dimensional Image Model into which the pixels values are being placed.

Note:Typically presentation settings such as VOI and Presentation LUTs are not used in creating Abstract Multi-Dimensional Image Models from DICOM SOP Instances. The exception is when the application of such LUTs is needed to match the Semantics and Units of the Component. Modality LUTs or Rescale Slope and Intercept often must be applied to match the Semantics and Units of the Abstract Multi-Dimensional Image Model.

Any pixel values that correspond to the pixel padding values shall be stripped out (i.e. set to zero or other suitable replacement value) and the spatially corresponding values in the PixelMapOfValidData shall be set to the outValue or something other than the inValue, as appropriate. 

When converting data within an instance of the Abstract Multi-Dimensional Image Models into DICOM SOP Instances, the recipient of an abstract model instance shall convert the pixel data back into values compatible with the native form of the DICOM SOP Instances being created. This conversion may include recreating Modality LUT information, inserting pixel padding values, converting pixel spacing and origins, etc. as dictated by the SOP Class the data is being converted to. When converting a single Abstract Multi-Dimensional Image Model into multiple DICOM SOP Instances, the DICOM SOP Instances shall all have the same Frame of Reference UID (0020,0052), if permitted by the SOP Class.

    1. A.2.2Identification
The ObjectDescriptors MIME content type for the Abstract Multi-Dimensional Image Model is application/x-dicom.abstract.

Note:This is an experimental MIME type. A formal MIME type will be applied for. Implementations will be expected to support both the experimental and formal MIME type going forward without a version change to the interface.

The ObjectDescriptors class UID for the Abstract Multi-Dimensional Image Model is 1.2.840.10008.7.1.2.

    1. A.2.3Support
Support of the Abstract Multi-Dimensional Image Model as both a data source and a data recipient is required of all Hosting Systems implementing the interface.

Support of the Abstract Multi-Dimensional Image Model as either a data source or a data recipient is optional for all Hosted Applications implementing the interface. 

    1. A.2.4Information Model
A diagram of the Abstract Multi-Dimensional Image Model appears in Figure A.2.4-1.


[Image:](Image:)(Image:.md) 

center**Figure A.2.4-1 Abstract Multi-Dimensional Image Model**/center

    1. A.2.5Description
center**Table A.2.5-1 Abstract Image Model**/center


{| style="border-spacing:0;"
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Name**/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Optionality**/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Cardinality**/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center**Description**/center

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| AbstractImageDataSet
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The top level element required of all abstract image models, holding the entire abstract image Data Set. 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Component
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1-n
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Describes a component of the function output. If the output is a scalar, there is only one Component. Vector outputs require a Component for each position in the vector. When there are multiple components, the components appear in each value in the order defined by their respective idNumbers.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| idNumber
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Identifies this particular component, with numbering monotonically increasing from 1. 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| datatype
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Describes how this component value is represented. Enumerated values are:

SIGNED_INT8SIGNED_INT16SIGNED_INT32UNSIGNED_INT8UNSIGNED_INT16UNSIGNED_INT32FLOAT32FLOAT64

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| minValue
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The minimum value that this component takes on. If this XML Attribute is missing, this is the minimum value that can be represented by the Datatype.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| maxValue
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The maximum value that this component takes on. If this XML Attribute is missing, this is the maximum value that can be represented by the Datatype.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Semantics
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A coded value describing what this component represents.

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| * Include Coded Terminology Macro Table 10.1-1*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Defined Context ID is 7180.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Unit
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A coded value describing what units this dimension is in.

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| * Include Coded Terminology Macro Table 10.1-1*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Defined Context ID is 7181.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Dimension
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1-n
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Describes a dimension.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| idNumber
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Identifies this particular dimension, with numbering starting from 1. Dimensions with a lower idNumber vary faster than those with a higher idNumber. 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| numberOfSamples
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The number of samples in this dimension, for example: the number of columns along the X-axis, the number of rows along the Y-axis, the number of slices along the Z-axis,the number of qualitative descriptions. 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Semantics
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A coded value describing what this dimension represents.

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| * Include Coded Terminology Macro Table 10.1-1*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Defined Context ID is 7182

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"|  Regular
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Used to describe regularly spaced samples in this dimension. Required if neither Irregular nor Qualitative are present. Shall not be present otherwise.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| width
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The sample width.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| spacing
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The sample spacing.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Unit
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A coded value describing what units the sample width and spacing are in.

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| * Include Coded Terminology Macro Table 10.1-1*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Defined Context ID is 7183.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| AxisDirection
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The direction of the axis of this dimension. 

Note:This XML Element might only be applicable to spatial dimensions, such as those dealing with linear displacement. Typically this is in relationship to the patient.

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| * Include Coded Terminology Macro Table 10.1-1*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Defined Context ID is 7184

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| AxisOrientation
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The orientation of the axis of this dimension along which values are increasing.

Note:This XML Element might only be applicable to spatial dimensions, such as those dealing with linear displacement. Typically this is in relationship to the patient.

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| * Include Coded Terminology Macro Table 10.1-1*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Defined Context ID is 7185

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Irregular
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Used to describe irregularly spaced samples in this dimension. Required if neither Regular nor Qualitative are present. Shall not be present otherwise.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| origin
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The reference location from which each of the sample locations are measured.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| SampleLocation
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1-n
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Describes the locations of each sample as an offset from the origin. There shall be numberOfSamples SampleLocation XML Elements in this sequence.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| index
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The index value of this sample location, with numbering starting from 1 and increating to numberOfSamples.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| width
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The sample width.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| distanceToOrigin
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The distance of this sample location from the Origin location.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Unit
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A coded value describing what units the sample widths and locations are in.

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| * Include Coded Terminology Macro Table 10.1-1*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Defined Context ID is 7183.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| AxisDirection
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The direction of the axis of this dimension.

Note:This XML Element might only be applicable to spatial dimensions, such as those dealing with linear displacement. Typically this is in relationship to the patient.

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| * Include Coded Terminology Macro Table 10.1-1*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Defined Context ID is 7184

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| AxisOrientation
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The orientation of the axis of this dimension along which values are increasing.

Note:This XML Element might only be applicable to spatial dimensions, such as those dealing with linear displacement. Typically this is in relationship to the patient.

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| * Include Coded Terminology Macro Table 10.1-1*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Defined Context ID is 7185

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Qualitative
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Used to describe a qualitative dimension. Required if neither Regular nor Irregular are present. Shall not be present otherwise.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Sample
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1-n
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Description of what each sample along this dimension represents. There shall be numberOfSamples Sample XML Elements in this sequence.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| index
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The index value of this sample, with numbering starting from 1 and increasing to numberOfSamples.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Semantics
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A coded value describing what this sample represents.

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| * Include Coded Terminology Macro Table 10.1-1*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Defined Context ID is 7186

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Origin
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 0-n
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Specifies the spatial position in the coordinate system of the Abstract Multi-Dimensional Image Model of the spatial frames or volumes of image data values. Different frames or volumes may either share an origin, or have a different origin for each frame or volume. If there is only a single Origin XML element within this Dimension, then this Origin applies to all samples along this Dimension. Otherwise, there shall be numberOfSamples Origin XML elements, one for each sample along this Dimension. Sample index values for Dimensions whose idNumbers are less than this Dimensions idNumber, are all equal to 1. 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| index
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Index of the sample to which this Origin,. If this is a single Origin that applies to all samples along this Dimension, then index shall either be left out or given a value of 0 (zero). Otherwise, the value shall be the appropriate number between 1 and nubmerOfSamles.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| xCoord
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The X position of this Origin in the coordinate system of the Abstract Multi-Dimensional Image Model.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| yCoord
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The Y position of this Origin in the coordinate system of the Abstract Multi-Dimensional Image Model.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| zCoord
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The Z position of this Origin in the coordinate system of the Abstract Multi-Dimensional Image Model. 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| DirectionCosines
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 0-n
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Specifies the direction in the coordinate system of the Abstract Multi-Dimensional Image Model of the Dimension whose idNumber is given in concernedSpatialDimension. The idNumber of the concernedSpatialDimension shall be less than the idNumber of this Dimension. If there is only a single DirectionCosines XML element within this Dimension XML element with a particular concernedSpatialDimension, then this Direction Cosine applies to all samples along this Dimension. Otherwise, there shall be numberOfSamples DirectionCosines XML elements with this particular concernedSpatialDimension, one for each sample along this Dimension.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| concernedSpatialDimension
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The idNumber of the particular Dimension for which this DirectionCosines XML element applies. The value of concernedSpatialDimension shall be less than the idNumber of this Dimension.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| index
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Index of this direction specification, with numbering starting from 1. If this is a single-valued DirectionCosines that applies to all samples along this Dimension then index shall either be left out or given a value of 0 (zero). Otherwise, the value of index refers to the DirectionCosines of a particular sample value along this Dimension.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| cosAlongX
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The direction cosine along the X axis of the coordinate system of the Abstract Multi-Dimensional Image Model for this concernedSpatialDimension.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| cosAlongY
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The direction cosine along the Y axis of the coordinate system of the Abstract Multi-Dimensional Image Model for this concernedSpatialDimension.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| cosAlongZ
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The direction cosine along the Z axis of the coordinate system of the Abstract Multi-Dimensional Image Model for this concernedSpatialDimension.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| PixelData
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Structure that defines where the pixel data is located, organized along dimensional lines.

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *Include Dimensional Data Macro Table A.2.5-2*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| PixelMapOfValidData
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 0-1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A pixel map that identifies which pixels either belong in or out of the Data Set. The dimensions of the pixel map match the dimensions of the image data, i.e., there is a one-to-one correspondence between samples in the image data and samples in the pixel map. The pointers to the pixel map data are included one of the Dimension XML elements.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| datatype
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Describes how samples in the pixel map are encoded. Enumerated values are:

BIT1UNSIGNED_INT8 

For BIT1, the bit ordering starts from the least significant bit going to the most significant bit within an UNSIGNED_INT8 (i.e. 8 bit) byte. The bits are zero-padded to make a full 8-bit byte at the end of the most rapidly changing dimension (i.e. the Dimension whose idNumber is 1).

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| inValue
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The value within the pixel map that indicates that this sample shall be considered as part of the Data Set. All samples whose pixel map values do not match inValue shall not be considered as part of the Data Set. Required if outValue is not present. Shall not be present if outValue is present.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| outValue
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The value within the pixel map that indicates that this sample shall not be considered as part of the Data Set. All samples whose pixel map values do not match outValue shall be considered as part of the Data Set. Required if inValue is not present. Shall not be present if inValue is present.

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *Include Dimensional Data Macro Table A.2.5-2*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 

|}
center**Table A.2.5-2 Dimensional Data Macro**/center


{| style="border-spacing:0;"
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| DimensionalData
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A nested tree structure that organizes the data for each dimension. The top level of the tree structure should refer to the Dimension with the highest idNumber.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| dimensionID
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The idNumber of the Dimension in this AbstractImageDataSet to which this DimensionalData refers.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| DataAt
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| O
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| 1-n
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| References to where the image data is located. Only one Dimension XML Element within this AbstractImageDataSet shall have UUIDs for bulk pixel data (i.e. all bulk data references are at the same dimensional level).

Note:If the source of the data, as part of the model preparation, creates a single file for pixel data from multiple smaller native objects, then in order to provide the descriptorUUID XML Attributes the source may need to create multiple bulkDataUUIDs referring to different offsets within that single pixel data file.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| indexWithinDimension
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The ordinal position (e.g. index number) of this sample point in the array of data at this level. Numbering starts from 1.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| descriptorUUID
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A UUID that refers to the ObjectDescriptor from which this data is drawn, formatted in the hexadecimal representation defined by ITU-T Recommendation X.667,. 

Required at the level of the nested tree structure where the source added the data from the descriptorUUID into the Abstract Multi-Dimensional Image Model.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| bulkDataUUID
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| C
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The identifier that the recipient of the data may use in a getData() call to gain access to the bulk pixel data formatted as a UUID using the hexadecimal representation defined in ITU-T Recommendation X.667,.

Required if the Dimensional Data Macro is not present at this level of the nested tree structure. Shall not be present otherwise.

|-
| colspan="3"  style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *Conditionally include the Dimensional Data Macro Table A.2.5-2*
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Only one of bulkDataUUID or Dimensional Data shall be included at each level. If Dimensional Data is included, it shall be the next lower level of the nested tree structure, that is the Dimension with an idNumber one less than the Dimension referred to by the enclosing DimensionalData.

|}
    1. A.2.6Schema
The Relax NG Compact schema for the Abstract Multi-Dimensional Image Model follows:

default namespace = "http://dicom.nema.org/PS3.19/models/AbstractImage"


start = AbstractImageDataSet

AbstractImageDataSet = 


element AbstractImageDataSet {

element Component{

attribute idNumber { xsd:positiveInteger },

attribute datatype { ComponentDatatype },

attribute minValue { xsd:double }?,

attribute maxValue { xsd:double }?,

element Semantics { CodedTerm },

element Unit { CodedTerm },

element RealWordMapping {

attribute rescaleSlope { xsd:double },

attribute rescaleIntercept { xsd:double },

element Unit { CodedTerm },

element Semantics { CodedTerm }

}*

}+,

element Dimension {

attribute idNumber { xsd:positiveInteger },

attribute numberOfSamples { xsd:positiveInteger },

element Semantics { CodedTerm },

(element Regular {

attribute width { xsd:double },

attribute spacing { xsd:double },

element Unit { CodedTerm },

element AxisDirection { CodedTerm }?,

element AxisOrientation { CodedTerm }?

}

| element Irregular {

element origin { xsd:double },

element SampleLocation {

attribute index { xsd:positiveInteger },

attribute width { xsd:double },

attribute distanceToOrigin { xsd:double }

}+,

element Unit { CodedTerm },

element AxisDirection { CodedTerm }?,

element AxisOrientation { CodedTerm }?

}

| element Qualitative {

element Sample {

attribute index { xsd:positiveInteger },

element Semantics { CodedTerm }

}+

}),

element Origin {

attribute index { xsd:positiveInteger }?,

attribute xCoord { xsd:double },

attribute yCoord { xsd:double },

attribute zCoord { xsd:double }

}*,

element DirectionCosines {

attribute concernedSpatialDimension { xsd:positiveInteger },

attribute index { xsd:positiveInteger }?,

attribute cosAlongX { xsd:double },

attribute cosAlongY { xsd:double },

attribute cosAlongZ { xsd:double }

}*

}+,

element PixelData { DimensionalData },

element PixelMapOfValidData {

attribute datatype { PixelMapDatatype },

(

attribute inValue { xsd:positiveInteger }

| attribute outValue { xsd:positiveInteger }

),

DimensionalData

}?

}


ComponentDatatype =

"SIGNED_INT8"

| "SIGNED_INT16"

| "SIGNED_INT32"

| "UNSIGNED_CHAR8"

| "UNSIGNED_INT16"

| "UNSIGNED_INT32"

| "FLOAT32"

| "FLOAT64"


PixelMapDatatype = 

"BIT1"

| "UNSIGNED_INT8"


DimensionalData =

element DimensionalData {

attribute dimensionID { xsd:positiveInteger },

element DataAt 

{

attribute sampleNumber { xsd:positiveInteger },

attribute descriptorUUID { xsd:string }?,

( DimensionalData | BulkDataPointer )

}+

}


BulkDataPointer = 

attribute UUID { xsd:string }


CodedTerm = 

element CodeValue { xsd:string },

element CodingSchemeDesignator { xsd:string },

element CodingSchemeVersion { xsd:string }?,

element CodeMeaning { xsd:string }?,

(

element ContextIdentifier { xsd:string },

element MappingResource { xsd:string },

element ContextGroupVersion { xsd:string }

)?,

(

element ContextGroupExtensionFlag { xsd:string },

element ContextGroupLocalVersion { xsd:string }?,

element ContextGroupExtensionCreatorUID { xsd:string }?

)?


    1. A.2.7Examples
      1. A.2.7.1Simple 3D Volume
[Image:](Image:)(Image:.md)

center**Figure A.2.7.1-1 Simple 3D Volume Example**/center

      1. A.2.7.2Simple 4D Volume
[Image:](Image:)(Image:.md)

center**Figure A.2.7.2-1 Simple 4D Volume Example**/center

      1. A.2.7.32D Ultrasound
center/center

center**Figure A.2.7.3-1 2D Ultrasound Example**/center

- In this particular case, we have three dimensions, numbered #1 for displacements along X, #2 for displacements along Y, and #3 to index the time series. If we have 200 images along time (i.e., the *numberOfSamples* XML Attribute is set to 200), we will then have 400 occurrences of the *DirectionCosines *XML Element within the *Dimension* XML Element whose *idNumber* XML Attribute is set to #3 (the dimension referring to time). The 200 first occurrences will have the XML Attribute *concernedSpatialDimension* with value #1 (to specify direction cosines along the X axis) and will be indexed by the XML Attribute *index* varying from 1 to 200 corresponding to the 200 images along time. The 200 following occurrences will have the XML Attribute *concernedSpatialDimension* with value #2 (to specify direction cosines along the Y axis), and will also be indexed by the XML Attribute* index* varying from 1 to 200.

- Similarly, in this example we will have 200 occurrences of the *Origin* XML Element within the Dimension XML Element that has the *idNumber* XML Attribute set to the value 3, and of course by the XML Attribute *index* varying from 1 to 200.

      1. A.2.7.43D MR Metabolite Map  Single Component
center[Image:](Image:)(Image:.md)/center

center**Figure A.2.7.4-1 Single Component 3D MR Metabolite Example**/center

      1. A.2.7.53D MR Metabolite Map  Multiple Component
center[Image:](Image:)(Image:.md)/center

center**Figure A.2.7.5-1 Multiple Component 3D MR Metabolite Map Example**/center

1. Annex B Interface Definitions
  1. B.1Application Interface  Version 20100825
    1. B.1.1WSDL Definition of the Interface
The following is the content of ApplicationService-20100825.wsdl:

nowiki?xml version="1.0" encoding="utf-8"?/nowiki

nowikiwsdl:definitions name="ApplicationService-20100825"/nowiki

targetNamespace="http://dicom.nema.org/PS3.19/ApplicationService-20100825"

xmlns:tns="http://dicom.nema.org/PS3.19/ApplicationService-20100825"

xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"

xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"

xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"

xmlns:wsam="http://www.w3.org/2007/05/addressing/metadata"

xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"

xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy"

xmlns:wsap="http://schemas.xmlsoap.org/ws/2004/08/addressing/policy"

xmlns:xsd="http://www.w3.org/2001/XMLSchema"

xmlns:msc="http://schemas.microsoft.com/ws/2005/12/wsdl/contract"

xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl"

xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/"

xmlns:wsa10="http://www.w3.org/2005/08/addressing"

xmlns:wsx="http://schemas.xmlsoap.org/ws/2004/09/mex"

xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"

nowikiwsdl:types/nowiki

nowikixsd:schema targetNamespace="http://dicom.nema.org/PS3.19/Imports/ApplicationService-20100825"/nowiki

nowikixsd:import namespace="http://dicom.nema.org/PS3.19/ApplicationService-20100825"/nowiki

schemaLocation="./ApplicationService-20100825.xsd"/

nowikixsd:import namespace="http://schemas.microsoft.com/2003/10/Serialization/"/nowiki

schemaLocation="./Types.xsd" /

nowikixsd:import namespace="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/nowiki

schemaLocation="./ArrayOfString.xsd" /

nowikixsd:import namespace="http://schemas.datacontract.org/2004/07/System.Xml.XPath"/nowiki

schemaLocation="./XPathNodeType.xsd" /

nowiki/xsd:schema/nowiki

nowiki/wsdl:types/nowiki

nowikiwsdl:message name="IApplicationService_GetState_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GetState"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_GetState_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GetStateResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_SetState_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:SetState"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_SetState_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:SetStateResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_BringToFront_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:BringToFront"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_BringToFront_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:BringToFrontResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_NotifyDataAvailable_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:NotifyDataAvailable"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_NotifyDataAvailable_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:NotifyDataAvailableResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_GetData_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GetData"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_GetData_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GetDataResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_ReleaseData_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:ReleaseData"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_ReleaseData_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:ReleaseDataResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_GetAsModels_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GetAsModels"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_GetAsModels_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GetAsModelsResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_ReleaseModels_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:ReleaseModels"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_ReleaseModels_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:ReleaseModelsResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_QueryModel_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:QueryModel"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_QueryModel_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:QueryModelResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_QueryInfoSet_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:QueryInfoSet"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IApplicationService_QueryInfoSet_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:QueryInfoSetResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:portType name="IApplicationService-20100825"/nowiki

nowikiwsdl:operation name="GetState"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/GetState"/nowiki

message="tns:IApplicationService_GetState_InputMessage"/

nowikiwsdl:output wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/GetStateResponse"/nowiki

message="tns:IApplicationService_GetState_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="SetState"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/SetState"/nowiki

message="tns:IApplicationService_SetState_InputMessage"/

nowikiwsdl:output wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/SetStateResponse"/nowiki

message="tns:IApplicationService_SetState_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="BringToFront"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/BringToFront"/nowiki

message="tns:IApplicationService_BringToFront_InputMessage"/

nowikiwsdl:output/nowiki

wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/BringToFrontResponse"

message="tns:IApplicationService_BringToFront_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="NotifyDataAvailable"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/NotifyDataAvailable"/nowiki

message="tns:IApplicationService_NotifyDataAvailable_InputMessage"/

nowikiwsdl:output/nowiki

wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/NotifyDataAvailableResponse"

message="tns:IApplicationService_NotifyDataAvailable_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="GetData"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/GetData"/nowiki

message="tns:IApplicationService_GetData_InputMessage"/

nowikiwsdl:output wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/GetDataResponse"/nowiki

message="tns:IApplicationService_GetData_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="ReleaseData"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/ReleaseData"/nowiki

message="tns:IApplicationService_ReleaseData_InputMessage"/

nowikiwsdl:output/nowiki

wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/ReleaseDataResponse"

message="tns:IApplicationService_ReleaseData_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="GetAsModels"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/GetAsModels"/nowiki

message="tns:IApplicationService_GetAsModels_InputMessage"/

nowikiwsdl:output/nowiki

wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/GetAsModelsResponse"

message="tns:IApplicationService_GetAsModels_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="ReleaseModels"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/ReleaseModels"/nowiki

message="tns:IApplicationService_ReleaseModels_InputMessage"/

nowikiwsdl:output/nowiki

wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/ReleaseModelsResponse"

message="tns:IApplicationService_ReleaseModels_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="QueryModel"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/QueryModel"/nowiki

message="tns:IApplicationService_QueryModel_InputMessage"/

nowikiwsdl:output wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/QueryModelResponse"/nowiki

message="tns:IApplicationService_QueryModel_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="QueryInfoSet"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/QueryInfoSet"/nowiki

message="tns:IApplicationService_QueryInfoSet_InputMessage"/

nowikiwsdl:output/nowiki

wsaw:Action="http://dicom.nema.org/PS3.19/IApplicationService/QueryInfoSetResponse"

message="tns:IApplicationService_QueryInfoSet_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowiki/wsdl:portType/nowiki

nowikiwsdl:binding name="ApplicationService-20100825Binding" type="tns:IApplicationService-20100825"/nowiki

nowikisoap:binding transport="http://schemas.xmlsoap.org/soap/http"//nowiki

nowikiwsdl:operation name="GetState"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IApplicationService/GetState"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="SetState"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IApplicationService/SetState"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="BringToFront"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IApplicationService/BringToFront"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="NotifyDataAvailable"/nowiki

nowikisoap:operation/nowiki

soapAction="http://dicom.nema.org/PS3.19/IApplicationService/NotifyDataAvailable"

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="GetData"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IApplicationService/GetData"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="ReleaseData"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IApplicationService/ReleaseData"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="GetAsModels"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IApplicationService/GetAsModels"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="ReleaseModels"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IApplicationService/ReleaseModels"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="QueryModel"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IApplicationService/QueryModel"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="QueryInfoSet"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IApplicationService/QueryInfoSet"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowiki/wsdl:binding/nowiki

nowikiwsdl:service name="ApplicationService-20100825"/nowiki

nowikiwsdl:port name="ApplicationServiceBinding" binding="tns:ApplicationService-20100825Binding"/nowiki

nowikisoap:address location="http://localhost/Service"//nowiki

nowiki/wsdl:port/nowiki

nowiki/wsdl:service/nowiki

nowiki/wsdl:definitions /nowiki


    1. B.1.2Definition of Data Structures Used
      1. B.1.2.1Primary Definitions
The following is the content of ApplicationService-20100825.xsd

nowiki?xml version="1.0" encoding="utf-8"?/nowiki

nowikixs:schema xmlns:tns="http://dicom.nema.org/PS3.19/ApplicationService-20100825" elementFormDefault="qualified"/nowiki

targetNamespace="http://dicom.nema.org/PS3.19/ApplicationService-20100825" xmlns:xs="http://www.w3.org/2001/XMLSchema"

nowikixs:import namespace="http://schemas.microsoft.com/2003/10/Serialization/Arrays"//nowiki

nowikixs:import namespace="http://schemas.datacontract.org/2004/07/System.Xml.XPath"//nowiki

nowikixs:element name="GetState"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence//nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="GetStateResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="GetStateResult" type="tns:State"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:simpleType name="State"/nowiki

nowikixs:restriction base="xs:string"/nowiki

nowikixs:enumeration value="IDLE"//nowiki

nowikixs:enumeration value="INPROGRESS"//nowiki

nowikixs:enumeration value="SUSPENDED"//nowiki

nowikixs:enumeration value="COMPLETED"//nowiki

nowikixs:enumeration value="CANCELED"//nowiki

nowikixs:enumeration value="EXIT"//nowiki

nowiki/xs:restriction/nowiki

nowiki/xs:simpleType/nowiki

nowikixs:element name="State" nillable="true" type="tns:State"//nowiki

nowikixs:element name="SetState"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="state" type="tns:State"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="SetStateResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="SetStateResult" type="xs:boolean"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="BringToFront"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="location" nillable="true" type="tns:Rectangle"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="Rectangle"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Height" type="xs:int"//nowiki

nowikixs:element minOccurs="0" name="Width" type="xs:int"//nowiki

nowikixs:element minOccurs="0" name="RefPointX" type="xs:int"//nowiki

nowikixs:element minOccurs="0" name="RefPointY" type="xs:int"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="Rectangle" nillable="true" type="tns:Rectangle"//nowiki

nowikixs:element name="BringToFrontResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="BringToFrontResult" type="xs:boolean"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="NotifyDataAvailable"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="data" nillable="true" type="tns:AvailableData"//nowiki

nowikixs:element minOccurs="0" name="lastData" type="xs:boolean"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="AvailableData"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="ObjectDescriptors" nillable="true"/nowiki

type="tns:ArrayOfObjectDescriptor"/

nowikixs:element minOccurs="0" name="Patients" nillable="true" type="tns:ArrayOfPatient"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="AvailableData" nillable="true" type="tns:AvailableData"//nowiki

nowikixs:complexType name="ArrayOfObjectDescriptor"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="ObjectDescriptor" nillable="true"/nowiki

type="tns:ObjectDescriptor"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfObjectDescriptor" nillable="true" type="tns:ArrayOfObjectDescriptor"//nowiki

nowikixs:complexType name="ObjectDescriptor"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="ClassUID" nillable="true" type="tns:UID"//nowiki

nowikixs:element minOccurs="0" name="MimeType" nillable="true" type="tns:MimeType"//nowiki

nowikixs:element minOccurs="0" name="Modality" nillable="true" type="tns:Modality"//nowiki

nowikixs:element minOccurs="0" name="TransferSyntaxUID" nillable="true" type="tns:UID"//nowiki

nowikixs:element minOccurs="0" name="DescriptorUuid" nillable="true" type="tns:UUID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ObjectDescriptor" nillable="true" type="tns:ObjectDescriptor"//nowiki

nowikixs:complexType name="UID"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Uid" nillable="true" type="xs:string"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="UID" nillable="true" type="tns:UID"//nowiki

nowikixs:complexType name="MimeType"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Type" nillable="true" type="xs:string"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="MimeType" nillable="true" type="tns:MimeType"//nowiki

nowikixs:complexType name="Modality"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Modality" nillable="true" type="xs:string"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="Modality" nillable="true" type="tns:Modality"//nowiki

nowikixs:complexType name="UUID"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Uuid" nillable="true" type="xs:string"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="UUID" nillable="true" type="tns:UUID"//nowiki

nowikixs:complexType name="ArrayOfPatient"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="Patient" nillable="true"/nowiki

type="tns:Patient"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfPatient" nillable="true" type="tns:ArrayOfPatient"//nowiki

nowikixs:complexType name="Patient"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="AssigningAuthority" nillable="true" type="xs:string"//nowiki

nowikixs:element minOccurs="0" name="DateOfBirth" type="xs:dateTime"//nowiki

nowikixs:element minOccurs="0" name="ID" nillable="true" type="xs:string"//nowiki

nowikixs:element minOccurs="0" name="Name" nillable="true" type="xs:string"//nowiki

nowikixs:element minOccurs="0" name="ObjectDescriptors" nillable="true"/nowiki

type="tns:ArrayOfObjectDescriptor"/

nowikixs:element minOccurs="0" name="Sex" nillable="true" type="xs:string"//nowiki

nowikixs:element minOccurs="0" name="Studies" nillable="true" type="tns:ArrayOfStudy"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="Patient" nillable="true" type="tns:Patient"//nowiki

nowikixs:complexType name="ArrayOfStudy"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="Study" nillable="true" type="tns:Study"/nowiki

/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfStudy" nillable="true" type="tns:ArrayOfStudy"//nowiki

nowikixs:complexType name="Study"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="ObjectDescriptors" nillable="true"/nowiki

type="tns:ArrayOfObjectDescriptor"/

nowikixs:element minOccurs="0" name="Series" nillable="true" type="tns:ArrayOfSeries"//nowiki

nowikixs:element minOccurs="0" name="StudyUID" nillable="true" type="tns:UID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="Study" nillable="true" type="tns:Study"//nowiki

nowikixs:complexType name="ArrayOfSeries"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="Series" nillable="true"/nowiki

type="tns:Series"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfSeries" nillable="true" type="tns:ArrayOfSeries"//nowiki

nowikixs:complexType name="Series"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="ObjectDescriptors" nillable="true"/nowiki

type="tns:ArrayOfObjectDescriptor"/

nowikixs:element minOccurs="0" name="SeriesUID" nillable="true" type="tns:UID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="Series" nillable="true" type="tns:Series"//nowiki

nowikixs:element name="NotifyDataAvailableResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="NotifyDataAvailableResult" type="xs:boolean"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="GetData"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="objects" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowikixs:element minOccurs="0" name="acceptableTransferSyntaxes" nillable="true"/nowiki

type="tns:ArrayOfUID"/

nowikixs:element minOccurs="0" name="includeBulkData" type="xs:boolean"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="ArrayOfUUID"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="UUID" nillable="true" type="tns:UUID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfUUID" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowikixs:complexType name="ArrayOfUID"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="UID" nillable="true" type="tns:UID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfUID" nillable="true" type="tns:ArrayOfUID"//nowiki

nowikixs:element name="GetDataResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="GetDataResult" nillable="true"/nowiki

type="tns:ArrayOfObjectLocator"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="ArrayOfObjectLocator"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="ObjectLocator" nillable="true"/nowiki

type="tns:ObjectLocator"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfObjectLocator" nillable="true" type="tns:ArrayOfObjectLocator"//nowiki

nowikixs:complexType name="ObjectLocator"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Length" type="xs:long"//nowiki

nowikixs:element minOccurs="0" name="Offset" type="xs:long"//nowiki

nowikixs:element minOccurs="0" name="TransferSyntax" nillable="true" type="tns:UID"//nowiki

nowikixs:element minOccurs="0" name="URI" nillable="true" type="xs:anyURI"//nowiki

nowikixs:element minOccurs="0" name="Locator" nillable="true" type="tns:UUID"//nowiki

nowikixs:element minOccurs="0" name="Source" nillable="true" type="tns:UUID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ObjectLocator" nillable="true" type="tns:ObjectLocator"//nowiki

nowikixs:element name="ReleaseData"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="objects" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="ReleaseDataResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence//nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="GetAsModels"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="objects" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowikixs:element minOccurs="0" name="classUID" nillable="true" type="tns:UID"//nowiki

nowikixs:element minOccurs="0" name="supportedInfoSetTypes" nillable="true"/nowiki

type="tns:ArrayOfMimeType"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="ArrayOfMimeType"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="MimeType" nillable="true"/nowiki

type="tns:MimeType"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfMimeType" nillable="true" type="tns:ArrayOfMimeType"//nowiki

nowikixs:element name="GetAsModelsResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="GetAsModelsResult" nillable="true"/nowiki

type="tns:ModelSetDescriptor"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="ModelSetDescriptor"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="FailedSourceObjects" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowikixs:element minOccurs="0" name="InfosetType" nillable="true" type="tns:MimeType"//nowiki

nowikixs:element minOccurs="0" name="Models" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ModelSetDescriptor" nillable="true" type="tns:ModelSetDescriptor"//nowiki

nowikixs:element name="ReleaseModels"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="models" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="ReleaseModelsResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence//nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="QueryModel"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="models" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowikixs:element minOccurs="0" name="xPaths" nillable="true"/nowiki

xmlns:q1="http://schemas.microsoft.com/2003/10/Serialization/Arrays"

type="q1:ArrayOfstring"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="QueryModelResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="QueryModelResult" nillable="true"/nowiki

type="tns:ArrayOfQueryResult"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="ArrayOfQueryResult"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="QueryResult" nillable="true"/nowiki

type="tns:QueryResult"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfQueryResult" nillable="true" type="tns:ArrayOfQueryResult"//nowiki

nowikixs:complexType name="QueryResult"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Model" nillable="true" type="tns:UUID"//nowiki

nowikixs:element minOccurs="0" name="Result" nillable="true" type="tns:ArrayOfXPathNode"//nowiki

nowikixs:element minOccurs="0" name="XPath" nillable="true" type="xs:string"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="QueryResult" nillable="true" type="tns:QueryResult"//nowiki

nowikixs:complexType name="ArrayOfXPathNode"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="XPathNode" nillable="true"/nowiki

type="tns:XPathNode"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfXPathNode" nillable="true" type="tns:ArrayOfXPathNode"//nowiki

nowikixs:complexType name="XPathNode"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="NodeType"/nowiki

xmlns:q2="http://schemas.datacontract.org/2004/07/System.Xml.XPath" type="q2:XPathNodeType"/

nowikixs:element minOccurs="0" name="Value" nillable="true" type="xs:string"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="XPathNode" nillable="true" type="tns:XPathNode"//nowiki

nowikixs:element name="QueryInfoSet"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="models" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowikixs:element minOccurs="0" name="xPaths" nillable="true"/nowiki

xmlns:q3="http://schemas.microsoft.com/2003/10/Serialization/Arrays"

type="q3:ArrayOfstring"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="QueryInfoSetResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="QueryInfoSetResult" nillable="true"/nowiki

type="tns:ArrayOfQueryResultInfoSet"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="ArrayOfQueryResultInfoSet"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="QueryResultInfoSet" nillable="true"/nowiki

type="tns:QueryResultInfoSet"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfQueryResultInfoSet" nillable="true" type="tns:ArrayOfQueryResultInfoSet"//nowiki

nowikixs:complexType name="QueryResultInfoSet"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Model" nillable="true" type="tns:UUID"//nowiki

nowikixs:element minOccurs="0" name="Result" nillable="true" type="tns:ArrayOfXPathNodeInfoSet"//nowiki

nowikixs:element minOccurs="0" name="XPath" nillable="true" type="xs:string"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="QueryResultInfoSet" nillable="true" type="tns:QueryResultInfoSet"//nowiki

nowikixs:complexType name="ArrayOfXPathNodeInfoSet"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="XPathNodeInfoSet" nillable="true"/nowiki

type="tns:XPathNodeInfoSet"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfXPathNodeInfoSet" nillable="true" type="tns:ArrayOfXPathNodeInfoSet"//nowiki

nowikixs:complexType name="XPathNodeInfoSet"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="InfoSetValue" nillable="true" type="xs:base64Binary"//nowiki

nowikixs:element minOccurs="0" name="NodeType"/nowiki

xmlns:q4="http://schemas.datacontract.org/2004/07/System.Xml.XPath" type="q4:XPathNodeType"

/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="XPathNodeInfoSet" nillable="true" type="tns:XPathNodeInfoSet"//nowiki

nowiki/xs:schema /nowiki


      1. B.1.2.2Referenced Definitions
The following is the content of XPathNodeType.xsd:

nowiki?xml version="1.0" encoding="utf-8"?/nowiki

nowikixs:schema xmlns:tns="http://schemas.datacontract.org/2004/07/System.Xml.XPath" elementFormDefault="qualified" targetNamespace="http://schemas.datacontract.org/2004/07/System.Xml.XPath" xmlns:xs="http://www.w3.org/2001/XMLSchema"/nowiki

nowikixs:simpleType name="XPathNodeType"/nowiki

nowikixs:restriction base="xs:string"/nowiki

nowikixs:enumeration value="Root" //nowiki

nowikixs:enumeration value="Element" //nowiki

nowikixs:enumeration value="Attribute" //nowiki

nowikixs:enumeration value="Namespace" //nowiki

nowikixs:enumeration value="Text" //nowiki

nowikixs:enumeration value="SignificantWhitespace" //nowiki

nowikixs:enumeration value="Whitespace" //nowiki

nowikixs:enumeration value="ProcessingInstruction" //nowiki

nowikixs:enumeration value="Comment" //nowiki

nowikixs:enumeration value="All" //nowiki

nowiki/xs:restriction/nowiki

nowiki/xs:simpleType/nowiki

nowikixs:element name="XPathNodeType" nillable="true" type="tns:XPathNodeType" //nowiki

nowiki/xs:schema/nowiki


The following is the content of Types.xsd:

nowiki?xml version="1.0" encoding="utf-8"?/nowiki

nowikixs:schema xmlns:tns="http://schemas.microsoft.com/2003/10/Serialization/" attributeFormDefault="qualified" elementFormDefault="qualified" targetNamespace="http://schemas.microsoft.com/2003/10/Serialization/" xmlns:xs="http://www.w3.org/2001/XMLSchema"/nowiki

nowikixs:element name="anyType" nillable="true" type="xs:anyType" //nowiki

nowikixs:element name="anyURI" nillable="true" type="xs:anyURI" //nowiki

nowikixs:element name="base64Binary" nillable="true" type="xs:base64Binary" //nowiki

nowikixs:element name="boolean" nillable="true" type="xs:boolean" //nowiki

nowikixs:element name="byte" nillable="true" type="xs:byte" //nowiki

nowikixs:element name="dateTime" nillable="true" type="xs:dateTime" //nowiki

nowikixs:element name="decimal" nillable="true" type="xs:decimal" //nowiki

nowikixs:element name="double" nillable="true" type="xs:double" //nowiki

nowikixs:element name="float" nillable="true" type="xs:float" //nowiki

nowikixs:element name="int" nillable="true" type="xs:int" //nowiki

nowikixs:element name="long" nillable="true" type="xs:long" //nowiki

nowikixs:element name="QName" nillable="true" type="xs:QName" //nowiki

nowikixs:element name="short" nillable="true" type="xs:short" //nowiki

nowikixs:element name="string" nillable="true" type="xs:string" //nowiki

nowikixs:element name="unsignedByte" nillable="true" type="xs:unsignedByte" //nowiki

nowikixs:element name="unsignedInt" nillable="true" type="xs:unsignedInt" //nowiki

nowikixs:element name="unsignedLong" nillable="true" type="xs:unsignedLong" //nowiki

nowikixs:element name="unsignedShort" nillable="true" type="xs:unsignedShort" //nowiki

nowikixs:element name="char" nillable="true" type="tns:char" //nowiki

nowikixs:simpleType name="char"/nowiki

nowikixs:restriction base="xs:int" //nowiki

nowiki/xs:simpleType/nowiki

nowikixs:element name="duration" nillable="true" type="tns:duration" //nowiki

nowikixs:simpleType name="duration"/nowiki

nowikixs:restriction base="xs:duration"/nowiki

nowikixs:pattern value="\-?P(\d*D)?(T(\d*H)?(\d*M)?(\d*(\.\d*)?S)?)?" //nowiki

nowikixs:minInclusive value="-P10675199DT2H48M5.4775808S" //nowiki

nowikixs:maxInclusive value="P10675199DT2H48M5.4775807S" //nowiki

nowiki/xs:restriction/nowiki

nowiki/xs:simpleType/nowiki

nowikixs:element name="guid" nillable="true" type="tns:guid" //nowiki

nowikixs:simpleType name="guid"/nowiki

nowikixs:restriction base="xs:string"/nowiki

nowikixs:pattern value="[\da-fA-F](\da-fA-F){8}-[\da-fA-F](\da-fA-F){4}-[\da-fA-F](\da-fA-F){4}-[\da-fA-F](\da-fA-F){4}-[\da-fA-F](\da-fA-F){12}" //nowiki

nowiki/xs:restriction/nowiki

nowiki/xs:simpleType/nowiki

nowikixs:attribute name="FactoryType" type="xs:QName" //nowiki

nowikixs:attribute name="Id" type="xs:ID" //nowiki

nowikixs:attribute name="Ref" type="xs:IDREF" //nowiki

nowiki/xs:schema/nowiki


The following is the content of ArrayOfString.xsd

nowiki?xml version="1.0" encoding="utf-8"?/nowiki

nowikixs:schema xmlns:tns="http://schemas.microsoft.com/2003/10/Serialization/Arrays" elementFormDefault="qualified" targetNamespace="http://schemas.microsoft.com/2003/10/Serialization/Arrays" xmlns:xs="http://www.w3.org/2001/XMLSchema"/nowiki

nowikixs:complexType name="ArrayOfstring"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="string" nillable="true" type="xs:string" //nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfstring" nillable="true" type="tns:ArrayOfstring" //nowiki

nowiki/xs:schema/nowiki


  1. B.2Host Interface  Version 20100825
    1. B.2.1WSDL Definition of the Interface
The following is the content of HostService-20100825.wsdl:

nowiki?xml version="1.0" encoding="utf-8"?/nowiki

nowikiwsdl:definitions name="HostService-20100825"/nowiki

targetNamespace="http://dicom.nema.org/PS3.19/HostService-20100825"

xmlns:tns="http://dicom.nema.org/PS3.19/HostService-20100825"

xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"

xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"

xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"

xmlns:wsam="http://www.w3.org/2007/05/addressing/metadata"

xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"

xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy"

xmlns:wsap="http://schemas.xmlsoap.org/ws/2004/08/addressing/policy"

xmlns:xsd="http://www.w3.org/2001/XMLSchema"

xmlns:msc="http://schemas.microsoft.com/ws/2005/12/wsdl/contract"

xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl"

xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/"

xmlns:wsa10="http://www.w3.org/2005/08/addressing"

xmlns:wsx="http://schemas.xmlsoap.org/ws/2004/09/mex"

xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"

nowikiwsdl:types/nowiki

nowikixsd:schema targetNamespace="http://dicom.nema.org/PS3.19/Imports/HostService-20100825"/nowiki

nowikixsd:import namespace="http://dicom.nema.org/PS3.19/HostService-20100825"/nowiki

schemaLocation="./HostService-20100825.xsd"/

nowikixsd:import namespace="http://schemas.microsoft.com/2003/10/Serialization/"/nowiki

schemaLocation="./Types.xsd" /

nowikixsd:import namespace="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/nowiki

schemaLocation="./ArrayOfString.xsd" /

nowikixsd:import namespace="http://schemas.datacontract.org/2004/07/System.Xml.XPath"/nowiki

schemaLocation="./XPathNodeType.xsd"/

nowiki/xsd:schema/nowiki

nowiki/wsdl:types/nowiki

nowikiwsdl:message name="IHostService_GenerateUID_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GenerateUID"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_GenerateUID_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GenerateUIDResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_GetAvailableScreen_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GetAvailableScreen"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_GetAvailableScreen_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GetAvailableScreenResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_GetOutputLocation_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GetOutputLocation"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_GetOutputLocation_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GetOutputLocationResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_NotifyStateChanged_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:NotifyStateChanged"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_NotifyStateChanged_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:NotifyStateChangedResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_NotifyStatus_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:NotifyStatus"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_NotifyStatus_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:NotifyStatusResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_NotifyDataAvailable_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:NotifyDataAvailable"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_NotifyDataAvailable_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:NotifyDataAvailableResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_GetData_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GetData"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_GetData_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GetDataResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_ReleaseData_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:ReleaseData"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_ReleaseData_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:ReleaseDataResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_GetAsModels_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GetAsModels"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_GetAsModels_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:GetAsModelsResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_ReleaseModels_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:ReleaseModels"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_ReleaseModels_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:ReleaseModelsResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_QueryModel_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:QueryModel"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_QueryModel_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:QueryModelResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_QueryInfoSet_InputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:QueryInfoSet"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:message name="IHostService_QueryInfoSet_OutputMessage"/nowiki

nowikiwsdl:part name="parameters" element="tns:QueryInfoSetResponse"//nowiki

nowiki/wsdl:message/nowiki

nowikiwsdl:portType name="IHostService-20100825"/nowiki

nowikiwsdl:operation name="GenerateUID"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/GenerateUID"/nowiki

message="tns:IHostService_GenerateUID_InputMessage"/

nowikiwsdl:output wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/GenerateUIDResponse"/nowiki

message="tns:IHostService_GenerateUID_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="GetAvailableScreen"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/GetAvailableScreen"/nowiki

message="tns:IHostService_GetAvailableScreen_InputMessage"/

nowikiwsdl:output/nowiki

wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/GetAvailableScreenResponse"

message="tns:IHostService_GetAvailableScreen_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="GetOutputLocation"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/GetOutputLocation"/nowiki

message="tns:IHostService_GetOutputLocation_InputMessage"/

nowikiwsdl:output wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/GetOutputLocationResponse"/nowiki

message="tns:IHostService_GetOutputLocation_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="NotifyStateChanged"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/NotifyStateChanged"/nowiki

message="tns:IHostService_NotifyStateChanged_InputMessage"/

nowikiwsdl:output/nowiki

wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/NotifyStateChangedResponse"

message="tns:IHostService_NotifyStateChanged_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="NotifyStatus"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/NotifyStatus"/nowiki

message="tns:IHostService_NotifyStatus_InputMessage"/

nowikiwsdl:output wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/NotifyStatusResponse"/nowiki

message="tns:IHostService_NotifyStatus_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="NotifyDataAvailable"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/NotifyDataAvailable"/nowiki

message="tns:IHostService_NotifyDataAvailable_InputMessage"/

nowikiwsdl:output/nowiki

wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/NotifyDataAvailableResponse"

message="tns:IHostService_NotifyDataAvailable_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="GetData"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/GetData"/nowiki

message="tns:IHostService_GetData_InputMessage"/

nowikiwsdl:output wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/GetDataResponse"/nowiki

message="tns:IHostService_GetData_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="ReleaseData"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/ReleaseData"/nowiki

message="tns:IHostService_ReleaseData_InputMessage"/

nowikiwsdl:output wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/ReleaseDataResponse"/nowiki

message="tns:IHostService_ReleaseData_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="GetAsModels"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/GetAsModels"/nowiki

message="tns:IHostService_GetAsModels_InputMessage"/

nowikiwsdl:output wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/GetAsModelsResponse"/nowiki

message="tns:IHostService_GetAsModels_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="ReleaseModels"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/ReleaseModels"/nowiki

message="tns:IHostService_ReleaseModels_InputMessage"/

nowikiwsdl:output wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/ReleaseModelsResponse"/nowiki

message="tns:IHostService_ReleaseModels_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="QueryModel"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/QueryModel"/nowiki

message="tns:IHostService_QueryModel_InputMessage"/

nowikiwsdl:output wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/QueryModelResponse"/nowiki

message="tns:IHostService_QueryModel_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="QueryInfoSet"/nowiki

nowikiwsdl:input wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/QueryInfoSet"/nowiki

message="tns:IHostService_QueryInfoSet_InputMessage"/

nowikiwsdl:output wsaw:Action="http://dicom.nema.org/PS3.19/IHostService/QueryInfoSetResponse"/nowiki

message="tns:IHostService_QueryInfoSet_OutputMessage"/

nowiki/wsdl:operation/nowiki

nowiki/wsdl:portType/nowiki

nowikiwsdl:binding name="HostService-YYYYNNDDBinding" type="tns:IHostService-20100825"/nowiki

nowikisoap:binding transport="http://schemas.xmlsoap.org/soap/http"//nowiki

nowikiwsdl:operation name="GenerateUID"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IHostService/GenerateUID"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="GetAvailableScreen"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IHostService/GetAvailableScreen"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="GetOutputLocation"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IHostService/GetOutputLocation"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="NotifyStateChanged"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IHostService/NotifyStateChanged"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="NotifyStatus"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IHostService/NotifyStatus"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="NotifyDataAvailable"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IHostService/NotifyDataAvailable"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="GetData"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IHostService/GetData"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="ReleaseData"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IHostService/ReleaseData"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="GetAsModels"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IHostService/GetAsModels"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="ReleaseModels"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IHostService/ReleaseModels"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="QueryModel"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IHostService/QueryModel"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowikiwsdl:operation name="QueryInfoSet"/nowiki

nowikisoap:operation soapAction="http://dicom.nema.org/PS3.19/IHostService/QueryInfoSet"/nowiki

style="document"/

nowikiwsdl:input/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:input/nowiki

nowikiwsdl:output/nowiki

nowikisoap:body use="literal"//nowiki

nowiki/wsdl:output/nowiki

nowiki/wsdl:operation/nowiki

nowiki/wsdl:binding/nowiki

nowikiwsdl:service name="HostService-20100825"/nowiki

nowikiwsdl:port name="HostServiceBinding" binding="tns:HostService-YYYYNNDDBinding"/nowiki

nowikisoap:address location="http://localhost/Service"//nowiki

nowiki/wsdl:port/nowiki

nowiki/wsdl:service/nowiki

nowiki/wsdl:definitions /nowiki


    1. B.2.2Definition of Data Structures Used
      1. B.2.2.1Primary Definitions
The following is the the contents of HostService-20100825.xsd:

nowiki?xml version="1.0" encoding="utf-8"?/nowiki

nowikixs:schema xmlns:tns="http://dicom.nema.org/PS3.19/HostService-20100825" elementFormDefault="qualified"/nowiki

targetNamespace="http://dicom.nema.org/PS3.19/HostService-20100825" xmlns:xs="http://www.w3.org/2001/XMLSchema"

nowikixs:import namespace="http://schemas.microsoft.com/2003/10/Serialization/Arrays"//nowiki

nowikixs:import namespace="http://schemas.datacontract.org/2004/07/System.Xml.XPath"//nowiki

nowikixs:element name="GenerateUID"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence//nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="GenerateUIDResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="GenerateUIDResult" nillable="true" type="tns:UID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="UID"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Uid" nillable="true" type="xs:string"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="UID" nillable="true" type="tns:UID"//nowiki

nowikixs:element name="GetAvailableScreen"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="preferredScreen" nillable="true" type="tns:Rectangle"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="Rectangle"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Height" type="xs:int"//nowiki

nowikixs:element minOccurs="0" name="Width" type="xs:int"//nowiki

nowikixs:element minOccurs="0" name="RefPointX" type="xs:int"//nowiki

nowikixs:element minOccurs="0" name="RefPointY" type="xs:int"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="Rectangle" nillable="true" type="tns:Rectangle"//nowiki

nowikixs:element name="GetAvailableScreenResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="GetAvailableScreenResult" nillable="true"/nowiki

type="tns:Rectangle"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="GetOutputLocation"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="preferredProtocols" nillable="true"/nowiki

xmlns:q1="http://schemas.microsoft.com/2003/10/Serialization/Arrays"

type="q1:ArrayOfstring"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="GetOutputLocationResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="GetOutputLocationResult" nillable="true" type="xs:anyURI"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="NotifyStateChanged"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="state" type="tns:State"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:simpleType name="State"/nowiki

nowikixs:restriction base="xs:string"/nowiki

nowikixs:enumeration value="IDLE"//nowiki

nowikixs:enumeration value="INPROGRESS"//nowiki

nowikixs:enumeration value="SUSPENDED"//nowiki

nowikixs:enumeration value="COMPLETED"//nowiki

nowikixs:enumeration value="CANCELED"//nowiki

nowikixs:enumeration value="EXIT"//nowiki

nowiki/xs:restriction/nowiki

nowiki/xs:simpleType/nowiki

nowikixs:element name="State" nillable="true" type="tns:State"//nowiki

nowikixs:element name="NotifyStateChangedResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence//nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="NotifyStatus"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="status" nillable="true" type="tns:Status"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="Status"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="StatusType" type="tns:StatusType"//nowiki

nowikixs:element minOccurs="0" name="CodeValue" type="xs:int"//nowiki

nowikixs:element minOccurs="0" name="CodingSchemeDesignator" nillable="true" type="xs:string"//nowiki

nowikixs:element minOccurs="0" name="CodeMeaning" nillable="true" type="xs:string"//nowiki

nowikixs:element minOccurs="0" name="ContextIdentifier" nillable="true" type="xs:string"//nowiki

nowikixs:element minOccurs="0" name="MappingResource" nillable="true" type="xs:string"//nowiki

nowikixs:element minOccurs="0" name="ContextGroupVersion" nillable="true" type="xs:string"//nowiki

nowikixs:element minOccurs="0" name="ContextGroupExtensionFlag" nillable="true" type="xs:string"//nowiki

nowikixs:element minOccurs="0" name="ContextGroupLocalVersion" nillable="true" type="xs:string"//nowiki

nowikixs:element minOccurs="0" name="ContextGroupExtensionCreatorUID" nillable="true" type="xs:string"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="Status" nillable="true" type="tns:Status"//nowiki

nowikixs:simpleType name="StatusType"/nowiki

nowikixs:restriction base="xs:string"/nowiki

nowikixs:enumeration value="INFORMATION"//nowiki

nowikixs:enumeration value="WARNING"//nowiki

nowikixs:enumeration value="ERROR"//nowiki

nowikixs:enumeration value="FATALERROR"//nowiki

nowiki/xs:restriction/nowiki

nowiki/xs:simpleType/nowiki

nowikixs:element name="StatusType" nillable="true" type="tns:StatusType"//nowiki

nowikixs:element name="NotifyStatusResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence//nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="NotifyDataAvailable"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="data" nillable="true" type="tns:AvailableData"//nowiki

nowikixs:element minOccurs="0" name="lastData" type="xs:boolean"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="AvailableData"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="ObjectDescriptors" nillable="true"/nowiki

type="tns:ArrayOfObjectDescriptor"/

nowikixs:element minOccurs="0" name="Patients" nillable="true" type="tns:ArrayOfPatient"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="AvailableData" nillable="true" type="tns:AvailableData"//nowiki

nowikixs:complexType name="ArrayOfObjectDescriptor"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="ObjectDescriptor" nillable="true"/nowiki

type="tns:ObjectDescriptor"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfObjectDescriptor" nillable="true" type="tns:ArrayOfObjectDescriptor"//nowiki

nowikixs:complexType name="ObjectDescriptor"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="ClassUID" nillable="true" type="tns:UID"//nowiki

nowikixs:element minOccurs="0" name="MimeType" nillable="true" type="tns:MimeType"//nowiki

nowikixs:element minOccurs="0" name="Modality" nillable="true" type="tns:Modality"//nowiki

nowikixs:element minOccurs="0" name="TransferSyntaxUID" nillable="true" type="tns:UID"//nowiki

nowikixs:element minOccurs="0" name="DescriptorUuid" nillable="true" type="tns:UUID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ObjectDescriptor" nillable="true" type="tns:ObjectDescriptor"//nowiki

nowikixs:complexType name="MimeType"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Type" nillable="true" type="xs:string"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="MimeType" nillable="true" type="tns:MimeType"//nowiki

nowikixs:complexType name="Modality"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Modality" nillable="true" type="xs:string"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="Modality" nillable="true" type="tns:Modality"//nowiki

nowikixs:complexType name="UUID"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Uuid" nillable="true" type="xs:string"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="UUID" nillable="true" type="tns:UUID"//nowiki

nowikixs:complexType name="ArrayOfPatient"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="Patient" nillable="true"/nowiki

type="tns:Patient"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfPatient" nillable="true" type="tns:ArrayOfPatient"//nowiki

nowikixs:complexType name="Patient"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="AssigningAuthority" nillable="true" type="xs:string"//nowiki

nowikixs:element minOccurs="0" name="DateOfBirth" type="xs:dateTime"//nowiki

nowikixs:element minOccurs="0" name="ID" nillable="true" type="xs:string"//nowiki

nowikixs:element minOccurs="0" name="Name" nillable="true" type="xs:string"//nowiki

nowikixs:element minOccurs="0" name="ObjectDescriptors" nillable="true"/nowiki

type="tns:ArrayOfObjectDescriptor"/

nowikixs:element minOccurs="0" name="Sex" nillable="true" type="xs:string"//nowiki

nowikixs:element minOccurs="0" name="Studies" nillable="true" type="tns:ArrayOfStudy"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="Patient" nillable="true" type="tns:Patient"//nowiki

nowikixs:complexType name="ArrayOfStudy"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="Study" nillable="true" type="tns:Study"/nowiki

/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfStudy" nillable="true" type="tns:ArrayOfStudy"//nowiki

nowikixs:complexType name="Study"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="ObjectDescriptors" nillable="true"/nowiki

type="tns:ArrayOfObjectDescriptor"/

nowikixs:element minOccurs="0" name="Series" nillable="true" type="tns:ArrayOfSeries"//nowiki

nowikixs:element minOccurs="0" name="StudyUID" nillable="true" type="tns:UID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="Study" nillable="true" type="tns:Study"//nowiki

nowikixs:complexType name="ArrayOfSeries"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="Series" nillable="true"/nowiki

type="tns:Series"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfSeries" nillable="true" type="tns:ArrayOfSeries"//nowiki

nowikixs:complexType name="Series"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="ObjectDescriptors" nillable="true"/nowiki

type="tns:ArrayOfObjectDescriptor"/

nowikixs:element minOccurs="0" name="SeriesUID" nillable="true" type="tns:UID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="Series" nillable="true" type="tns:Series"//nowiki

nowikixs:element name="NotifyDataAvailableResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="NotifyDataAvailableResult" type="xs:boolean"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="GetData"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="objects" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowikixs:element minOccurs="0" name="acceptableTransferSyntaxes" nillable="true"/nowiki

type="tns:ArrayOfUID"/

nowikixs:element minOccurs="0" name="includeBulkData" type="xs:boolean"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="ArrayOfUUID"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="UUID" nillable="true" type="tns:UUID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfUUID" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowikixs:complexType name="ArrayOfUID"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="UID" nillable="true" type="tns:UID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfUID" nillable="true" type="tns:ArrayOfUID"//nowiki

nowikixs:element name="GetDataResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="GetDataResult" nillable="true"/nowiki

type="tns:ArrayOfObjectLocator"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="ArrayOfObjectLocator"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="ObjectLocator" nillable="true"/nowiki

type="tns:ObjectLocator"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfObjectLocator" nillable="true" type="tns:ArrayOfObjectLocator"//nowiki

nowikixs:complexType name="ObjectLocator"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Length" type="xs:long"//nowiki

nowikixs:element minOccurs="0" name="Offset" type="xs:long"//nowiki

nowikixs:element minOccurs="0" name="TransferSyntax" nillable="true" type="tns:UID"//nowiki

nowikixs:element minOccurs="0" name="URI" nillable="true" type="xs:anyURI"//nowiki

nowikixs:element minOccurs="0" name="Locator" nillable="true" type="tns:UUID"//nowiki

nowikixs:element minOccurs="0" name="Source" nillable="true" type="tns:UUID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ObjectLocator" nillable="true" type="tns:ObjectLocator"//nowiki

nowikixs:element name="ReleaseData"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="objects" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="ReleaseDataResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence//nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="GetAsModels"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="objects" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowikixs:element minOccurs="0" name="classUID" nillable="true" type="tns:UID"//nowiki

nowikixs:element minOccurs="0" name="supportedInfoSetTypes" nillable="true"/nowiki

type="tns:ArrayOfMimeType"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="ArrayOfMimeType"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="MimeType" nillable="true"/nowiki

type="tns:MimeType"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfMimeType" nillable="true" type="tns:ArrayOfMimeType"//nowiki

nowikixs:element name="GetAsModelsResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="GetAsModelsResult" nillable="true"/nowiki

type="tns:ModelSetDescriptor"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="ModelSetDescriptor"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="FailedSourceObjects" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowikixs:element minOccurs="0" name="InfosetType" nillable="true" type="tns:MimeType"//nowiki

nowikixs:element minOccurs="0" name="Models" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ModelSetDescriptor" nillable="true" type="tns:ModelSetDescriptor"//nowiki

nowikixs:element name="ReleaseModels"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="models" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="ReleaseModelsResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence//nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="QueryModel"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="models" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowikixs:element minOccurs="0" name="xPaths" nillable="true"/nowiki

xmlns:q2="http://schemas.microsoft.com/2003/10/Serialization/Arrays"

type="q2:ArrayOfstring"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="QueryModelResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="QueryModelResult" nillable="true"/nowiki

type="tns:ArrayOfQueryResult"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="ArrayOfQueryResult"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="QueryResult" nillable="true"/nowiki

type="tns:QueryResult"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfQueryResult" nillable="true" type="tns:ArrayOfQueryResult"//nowiki

nowikixs:complexType name="QueryResult"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Model" nillable="true" type="tns:UUID"//nowiki

nowikixs:element minOccurs="0" name="Result" nillable="true" type="tns:ArrayOfXPathNode"//nowiki

nowikixs:element minOccurs="0" name="XPath" nillable="true" type="xs:string"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="QueryResult" nillable="true" type="tns:QueryResult"//nowiki

nowikixs:complexType name="ArrayOfXPathNode"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="XPathNode" nillable="true"/nowiki

type="tns:XPathNode"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfXPathNode" nillable="true" type="tns:ArrayOfXPathNode"//nowiki

nowikixs:complexType name="XPathNode"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="NodeType"/nowiki

xmlns:q3="http://schemas.datacontract.org/2004/07/System.Xml.XPath" type="q3:XPathNodeType"/

nowikixs:element minOccurs="0" name="Value" nillable="true" type="xs:string"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="XPathNode" nillable="true" type="tns:XPathNode"//nowiki

nowikixs:element name="QueryInfoSet"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="models" nillable="true" type="tns:ArrayOfUUID"//nowiki

nowikixs:element minOccurs="0" name="xPaths" nillable="true"/nowiki

xmlns:q4="http://schemas.microsoft.com/2003/10/Serialization/Arrays"

type="q4:ArrayOfstring"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:element name="QueryInfoSetResponse"/nowiki

nowikixs:complexType/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="QueryInfoSetResult" nillable="true"/nowiki

type="tns:ArrayOfQueryResultInfoSet"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowiki/xs:element/nowiki

nowikixs:complexType name="ArrayOfQueryResultInfoSet"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="QueryResultInfoSet" nillable="true"/nowiki

type="tns:QueryResultInfoSet"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfQueryResultInfoSet" nillable="true" type="tns:ArrayOfQueryResultInfoSet"//nowiki

nowikixs:complexType name="QueryResultInfoSet"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="Model" nillable="true" type="tns:UUID"//nowiki

nowikixs:element minOccurs="0" name="Result" nillable="true" type="tns:ArrayOfXPathNodeInfoSet"//nowiki

nowikixs:element minOccurs="0" name="XPath" nillable="true" type="xs:string"//nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="QueryResultInfoSet" nillable="true" type="tns:QueryResultInfoSet"//nowiki

nowikixs:complexType name="ArrayOfXPathNodeInfoSet"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="XPathNodeInfoSet" nillable="true"/nowiki

type="tns:XPathNodeInfoSet"/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfXPathNodeInfoSet" nillable="true" type="tns:ArrayOfXPathNodeInfoSet"//nowiki

nowikixs:complexType name="XPathNodeInfoSet"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" name="InfoSetValue" nillable="true" type="xs:base64Binary"//nowiki

nowikixs:element minOccurs="0" name="NodeType"/nowiki

xmlns:q5="http://schemas.datacontract.org/2004/07/System.Xml.XPath" type="q5:XPathNodeType"

/

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="XPathNodeInfoSet" nillable="true" type="tns:XPathNodeInfoSet"//nowiki

nowiki/xs:schema /nowiki


      1. B.2.2.2Referenced Definitions
The following is the content of XPathNodeType.xsd:

nowiki?xml version="1.0" encoding="utf-8"?/nowiki

nowikixs:schema xmlns:tns="http://schemas.datacontract.org/2004/07/System.Xml.XPath" elementFormDefault="qualified" targetNamespace="http://schemas.datacontract.org/2004/07/System.Xml.XPath" xmlns:xs="http://www.w3.org/2001/XMLSchema"/nowiki

nowikixs:simpleType name="XPathNodeType"/nowiki

nowikixs:restriction base="xs:string"/nowiki

nowikixs:enumeration value="Root" //nowiki

nowikixs:enumeration value="Element" //nowiki

nowikixs:enumeration value="Attribute" //nowiki

nowikixs:enumeration value="Namespace" //nowiki

nowikixs:enumeration value="Text" //nowiki

nowikixs:enumeration value="SignificantWhitespace" //nowiki

nowikixs:enumeration value="Whitespace" //nowiki

nowikixs:enumeration value="ProcessingInstruction" //nowiki

nowikixs:enumeration value="Comment" //nowiki

nowikixs:enumeration value="All" //nowiki

nowiki/xs:restriction/nowiki

nowiki/xs:simpleType/nowiki

nowikixs:element name="XPathNodeType" nillable="true" type="tns:XPathNodeType" //nowiki

nowiki/xs:schema/nowiki


The following is the content of Types.xsd:

nowiki?xml version="1.0" encoding="utf-8"?/nowiki

nowikixs:schema xmlns:tns="http://schemas.microsoft.com/2003/10/Serialization/" attributeFormDefault="qualified" elementFormDefault="qualified" targetNamespace="http://schemas.microsoft.com/2003/10/Serialization/" xmlns:xs="http://www.w3.org/2001/XMLSchema"/nowiki

nowikixs:element name="anyType" nillable="true" type="xs:anyType" //nowiki

nowikixs:element name="anyURI" nillable="true" type="xs:anyURI" //nowiki

nowikixs:element name="base64Binary" nillable="true" type="xs:base64Binary" //nowiki

nowikixs:element name="boolean" nillable="true" type="xs:boolean" //nowiki

nowikixs:element name="byte" nillable="true" type="xs:byte" //nowiki

nowikixs:element name="dateTime" nillable="true" type="xs:dateTime" //nowiki

nowikixs:element name="decimal" nillable="true" type="xs:decimal" //nowiki

nowikixs:element name="double" nillable="true" type="xs:double" //nowiki

nowikixs:element name="float" nillable="true" type="xs:float" //nowiki

nowikixs:element name="int" nillable="true" type="xs:int" //nowiki

nowikixs:element name="long" nillable="true" type="xs:long" //nowiki

nowikixs:element name="QName" nillable="true" type="xs:QName" //nowiki

nowikixs:element name="short" nillable="true" type="xs:short" //nowiki

nowikixs:element name="string" nillable="true" type="xs:string" //nowiki

nowikixs:element name="unsignedByte" nillable="true" type="xs:unsignedByte" //nowiki

nowikixs:element name="unsignedInt" nillable="true" type="xs:unsignedInt" //nowiki

nowikixs:element name="unsignedLong" nillable="true" type="xs:unsignedLong" //nowiki

nowikixs:element name="unsignedShort" nillable="true" type="xs:unsignedShort" //nowiki

nowikixs:element name="char" nillable="true" type="tns:char" //nowiki

nowikixs:simpleType name="char"/nowiki

nowikixs:restriction base="xs:int" //nowiki

nowiki/xs:simpleType/nowiki

nowikixs:element name="duration" nillable="true" type="tns:duration" //nowiki

nowikixs:simpleType name="duration"/nowiki

nowikixs:restriction base="xs:duration"/nowiki

nowikixs:pattern value="\-?P(\d*D)?(T(\d*H)?(\d*M)?(\d*(\.\d*)?S)?)?" //nowiki

nowikixs:minInclusive value="-P10675199DT2H48M5.4775808S" //nowiki

nowikixs:maxInclusive value="P10675199DT2H48M5.4775807S" //nowiki

nowiki/xs:restriction/nowiki

nowiki/xs:simpleType/nowiki

nowikixs:element name="guid" nillable="true" type="tns:guid" //nowiki

nowikixs:simpleType name="guid"/nowiki

nowikixs:restriction base="xs:string"/nowiki

nowikixs:pattern value="[\da-fA-F](\da-fA-F){8}-[\da-fA-F](\da-fA-F){4}-[\da-fA-F](\da-fA-F){4}-[\da-fA-F](\da-fA-F){4}-[\da-fA-F](\da-fA-F){12}" //nowiki

nowiki/xs:restriction/nowiki

nowiki/xs:simpleType/nowiki

nowikixs:attribute name="FactoryType" type="xs:QName" //nowiki

nowikixs:attribute name="Id" type="xs:ID" //nowiki

nowikixs:attribute name="Ref" type="xs:IDREF" //nowiki

nowiki/xs:schema/nowiki


The following is the content of ArrayOfString.xsd:

nowiki?xml version="1.0" encoding="utf-8"?/nowiki

nowikixs:schema xmlns:tns="http://schemas.microsoft.com/2003/10/Serialization/Arrays" elementFormDefault="qualified" targetNamespace="http://schemas.microsoft.com/2003/10/Serialization/Arrays" xmlns:xs="http://www.w3.org/2001/XMLSchema"/nowiki

nowikixs:complexType name="ArrayOfstring"/nowiki

nowikixs:sequence/nowiki

nowikixs:element minOccurs="0" maxOccurs="unbounded" name="string" nillable="true" type="xs:string" //nowiki

nowiki/xs:sequence/nowiki

nowiki/xs:complexType/nowiki

nowikixs:element name="ArrayOfstring" nillable="true" type="tns:ArrayOfstring" //nowiki

nowiki/xs:schema/nowiki


1. Changes to NEMA Standards Publication PS3.16-2009
**PS3.16: Add the following context groups to Annex B:**

    1. CID 7180 Abstract Multi-Dimensional Image Model Component Semantics
center**CONTEXT ID 7180**/center

**Abstract Multi-Dimensional Image Model Component Semantics**

center**Type: ExtensibleVersion: 20100825 **/center


{| style="border-spacing:0;"
! centerCoding Scheme Designator(0008,0102)/center
! centerCode Value(0008,0100)/center
! centerCode Meaning (0008,0104)/center

|-
| colspan="3"  style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *INCLUDE CID 4033 MR Proton Spectroscopy Metabolites*

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center113063/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| T1 Map

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center113065/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| T2 Map

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center113064/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| T2* Map

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center113058/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Proton Density Map

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110800/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Spin Tagging Perfusion MR Signal Intensity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center113070/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Velocity encoded

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center113067/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Temperature encoded

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110801/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Contrast Agent Angio MR Signal Intensity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110802/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Time Of Flight Angio MR Signal Intensity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110803/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Proton Density Weighted MR Signal Intensity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110804/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| T1 Weighted MR Signal Intensity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110805/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| T2 Weighted MR Signal Intensity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110806/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| T2* Weighted MR Signal Intensity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center113043/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Diffusion weighted

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110807/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Field Map MR Signal Intensity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110808/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Fractional Anisotropy

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110809/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Relative Anisotropy

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center113041/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Apparent Diffusion Coefficient

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110810/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dxx Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110811/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dxy Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110812/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dxz Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110813/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dyy Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110814/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dyz Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110815/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dzz Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110816/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| T1 Weighted Dynamic Contrast Enhanced MR Signal Intensity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110817/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| T2 Weighted Dynamic Contrast Enhanced MR Signal Intensity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110818/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| T2* Weighted Dynamic Contrast Enhanced MR Signal Intensity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center113055/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Regional Cerebral Blood Flow

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center113056/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Regional Cerebral Blood Volume

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center113052/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Mean Transit Time

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center113069/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Time To Peak map

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110819/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Blood Oxygenation Level

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110820/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Nuclear Medicine Projection Activity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110821/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Nuclear Medicine Tomographic Activity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110822/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Spatial Displacement X Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110823/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Spatial Displacement Y Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110824/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Spatial Displacement Z Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110825/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Hemodynamic Resistance

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110826/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Indexed Hemodynamic Resistance

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center112031/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Attenuation Coefficient

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110827/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Tissue Velocity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110828/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Flow Velocity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerSRT/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerP0-02241/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Power Doppler

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110829/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Flow Variance

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110830/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Elasticity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110831/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Perfusion

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110832/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Speed of sound

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110833/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Ultrasound Attenuation

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center113068/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Students T-test

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center113071/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Z-score Map

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center113057/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| R-Coefficient Map 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110834/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| RGB R Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110835/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| RGB G Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110836/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| RGB B Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110837/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR FULL Y Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110838/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR FULL CB Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110839/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR FULL CR Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110840/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR PARTIAL Y Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110841/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR PARTIAL CB Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110842/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR PARTIAL CR Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110843/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR ICT Y Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110844/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR ICT CB Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110845/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR ICT CR Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110846/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR RCT Y Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110847/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR RCT CB Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110848/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR RCT CR Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110849/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Echogenicity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110850/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| X-Ray Attenuation

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110851/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| X-Ray Attenuation Coefficient

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110852/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| MR signal intensity

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110853/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Binary Segmentation

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110854/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Fractional Probabilistic Segmentation

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110855/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Fractional Occupancy Segmentation

|}
    1. CID 7181 Abstract Multi-Dimensional Image Model Component Units
center**CONTEXT ID 7181**/center

**Abstract Multi-Dimensional Image Model Component Units**

center**Type: ExtensibleVersion: 20100825**/center


{| style="border-spacing:0;"
! centerCoding Scheme Designator(0008,0102)/center
! centerCode Value(0008,0100)/center
! centerCode Meaning (0008,0104)/center

|-
| colspan="3"  style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *INCLUDE CID 3500 Pressure Units*

|-
| colspan="3"  style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *INCLUDE CID 3502 Hemodynamic Resistance Units*

|-
| colspan="3"  style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *INCLUDE CID 3503 Indexed Hemodynamic Resistance Units*

|-
| colspan="3"  style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *INCLUDE CID 7460 Units of Linear Measurement*

|-
| colspan="3"  style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *INCLUDE CID 7461 Units of Area Measurement*

|-
| colspan="3"  style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *INCLUDE CID 7462 Units of Volume Measurement*

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center1/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| no units

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center{ratio}/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| ratio

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centernowiki[hnsfU](hnsfU)/nowiki/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Hounsfield Unitnbsp;

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center{counts}/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Counts

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center{counts}/s/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Counts per second

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centernowiki[arbU](arbU)/nowiki/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| arbitrary unit

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centercm/s/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centimeter/second

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centermm/s/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| millimeter/second

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerdB/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| decibel

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerCel/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| degrees Celsius

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerml/min/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| milliliter per minute

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerml/s/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| milliliter per second

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerms/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| millisecond

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centers/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| second

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerHz/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Herz

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centermT/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| milliTesla

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centernowiki{Particles}/[100](100)g{Tissue}/nowiki/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| number particles per 100 gram of tissue

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centermm2/s/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| square millimeter per second

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centers/mm2/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| second per square millimeter

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centernowikiml/[100](100)g/min/nowiki/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| milliliter per 100 gram per minute

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centernowikiml/[100](100)ml/nowiki/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| milliliter per 100 milliter

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centermmol/kg{WetWeight}/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| millimoles per kg wet weight

|}
    1. CID 7182 Abstract Multi-Dimensional Image Model Dimension Semantics
center**CONTEXT ID 7182**/center

**Abstract Multi-Dimensional Image Model Dimension Semantics**

center**Type: ExtensibleVersion: 20100825**/center


{| style="border-spacing:0;"
! centerCoding Scheme Designator(0008,0102)/center
! centerCode Value(0008,0100)/center
! centerCode Meaning (0008,0104)/center

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110856/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Linear Displacement

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110857/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Photon Energy

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110858/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Time

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110859/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Angle

|}
    1. CID 7183 Abstract Multi-Dimensional Image Model Dimension Units
center**CONTEXT ID 7183**/center

**Abstract Multi-Dimensional Image Model Dimension Units**

center**Type: ExtensibleVersion: 20100825**/center


{| style="border-spacing:0;"
! centerCoding Scheme Designator(0008,0102)/center
! centerCode Value(0008,0100)/center
! centerCode Meaning (0008,0104)/center

|-
| colspan="3"  style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *INCLUDE CID 7460 Units of Linear Measurement*

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerms/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Millisecond

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centers/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Second

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerdeg/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Degree

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerUCUM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerrad/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Radian

|}
    1. CID 7184 Abstract Multi-Dimensional Image Model Axis Direction
center**CONTEXT ID 7184**/center

**Abstract Multi-Dimensional Image Model Axis Direction**

center**Type: ExtensibleVersion: 20100825**/center


{| style="border-spacing:0;"
! centerCoding Scheme Designator(0008,0102)/center
! centerCode Value(0008,0100)/center
! centerCode Meaning (0008,0104)/center

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110860/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Left-Right Axis

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110861/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Head-Foot Axis

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110862/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Anterior-Posterior Axis

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110863/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Apex-Base Axis

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110864/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Anterior-Inferior Axis

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110865/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Septum-Wall Axis

|}
    1. CID 7185 Abstract Multi-Dimensional Image Model Axis Orientation
center**CONTEXT ID 7185**/center

**Abstract Multi-Dimensional Image Model Axis Orientation**

center**Type: ExtensibleVersion: 20100825**/center


{| style="border-spacing:0;"
! centerCoding Scheme Designator(0008,0102)/center
! centerCode Value(0008,0100)/center
! centerCode Meaning (0008,0104)/center

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110866/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Right To Left

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110867/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Left To Right

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110868/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Head To Foot

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110869/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Foot To Head

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110870/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Anterior To Posterior

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110871/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Posterior To Anterior

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110872/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Apex To Base

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110873/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Base To Apex

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110874/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Anterior To Inferior

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110875/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Inferior To Anterior

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110876/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Septum To Wall

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110877/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Wall To Septum

|}
    1. CID 7186 Abstract Multi-Dimensional Image Model Qualitative Dimension Sample Semantics
center**CONTEXT ID 7186**/center

**Abstract Multi-Dimensional Image Model Qualitative Dimension Sample Semantics**

center**Type: ExtensibleVersion: 20100825**/center


{| style="border-spacing:0;"
! centerCoding Scheme Designator(0008,0102)/center
! centerCode Value(0008,0100)/center
! centerCode Meaning (0008,0104)/center

|-
| colspan="3"  style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| *INCLUDE CID 4033 MR Proton Spectroscopy Metabolites*

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110810/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dxx Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110811/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dxy Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110812/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dxz Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110813/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dyy Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110814/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dyz Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110815/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dzz Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110834/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| RGB R Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110835/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| RGB G Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110836/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| RGB B Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110837/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR FULL Y Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110838/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR FULL CB Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110839/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR FULL CR Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110840/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR PARTIAL Y Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110841/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR PARTIAL CB Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110842/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR PARTIAL CR Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110843/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR ICT Y Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110844/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR ICT CB Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110845/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR ICT CR Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110846/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR RCT Y Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110847/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR RCT CB Component

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| centerDCM/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110848/center
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR RCT CR Component

|}
**PS3.16: Add the following terminology definitions to Annex D:**

1. Annex DDICOM Controlled Terminology Definitions (Normative)
This Annex specifies the meanings of codes defined in DICOM, either explicitly or by reference to another part of DICOM or an external reference document or standard.

center**DICOM Code Definitions (Coding Scheme Designator DCM Coding Scheme Version 01)**/center


{| style="border-spacing:0;"
! centerCode Value/center
! centerCode Meaning/center
! centerDefinition/center

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110800/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Spin Tagging Perfusion MR Signal Intensity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Signal intensity of a Spin tagging Perfusion MR image. Spin tagging is a technique for the measurement of blood perfusion, based on magnetically labeled arterial blood water as an endogenous tracer. 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110801/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Contrast Agent Angio MR Signal Intensity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Signal intensity of a Contrast Agent Angio MR image.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110802/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Time Of Flight Angio MR Signal Intensity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Signal intensity of a Time-of-flight (TOF) MR image. Time-of-flight (TOF) is based on the phenomenon of flow-related enhancement of spins entering into an imaging slice. As a result of being unsaturated, these spins give more signal that surrounding stationary spins. 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110803/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Proton Density Weighted MR Signal Intensity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Signal intensity of a Proton Density Weighted MR image. All MR images have intensity proportional to proton density. Images with very little T1 or T2 weighting are called PD-weighted. 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110804/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| T1 Weighted MR Signal Intensity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Signal intensity of T1 Weighted MR image. A T1 Weighted MR image is created typically by using short TE and TR times.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110805/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| T2 Weighted MR Signal Intensity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Signal intensity of a T2 Weighted MR image. T2 Weighted image contrast state is approached by imaging with a TR long compared to tissue T1 (to reduce T1 contribution to image contrast) and a TE between the longest and shortest tissue T2s of interest. 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110806/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| T2* Weighted MR Signal Intensity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Signal intensity of a T2* Weighted MR image. The T2* phenomenon results from molecular interactions (spin spin relaxation) and local magnetic field non-uniformities, which cause the protons to precess at slightly different frequencies.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110807/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Field Map MR Signal Intensity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Signal intensity of a Field Map MR image. A Field Map MR image provides a direct measure of the *B*sub0/sub inhomogeneity at each point in the image.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110808/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Fractional Anisotropy
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Coefficient reflecting the fractional anisotropy of the tissues, derived from a diffusion weighted MR image. Fractional anisotropy is proportional to the square root of the variance of the Eigen values divided by the square root of the sum of the squares of the Eigen values.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110809/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Relative Anisotropy
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Coefficient reflecting the relative anisotropy of the tissues, derived from a diffusion weighted MR image.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110810/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dxx Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Dxx Component of the diffusion tensor, quantifying the molecular mobility along the X axis.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110811/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dxy Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Dxy Component of the diffusion tensor, quantifying the correlation of molecular displacements in the X and Y directions.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110812/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dxz Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Dxz Component of the diffusion tensor, quantifying the correlation of molecular displacements in the X and Z directions.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110813/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dyy Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Dyy Component of the diffusion tensor, quantifying the molecular mobility along the Y axis.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110814/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dyz Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Dyz Component of the diffusion tensor, quantifying the correlation of molecular displacements in the Y and Z directions.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110815/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Volumetric Diffusion Dzz Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Dzz Component of the diffusion tensor, quantifying the molecular mobility along the Z axis.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110816/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| T1 Weighted Dynamic Contrast Enhanced MR Signal Intensity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Signal intensity of a T1 Weighted Dynamic Contrast Enhanced MR image. A T1 Weighted Dynamic Contrast Enhanced MR image reflects the dynamics of diffusion of the exogenous contrast media from the blood pool into the extra vascular extracellular space (EES) of the brain at a rate determined by the blood flow to the tissue, the permeability of the Brain Blood Barrier (BBB), and the surface area of the perfusing vessels.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110817/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| T2 Weighted Dynamic Contrast Enhanced MR Signal Intensity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Signal intensity of a T2 Weighted Dynamic Contrast Enhanced MR image. A T2 Weighted Dynamic Contrast Enhanced MR image reflects the T2 of tissue decrease as the Gd contrast agent bolus passes through the brain. 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110818/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| T2* Weighted Dynamic Contrast Enhanced MR Signal Intensity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Signal intensity of a T2* Weighted Dynamic Contrast Enhanced MR image. A T2* Weighted Dynamic Contrast Enhanced MR image reflects the T2* of tissue decrease as the Gd contrast agent bolus passes through the brain.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110819/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Blood Oxygenation Level
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Signal intensity of a Blood Oxygenation Level image. BOLD imaging is sensitive to blood oxygenation (but also to cerebral blood flow and volume). This modality is essentially used for detecting brain activation (functional MR). 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110820/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Nuclear Medicine Projection Activity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Accumulated decay event counts in a nuclear medicine projection image.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110821/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Nuclear Medicine Tomographic Activity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Accumulated decay event counts in a Nuclear Medicine Tomographic image (including PET).

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110822/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Spatial Displacement X Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Spatial Displacement along axis X of a non linear deformable spatial registration image. The X axis is defined in reference to the patients orientation, and is increasing to the left hand side of the patient.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110823/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Spatial Displacement Y Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Spatial Displacement along axis Y of a non linear deformable spatial registration image. The Y axis is defined in reference to the patients orientation, and is increasing to the posterior side of the patient.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110824/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Spatial Displacement Z Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Spatial Displacement along axis Z of a Non linear deformable spatial registration image. The Z axis is defined in reference to the patients orientation, and is increasing toward the head of the patient.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110825/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Hemodynamic Resistance
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Measured resistance to the flow of blood, e.g. through the vasculature or through a heart value.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110826/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Indexed Hemodynamic Resistance
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Measured resistance to the flow of blood, e.g. through the vasculature or through a heart value, normalized to a particular indexed scale.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110827/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Tissue Velocity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Velocity of tissue based on Doppler measurements. 

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110828/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Flow Velocity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Velocity of blood flow based on Doppler measurements.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110829/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Flow Variance
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Statistical variance of blood velocity relative to mean.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110830/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Elasticity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Scalar value related to the elastic properties of the tissue.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110831/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Perfusion
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Scalar value related to the volume of blood perfusing into tissue.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110832/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Speed of sound
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Speed of sound in tissue.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110833/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Ultrasound Attenuation
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Reduction in strength of ultrasound signal as the wave.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110834/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| RGB R Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Red component of a true color image (RGB).

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110835/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| RGB G Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Green component of a true color image (RGB).

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110836/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| RGB B Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Blue component of a true color image (RGB).

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110837/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR FULL Y Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Y (Luminance) component of a YBR FULL image, as defined in JPEG 2000.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110838/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR FULL CB Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CB (Blue chrominance) component of a YBR FULL image, as defined in JPEG 2000.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110839/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR FULL CR Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CR (Red chrominance) component of a YBR FULL image, as defined in JPEG 2000.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110840/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR PARTIAL Y Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Y (Luminance) component of a YBR PARTIAL image, as defined in JPEG 2000.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110841/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR PARTIAL CB Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CB (Blue chrominance) component of a YBR PARTIAL image, as defined in JPEG 2000.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110842/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR PARTIAL CR Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CR (Red chrominance) component of a YBR PARTIAL image, as defined in JPEG 2000.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110843/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR ICT Y Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Y (Luminance) component of a YBR ICT image (Irreversible Color Transform), as defined in JPEG 2000.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110844/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR ICT CB Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CB (Blue chrominance) component of a YBR ICT image (Irreversible Color Transform), as defined in JPEG 2000.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110845/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR ICT CR Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CR (Red chrominance) component of a YBR ICT image (Irreversible Color Transform), as defined in JPEG 2000.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110846/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR RCT Y Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Y (Luminance) component of a YBR RCT image (Reversible Color Transform), as defined in JPEG 2000.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110847/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR RCT CB Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CB (Blue chrominance) component of a YBR RCT image (Reversible Color Transform), as defined in JPEG 2000.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110848/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| YBR RCT CR Component
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| CR (Red chrominance) component of a YBR RCT image (Reversible Color Transform), as defined in JPEG 2000.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110849/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Echogenicity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| The ability of a material to create an ultrasound return echo.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110850/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| X-Ray Attenuation
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Decrease in the number of photons in an X-ray beam due to interactions with the atoms of a material substance. Attenuation is due primarily to two processes, absorption and scattering.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110851/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| X-Ray Attenuation Coefficient
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Coefficient which describes the fraction of a beam of x-rays or gamma rays that is absorbed or scattered per unit thickness of the absorber. This value basically accounts for the number of atoms in a cubic cm volume of material and the probability of a photon being scattered or absorbed from the nucleus or an electron of one of these atoms.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110852/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| MR signal intensity
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Signal intensity of an MR image, not otherwise specified.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110853/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Binary Segmentation
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Binary value denoting that the segmented property is present.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110854/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Fractional Probabilistic Segmentation
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Probability, defined as a percentage, that the segmented property occupies the spatial area defined by the voxel.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110855/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Fractional Occupancy Segmentation
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Percentage of the voxel area occupied by the segmented property.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110856/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Linear Displacement
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Spatial dimension, denoting a linear displacement.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110857/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Photon Energy
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Dimension denoting the energy (frequency or wavelength) of photons.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110858/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Time
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Dimension used to sequence events, to compare the duration of events and the intervals between events.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110859/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Angle
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Spatial dimension, denoting an angle.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110860/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Left-Right Axis
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A spatial dimension axis running along a line between the patients left and right side.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110861/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Head-Foot Axis
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A spatial dimension axis running along a line between the patients head and foot.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110862/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Anterior-Posterior Axis
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A spatial dimension axis running along a line between the patients anterior and posterior sides.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110863/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Apex-Base Axis
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A spatial dimension axis running along a line between the apex and base of an organ, object, or chamber.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110864/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Anterior-Inferior Axis
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A spatial dimension axis running along a line between the anterior and inferior sides of an organ, object, or chamber.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110865/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Septum-Wall Axis
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| A spatial dimension axis running along a line between the septum and wall of a chamber.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110866/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Right To Left
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Orientation of a spatial dimension where increasing values run from the right to the left side of the patient.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110867/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Left To Right
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Orientation of a spatial dimension where increasing values run from the left to the right side of the patient.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110868/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Head To Foot
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Orientation of a spatial dimension where increasing values run from the head to the foot of the patient.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110869/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Foot To Head
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Orientation of a spatial dimension where increasing values run from the foot to the head of the patient.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110870/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Anterior To Posterior
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Orientation of a spatial dimension where increasing values run from the anterior to the posterior side of the patient.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110871/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Posterior To Anterior
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Orientation of a spatial dimension where increasing values run from the posterior to the anterior side of the patient.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110872/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Apex To Base
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Orientation of a spatial dimension where increasing values run from the apex to the base.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110873/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Base To Apex
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Orientation of a spatial dimension where increasing values run from the base to the apex.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110874/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Anterior To Inferior
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Orientation of a spatial dimension where increasing values run from the anterior to the inferior.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110875/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Inferior To Anterior
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Orientation of a spatial dimension where increasing values run from the inferior to the anterior.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110876/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0069in solid #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Septum To Wall
| style="border:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Orientation of a spatial dimension where increasing values run from the septum of a chamber to the opposite wall.

|-
| style="border-top:0.0069in solid #000000;border-bottom:0.0153in double #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| center110877/center
| style="border-top:0.0069in solid #000000;border-bottom:0.0153in double #000000;border-left:0.0069in solid #000000;border-right:none;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Wall To Septum
| style="border-top:0.0069in solid #000000;border-bottom:0.0153in double #000000;border-left:0.0069in solid #000000;border-right:0.0069in solid #000000;padding-top:0in;padding-bottom:0in;padding-left:0.075in;padding-right:0.075in;"| Orientation of a spatial dimension where increasing values run from the opposite wall to the septum of a chamber.

|}