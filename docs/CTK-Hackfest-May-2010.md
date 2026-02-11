---
title: CTK-Hackfest-May-2010
render_with_liquid: false
---


1. Event pictures
{|
|align="left"|This is a working meeting - the goal is to start writing code!
|[team hacking.../big](team hacking.../big)(thumb|300px|bigCTK)(File:DSC00681.JPG.md)
|[team hacking.../big](team hacking.../big)(thumb|300px|bigCTK)(File:DSC00684.JPG.md)
|}


  1. Introduction
**Date:** May 17-21

**Location:** 
:Georgetown University, [ISIS Center](ISIS Center)(http://www.isis.georgetown.edu)
:2115 Wisconsin Ave. NW. Ste 603, Washington, DC 20007 ([Google map](Google map)(http://maps.google.com/maps?f=qsource=s_qhl=engeocode=q=2115+Wisconsin+Ave.+NW.+Ste+603,+Washington,+DC+20007sll=37.0625,-95.677068sspn=54.401733,135.263672ie=UTF8hq=hnear=2115+Wisconsin+Ave+NW+%23603,+Washington,+District+of+Columbia,+20007ll=38.917608,-77.068346spn=0.003301,0.008256z=18))
:USA

**Goal:** A follow on to the wildly successful [March 2010 pre-hackfest](March 2010 pre-hackfest)(http://www.na-mic.org/Wiki/index.php/Events:CTK-Pre-Hackfest-2010).

**Requirements:** attendees must be willing to spend their time with the details of dicom, git, cmake, c++, Qt, vtk, itk, openinventor, and related technologies.  People who do not feel qualified for this are politely not invited :)

**Group size:** maximum 20 participants so we can have a manageable working meeting.  The organizing committee will invite and select participants based on input from [TheTeam](TheTeam)(TheTeam.md).

**Organizers:** Ivo Wolf, Steve Pieper, Stephen Aylward

**Site Hosts:** Kevin Cleary and Patrick Cheng

**Attendees:** (due to limited space, please contact the organizers to attend)
1. Steve Pieper,                     Isomics, Inc., USA
1. Ivo Wolf,                         Hochschule Mannheim and DKFZ, Germany
1. Marco Nolden,                     DKFZ, Germany
1. Sascha Zelzer,                    DKFZ, Germany
1. Dan Blezek,                       Mayo Clinic, USA
1. Daniele Giunchi,                  Italy
1. Alessandro Chiarini,              Italy
1. Pedro Omedas,                     Spain
1. Xavier Planes,                    Spain
1. Patrick Cheng,                    Georgetown
1. Ziv Yaniv,                        Georgetown
1. Micheal Onken,                    OFFIS, Germany
1. Will Schroeder,                   Kitware
1. Stephen Aylward,                  Kitware
1. Julien Jomier,                    Kitware
1. Julien Finet,                     Kitware
1. Jean-Christophe Fillion-Robin,    Kitware
1. Oliver Kutter                     Siemens
1. Nicolas Rannou                    Harvard

**Future Events:** The organizing committee invited a group of developers to get the CTK project started and we've believe we've reached capacity for this event.  Future hackfests will be announced in advance and we hope lots of people will be interested in participating.  The venue and activities at future hackfests will be determined based on the number of active participants in the project.

  1. Preparation
Developers should bring a laptop with the [current CTK source code](current CTK source code)(http://github.com/pieper/CTK) downloaded and [built](built)(Build_Instructions.md).

Use the [CTK developers mailing list](CTK developers mailing list)(http://public.kitware.com/cgi-bin/mailman/listinfo/ctk-developers) to discuss build issues and topics for ongoing work.

  1. Topics and Projects
Pick up threads of discussion and activity from [Pre-Hackfest](Pre-Hackfest)(http://www.na-mic.org/Wiki/index.php/Events:CTK-Hackfest-2010)

General set of topics (attendees, please flesh this out with your own ideas!)

    1. DICOM
- Marco
- Cache/Database issues
- Application Hosting
- Unified CMake for DCMTK (Michael, JJ, Dan, Jc)

*Wednesday:
** MITK superbuild, with CTK widgets
** DCMTK CMakeFiles
** Stalled on findscu - integrating dcmtk, fetchdicom, sumatra ideas into CTK implementation

*Friday:
** Progress on ctkDICOM app (still much to do)
** MITK now uses superbuild and ctkDICOMIndexer (to be committed in the next few weeks)
** New demos of Service Class User (SCU) classes for DCMTK in CTK repository
** Need more testing data and "dummy" server that can be run during tests
** mingw build ctk for MAF to incorporate DCMTK in MAF (nightly build on mingw coming).

    1. Integration
- Marco and Ivo
- Integrating CTK into MITK and Slicer, gimias, MAF 
- Slicer's Execution Model into MITK

- Wednesday
** Started the CTK App Launcher: http://github.com/jcfr/CTK-AppLauncher
** Discussion of generalizing execution model independent of MRML, but may wait until next hackfest
- Friday
** More progress on app launcher (almost finished)  Need to think about the GPL for statically linked binary.
** discussions of unstructured grids for command line module i/o

    1. Widgets
- Julien F.
- Review of CTKWidgets and [wishlist](wishlist)(Documentation/WidgetPlans.md)
- PythonQt
- Wednesday
** progress on [function](function)(transfer)(Documentation/ctkTransferFunctionWidget.md) editor
- Friday
** New functionality in transfer function editor
** Some new widgets from DICOM
** New Qt-based command line argument parser
** Log4Qt is now in CTK

    1. Events and Communications
- Patrick
- [and Intra-process events](and Intra-process events)(Inter-)(Documentation/Events.md)
- Sascha
- EventBus as a Service
- Wednesday
** patches for ZMQ and git repository
- Friday
** CMake'ifying the latest ZMQ - into github fork of ZMQ  
***http://github.com/PatrickCheng/zeromq2
** Included in CTK (builds on multiple platforms)
** requires cmake 2.8.1
** Initial tests, more applications to come
** Sascha, Daniele and Patrick to discuss
** MAF event bus integrated with ctk Plugin event bus (to be integrated with MAF after some more discussion and testing)

    1. Plugins, Modules
- Sascha
- Plugin system: [Design Document](Design Document)(http://github.com/commontk/CTK/wiki/CTK-Plugin-Framework)
** Xavier: Writing a plugin for a vtk bulls eye plot as a service
** Xavier: Writing an LDAP expression filter for use in the service framework
** Sascha: Finishing the service registry for the plugin framework
** Daniele: Integrating the MAF Event Bus as a plugin - maybe discussion with Patrick needed
- Friday
** Plugin branch is merged with master in CTK/Libs/PluginFramework

    1. Interoperability
- Oliver
- [systems at the OpenGL level (i.e. VTK and OpenInventor)](systems at the OpenGL level (i.e. VTK and OpenInventor))(Interfacing)(Documentation/Interfacing_Via_OpenGL.md)
- Wednesday
** VTK/Inventor integration - basic demo working, but many integration issues being investigated
- Friday
** Now working to load scene graphs into VTK render windows (tested volume rendering, transparent rendering...)
** Events, resize, etc being mapped from VTK to XIP
** need to have generic input setting (need to be able to export image data into XIP volumes)

    1. Organization and Workflow
- Steve and Jean-Christophe
- Conventions for using git.  Ideas: [gitwash example](gitwash example)(https://cirl.berkeley.edu/mb312/gitwash/index.html), [dead simple example](dead simple example)(http://www.dinnermint.org/tutorial/dead-simple-git-workflow-for-agile-teams/), [vtk plans](vtk plans)(http://www.vtk.org/Wiki/VTK/Git).
- Coding styles and conventions
- Dashboard issues (setting up nightly and continuous build machines)
** Dash21 now has a nightly (documentation + coverage) and continuous dashboard
- Superbuild (Jc)
** Solve problem related to MITK/CTK
** Fix bug in FindDCMTK
- Wednesday
** Work on git documentation
** doxygen coming soon to doc.commontk.org
** superbuild/CTK support for multiple applications MITK, MAF, gimias
** Now 3 machines submitting to dashboard - JJ will do mac submission, SA and SP to do windows machines.
- Friday
** Doxygen documentation is online (being built at 7:00 am Eastern time) - perhaps it can be grouped automatically based on directory structure?
** Code coverage is reported in nightly build
** More nightly test machines to be set up (builds should enable all options for better testing)
** topic forks preferred in general over topic branches (good for experiments that you may delete).
** people should be careful not to push things to the main repository that might break other people's work (in the future we may move to pull requests and have fewer people with write access to the main repos)
** "Georgetown Breadsoda Snapshot" of CTK - 0.01 pre-alpha.
** KWStyle will be set up (Jc) - use Qt style for most classes unless explicitly derived from VTK or other package
** git workflow:
*** write a wiki page on commontk.org (or link to git hub wiki) and announce to mailing list to solicit other help.
*** fork ctk on github for topic specific work, then create and publish a branch to name your project topic - give write access to your collaborators for the topic.
*** keep rebasing your fork from CTK git (when needing features) into fork while adding new functionality
*** run tests with make Experimental - or create topic-specific mycdash dashboard and point your build submissions to that dashboard
*** when finished with new functionality:
**** do final rebase and test
**** announce to mailinglist with pointer to your forked project (URL of diffs on github)
**** push to master
**** Watch continuous and nightly builds and fix any issues that arise

- Next hackfest Sept 13 - 17 in Barcelona?  Bologna?  Sophia-Antipolis?
- Also need a 'talkers' meeting

  1. Travel  Hotel
**Travel:** 
1. For flights you can use Dulles Airport (code: **IAD**) (most international flights), National Airport (code: **DCA**) (closest), or Baltimore Airport (code: **BWI**) (alternative international airport but the furthest away)
#* DCA is about 7 miles away
#** Travel option 1: Taxi ($25)
#** Travel option 2: Metro blue line ($1.35 direction Largo Town, [see map](see map)(http://www.wmata.com/rail/maps/map.cfm)) to Rosslyn, and then take a taxi ($10)
#* IAD is about 23 miles away from the hotel
#** Travel option 1: Taxi/[Super Shuttle](Super Shuttle)(http://www.supershuttle.com/) ($50)
#** Travel option 2: [Bus 5A](Bus 5A)(http://www.wmata.com/getting_around/metro_events/5a%20Time%20Table_1.pdf) ($3-$4) to Rosslyn, then take a Taxi ($10)

**Hotel**
1. We are reserving a room block at the Georgetown Holiday Inn: http://www.higeorgetown.com/
#* Room rate Monday to Friday May 17-21 will be 169 per night: single or double
#** We need to book 10 rooms to get this rate
#** Please sign up on the Wiki if you are attending and email me your hotel needs
#* Room rate the weekend before (May 14-16) will be 149 per night: single or double
#* Taxes are 14.5% additional
1. The meetings will be next door to the hotel at our research center

**Connectivity**
1. We will provide both wired and wireless connection

