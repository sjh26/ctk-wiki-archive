---
title: CTK-Hackfest-May-2013
---

1. Event pictures
Images from the hackfest
gallery widths=300 px heights=200px perrow=3

File:2013-05-20_16.16.28.jpg|bigDiscussions on Monday/big
File:2013-05-21_11.33.58.jpg|bigPlanning on Tuesday/big
/gallery

Social programs

gallery widths=150 px heights=100px perrow=4
File:Hackfest2013_AtGabors1.jpg|Dinner at Gabor's house
File:Hackfest2013_AtGabors2.jpg
File:Hackfest2013_bbq1.jpg|BBQ with the PerkLab
File:Hackfest2013_bbq2.jpg
File:Hackfest2013_bbq3.jpg
File:Hackfest2013_PerkLabAndCtkGroup1.jpg|Group picture with the PerkLab
File:Hackfest2013_PerkLabAndCtkGroup2.jpg
File:Poutine.jpg|[Poutine for lunch!](http://en.wikipedia.org/wiki/Poutine)
/gallery

  1. Introduction
**Date:** May 20-24, 2013

**Location:**  [Kingston, Ontario, Canada](http://en.wikipedia.org/wiki/Kingston,_Ontario).  In a classroom at Queens University.

**Goal:** A follow on to the [wildly successful previous hackfests!](CommontkCurrent-events.html#Past_events)

**Requirements:** Attendees must be willing to spend their time during the event writing ctk code that contributes to the main [ctk roadmap](CTK-Roadmap.html).  This means spending the week immersed in C++, Qt, DCMTK, CMake, and related technologies.  People who do not feel qualified for this task are politely not invited :)

**Group size:** Maximum 20 participants so we can have a manageable working meeting.  The organizing committee will invite and select participants based on input from [TheTeam](TheTeam.html).

**Site Hosts:** Gabor Fichtinger, Csaba Pinter, Andras Lasso

**Organizing Committee:** Ivo Wolf, Stephen Aylward, Steve Pieper

**Future Events:** Future hackfests will be announced in advance, and we hope lots of people will be interested in participating.  The venue and activities at future hackfests will be determined based on the number of active participants in the project.   We welcome participation via the CTK email lists, the source code repository, and this website.

  1. Attendees
*So far we have received confirmation for the following people (in no particular order). 


Please fill in your intentions in terms of common accommodation.

{|class="wikitable alternance" style="text-align:left; border:1px solid black;"
|+ ***Participants***
|-
! scope=col style="background:#cde6f8;"| Name
! scope=col style="background:#cde6f8;"| Organization
|-
|Steve Pieper
|Isomics, Inc., Cambridge, MA, USA
|-
|Ivo Wolf
|Hochschule Mannheim
|-
|Marco Nolden
|German Cancer Research Center (DKFZ)
|-
|Sascha Zelzer
|German Cancer Research Center (DKFZ)
|-
|Andreas Fetzer
|German Cancer Research Center (DKFZ)
|-
|Florian Vichot
|INRIA
|-
|Lawrence Tarbox
|Washington University, St. Louis
|-
|Andras Lasso
|Queen's University, Kingston, ON
|-
|Csaba Pinter
|Queen's University, Kingston, ON
|-
|Alberto Biancardi
|The University of Sheffield, UK
|-
| Xenios Papademetris
| Yale University US
|-
|}

{|class="wikitable alternance" style="text-align:left; border:1px solid black;"
|+ ***Google Hangout Participants***
|-
! scope=col style="background:#cde6f8;"| Name
! scope=col style="background:#cde6f8;"| Organization
|-
| Jean-Christophe Fillion-Robin
| Kitware Inc. 
|-
|}

!--
- People who manifested interest in joining the fest. Please move your names up to the confirmed table, with the details as soon as you can to facilitate discussions with potential hotels.

{|class="wikitable alternance" style="text-align:left; border:1px solid black;"
|+ ***Confirmed***
|-
! scope=col style="background:#cde6f8;"| Name
! scope=col style="background:#cde6f8;"| Organization

|}
--

`{{Note}}`There were also other invitations sent to active people on the community, and people who recently showed interest. When their intent will be known they will be added to the list.

  1. Preparation
Developers should bring a laptop with the [current CTK source code](http://github.com/commontk/CTK) downloaded and [built](Build-Instructions.html).

Use the [CTK developers mailing list](http://public.kitware.com/cgi-bin/mailman/listinfo/ctk-developers) to discuss build issues and topics for ongoing work.

Phone conferences have been scheduled in the weeks leading to the event:
- To be announced

  1. Topics and Projects
      1. DICOM Application Hosting
- Results:
** Merged DAH branch into master
** Slicer as Hosted Application (Ivo, Lawrence, Steve) [https://github.com/pieper/SlicerDICOMHosting](https://github.com/pieper/SlicerDICOMHosting)
*** launch hosted app, send data
*** loaded into slicer for manipulation
*** changed data detected automatically
*** TODO: data sent back to host
*** TODO: act on bringToFront events (includes resizing)
** pushed corresponding CTK-based MITK hosted/host application
** Started to develop integration tests
- Plans
** finish data return to host by end of next hackfest ;)
** Interoperability testing of CTK with other Application Hosting code
** Lawrence to test CTK code against the XIP hosting implementation
** Testing framework to be continued

      1. DICOM Database and Networking
- Review implementation issues when using CTK DICOM
** DICOM issues in github [https://github.com/commontk/CTK/issues?labels=DICOMstate=open](https://github.com/commontk/CTK/issues?labels=DICOMstate=open)
** del Incorrect import when DICOMDIR is present [http://na-mic.org/Bug/view.php?id=3111](http://na-mic.org/Bug/view.php?id=3111).  Should we skip DICOMDIR when it is not picked explicitly? /del `{{done}}`
** Incorrect/slow database behavior when multiple processes access it simultaneously [http://na-mic.org/Bug/view.php?id=3106](http://na-mic.org/Bug/view.php?id=3106) (interference between ctkDICOMIndexer and ctkDICOMModel)
- Discuss DICOM-RT for CTK
- Discuss DICOM Export options
** CLI outputs converted into real DICOM
** RT and other non-imaging types
*** GUI Issues
*** Lower-level dcmrt issues, possible use of DKFZ toolkit
*** Use of various tools (VTK, ITK, Plastimatch), validation

- GUI
** https://bigfiles.assembla.com/spaces/slicerrt/documents/download/DicomPatientBrowsersReview.pptx

- Results
** New DB table of display overrides
** New table view of patient/study/series - ctkDICOMTableView
** New Layout control for ctkDICOMBrowser to replace tree and ctkDICOMModel
** New signals to match use cases
** New signals for ctkDICOMDatabase during imports and new dialog in app widget to show summary results
- Plans
** issue #336 - create replacement for ctkDICOMAppWidget and deprecate old (Marco)
** issue #337 - implement signals from table view (Marco and Andras with Steve)
** issue #331 - to be completed soon by Andreas
** issue #332 - ctkDICOMTableManager to control layouts (also Andreas)
** issue #276 - fix up RT use cases (Andras and Csaba)
** Review naming View vs. Widget 
** Look into re-using  http://www.commontk.org/index.php/File:CtkSearchBox3.png
** Marco is making ctkDICOM2

      1. Widgets
- Spin box development [http://public.kitware.com/pipermail/ctk-developers/2013-May/001125.html](http://public.kitware.com/pipermail/ctk-developers/2013-May/001125.html)
- delctkDICOMModel and display of real-world patient data (RT special cases for example)/del - `{{done}}`
- Compare [widget plans](Documentation/WidgetPlans.html) with [current set](Documentation/ImageGallery.html).
- Qt5 Compatibility?
** delWorking on VTK / Qt5 compatibility/del - `{{done}}` VTK6 topic : http://review.source.kitware.com/#/t/2803

- Results
** Miklos and Julien developed plan for resolving spin box features: there will be a ctkDoubleSpinBox with new precision features migrated from current ctkSpinBox and Miklos's changes to expose more of the QSpinBox features.
** Jc was Qt5+VTK6 issues and plans to backport them to VTK5.10

      1. Tests Framework
- Qt testing framework
** Checkpoint verification
** Possibly help debugging when a test is failing and fixing a test
- Check log for warnings and errors
- Integrate with Error Log widget and the app launcher (but won't work on mac)
- Suggest as something for student at CREATIS
** Rotating log files
** capturing screen during test to help diagnose failures
** capturing all output to log files and flushing
** report crash utility for user to send all files to file issue
** auto-detect crashes using some kind of token
** track the exact version of libraries and stack traces (platform specific)  Look into google crashpad.
** Review squish video: http://www.froglogic.com/squish/gui-testing/squish-qt-webinar-qanda.php

- Results  Plans
** CREATIS group attended hangout and plans to contribute to QtTesting

      1. Build Systems  Software process
- delDCMTK build issues [http://public.kitware.com/pipermail/ctk-developers/2013-May/001122.html](http://public.kitware.com/pipermail/ctk-developers/2013-May/001122.html) [http://public.kitware.com/pipermail/ctk-developers/2013-May/001120.html](http://public.kitware.com/pipermail/ctk-developers/2013-May/001120.html)/del `{{done}}` Fixed by [74b4b07b9](https://github.com/commontk/CTK/commit/74b4b07b92f2a3ac492fef6dcb429bd08c513d59)
- A drop-in CMake module allowing to easily setup Superbuild project. 
** Consolidate CTK, Slicer, .. approach
- Collection of "External_XXX.cmake" file that could easily be re-used ? (See https://github.com/BRAINSia/NAMICExternalProjects)
- delFinalize work related to qRestAPI project (pending since Bologna hackfest)/del `{{done}}` History cleaned and pushed: https://github.com/commontk/qRestAPI
- Results
** Fixed and tested the DCMTK build issues
** Windows build issues identified for PythonQt on windows vs 2010/2012 (include order of std vector header)
** Still some more issues, likely also to do with include order

      1. Command Line Modules
- Using CLI XML to build stand-alone widget [https://github.com/pieper/CTK/blob/8391b2f54e18e68e6672a4d3a54da38bc9c77b79/Libs/CommandLineModules/Widgets/Testing/Cpp/ctkCmdLineModuleWidgetTest1.cpp#L86](https://github.com/pieper/CTK/blob/8391b2f54e18e68e6672a4d3a54da38bc9c77b79/Libs/CommandLineModules/Widgets/Testing/Cpp/ctkCmdLineModuleWidgetTest1.cpp#L86)[http://www.commontk.org/index.php/File:Cli-widget-prototype-2012-12-14.png](http://www.commontk.org/index.php/File:Cli-widget-prototype-2012-12-14.png)
- Contribute Slicer fixes to CLI infrastructure. See https://github.com/jcfr/CTK/tree/279-tweak-cmdlinemodule-library-for-slicer-integration
- Hierarchy nodes preserved on CLI execution
** keep the CLI simple.
** xinclude to allow people to centralize their grant support and other boilerplate info

- Results
** Xenios and Sascha performed tests and discussed many options 
*** Explored C++ tools for generating the CLI XML on the fly
*** Lots of ideas and Xenios has some TODO items and he will push to a fork for review.

      1. qRestAPI and XNAT API
- Results
** Sascha and Florian built on Miklos's work from last hackfest
** Many C++ level accessors are now available in a rough application
** Can login to XNAT, list projects, lists subjects in project
** Florian and Sascha contacted Tim Olsen and Dan Marcus to work through some questions on the REST API of XNAT
- Plans
** Work will continue and people will stay in touch.
** Now there is a CTK library outside the plugin framework
** New widgets and models reflecting status
** The XNAT group expressed enthusiasm to work with CTK
** INRIA is researching and evaluating XNAT to see if it will fill needs
** Maxime is in contact with the CVI (cardiovascular) group associated with the XNAT developers (http://cvrgrid.org/featured/xnat-cvi)
** DKFZ is likely to deploy XNAT instances unless there are unforeseen roadblocks
*** Want to take advantage of distributed project sharing
*** Pushing from PACS into common space
** BWH also has internal XNAT implementations with several years worth of prostate biopsy databases.

  1. Agenda
      1. Monday
Opening discussion
- Review topics and projects
- Plans for the week

Evening: BBQ at the Fichtinger residence

      1. Tuesday
During the day: hack, hack, hack...

Evening: Dinner and beers at the [Kingston Brewery](http://www.kingstonbrewing.ca/)

      1. Wednesday
During the day: hack, hack, hack...
10:30 Hangout to review status

Evening: [Kingston Haunted Walks](http://www.hauntedwalk.com/kingstontours.php)

      1. Thursday
During the day: hack, hack, hack...

Evening: BBQ by the [gazebo](http://farm5.staticflickr.com/4042/4276978263_96c7a234ff_b.jpg) on the waterfront

      1. Friday
During the day: hack, hack, hack...

Late morning; Closing discussion

https://plus.google.com/hangouts/_/33c4f3b6fd88ee2330172c2c91439632c7d6e9b6?authuser=0hl=en

- [Next hackfest in London, UK](http://public.kitware.com/pipermail/ctk-developers/2013-May/001126.html)!?! 
- Then back in North America - St. Louis - when?

Afternoon: hack or travel

  1. Gallery of Results
Images from the hackfest
gallery widths=300 px heights=200px perrow=3
File:Screen Shot 2013-05-24 at 10.23.16 AM.png |bigSlicer running as DICOM Hosted Application using CTK infrastructure/big
Image:MITKasHostedApp-and-asHost-withCLIasHostedApp.jpg|For comparison image from Bologna Hackfest: MITK running as DICOM Application Hosting hosted application (hosted by ctkDICOMHost) as well as hosting system with CTK-CLI as hosted application
File:Screen Shot 2013-05-24 at 11.27.52 AM.png |bigSummary dialog after DICOM import shown in use in slicer.  Uses new signals from ctkDICOMDatabase and the signal tracking in ctkDICOMAppWidget/big
File:TableView_Horizontal_Sorting.png |bigNew DICOMWidgets with horizontal orientation. The ctkDICOMTableView uses the QSqlQueryModel to display the database content/big
File:TableView_Vertical_Sorting.png |bigNew DICOMWidgets with vertical orientation./big

/gallery

  1. Travel  Hotel
**Local contact**

Need any help in organizing your visit, contact Andras Lasso (lasso@cs.queensu.ca).
If you have any troubles during your visit, call *TBD*.

**Airport** 

- Option A: Fly into Kingston via Toronto
- Option B: Fly into Toronto, take a bus to Kingston
** Recommended: Coach Canada direct bus from Toronto Airport to Kingston, leaves twice a day: 2.30pm and 7pm. You can buy the ticket from a Kiosk at the airport or [buy online](http://www.coachcanada.com/coachcanada/index.asp?_lp.lang=en)
** Megabus from Toronto downtown: [get to the Toronto Coach Terminal](http://www.tripadvisor.ca/Travel-g155019-c116016/Toronto:Ontario:Getting.Downtown.From.Pearson.Airport.html), take a bus to Kingston, leaves in about every hour. [Online reservation](http://ca.megabus.com/default.aspx) is strongly recommended, as early as possible, because the prices are continuously increasing (starts from $1 and increased to about $40).

**Transportation on Site**

Take a cab at the Kingston airport or bus terminal to your hotel. After that everything is in walking distance.

**Lodging** 

Be aware there is a Queen's event during the week of the hackfest so try to book your hotel early

- Frontenac http://www.frontenacclub.com Queens rate $143 per day (plus tax)
- The Belvedere http://www.hotelbelvedere.com is a small hotel of Colonial character, they only have 20 rooms.
- Holiday Inn Kingston Waterfront, http://www.hikingstonwaterfront.com/ about $140
- There are cheaper motels (Super-8 for $100 / night) 

**Meeting Location**

[Queen's University](https://maps.google.ca/maps?q=Queen's+Universityhl=ensll=44.225024,-76.493151sspn=0.010379,0.026157t=vhq=Queen's+Universityz=16iwloc=A), [Kinesiology building](http://www.queensu.ca/campusmap/?mapquery=kinesiology), room #107.

**Weather**

Can be still chilly in May, average temperature is about 15�C.

**Food**

Plan on having breakfast at your hotel before the meeting.  A variety of lunch options will be available, as will access to snacks and beverages during the day.  Please email the organizers if you have any allergies or dietary restrictions.

**Optional Activities in the Area**

- [Boat Cruise in Thousand Islands](http://www.ganboatline.com/LostShipsTour.asp)
- [Trip to Niagara Falls (Sat-Sun)](http://www.niagarafallstourism.com/)
- Wildlife Canoeing ([Thousand Islands](http://www.1000islandskayaking.com/), [Bon Echo](http://www.ontarioparks.com/english/bone.html), [Charleston Lake](http://www.ontarioparks.com/english/char.html), etc.)
- [Kingston Haunted Walks](http://www.hauntedwalk.com/kingstontours.php)
- Art after dark:
** http://www.downtownkingston.ca/files/13%20Art%20After%20Dark_Spring%20Featured%20Artists.pdf
** http://www.downtownkingston.ca/files/13%20Art%20After%20Dark_Spring%20Gallery%20Map.pdf
- Canadian Souvenirs: [Red Maple](https://maps.google.ca/maps?ie=UTF-8q=red+maple+kingstonfb=1gl=cahq=red+maplehnear=0x4cd2ab0674408ea9:0x76a5497715d6d9ea,Kingston,+ONcid=0,0,6137054689914097153ei=ZkOeUbWiI8PWygGD0YG4Cgved=0CIEBEPwSMAA), some stuff they sell: http://shop.red-maple.ca/