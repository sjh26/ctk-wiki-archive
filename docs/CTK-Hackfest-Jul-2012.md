---
title: CTK-Hackfest-Jul-2012
render_with_liquid: false
---

1. Event pictures
Images from the hackfest:
{|
|[thumb|right|220px|bigHacking/big](thumb|right|220px|bigHacking/big)(image:Ctk-boston-2012.jpg.md)
|[and Steve hacking on CTK DICOM/big](and Steve hacking on CTK DICOM/big)(thumb|right|220px|bigMarco)(image:CTK-Hackfest-2012-Boston IMGP4168.JPG.md)
|[thumb|right|220px|bigBrainstorming/big](thumb|right|220px|bigBrainstorming/big)(image:CTK-Hackfest-2012-Boston IMGP4167.JPG.md)
|[Tour/big](Tour/big)(thumb|right|220px|bigAMIGO)(image:CTK-AMIGO-IMG 20120713 135006.jpg.md)
|[dinner at after some intense hacking/big](dinner at after some intense hacking/big)(thumb|right|220px|bigGreat)(image:CTK-Hackfest-2012-Boston_IMGP4174.JPG.md)
|}

  1. Introduction
**Date:** July 9-13, 2012

**Location:** 1249 Boylston  Street - Brigham and Women's Hospital, Boston, Massachusetts USA

**Goal:** A follow on to the [successful previous hackfests!](successful previous hackfests!)(wildly)(Commontk:Current_events#Past_events.md)

**Requirements:** Attendees must be willing to spend their time during the event writing ctk code that contributes to the main [ ctk roadmap]( ctk roadmap)(CTK-Roadmap .md).  This means spending the week immersed in C++, Qt, DCMTK, CMake, and related technologies.  People who do not feel qualified for this task are politely not invited :)

**Group size:** Maximum 20 participants so we can have a manageable working meeting.  The organizing committee will invite and select participants based on input from [TheTeam](TheTeam)(TheTeam.md).

**Site Hosts:** Steve Pieper and Ron Kikinis

**Organizing Committee:** Ivo Wolf, Stephen Aylward, Steve Pieper

**Future Events:** Future hackfests will be announced in advance, and we hope lots of people will be interested in participating.  The venue and activities at future hackfests will be determined based on the number of active participants in the project.   We welcome participation via the CTK email lists, the source code repository, and this website.

  1. Attendees
*So far we have received confirmation for the following people (in no particular order). Please fill in your intentions in terms of common accommodation.

{|class="wikitable alternance" style="text-align:left; border:1px solid black;"
|+ ***Participants***
|-
! scope=col style="background:#cde6f8;"| Name
! scope=col style="background:#cde6f8;"| Organization
|-
| Jean-Chistophe Fillion-Robin #5
| Kitware
|-
| Julien Finet #7
| Kitware
|-
| Stephen Aylward (in spirit)
| Kitware
|-
| Steve Pieper
| Isomics
|-
| Ivo Wolf #9
| Hochschule Mannheim
|-
| Marco Nolden #12
| DKFZ, Heidelberg
|-
| Sascha Zelzer #8
| DKFZ, Heidelberg
|-
| Florian Vichot #11
| INRIA
|-
| Daniele Giunchi #10
| SCS, Bologna
|-
| Andr� Aichert #13
| University Erlangen-Nuremberg
|}


!--
- People who manifested interest in joining the fest. Please move your names up to the confirmed table, with the details as soon as you can to facilitate discussions with potential hotels.

{|class="wikitable alternance" style="text-align:left; border:1px solid black;"
|+ ***Confirmed***
|-
! scope=col style="background:#cde6f8;"| Name
! scope=col style="background:#cde6f8;"| Organization
|-
|}
--

{{Note}}There were also other invitations sent to active people on the community, and people who recently showed interest. When their intent will be known they will be added to the list.

  1. Preparation
Developers should bring a laptop with the [current CTK source code](current CTK source code)(http://github.com/commontk/CTK) downloaded and [built](built)(Build_Instructions.md).

Use the [CTK developers mailing list](CTK developers mailing list)(http://public.kitware.com/cgi-bin/mailman/listinfo/ctk-developers) to discuss build issues and topics for ongoing work.

Phone conferences have been scheduled in the weeks leading to the event:
- To be announced

  1. Topics and Projects
      1. Roadmap development
*As needed, refine the [for the CTK core](for the CTK core)(roadmap)(CTK-Roadmap.md).

      1. DICOM Application Hosting
- Refine, extend, [ test]( test)(DICOM_Application_Hosting_Testing .md), and integrate with applications
- See also [ (some still open) tasks]( (some still open) tasks)(CTK-Hackfest-Nov-2011#DICOM_Application_Hosting .md) and [ progress]( progress)(Hackfest_Nice_AppHosting_Progress .md) from the last hackfest
- Goal: connect some real code via command line interface

      1. DICOM Database and Networking
- Dig into ongoing developments.  See [CtkDICOM](CtkDICOM)(CtkDICOM.md) for discussion.
** Review [patches provided by the SlicerRT team](patches provided by the SlicerRT team)(https://github.com/SlicerRt/CTK/commits/slicerRT-patches) 
** Performance Optimization (loadHeader in ctkDICOMDatabase)

- See [in Slicer4](in Slicer4)(ctkDICOM)(ctkDICOM in Slicer4.md) for information on a particular application use case.
- [Slicer4 DICOM Bugs and Feature Requests](Slicer4 DICOM Bugs and Feature Requests)(http://na-mic.org/Bug/search.php?project_id=3search=dicomcategory=DICOMstatus_id%5B%5D=10status_id%5B%5D=20status_id%5B%5D=30status_id%5B%5D=40status_id%5B%5D=50sticky_issues=offsortby=last_updateddir=DESChide_status_id=-2)

      1. Widgets
- Discuss and refine as needed.
- [SlicerRt example dicom interfaces discussion](SlicerRt example dicom interfaces discussion)(https://www.assembla.com/spaces/slicerrt/wiki/20120125_Slicer_DICOM_browser_meeting)

      1. Tests Framework
Try QtTesting with CTK applications

      1. Build Systems  Software process
- delUpdate PythonQt dependency so that CTK can build against Qt 4.8/del
** delSee [this experiment](this experiment)(https://github.com/pieper/PythonQt/tree/svn-mirror) to make a ctk-compatible version of the updated PythonQt - it works, but is not yet fully patched./del
** del[Some operator overloading issues in DAH](Some operator overloading issues in DAH)(http://my.cdash.org/viewBuildError.php?buildid=362919)/del
** Updated PythonQt: [#1](#1)(https://github.com/commontk/PythonQt/pull/1), [#2](#2)(https://github.com/commontk/PythonQt/pull/2) and [#3](#3)(https://github.com/commontk/PythonQt/pull/3) {{done}}
** Updated CTK: [#189](#189)(https://github.com/commontk/CTK/issues/189), [#157](#157)(https://github.com/commontk/CTK/issues/157) {{done}}
** Updated Slicer [r20601](r20601)(http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revisionrevision=20601) {{done}}
** Added [documentation](documentation)(https://github.com/commontk/PythonQt#readme) on PythonQt.  {{done}}


- Update to [latest DCMTK](latest DCMTK)(http://git.dcmtk.org/web?p=dcmtk.git;a=summary)
** includes dcmrt
** need to pick a commit to standardize on
** investigate shared/static library building.  (Static instances of classes getting destructed in wrong order)
** incorporate version checking 
*** build ctk against head or snapshot version


- delSetup developer package/del
** See [#10](#10)(https://github.com/commontk/CTK/issues/10) and [#65](#65)(https://github.com/commontk/CTK/issues/65)
** Work in progress - See topic [65-packaging-support](65-packaging-support)(https://github.com/jcfr/CTK/compare/65-packaging-support)


- delTalk with Dominique (Debian packager) to understand what is missing/del See https://github.com/commontk/CTK/pull/158
** delBuild from upstream PythonQt (to be done this week)/del {{done}} Few patches still need to be contributed upstream. See [documentation](documentation)(https://github.com/commontk/PythonQt#readme)
** Release a version of CTK (Work on policy this week and maybe release this week).

- delGeneralize documentation of CMake macro so that it can be-used./del
** Work in progress - See [cmake-doxygen-filter-reuse](cmake-doxygen-filter-reuse)(https://github.com/jcfr/CTK/compare/master...cmake-doxygen-filter-reuse)

      1. Command Line Modules
- Extract CLI interface 
** Unify VPH and Slicer refactoring
- Qt SEM XML widget

[Line Module Work Items](Line Module Work Items)(Cmd)(Boston Hackfest:Cmd Line Module Work Items.md)

  1. Agenda
      1. Monday
Start at 9:00am
Arrive and get settled in the morning.  Discussion of plans for the week will get underway when everyone has arrived.

Review of goals and ideas
      1. Tuesday
hack, hack, hack...
      1. Wednesday
Review of progress
      1. Thursday
Hack, hack, hack...

      1. Friday
- 10:30 Review hacking progress
*Tour of [AMIGO](AMIGO)(http://ncigt.org/pages/AMIGO).
** Leave 1249 by 12:00.  Stop for lunch on the way and meet Isaiah at AMIGO at 2:00.
** Turn in badges - do not plan to return to 1249.
End by 5:00pm

  1. Travel  Hotel
**Local contact**
- If you have any troubles during your visit, call Steve: +1 617 596 2719

**Airport** 
- [Boston Logan (BOS)](Boston Logan (BOS))(http://www.massport.com/logan-airport/Pages/Default.aspx)

**Transportation on Site**

Google's public transit search works well in Boston.  The site is about 5 blocks from subway stops and busses.  Parking on-site is $10-$15 per day.  Cabs are fairly convenient for most trips (perhaps $40 to/from the airport but $10-$15 for trips within town).

**Lodging** 

There are a lot of hotel options in Boston - several within easy walking distance of the 1249 Boylston facility and everything is accessible by public transport.  Note that on Sunday night before the hackfest there is a big baseball game in the neighborhood (at Fenway Park) so hotels may be more expensive the first night, but should be cheaper the rest of the week.

- Closest, cheapest, but least nice:  

Howard Johnsons
1271 Boylston Street
Boston, MA 02215
(800) 446-4656
howardjohnsonboston.com

- Not too far - mid price:

Boston Hotel Buckminster
645 Beacon Street
Boston, MA 02215
(800) 727-2825
bostonhotelbuckminster.com

- Not too far - higher price:

Hotel Commonwealth
500 Commonwealth Avenue
Boston, MA 02215
(617) 933-5000
hotelcommonwealth.com


**Meeting Location** 
- [BWH Surgical Planning Laboratory](BWH Surgical Planning Laboratory)(http://www.spl.harvard.edu/pages/Directions#Getting_to_1249_Boylston_Street.) [1249 Boylston Street](1249 Boylston Street)(http://maps.google.com/maps?q=1249+boylston+street+boston+ma+02215hl=enhnear=1249+Boylston+St,+Boston,+Massachusetts+02215gl=ust=mz=16).

**Catering**

- To be determined.

**Weather**

- Probably pretty hot and humid...