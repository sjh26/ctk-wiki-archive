---
title: CTK-Hackfest-Nov-2014
---

1. Event pictures
[600px](600px)(File:Ctk.2014,11.png.md)

    1. Progress
  1. Introduction
**Date:** November 3-7, 2014

**Location:**

German Cancer Research Center, Heidelberg, Germany

More details to follow.

**Goal:** A follow on to the [successful previous hackfests!](successful previous hackfests!)(wildly)(Commontk:Current_events#Past_events.md)

**Requirements:** Attendees must be willing to spend their time during the event writing ctk code that contributes to the main [ ctk roadmap]( ctk roadmap)(CTK-Roadmap .md).  This means spending the week immersed in C++, Qt, DCMTK, CMake, and related technologies.  People who do not feel qualified for this task are politely not invited :)

**Group size:** Maximum 20 participants so we can have a manageable working meeting.  The organizing committee will invite and select participants based on input from [TheTeam](TheTeam)(TheTeam.md).

**Site Hosts:** Marco Nolden, Sascha Zelzer, Ivo Wolf

**Organizing Committee:** Steve Pieper, Ivo Wolf, Stephen Aylward

**Future Events:** Future hackfests will be announced in advance, and we hope lots of people will be interested in participating.  The venue and activities at future hackfests will be determined based on the number of active participants in the project.   We welcome participation via the CTK email lists, the source code repository, and this website.

  1. Attendees
- So far we have received confirmation for the following people (in no particular order). 


Please fill in your intentions in terms of common accommodation.

{|class="wikitable alternance" style="text-align:left; border:1px solid black;"
|+ ***Participants***
|-
! scope=col style="background:#cde6f8;"| Name
! scope=col style="background:#cde6f8;"| Organization
|-
|Marco Nolden
|German Cancer Research Center, Heidelberg, Germany
|-
|Sascha Zelzer
|German Cancer Research Center, Heidelberg, Germany
|-
|Andreas Fetzer
|German Cancer Research Center, Heidelberg, Germany
|-
|Stefan Kislinkiy
|German Cancer Research Center, Heidelberg, Germany
|-
|Ralf Floca
|German Cancer Research Center, Heidelberg, Germany
|-
|Ivo Wolf
|Mannheim University of Applied Sciences, Germany
|-
|Steve Pieper
|Isomics, Inc., USA
|-
|Michael Onken
|Open Connections GmbH / OFFIS
|-
|Jean-Christophe Fillion-Robin
|Kitware, Inc., USA
|-
|Miklos Espak
|University College London, UK
|-
|Nicolas Toussaint
|University College London, UK
|-
|Gergely Zombori
|University College London, UK
|-
|Christian Askeland
|SINTEF Medical Technology, Trondheim, Norway
|-
|Stefan Baumann
|Basel, Switzerland
|-
|Hans Meine
|Fraunhofer MEVIS, Germany
|-
|}

{|class="wikitable alternance" style="text-align:left; border:1px solid black;"
|+ ***Google Hangout Participants***
|-
! scope=col style="background:#cde6f8;"| Name
! scope=col style="background:#cde6f8;"| Organization
! scope=col style="background:#cde6f8;"| Availablity (Central European Time)
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

{{Note}}There were also other invitations sent to active people on the community, and people who recently showed interest. When their intent will be known they will be added to the list.

  1. Preparation
Developers should bring a laptop with the [current CTK source code](current CTK source code)(http://github.com/commontk/CTK) downloaded and [built](built)(Build_Instructions.md).

Use the [CTK developers mailing list](CTK developers mailing list)(http://public.kitware.com/cgi-bin/mailman/listinfo/ctk-developers) to discuss build issues and topics for ongoing work.

Phone conferences have been scheduled in the weeks leading to the event:

**https://plus.google.com/hangouts/_/g3vi3lz7sycalj74ys2xpnpr3ya**

  1. Topics and Projects
Consider reading [Contributing_to_CTK#Integrate_your_new_feature](Contributing_to_CTK#Integrate_your_new_feature)(http://www.commontk.org/index.php/Contributing_to_CTK#Integrate_your_new_feature)

Reminder: when integrating branches, remember to use --log --no-ff when merging.

We plan to have concrete hacking topics as well as dedicated discussions in smaller groups. People are encouraged to show their interest in a particular subject by adding their name to the list below.

    1. Hacking Topics
      1. Infrastructure
- Qt5 migration (Christian)
** compile and run on Mac
- Packaging / install support (Marco, Jc)
- Fix issue related to [Artichoke](Artichoke)(https://github.com/commontk/Artichoke) and improve documentation (Jc)
- Dashboard
** General Situation: Continuous/Nightly clients, coverage
** Configurations: Qt4, Qt5, etc.
** Travis CI (Sascha, Steve)
- Incomplete doxygen on the website (Christian)
- Component / target oriented build system (Jc, Sascha)
- Review commontk/* repositories (delete/update/etc.)
- Check support for MacOS 10.10

      1. DICOM
- dcmtk Features
** Support building with emscripten, pinnacle
** Multi-frame support (Steve, Christian, Michael)
** SEG support
*** Investigate compatibility of DCMTK seg functionality with BrainLab segmentations; [sample dataset](sample dataset)(http://slicer.kitware.com/midas3/item/162562) (QIICR community, Steve has access) - RLE compressed
*** Investigate DCMTK RLE compression tools applied to segmentations; trying to apply it to sample objects generates "F: No conversion to transfer syntax RLE Lossless possible!" error; [SPL segmentation dataset example](SPL segmentation dataset example)(http://slicer.kitware.com/midas3/item/162428), [PET segmentation example](PET segmentation example)(http://slicer.kitware.com/midas3/item/161740)

- Making CLIs read and write valid DICOM (Steve, Michael)

- Anonymization (Andreas Fetzer, Marco, Steve, Stefan, Ralf)
** Client-side options: gdcmanon, dcmtk (?), dcmjs, DicomCleaner, CTP...
** Testing can use [ this freely sharable identified MR scan]( this freely sharable identified MR scan)(File:PieperMRI.tar.gz .md)
** Goal is to de-identify with various tools and compare results with [supplement 142 of the DICOM standard](supplement 142 of the DICOM standard)(ftp://medical.nema.org/medical/dicom/Final/sup142_ft.pdf).
** There is a separate page, which provides an overview of existing de-identification tools: [de-identification tool overview](de-identification tool overview)(DICOM)(DICOM de-identification tool overview.md)

- ctkDICOM improvments (Ralf); discussed ideas:
** Introduce "compact and detailed view mode" to ctkDICOMTableView and ctkDICOMTableManager. Basic idea is that you can give the widgets a list of "high priority" tags - in compact mode all columns of non priority tags will be filter. You can define the active mode via property / slot (to e.g. easily connect it with a control widget signal).
** Refactoring of one unified "search definition widget" and separated generators for "dicom q/r" and sql statement that use the search definition. This would give the possibility for instance to use the same search widget in different places (e.g. in the ctkDICOMQueryRetrieveWidget or ctkDICOMTableManager)

      1. XNAT
- Improve and extend the XNAT API (Sascha Zelzer, Miklos Espak, Ralf)
** Python Wrapping (Sascha, Nicolas)
** Data editing (post-poned)
** Uploading (Andreas, Ivo)
** Caching (Miklos, (Ralf))
** C++ VS XNAT data model (Nicolas, Andreas)
** Filtered data query based on data type and/or properties (Miklos)
** Launch pipelines (remote) and follow progress (Miklos)

      1. CLI
- Make it customisable what options to generate to the final command (Gergely Zombori)
- Finalize integration of CTK CLI frontend into Slicer and investigate how to integrate the backend (Jc)
- Improved entry point / documentation for CLI users  developers

      1. Documentation  Presentation
- Nice landing page?
- Improve wiki? Something different?

  1. Agenda
      1. Monday
Start: The meeting room will be open starting at 9am. Official start and kick-off will be early afternoon after everybody arrived.

Opening discussion
- Review topics and projects
- Plans for the week
- Review [open issues on github](open issues on github)(https://github.com/commontk/CTK/issues?state=open).

Afternoon:
- Welcome by Prof. Hans-Peter Meinzer
- Presentation about [Common Toolkit Jubilee](Common Toolkit Jubilee)(The)(Media:The_Common_Toolkit_Jubilee.pptx.md)

Evening:

- Dinner 20:15 @ [Kulturbrauerei](Kulturbrauerei)(http://www.heidelberger-kulturbrauerei.de/en/), [directions](directions)(https://www.google.de/maps/dir/Hotel+Holl%C3%A4nder+Hof,+Neckarstaden+66,+69117+Heidelberg/Kulturbrauerei+Heidelberg,+Leyergasse+6,+69117+Heidelberg/@49.413196,8.7102803,18z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x4797c10638e496a5:0xe28b6a91325a2c23!2m2!1d8.709242!2d49.413192!1m5!1m1!1s0x4797c1a81df9996d:0xb0cec22d395e79e1!2m2!1d8.713414!2d49.41318!3e2), Pickup ~20:00 at Holl�nder Hof

      1. Tuesday
Morning:

- Steve QIICR
- Michael Onken presentation about upcoming dcmtk modules
- XNAT discussion


Afternoon:
 
- 13:30 [Tour](Tour)(Lab)(CTK-Hackfest-Nov-2014/LabTour.md)

Evening:

- 16:00 Famous Old City tour guided by Hans-Peter Meinzer

- 20:00 Beer Topics
** Defacing

      1. Wednesday
Morning

During the day: hack, hack, hack...

      1. Thursday
Morning:

- IGT  OpenIGTLink discussion

During the day: hack, hack, hack

Short wrap-up:

Christian:
- Fixed Qt5 DICOM  Plugin Framework issues
- Doxygen fixes
- Started integrating CTK DICOM Widget improvements

JC:
- dcmjs: Update to use latest version of emscripten
- dcmjs: create dcmjs.org github project and add deploy mechanism
- dcmjs: Improve user experience of http://dcmjs.org website
- Re-started Slicer CTK CLI integration
- Discussed extension of CLI schema to support optional parameter.
- Improved CTK PythonQt wrapping to support import from regular python shell. See [commontk/CTK#520](commontk/CTK#520)(https://github.com/commontk/CTK/pull/520)

Hans:
- Many discussion topics (Chronicle, CLI)
- CLI documentation overview (CTK Wiki)
- Investigated elasticsearch database for CLI modules
- OpenInventor - VTK integration

Stefan:
- Added [ mapping/de-identification]( mapping/de-identification)(Media:Testmr.txt .md) functionality to dcmjs (minimal feature set like CTP)

Steve:
- dcmjs organize tool
** exploring boundaries (extracting data etc.)
** anonymization
- DICOM segmentation object discussions
** How to support CLIs?

Michael:
- Compiled CTK with new dcmtk snapshot (worked)
- Worked on dcmseg module

Marco:
- Discussions about QIICR
- Closed a couple of GitHub issues

Ivo:
- Discussions about QIICR, XNAT
- Compiling MRML outside of Slicer

Andreas:
- XNAT upload (qRestAPI changes)
- DICOM discussions (widget usability, anonymization tools)

Nicolas:
- Wrapped XNAT library into Python (for usage in NiPype)
- Usage outside of a QApplication needs investigation

Gergely:
- Added possibility for optional CLI parameter

Miklos:
- Started XNAT query API
- Hit API limits - focus on caching objects
- Needs more discussion

Sascha:
- Qt5 fixes
- Travis integration


Evening:

      1. Friday
During the day: hack, hack, hack...

11:00: Closing discussion
- CLI Elasticsearch (Hans)
** Search for keywords and get matching CLIs
** Use it to browse CLI descriptions and clean-up contents
** [commontk/cli-indexer](commontk/cli-indexer)(https://github.com/commontk/cli-indexer) repository. Creates JSON descriptions from CLI XML.
** Every institution could publish the JSON description of their CLIs and publish it
** There is a pypi package for cli-indexer

Afternoon: hack or travel

  1. Travel  Hotel
    1. Local contacts
- Marco Nolden (m.nolden@dkfz-heidelberg.de)
- Sascha Zelzer (s.zelzer@dkfz-heidelberg.de) [130px](130px)(File:Sascha_phone.png.md)
- Andreas Fetzer (a.fetzer@dkfz-heidelberg.de)

    1. Transportation
It takes about an hour from Frankfurt Airport (FRA) to Heidelberg Main Station with one change in Mannheim. If you stay in the Old Town you can also look for connections going to "Heidelberg Altstadt". You can look it up at [Deutsche Bahn](Deutsche Bahn)(http://www.bahn.de/p_en/view/index.shtml), but they run quite frequently.

**Local:** from the Old Town, "Universit�tsplatz", runs [bus number 32](bus number 32)(http://www.vrn.de/mam/vrn/einfach-ankommen/dokumente/stadtlinienplaene/heidelberg_schematisch.pdf) ([geographic map](geographic map)(http://www.vrn.de/mam/vrn/einfach-ankommen/dokumente/stadtlinienplaene/heidelberg.pdf)) via Main Station to DKFZ, exit at "Chirurgische Klinik", bus direction is "Neuenheim". After you exit, DKFZ is on your right.

[700px](700px)(File:Heidelberg_map.png.md)

During the day the bus runs every 10 minutes in both directions, timetables are also available at [VRN](VRN)(http://fahrplanauskunft.vrn.de/vrn/XSLT_TRIP_REQUEST2?language=en).

      1. To Frankfurt Airport
The German Railways is affected by a strike from Thursday to Monday morning. Trains will operate on a limited basis - check the website of [Deutsch Bahn](Deutsch Bahn)(http://www.bahn.de).

You may also use a [Shuttle Bus](Shuttle Bus)(http://www.transcontinental-group.com/en/airport-shuttle-buchen) departing from the Crown Plaza in Heidelberg. It is recommended to book online as early as possible.

    1. Lodging
We recommend to stay in the historic Old Town. There is an easy direct bus ride every 10 minutes from there to DKFZ.

We have reserved a number of rooms at the [Holl�nder Hof](Holl�nder Hof)(http://www.hollaender-hof.de/en/) ([map](map)(http://www.openstreetmap.org/?mlat=49.41317mlon=8.70925#map=19/49.41317/8.70925)) hotel! Please use "CTK 2014" when you do a reservation there. Of course there are plenty of other hotels in that area, e.g. [Goldener Hecht](Goldener Hecht)(http://www.hotel-goldener-hecht.de/) or the oldest house in town, [Hotel zum Ritter](Hotel zum Ritter)(http://www.ritter-heidelberg.de/).

    1. Meeting Room
The full address for the DKFZ is

 Deutsches Krebsforschungszentrum
 Im Neuenheimer Feld 280
 69120 Heidelberg

We will meet in the main building on the second floor (European counting!). The cryptic room number is D0.02.032. Follow the description below to find it.

When leaving bus 32, you will see something similar to

[600px](600px)(File:DKFZ_Bus.jpg.md)

The large building on the right is the DKFZ main bulding

[600px](600px)(File:DKFZ_Hauptgebaeude_neu_600x402.jpg.md)

Walk through the main entrance and follow the map

[600px](600px)(File:DKFZ_Hackfest_map.jpg.md)

Ask the nice guys at the reception or call us in case of any problems.

    1. Weather
November is a rather wet month. [Average weather in Heidelberg](Average weather in Heidelberg)(http://www.weather-and-climate.com/average-monthly-Rainfall-Temperature-Sunshine,heidelberg,Germany)

    1. Food
Plan on having breakfast at your hotel before the meeting. Please email the organizers if you have any allergies or dietary restrictions. 

Being a university and hospital campus, there are several lunch possibilities, including cafeterias, a students mensa, and two restaurants.
 

    1. Optional Activities in the Area