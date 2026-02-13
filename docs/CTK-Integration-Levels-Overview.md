---
title: CTK Integration Levels Overview
---

CTK *supports* the *common use* of medical imaging software developments on 
*different levels* (not all of these levels are available yet).
This ranges from loosely coupled applications (level 1: basically data exchange) to more and more tight integration (level 2: parameter exchange; level 3: exchange of events; level 4: exchange of services; level 5: complete integration).

{|border="0" cellspacing="0" cellpadding="4"
!
! CTK benefit for Host
! CTK benefit for App/Module
|- style="background-color:#EEEEEE;"
| Level 1: DICOM Part 19
([Scenarios](IntegrationLevel1Details.html), [Details](Documentation/DicomApplicationHosting.html))
| 
- Host communication
- Data preparation for DataExchange interface
- Default implementation of host business logic
|
- Application communication
- Default implementation of application business logic
|-
| Level 2: Command line interface 
([Scenarios](IntegrationLevel2Details.html), [Details](Documentation/Command-Line-Interface.html))
| 
- parsing of parameter descriptions
- GUI generation (optional)
|
- publishing of parameter descriptions
|- style="background-color:#EEEEEE;"
| Level 3: CTK event bus 
([Scenarios](IntegrationLevel3Details.html), [Details](Documentation/Messaging.html))

|colspan="2"|
- publish and subscribe for arbitrary communication between modules and applications
- possibly out of process
|-
| Level 4: CTK services
([Scenarios](IntegrationLevel4Details.html), [Details](Documentation/CTK-Plugin-Framework-Introduction.html))
|colspan="2"|
- Component-based software development
- Service discovery
- Base services: event bus, configuration admin, logging, meta type management
|- style="background-color:#EEEEEE;"
| Level 5: Classic C++
([Scenarios](Level5Details.html))
|colspan="2"|
- DICOM Q/R ([ctkDICOMAppWidget](http://www.commontk.org/docs/html/classctkDICOMAppWidget.html), [ctkDICOMServerNodeWidget](http://www.commontk.org/docs/html/classctkDICOMServerNodeWidget.html))
- Local DICOM file management (indexer, database ) ([ctkDICOMModel](http://www.commontk.org/docs/html/classctkDICOMModel.html))
- DICOM testing infrastructure
- Qt widgets for DICOM, Medical Imaging applications  ([Image Gallery](Documentation/ImageGallery.html), [Plans](Documentation/WidgetPlans.html))
- Scripting support ([ctkPythonShell](http://www.commontk.org/docs/html/classctkPythonShell.html))
- Application launcher