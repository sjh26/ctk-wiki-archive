---
title: CTK-Hackfest-May-2014
render_with_liquid: false
---

1. Event pictures
Images from the hackfest: 
gallery widths=300 px heights=200px perrow=3
File:20140506_174248.jpg|bigHacking on Tuesday/big
/gallery


Social programs
gallery widths=150 px heights=100px perrow=4
File:ctk2014arch.JPG|[Visiting the Gateway Arch!](Visiting the Gateway Arch!)(http://en.wikipedia.org/wiki/Gateway_Arch)
/gallery


    1. Progress
gallery widths=400px heights=300px perrow=2

/gallery

  1. Introduction
**Date:** May 5-9, 2014

**Location:**

ERL conference room, [Washington University Saint Louis](Washington University Saint Louis)(http://www.wustl.edu/), [Electronic Radiology Laboratory](Electronic Radiology Laboratory)(http://erl.wustl.edu/aboutus/location.html), 4525 Scott Avenue, 3rd floor, room 3347.

[How to get here.](How to get here.)(http://erl.wustl.edu/aboutus/location.html)

**Goal:** A follow on to the [successful previous hackfests!](successful previous hackfests!)(wildly)(Commontk:Current_events#Past_events.md)

**Requirements:** Attendees must be willing to spend their time during the event writing ctk code that contributes to the main [ ctk roadmap]( ctk roadmap)(CTK-Roadmap .md).  This means spending the week immersed in C++, Qt, DCMTK, CMake, and related technologies.  People who do not feel qualified for this task are politely not invited :)

**Group size:** Maximum 20 participants so we can have a manageable working meeting.  The organizing committee will invite and select participants based on input from [TheTeam](TheTeam)(TheTeam.md).

**Site Hosts:** Lawrence Tarbox and Dan Marcus

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
|Steve Pieper
|Isomics, Inc. Cambridge, USA. (Arrive by noon Monday, leave noon Friday)
|-
|Stephen Aylward
|Kitware, Inc. North Carolina, USA.
|-
|Jean-Christophe Fillion-Robin
|Kitware, Inc. North Carolina, USA.
|-
|-
|Marco Nolden
|German Cancer Research Center, Heidelberg, Germany
|-
|-
|Sascha Zelzer
|German Cancer Research Center, Heidelberg, Germany
|-
|-
|Andreas Fetzer
|German Cancer Research Center, Heidelberg, Germany
|-
|-
|Ivo Wolf
|Mannheim University of Applied Sciences, Germany
|-
|-
|Florian Vichot
|INRIA - Asclepios, Sophia-Antipolis, France
|-
|-
|Alireza Mehrtash
|Brigham  Women's Hospital, Boston, USA.
|-
|Nicolas Toussaint
|UCL, London.
|-
|}

{|class="wikitable alternance" style="text-align:left; border:1px solid black;"
|+ ***Google Hangout Participants***
|-
! scope=col style="background:#cde6f8;"| Name
! scope=col style="background:#cde6f8;"| Organization
! scope=col style="background:#cde6f8;"| Availablity (St. Louis time)
|-
|[Jeremy Bentham's auto-icon](Jeremy Bentham's auto-icon)(http://en.wikipedia.org/wiki/Jeremy_Bentham#Death_and_the_Auto-Icon)
|University College, London
| Anytime
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
Consider reading [Contributing_to_CTK#Integrate_your_new_feature](Contributing_to_CTK#Integrate_your_new_feature)(http://www.commontk.org/index.php/Contributing_to_CTK#Integrate_your_new_feature)

    1. DICOM
- Investigate web service approach (WG27): [DICOM Web Services](DICOM Web Services)(CTK)(CTK DICOM Web Services.md)
- JavaScript DICOM Library
** For client side anonymization (like CTP does with java applet or jnlp but without java)
** emscripten option? DCMTK(dcmdata) Dan, Kevin, Steve, Jc  {{done}} See http://dcmjs.org


    1. DCMTK
- delTouch base with Michael for CMake build system patches/del. All patches have been integrated upstream. {{done}}
- Bump version of DCMTK in CTK


    1. ctkDICOM Issues
- [Slicer Infrastructure Projects](Slicer Infrastructure Projects)(https://github.com/QIICR/ProjectIssuesAndWiki/wiki/Slicer-Infrastructure-Projects) (Alireza with Andreas and Marco)
- Fix ctkDICOMApplicationTest1 (Steve, Jc)
- ctkDICOM Query with XNAT DICOM Gateway (Andreas, Misha)


    1. XNAT
- extend qRESTAPI used in ctkXNAT interface (used by ctkXNATTreeBrowser test interface and MITK custom interface)
** Add subject, new folders, data
** Demo of current state (Misha, Rick, Sascha)
** Access assessments, reports and forms
- Launch XNAT Pipelines via the REST API
- Adding caching support to avoid redundant downloads
- Asynchronous API (ctk level)


    1. Infrastructure
- Switch to regular CDash dashboard (jc)  {{done}}
- finalize integration of Qt5
** ctk (J2 and Sascha)
** Experiment with PythonQt and Qt5:
*** See https://github.com/Orochimarufan/PythonQt as discussed [on the PythonQt list](on the PythonQt list)(http://sourceforge.net/p/pythonqt/discussion/631392/thread/5f20c176/?limit=50)
*** See https://github.com/commontk/PythonQt/tree/add-qt5-support
- Leverage TravisCI (Sascha)
- Touch base with Dominique Belhachemi regarding Debian packaging (Marco)


    1. Application Hosting (Ivo and Larry)
- RESTful APIs Planning session (Ivo, Larry, Sascha, Andreas)
- Add integration testing
- Interoperability testing 
** with XIP host(?)
** with commercial system(?)


    1. CLIs
- DICOM Wrapper Proof of Concept test prototype hack experiment (Steve)
** Became [http://github.com/pieper/SlicerChronicle](http://github.com/pieper/SlicerChronicle)
- MedInria Integration of CLIs


Reminder: when integrating branches, remember to use --log --no-ff when merging.

  1. Agenda
      1. Monday
Opening discussion
- Review topics and projects
- Plans for the week
- Review [open issues on github](open issues on github)(https://github.com/commontk/CTK/issues?state=open).

Evening:

      1. Tuesday
During the day: hack, hack, hack...

[dcmjs.org is born!](dcmjs.org is born!)(http://dcmjs.org)

Evening:

      1. Wednesday
10:00 Roadmap discussion

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
    1. Local contacts
- Lawrence Tarbox (tarboxl@mir.wustl.edu)
- Dan Marcus (dmarcus@wustl.edu)


    1. Transportation
The facility is easy to get to from the airport via the Metrorail light rail system, with stations at the airport terminals and just around the corner from our building.  We do not recommend renting a car due to parking headaches, but if one chooses to rent a car, there are parking garages available that are not terribly expensive (e.g. $6 - $8 per day, no in and out).
 

    1. Lodging
Within walking distance is the Parkway Hotel (83% thumbs up and ranked #23 out of 123 hotels in St. Louis on tripadvisor.com).  If we were to reserve a room block, the Parkway would be very convenient.  The Parkway is affiliated with the medical campus, and one can use enclosed skyways to walk to our building (though the routing is a bit confusing).  There are other good hotels in the area.  Fred Prior likes the Chase Park Plaza, even though it is more expensive than the Parkway, and a several blocks longer walk.  A nearby Drury Inn said that they would provide a shuttle if enough people stayed there.  And of course there are several downtown hotels that are only a few Metrorail stops away.


    1. Weather
[Average weather in St. Louis](Average weather in St. Louis)(http://www.weather.com/weather/wxclimatology/monthly/graph/USMO0787)

    1. Food
Plan on having breakfast at your hotel before the meeting. Please email the organizers if you have any allergies or dietary restrictions. 

Being a university and hospital campus, there are several lunch possibilities, including several cafeterias and a daily show of high end food trucks just outside our door.  And both the nearby Grove and Central West neighborhoods have several restaurant choices for any meal and at multiple budget levels.  Naturally, we could also have pizza or Chinese food or sandwiches or whatever brought in if participants are interested, and dont want to be bothered with going out.
 

    1. Optional Activities in the Area
Fred did offer to host an outing to his country club (Meadowbrook), if there is interest.  The pool would not be open until Memorial Day (May 26th), but golf, tennis, and of course excellent food would be available.  While a country club outing would not be inexpensive, it would be less expensive than many other similar, high quality outings.  Other outing options could include a Cardinals game, if they are in town, or any of the museums and gardens in the area.