---
title: CTK-Hackfest-Dec-2012
---

1. Event pictures
Images from the hackfest
gallery widths=300 px heights=200px perrow=3
image:Bologna-2012-12-12 16.55.22.jpg|bigBologna as seen from Asinelli tower/big
image:CTK-Hackfest-2012-Bologna-Palazzo D Accursio.jpg|bigVisiting Bologna/big
image:Bologna-2012-12-12 17.23.11.jpg|bigJulien taking the photo of everyone else/big
image:DSC02729.JPG|bigPresenting results/big
image:DSC02730.JPG|bigExchanging ideas/big
image:DSC02727.JPG|bigHacking/big
image:DSC02726.JPG|big... and hacking/big
/gallery

  1. Introduction
**Date:** December 10-14, 2012

**Location:**  [| Hotel i Portici](http://www.iporticihotel.com/en) in Via Indipendenza , Bologna, Italy, Sala Montagnola (Room) 

**Goal:** A follow on to the [wildly successful previous hackfests!](CommontkCurrent-events.html#Past_events)

**Requirements:** Attendees must be willing to spend their time during the event writing ctk code that contributes to the main [ctk roadmap](CTK-Roadmap.html).  This means spending the week immersed in C++, Qt, DCMTK, CMake, and related technologies.  People who do not feel qualified for this task are politely not invited :)

**Group size:** Maximum 20 participants so we can have a manageable working meeting.  The organizing committee will invite and select participants based on input from [TheTeam](TheTeam.html).

**Site Hosts:** Alessandro Chiarini, Daniele Giunchi

**Organizing Committee:** Ivo Wolf, Stephen Aylward, Steve Pieper

**Future Events:** Future hackfests will be announced in advance, and we hope lots of people will be interested in participating.  The venue and activities at future hackfests will be determined based on the number of active participants in the project.   We welcome participation via the CTK email lists, the source code repository, and this website.

  1. Attendees
*So far we have received confirmation for the following people (in no particular order). 

'''WE HAVE REACHED THE MAXIMUM NUMBER OF PARTECIPANT - REGISTRATION CLOSED - 16 PARTECIPANTS
'''

Please fill in your intentions in terms of common accommodation.

{|class="wikitable alternance" style="text-align:left; border:1px solid black;"
|+ ***Participants***
|-
! scope=col style="background:#cde6f8;"| Name
! scope=col style="background:#cde6f8;"| Organization
|-
|Alessandro Chiarini
|SCS, Bologna IT
|-
|Daniele Giunchi
|SCS, Bologna IT
|-
|Alberto Losi
|SCS, Bologna IT
|-
|Steve Pieper
|Isomics, Inc., Cambridge, MA, USA
|-
| Ivo Wolf
| Mannheim University of Applied Sciences  DKFZ Heidelberg
|-
| Jean-Chistophe Fillion-Robin
| Kitware
|-
| Julien Finet
| Kitware
|-
| Andreas Fetzer
| DKFZ Heidelberg
|-
| Michael Bauer
| DKFZ Heidelberg
|-
| Marco Nolden
| DKFZ Heidelberg
|-
| Sascha Zelzer
| DKFZ Heidelberg
|-
| Florian Vichot
| INRIA
|-
| Yves Martelli
| UPF
|-
| Claire Mouton
| CREATIS
|-
| Miklos Espak
| University College London (UCL)
|-
| Luca Antiga
| Orobix
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
!--==== Roadmap development ====
*As needed, refine the [roadmap for the CTK core](CTK-Roadmap.html).--

      1. DICOM Application Hosting
- Refine, extend, [test](DICOM-Application-Hosting-Testing.html), and integrate with applications
- See also [(some still open) tasks](CTK-Hackfest-Nov-2011.html#DICOM_Application_Hosting) and [progress](Hackfest-Nice-AppHosting-Progress.html) from the last hackfest
- Goal: connect some real code via command line interface

      1. DICOM Database and Networking
- Dig into ongoing developments.  See [CtkDICOM](CtkDICOM.html) for discussion.
- See CTK DICOM support is used in Slicer 4.2
** [End-user documentation](http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.2/Modules/DICOM)
** [Slicer4 DICOM Bugs and Feature Requests](http://na-mic.org/Bug/search.php?project_id=3category=Module+DICOMsticky_issues=onsortby=last_updateddir=DESChide_status_id=90)
** SlicerRT Issues:
*** https://www.assembla.com/spaces/slicerrt/tickets/25 - display of ^ (carat character) in ctkDICOMModel
*** https://www.assembla.com/spaces/slicerrt/tickets/153 - extension import failure (slicer issue)
*** https://www.assembla.com/spaces/slicerrt/tickets/36 - non-uniform study information in RT files

      1. QAT
Quality Assurance Toolkit - how to integrate in CTK

      1. Widgets
- Discuss and refine as needed.
- [SlicerRt example dicom interfaces discussion](https://www.assembla.com/spaces/slicerrt/wiki/20120125_Slicer_DICOM_browser_meeting)

      1. Tests Framework
Try QtTesting with CTK applications

      1. Build Systems  Software process
!--* delUpdate PythonQt dependency so that CTK can build against Qt 4.8/del
** delSee [this experiment](https://github.com/pieper/PythonQt/tree/svn-mirror) to make a ctk-compatible version of the updated PythonQt - it works, but is not yet fully patched./del
** del[Some operator overloading issues in DAH](http://my.cdash.org/viewBuildError.php?buildid=362919)/del
** Updated PythonQt: [#1](https://github.com/commontk/PythonQt/pull/1), [#2](https://github.com/commontk/PythonQt/pull/2) and [#3](https://github.com/commontk/PythonQt/pull/3) `{{done}}`
** Updated CTK: [#189](https://github.com/commontk/CTK/issues/189), [#157](https://github.com/commontk/CTK/issues/157) `{{done}}`
** Updated Slicer [r20601](http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revisionrevision=20601) `{{done}}`
** Added [documentation](https://github.com/commontk/PythonQt#readme) on PythonQt.  `{{done}}`--


- Update to [latest DCMTK](http://git.dcmtk.org/web?p=dcmtk.git;a=summary)
** includes dcmrt
** need to pick a commit to standardize on
** investigate shared/static library building.  (Static instances of classes getting destructed in wrong order)
** incorporate version checking 
*** build ctk against head or snapshot version

- Prepare Debian packaging (Marco)
** Resolve outstanding issues
** Make CTK also build with latest stable DCMTK release (3.6.0)

- Evaluate Qt5 (Sascha)

- delSetup developer package/del
** See [#10](https://github.com/commontk/CTK/issues/10) and [#65](https://github.com/commontk/CTK/issues/65)
** Work in progress - See topic [65-packaging-support](https://github.com/jcfr/CTK/compare/65-packaging-support)


!-- * delTalk with Dominique (Debian packager) to understand what is missing/del See https://github.com/commontk/CTK/pull/158
** delBuild from upstream PythonQt (to be done this week)/del `{{done}}` Few patches still need to be contributed upstream. See [documentation](https://github.com/commontk/PythonQt#readme)--
** Release a version of CTK (Work on policy this week and maybe release this week).

!--* delGeneralize documentation of CMake macro so that it can be-used./del--
** Work in progress - See [cmake-doxygen-filter-reuse](https://github.com/jcfr/CTK/compare/master...cmake-doxygen-filter-reuse)

      1. Command Line Modules
- Extract CLI interface 
** Unify VPH and Slicer refactoring
- Qt SEM XML widget
- Follow on interoperability tests done in [CLI_In_Context](CLI-In-Context.html)
- Refine CLI XML standard
** Text format for description/help/acknowledgement/resources: plain text ? html ? structured text ? github markup ?
** Multiple categories per module ?
** CLI XML versioning.

  1. Agenda
      1. Monday
!--Start at 9:00am
Arrive and get settled in the morning. Discussion of plans for the week will get underway when everyone has arrived.
Review of goals and ideas--

10:30am Welcome

10:45 - 12:00 Round table: everyone presents 10-15 minutes how CTK is used in their project. And what's new in CTK (what has been added since previous hackfest)

: CTK in use:
:* MSVTK: [ECG](http://www.msvtk.org/content/electro-physiological-dataset-application), HAI, Buttons (DG/AL, JF) (10m)
:** Give your feedback: http://www.msvtk.org/content/evaluation
:* [DICOM in Slicer](http://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/DICOM) (SP) (5m)
:* [CLI in Gimias, MITK, NiftyView, Slicer](http://www.commontk.org/index.php/Documentation/CLI_In_Context) (SZ, YM, ME) (10m)
:* CTK in MITK (MN) (5m)
: What's new since last hackfest?
:* [CLI](http://www.commontk.org/index.php/Documentation/Command_Line_Interface) in CTK (SZ, YM) (15m)
:* DICOM Tag caching (SP) (5m)
:* [Widgets improvements](http://www.commontk.org/index.php/Documentation/ImageGallery) in CTK(JF, JCFR) (5m)
:** New: ctkExpandableWidget/ctkSizeGrip, ctkPathListWidget
:** Tweaks: ctkCoordinatesWidget (normalized), ctkPathLineEdit (sizeHint), ctkPanelSettings (user/revision settings),  

1:00pm Lunch

: Discuss plans/priorities for hacking

3:30pm Coffee Break

hack, hack, hack...

5:00pm Close

      1. Tuesday
!--hack, hack, hack...--
9:30am Welcome
- Review of Topics and demos
11:00am Coffee Break
- Discussion of goals for the week and breakout into working groups

- Command Line Module Working Group Topics
** Using ctk CLI infrastructure in Slicer (Jc, Sascha, Julien)
** CLI Incremental Communication (Luca, Steve)
** MAF CLI Integration (Daniele, Alberto)
** PythonQt wrapping of ctkCLI
** DAH and CLI (Ivo)
** CLI Compatibility Testing (Yves)
** CLI In MedINRIA (Florian)
- CTK Qt Testing and Quality Assurance Toolkit (Claire, Andreas, Julien, Jc)
- Transfer function interaction (Julien, Florian)
** Publish previous CTK hackfest work into VTK
** Minor interaction tweaks

1:00pm Lunch

hack, hack, hack...

5:00pm Close

hack, hack, hack...

      1. Wednesday
!--Review of progress--
9:30am Welcome

hack, hack, hack...


11:00am Coffee Break

hack, hack, hack...


1:00pm Lunch

hack, hack, hack...


5:00pm Close

      1. Thursday
!--Hack, hack, hack...--
9:30am Welcome

hack, hack, hack...


11:00am Coffee Break

hack, hack, hack...


1:00pm Lunch

hack, hack, hack...


5:00pm Close

      1. Friday
9:30am Welcome

hack, hack, hack...


11:00am Coffee Break

Wrap up discussion and presentations:
- Alberto, Allesandro (for Daniele)
**MAF2,3 migration
*** Use CTK command line module explorer as MAF3 Plugin
*** Wrap MAF2 modules as CLIs
*** Solution to the WXWidgets (MAF2) to Qt (MAF3) migration with uniform solution
** QAT running on CTK source code, working to make it more widely available
** Migrating MAF plugins to CTK plugins
- Claire
** Fixing configuration issues, to be improved by JCFR : https://github.com/commontk/CTK/issues/258
** Fixing compilation issues, merged to CTK master branch : https://github.com/commontk/CTK/issues/268
** Fixed a bug in QtTesting, merged to CTK master branch : https://github.com/commontk/CTK/issues/269
** Working with Qt Testing and QAT for CREATIS (working to migrate to Qt)
** Will report back in Lyon
- Miklos
** XNAT Plugin replacing curl with Qt network and ssl
** Working with Jc on REST API implementation generalized across MIDAS and XNAT
** With Sascha and Jc: updates to the build system to support plugins - new superrepository that has git submodules for optional plugins
- Sascha
** Superrepository and build system (see issue [#266](https://github.com/commontk/CTK/issues/266) and its corresponding [branch](https://github.com/commontk/CTK/tree/266-checkout-repositories-at-build-time))
** Looked into Qt5 (see issue [#277](https://github.com/commontk/CTK/issues/277) and the [qt5 branch](https://github.com/commontk/CTK/tree/qt5))
*** some ifdefs required for deprecated functions
- Andreas
** Putting Qt Testing into MITK
** Some issues being sorted out
- Marco
** Debian packaging
*** dcmtk 3.6.0 build compatibility (with remote help from Michael Onken)
*** Some debian specific patches in a separate branch
***vtk 5.8 compatibility
*** aim for named version release CTK within 6 months (for debian/ubuntu release)
- Michael
** Fixed selection of query results for retrieval
** Refactoring Query and Retrieve
*** New ctkDICOMOperation (superclass)
*** May rename some widgets for consistency
- Florian
** CLI modules now work in MedINRIA!
*** Interface is generated
*** command line executable can be run
*** Looking at specializations of GUI to support MedINRIA concepts
** Fixes to some Qt style / css compatibility issues
** Issue is reported to Qt, and now will be included in Qt 5.1
- Ivo
** DICOM Application Hosting
*** Updated dah branch to the latest master
*** Embedded dah into MITK
*** MITK as hosted application
*** ...and MITK as a host!
- Yves
** New tests for CLIs 
*** CLI finishes with error
*** CLI checks that defaults are as expected
*** CLI checks that image data passed from host is the same as when read from disk
** Code could go into Slicer Execution Model repository, for now it is there: https://github.com/ivmartel/semit
- Julien
** Lookup table editor
*** layers of lookup tables
*** Combine and edit layers independently
*** Integrates Florian's work from Boston hackfest
** Issues of ordering of XML for XML Schema comptibility
- Jc
** Build system work
** Shared library backend for CLI framework
** Updated XSD / XSL to handle additional element
** Integrated CTK CLI module framework to Slicer
*** Still uses Slicer custom logic for execution
*** Delegates to custom widgets for specific data types (extra XSL definitions)
- Steve
** DICOM Bug fixes (with Marco)
*** Name displays
*** Encoding crashes
** Command Line Module Widget - stand alone widget configured with CLI XML
*** Test version with subclassed module reference: https://github.com/pieper/CTK/tree/cli-widget-reference-subclass
*** improved version using QtGui subclass: https://github.com/pieper/CTK/tree/cli-widget
*** [working test code for the module](https://github.com/pieper/CTK/blob/8391b2f54e18e68e6672a4d3a54da38bc9c77b79/Libs/CommandLineModules/Widgets/Testing/Cpp/ctkCmdLineModuleWidgetTest1.cpp#L86)
- Luca
** Work on refactoring GenerateCLP into a more dynamic structure to support incremental CLI 
** https://github.com/lantiga/CLIInterface


1:00pm Lunch

hack, hack, hack...

- Reminder: Update project status on wiki
** Links to branches, repositories, bug reports
** Screen captures of progress to the Gallery below
** Action photos of hacking in progress...

  1. Gallery of Results
gallery widths=300 px heights=200px perrow=3
Image:Cli-widget-prototype-2012-12-14.png|[Example widget generated from XML description.](https://github.com/pieper/CTK/blob/8391b2f54e18e68e6672a4d3a54da38bc9c77b79/Libs/CommandLineModules/Widgets/Testing/Cpp/ctkCmdLineModuleWidgetTest1.cpp#L86)
Image:VtkCompositeControlPointsStack.png|Layers in VTK charts for transfer function edition.
Image:MedInria-cli.png|Command-line module integration in medInria
Image:MITKasHostedApp-and-asHost-withCLIasHostedApp.jpg|MITK running as DICOM Application Hosting hosted application (hosted by ctkDICOMHost) as well as hosting system with CTK-CLI as hosted application
/gallery

  1. Travel  Hotel
**Local contact**
If you have any troubles during your visit, call Alessandro: +39 342 1401554 or Daniele: +39 348 7260365

**Airport** 
- [Bologna G.Marconi (BLQ)](http://www.bologna-airport.it/uk/?LN=UK)

**Transportation on Site**

Airport Shuttle from airport to Railway Station (near to meeting location) 6 euro, link: http://www.atc.bo.it/orari/aerobus-airport-railway-station-link

Taxi  from airport to Railway Station 15-20 euro

!--Google's public transit search works well in Bologna.  The site is about 5 blocks from subway stops and busses.  Parking on-site is $10-$15 per day.  Cabs are fairly convenient for most trips (perhaps $40 to/from the airport but $10-$15 for trips within town).--

**Lodging** 

There are a lot of hotel options in Bologna.

Millennium Hotel[http://www.millennhotelbologna.it/en/index.html](http://www.millennhotelbologna.it/en/index.html): close to the centre and to the central railways station. 

Star Hotel [http://www.starhotels.com/hotels/excelsior/en/home.aspx](http://www.starhotels.com/hotels/excelsior/en/home.aspx): close to the centre and in front of the central railways station. 

Mercure Hotel [http://www.accorhotels.com/it/hotel-1310-mercure-bologna-centro/index.shtml](http://www.accorhotels.com/it/hotel-1310-mercure-bologna-centro/index.shtml) (Italian link, you need to find the page on your language from the Accor portal) In front of the central railways station.

Albergo Atlantic [http://www.albergoatlantic.net/ENGLISH/index.html](http://www.albergoatlantic.net/ENGLISH/index.html) In the city centre, 10' walking time from the central railways station.

I Portici Hotel [http://www.iporticihotel.com/en/i-portici-hotel-bologna](http://www.iporticihotel.com/en/i-portici-hotel-bologna)10' walking time from the central railways station. 



**Meeting Location** 
!--* [BWH Surgical Planning Laboratory](http://www.spl.harvard.edu/pages/Directions#Getting_to_1249_Boylston_Street.) [1249 Boylston Street](http://maps.google.com/maps?q=1249+boylston+street+boston+ma+02215hl=enhnear=1249+Boylston+St,+Boston,+Massachusetts+02215gl=ust=mz=16).--
TBA We are finding a meeting venue that could be in the city centre or in the central station area. 

**Catering**

It will be provided by the meeting venue. 

**Weather**

- Probably not sunny, colder than Italian average :-), even it is quite variable, temperatures can range from 0�C to 10�C (min) and from 5�C to 20�C.