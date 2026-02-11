---
title: CTK-Hackfest-Nov-2011
render_with_liquid: false
---

1. Event pictures
{|
|[is hard work!/big](is hard work!/big)(thumb|right|250px|bigHacking)(image:2011-11-Hackfest-photo.JPG.md)
|[out the demos/big](out the demos/big)(thumb|right|250px|bigChecking)(image:2011-11-Hackfest-photo-demos.JPG.md)
|[nice progress in Nice/big](nice progress in Nice/big)(thumb|right|250px|bigPretty)(image:2011-11-Hackfest-photo-demos2.JPG.md)
|}

  1. Introduction
**Note: this page is a work in progress -- some information subject to change**

**Date:** November 14-18, 2011

**Location:** INRIA - Sophia Antipolis, France

**Goal:** A follow on to the [successful previous hackfests!](successful previous hackfests!)(wildly)(Commontk:Current_events#Past_events.md)

**Requirements:** Attendees must be willing to spend their time during the event with writing ctk code that contributes to the main ctk roadmap.  People who do not feel qualified for this are politely not invited :)

**Group size:** Maximum 20 participants so we can have a manageable working meeting.  The organizing committee will invite and select participants based on input from [TheTeam](TheTeam)(TheTeam.md).

**Site Hosts:** Beno�t Bleuz�

**Future Events:** Future hackfests will be announced in advance, and we hope lots of people will be interested in participating.  The venue and activities at future hackfests will be determined based on the number of active participants in the project.   We welcome participation via the CTK email lists, the source code repository, and this website.

  1. Attendees
*So far we have received confirmation for the following people (in no particular order). Please fill in your intentions in terms of common accommodation.

{|class="wikitable alternance" style="text-align:left; border:1px solid black;"
|+ ***Participants***
|-
! scope=col style="background:#cde6f8;"| Name
! scope=col style="background:#cde6f8;"| Organization
! scope=col style="background:#cde6f8;"| Interested in grouped accommodation
|-
| Jean-Chistophe Fillion-Robin
| Kitware
| {{True}}
|-
| Julien Finet
| Kitware
| {{True}}
|-
| Steve Pieper
| Isomics
| {{True}}
|-
| Ivo Wolf
| Hochschule Mannheim
| {{True}}
|-
| Marco Nolden
| DKFZ, Heidelberg
| {{True}}
|-
| Sascha Zelzer
| DKFZ, Heidelberg
| {{True}}
|-
| Beno�t Bleuz�
| INRIA, Sophia-Antipolis
| {{False}}
|-
| Matt Clarkson
| University College London
| {{True}}
|-
| Daniele Giunchi
| SCS, Bologna
| {{True}}
|-
| Roberto Mucci
| SCS, Bologna
| {{True}} 
|-
| Martin Stegh�fer
| UPF, Barcelona
| {{True}}
|-
| Yves Martelli
| UPF, Barcelona
| {{True}} 
|-
| Anthony Dass
| Siemens Corporate Research, Princeton
| {{True}}
|-
| Michael Onken
| OFFIS, Oldenburg
| {{False}}
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
- Tuesday 25th October 2011 18:00 (CET) - 12:00 (EST)
- Tuesday 8th November 2011 18:00 (CET) - 12:00 (EST)

  1. Topics and Projects
      1. Roadmap development
*Develop a [for the CTK core](for the CTK core)(roadmap)(CTK-Roadmap.md). It is advised to begin pondering on this in the weeks leading to the hack-fest in order to dedicate as much time as possible to the real hacking during the week. The [for the CTK core](for the CTK core)(roadmap)(CTK-Roadmap.md) is a good place to start your thinking. It has been written by Ivo and Marco at the start of the CTK initiative.

Participants
*Steve
*Stephen
*Ivo
*Marco
*Ben
*Sascha

      1. DICOM Application Hosting
Possible work items:

- Data Exchange Interface (finish file-based data exchange, XPath Queries) (?)
** Research XPath libraries (Qt?)(Ben)
- Error handling
** throw execptions after a configurable timeout (Sascha)
- [ Conformance testing]( Conformance testing)(DICOM_Application_Hosting_Testing .md) (for both host and app)
** Interface (WSDL) compliance
** State transition tests
- Demo Application (Ivo, Anthony)
- Improve ease of use for host and app developers
** Extend ctkAbstractHost and ctkAbstractApp (Sascha)
** What about multiple apps running at once?
- Documentation (Daniele, Roberto)

Participants

- Benoit
- Michael
- Sascha
- Jc
- Ivo
- Anthony
- Daniele
- Roberto

Look at the [ progress]( progress)(Hackfest_Nice_AppHosting_Progress .md) made at the hackfest.

      1. DICOM Networking
Possible work items:

See [CtkDICOM](CtkDICOM)(CtkDICOM.md) for possible goals.

- See [in Slicer4](in Slicer4)(ctkDICOM)(ctkDICOM in Slicer4.md) for information on a particular application use case.

Participants

- Michael
- Steve
- Marco

      1. Widgets
      1. Tests Framework
Working towards a unified testing method throughout the whole code base.
- Julien (also linked but not limited to App hosting testing)
- Daniele
- Roberto

      1. Build Systems  Software process
Possible work items

- Clean up the code base so everything compiles
- "make install" support for CTK applications
- "make install" support for a CTK SDK (binaries + header files)
- Make CTK compatible with upstream 3rd party toolkits (i.e. DCMTK, VTK, Log4Qt, etc.)

Resolve github issues


{|class="wikitable alternance" style="text-align:left; border:1px solid black;"
|+ ***Issues***
|-
! scope=col style="background:#cde6f8;"| Issue
! scope=col style="background:#cde6f8;"| Who
! scope=col style="background:#cde6f8;"| Status
! scope=col style="background:#cde6f8;"| Remarks
|-
| [install target](install target)(https://github.com/commontk/CTK/issues/10)
|
| {{Not_Done}}
|
|-
| [ExternalProject to use CMAKE_CACHE_ARGS](ExternalProject to use CMAKE_CACHE_ARGS)(https://github.com/commontk/CTK/issues/13)
| Jc
| {{Done}}
| See https://github.com/commontk/CTK/commit/388a43f635ea40f49b36a3aa1695e750854d2cd3
|-
| [Error improperly reported on CDash](Error improperly reported on CDash)(https://github.com/commontk/CTK/issues/23)
|
| {{Not_Done}}
|
|-
| [CTK windows configuration error (DGraph-related)](CTK windows configuration error (DGraph-related))(https://github.com/commontk/CTK/issues/26)
| Matt
| {{Done}}
|
|-
| [Failing tests in ctkCore](Failing tests in ctkCore)(https://github.com/commontk/CTK/issues/27)
| Jc
| {{Doing}}
| See [https://github.com/commontk/CTK/commit/3b06461b8ffabc7c5763cac747c1a5104f4340c8](https://github.com/commontk/CTK/commit/3b06461b8ffabc7c5763cac747c1a5104f4340c8)
|-
| [Minimize confusion associated with buildsystem](Minimize confusion associated with buildsystem)(https://github.com/commontk/CTK/issues/30)
|
| {{Not_Done}}
| 
|}


Participants

- Jc
- Sascha

  1. Agenda
**Monday 14th**: 9:30-18:00
- Presentations 9:30 12:45:
** each institution will present in 15 minutes + 5 minutes of questions how they use CTK, or what do they expect from it.
*** [CTK within Slicer](CTK within Slicer)(http://www.commontk.org/index.php/File:2011_11_14-CTK_Hackfest-CTK_within_Slicer.pptx)
**** [CtkDICOM](CtkDICOM)(CtkDICOM_in_Slicer4.md)
*** [ CTK within MITK]( CTK within MITK)(Media:Hackfest-2011-11-CTKandMITK.pdf .md)
** Dicom Application Hosting introduction: where we stand, how much further this week? (Beno�t)
** Dicom Networking (Steve, Michael)
** Plugin Framework (Sascha) [ [ pdf]( [ pdf)(Media:Hackfest-2011-11-PluginFrameworkCurrentState.pdf .md) ]
** Testing Framework (Julien) 
*** [Presentation](Presentation)(http://www.commontk.org/index.php/File:2011_11_14-CTK_Hackfest-Unit_testing_framework.pptx)
- Afternoon:
** end of presentations
** Road Map

**Tuesday 15th**:
*Morning 9:00 12:45:
** Hacking
*Afternoon 18:00:
**Hacking

**Wednesday**
*Morning 9:00 12:45:
**Hacking
*Afternoon 13:45 - 16:00:
**[ Roadmap Discussion]( Roadmap Discussion)(Hackfest_Nice_Roadmap_Discussion .md)
*Afternoon 16:00 - 18:00:
**Hacking

**Thursday**
*More hacking
- 4:00 Afternoon Roadmap discussion 

**Friday**
*11:00 Demo and wrap-up
*More hacking

  1. Demos
CTK Dicom Widget used by brand new mafPluginCTK, inside a MAF3 Application: [videoDemo](videoDemo)(https://www.biomedtown.org/biomed_town/MAF/MAF3%20Floor/download/wiki_folder.2011-11-17.4013453397/CTKDicomimporter)

How about a QA system for CTK? Here the first preview:[QA](QA)(https://www.biomedtown.org/biomed_town/MAF/MAF3%20Floor/download/wiki_folder.2011-11-17.4013453397/CTKQA/image)


Demos / Progress reports on Friday:
#Daniele + Roberto : CTK DICOM app in MAF + coding QA on CTK code + started to implement DAH in MAF.
#Ivo + Anthony : DICOM application hosting  Pt19 widget integrated into a new widget.
#Martin + Yves Slicer Execution model as a Dicom hosted app.
#Sascha : App hosting overview and progress.
#Matt : Remove Qt dependency from DGraph.
#Michael : App hosting XML, dcm2xml
#Steve : Implement new DICOM query functions in CTK.
#Marco : CTK DICOM code cleanup and improvement.
#Julien :  Testing using QtTest framework.
#Jean-Christophe : Better build config.

  1. Travel  Hotel
**Local contact**
- If you have any troubles during your visit, call Benoit : +33 4 92 38 71 55 (or if not available, +33 6 32 78 59 92, but it's my mobile)

**Airport** 
- Nice Airport: http://en.nice.aeroport.fr/

**Transportation on Site**
The taxi is awfully expensive, count around 50 � to go from Nice Airport to Antibes.

The bus from Antibes to INRIA is the Express 100. It starts "Place De Gaulle", the closest stop to INRIA is "Templiers", costs 1�. 
From there it will only take you 3 minutes to reach INRIA: [map from Les Templiers](map from Les Templiers)(http://maps.google.com/maps?saddr=Route+des+Coll%C3%A9s%2FD504daddr=43.61662,7.07352+to:Unknown+roadhl=enie=UTF8sll=43.61678,7.07076sspn=0.005328,0.011362geocode=FdyLmQIdpO9rAA%3BFWyJmQId8O5rACln8B9JIivMEjE0Ny-_kgRFgQ%3BFZaHmQIdrNhrAAvpsrc=0dirflg=wmra=dmemrsp=2sz=17via=1t=hz=17)

**Lodging** 
Prefer Antibes to any other locations, Sophia-Antipolis is very badly connected to places to sustain you at night, and the buses stop after 20:00/20:30

*Rooms have been blocked for 11 people in the hotel l'Etoile:

http://www.hoteletoile.com/

phone number: +33 4 93 34 26 30 

address: 2 Avenue Gambetta, 06600 Antibes, France

(54� per night for a single room, 6.50� for breakfast)
Also here is a map with the hotel, and the departure of the bus line 100: [file:hotel_etoile.pdf](file:hotel_etoile.pdf)(file:hotel_etoile.pdf.md)
There are other addresses you might find attractive, but I have made no agreement with them:

*H�tel Relais du Postillon (not far from the other, good reputation among the visitors of INRIA)

8 Rue Championnet, 06600 Antibes, France

http://www.relaisdupostillon.com/

+33 4 93 34 20 77 

For the other hotels, Apparently you should avoid "Le Collier". Then I have no reports on how the other hotels in Antibes compares. But if you can't find a room in the above hotels, try others near the rail station or within the old town. This way you will get an easy access to the bus (the Express 100).

**Meeting Location** 
- Inria Sophia Antipolis: 
2004 route des Lucioles BP 93
06902 SOPHIA ANTIPOLIS Cedex - FRANCE

**Catering**

Good news, lunches will be covered for everyone as well as coffee breaks morning and afternoon, courtesy of Inria!

**Weather**
- Average min/max temperature in November in Sophia Antipolis:15-20 Celsius

  1. Related Events/Activities
INRIA Imaging Workshop November 21-23: http://www-sop.inria.fr/asclepios/events/VPHimaging11/