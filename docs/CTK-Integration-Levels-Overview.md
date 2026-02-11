---
title: CTK Integration Levels Overview
render_with_liquid: false
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
([Scenarios](Scenarios)(IntegrationLevel1Details.md), [Details](Details)(Documentation/DicomApplicationHosting.md))
| 
- Host communication
- Data preparation for DataExchange interface
- Default implementation of host business logic
|
- Application communication
- Default implementation of application business logic
|-
| Level 2: Command line interface 
([Scenarios](Scenarios)(IntegrationLevel2Details.md), [Details](Details)(Documentation/Command Line Interface.md))
| 
- parsing of parameter descriptions
- GUI generation (optional)
|
- publishing of parameter descriptions
|- style="background-color:#EEEEEE;"
| Level 3: CTK event bus 
([Scenarios](Scenarios)(IntegrationLevel3Details.md), [Details](Details)(Documentation/Messaging.md))

|colspan="2"|
- publish and subscribe for arbitrary communication between modules and applications
- possibly out of process
|-
| Level 4: CTK services
([Scenarios](Scenarios)(IntegrationLevel4Details.md), [Details](Details)(Documentation/CTK Plugin Framework: Introduction.md))
|colspan="2"|
- Component-based software development
- Service discovery
- Base services: event bus, configuration admin, logging, meta type management
|- style="background-color:#EEEEEE;"
| Level 5: Classic C++
([Scenarios](Scenarios)(Level5Details.md))
|colspan="2"|
- DICOM Q/R ([ctkDICOMAppWidget](ctkDICOMAppWidget)(http://www.commontk.org/docs/html/classctkDICOMAppWidget.html), [ctkDICOMServerNodeWidget](ctkDICOMServerNodeWidget)(http://www.commontk.org/docs/html/classctkDICOMServerNodeWidget.html))
- Local DICOM file management (indexer, database ) ([ctkDICOMModel](ctkDICOMModel)(http://www.commontk.org/docs/html/classctkDICOMModel.html))
- DICOM testing infrastructure
- Qt widgets for DICOM, Medical Imaging applications  ([Gallery](Gallery)(Image)(Documentation/ImageGallery.md), [Plans](Plans)(Documentation/WidgetPlans.md))
- Scripting support ([ctkPythonShell](ctkPythonShell)(http://www.commontk.org/docs/html/classctkPythonShell.html))
- Application launcher

