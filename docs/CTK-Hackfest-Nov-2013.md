---
title: CTK-Hackfest-Nov-2013
render_with_liquid: false
---

1. Event pictures
Images from the hackfest
gallery widths=300 px heights=200px perrow=3
File:20131107_192029.jpg|bigHacking/big
File:Bentham.png|big[Honorary CTK Hacker](Honorary CTK Hacker)(http://en.wikipedia.org/wiki/Jeremy_Bentham#Death_and_the_Auto-Icon)/big
/gallery

!--
Social programs

gallery widths=150 px heights=100px perrow=4
/gallery
--

    1. Progress
gallery widths=400px heights=300px perrow=2
File:Screen Shot 2013-11-07 at 1.24.00 PM.png|DICOM Table Interface integrated in 3D Slicer's nightly build [(Documentation)]((Documentation))(http://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/DICOM)
File:DICOM Header Browser.png|DICOM Header Browser
File:ctkDicomWidgetsInMITK.png|New ctkDicomTableWidgets in the MITK Dicom Editor
File:GIMIAS_CTK_WORKFLOW.png|Taverna Workflow with GIMIAS Command Line Plugins and CTK Command Line Modules, see more [here](here)(http://www.commontk.org/index.php/Documentation/CLI_In_Context#Second_Interoperability_tests).
/gallery

  1. Introduction
**Date:** Nov 4-8, 2013

**Location:**

Room 1.19 (Monday, Friday) and Room 2.14 (other days)
Malet Place Engineering Building, University College London.

[to get here.](to get here.)(How)(#location.md)

**Goal:** A follow on to the [successful previous hackfests!](successful previous hackfests!)(wildly)(Commontk:Current_events#Past_events.md)

**Requirements:** Attendees must be willing to spend their time during the event writing ctk code that contributes to the main [ ctk roadmap]( ctk roadmap)(CTK-Roadmap .md).  This means spending the week immersed in C++, Qt, DCMTK, CMake, and related technologies.  People who do not feel qualified for this task are politely not invited :)

**Group size:** Maximum 20 participants so we can have a manageable working meeting.  The organizing committee will invite and select participants based on input from [TheTeam](TheTeam)(TheTeam.md).

**Site Hosts:** Matt Clarkson (m.clarkson@ucl.ac.uk), Miklos Espak (m.espak@ucl.ac.uk)

**Organizing Committee:** (need to ask people)

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
|Matt Clarkson
|University College London, UK.
|-
|Miklos Espak
|University College London, UK.
|-
|Nicolas Toussaint
|University College London, UK.
|-
|Marco Nolden
|German Cancer Research Center, Heidelberg, Germany.
|-
|Sascha Zelzer
|German Cancer Research Center, Heidelberg, Germany.
|-
|Andreas Fetzer
|German Cancer Research Center, Heidelberg, Germany.
|-
|Steve Pieper
|Isomics, Inc. Cambridge, USA.
|-
|Florian Vichot
|INRIA, Sophia-Antipolis, France
|-
|Ivo Wolf
|Mannheim University of Applied Sciences, Germany
|-
| Ernesto Coto
| University of Sheffield, UK.
|-
|}

{|class="wikitable alternance" style="text-align:left; border:1px solid black;"
|+ ***Google Hangout Participants***
|-
! scope=col style="background:#cde6f8;"| Name
! scope=col style="background:#cde6f8;"| Organization
! scope=col style="background:#cde6f8;"| Availablity (London time)
|-
|Jean-Christophe Fillion-Robin
|Kitware Inc, North Carolina, USA
| 1pm to 6pm  
|-
|Michael Onken (planned)
|OFFIS, Germany.
| as needed. Skype: "michaeloffis"
|-
|Csaba Pinter
|Queen's University, Kingston, ON
| TBD
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
- To be announced

  1. Topics and Projects
    1. XNAT Library
Interested people: Miklos, Nicolas, Florian, Ivo, Sascha

- Stabilize API and make it more robust
- Merge to master

Open topics

- Error handling (Miklos)
- Timeout handling (Miklos)
- Unit tests for ctkXnatCore
- Zip support (Sascha)
- Up/Download support in the API (Sascha / Miklos)
- SSL support (ask about disabling SSL) (Florian?)
- Support browsing files attached to assessments
- General API review (Sascha, Miklos, Ivo, Florian)
- Add API documentation

    1. CLI Library
Florian, Sascha, Ernesto, Steve, Marco

Open Topics

- Add a CTK "test" for validating the XML of external CLIs
** Maybe a "web service" for quickly validating the XML files
- CTK should become the official CTK schema hosting site
- Default values for some elements are problematic (e.g. for SpinBox)
** Have a best practices document how to handle optional default values
- CLIs depending on external dependencies (shared libraries) are problematic
** Probably nothing we can solve inside CTK
- The UiLoader should be more customizable (JC did that in a branch for the Slicer integration)
- Maybe have a way to check for long running modules during the XML retrieval and cancel them (more of a developer thing)
- Add a method for clearing the XML cache (probably in ctkCmdLineModuleManager)
- Having a new web services front-end could be interesting
 
Discussion

- Make GIMIAS CLI modules work with the ctkCmdLineModuleExplorer (Ernesto)

    1. DICOM Application Hosting
Ivo, Sascha

    1. DICOM Libraries
Andreas, Steve

- Improve and finish the widgets
- DICOM Database backend (Marco, Steve)

    1. CTK packaging
Marco, Sascha

- continue [ Debian packaging support]( Debian packaging support)(Debian_Packaging .md)

    1. General Discussion
- Create support for CLI Web Services in CTK?
- Could we make CLI modules run in Osirix?

  1. Agenda
      1. Monday
Opening discussion
- Review topics and projects
- Plans for the week
- Review [open issues on github](open issues on github)(https://github.com/commontk/CTK/issues?state=open).

Evening:

      1. Tuesday
During the day: hack, hack, hack...

15:00 Google Hangout with US and other participants

- Talk about DCMTK_DIR ([Issue 382](Issue 382)(https://github.com/commontk/CTK/issues/382))
** Michael: Would integrate the DCMTKConfig.cmake file but needs more time to check the changes and make sure it works for everyone
** Jc: NO_DEFAULT_PATH in FindDCMTK.cmake would work for Slicer, CTK, etc. but in the future (when all distributions contain a DCMTK package with a DCMTKConfig.cmake) FindDCMTK.cmake should not be needed anymore
** Marco: We still need a way to find the system installed DCMTK
** Steve: We should be able to tell the scripts that it should find a specific DCMTK version and not automatically prefer one version over another. E.g. there could be a system DCMTK but we would still want to use a developer DCMTK build
** Jc: Is not sure why it failed at all on Csaba's machine. Will look remotely at the concrete problem on that machine.
** Marco: NO_DEFAULT_PATH would still work for the Debian packages if we pass DCMTK_DIR=/usr
** Steve: Mentions that find_program was gone from FindDCMTK.cmake leading to test failures. It is probably okay to add the find_program paths to the CMakeLists.txt file of the CTK tests.
** Jc: The DCMTK fixes are in the commontk DCMTK fork
** Marco: We should not depend on the commontk DCMTK fork since it makes compatibility with official snapshots difficult
** Jc: We should set-up a dashboard for DCMTK builds on cdash.org
- Discuss CTK install and Debian package support
** Marco: Let's have a separate hangout for that
- Failing tests on Steves machine (and others like Ivos)
** Steve: ctkCrosshairTest2 is failing on all platforms.
** Jc: It is not used anymore in Slicer
** Steve: We could remove the class and the test if nobody is using it
** General agreement
- Dashboard
** Jc suggests to move back to a traditional dashboard style (no splitting by library)
** Everyone agrees

Evening:

      1. Wednesday
10:00 Roadmap discussion

- Matt: Right now we have Widgets, DICOM, etc. is that still how we see CTK?
- Steve:
** Generally we factor out common stuff. Mainly project driven requirements
** Adding JavaScript widgets for image processing (on top of e.g. jQuery) would be nice
- Marco:
** Currently we are focusing on data management aspects (XNAT, DICOM RT, CLIs, etc.)
** Image guided therapy applications are driving the requirements for us
** New data structures for imaging are hard to agree on
- Marco:
** How CTK is presented to the outside is important
** CTK could provide standardized approaches to develop e.g. CLIs
- Florian:
** Students ask what they could CTK use for - has to tell them that it is rather for application/platform developers
- Matt:
** Pushing the XNAT work is important for us
** Also interested in mor DICOM data structure support
** Wrapping algorithms inside a proper DICOM workflow would be interesting
** What about Application Hosting?
- Steve:
** Its not directly in the QIICR proposal
- Sascha:
** We are still not ready for a production grade implementation
** Same goes for probably any other implementation
- Steve:
** Syngo Via does not seem to see a role for application hosting (they have a kind of distributed client server architecture)
** Doesn't fit with running applications locally on the workstation supporting application hosting
- Marco:
** Physicians are not really happy with proprietary solutions so there is some pressure for a more open system
** There is an IHE profile which contains application hosting, so there is also some interest
- Matt:
** We are working on XNAT support which also supports pipelines. But there is also Nipype, the GIMIAS Taverna approach, etc.
** Having XNAT in CTK is nice since people converge somehow to using the same type of database
- Marco:
** What is QIICR using as a data backend?
** Having a more light-weight, easily installable and searchable PACS would be nice
- Steve:
** The plan is to use TCIA
** It is unclear which backend technology is used for it

Conclusion:

- We are pretty much happy as it is
- A light-weight database solution would be really nice to have
- Same goes for a pipeline system


During the day: hack, hack, hack...

Evening:

      1. Thursday
During the day: hack, hack, hack...

Evening: 

      1. Friday
During the day: hack, hack, hack...

10:00; Closing discussion

Afternoon: hack or travel

  1. Travel  Hotel
**Local contact**

Need any help in organizing your visit, contact Miklos Espak (m.espak@ucl.ac.uk).
If you have any troubles during your visit, call +44 792 6656 927.

**Transportation**

[How to get to the UCL.](How to get to the UCL.)(http://www.ucl.ac.uk/maps/public-transport)

**Lodging** 

Hotels in central London can be expensive, this one seems reasonably priced:

- [The Tavistock Hotel](The Tavistock Hotel)(http://www.imperialhotels.co.uk/tavistock)

div id="location"**Meeting Location**/div

Malet Place Engineering Building, University College London
[http://goo.gl/maps/2encP](http://goo.gl/maps/2encP)

Monday and Friday: room 1.19
Other days: room 2.14

The reception is at the **Engineering Front Building** right at the gate, so please come there and refer to the CTK hackfest.

[UCL Bloomsbury campus map](UCL Bloomsbury campus map)(http://www.ucl.ac.uk/maps)

[UCL campus route finder](UCL campus route finder)(http://crf.casa.ucl.ac.uk/)

**Weather**

Daily temperature will be around 12-15C (53-59F), mostly dry, light rain is possible some days.

**Food**

Plan on having breakfast at your hotel before the meeting. Please email the organizers if you have any allergies or dietary restrictions. 

!--**Optional Activities in the Area**--