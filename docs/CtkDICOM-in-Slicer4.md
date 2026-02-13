---
title: CtkDICOM in Slicer4
---

1. Background
[3D Slicer version 4](http://www.slicer.org/slicerWiki/index.php/Slicer4) has been under development for several years and has grown along side CTK.  The DICOM support in Slicer4 draws heavily from the ctkDICOM effort and can serve as an example of how the CTK code can be used and what steps still need to be taken to make a more general tool.  This page was prepared as an outline for discussion at the [November 2011 CTK Hackfest](CTK-Hackfest-Nov-2011.html).

  1. Driving Use cases for Slicer4 DICOM
The [AMIGO Suite at Brigham and Women's Hospital](http://www.ncigt.org/pages/AMIGO) is the focus of much image guided therapy development with Slicer4 as a main component.  Typical usage includes:
- DICOM listener (manually or automatically push to slicer)
- Query/Retrieve diagnostic scans from hospital PACS or previous procedure scans from Syngo Via (local PACS in AMIGO)
- Ideally: Slicer Data Bundle to store planning information in PACS

Other (much more common) uses cases include:
- Import DICOM studies for research
** from disk
** by Query/Retrieve
- Use DICOM as format to save, organize, and share research processing results

  1. Current Capabilities
See [Slicer4 DICOM documentation page](http://wiki.slicer.org/slicerWiki/index.php/Documentation/4.0/Modules/DICOM).

- Import to ctkDICOMDatabase
- Display with ctkDICOMAppWidget
** thumbnails
** autoplay
** window/level
** pan-zoom
- Load into Slicer
** By Patient (multiple volumes)
** By Study (multiple volumes)
** By Series (single volumes)
- Listener loads automatically into ctkDICOMDatabase
- Query using ctkDICOMQueryWidget
** configure nodes and ae titles
** C-MOVE to listener (and into database)
- Export image data from Slicer
** Slicer Volume becomes DICOM Series
** User selects destination study (defines metadata)
- Send from ctkDICOMDatabase to remote listener
- Slicer Data Bundle (WIP)
** Slicer scene and all data saved to zip file
** zip file embedded as private creator tag in secondary capture

  1. Implementation
- PythonQt scripted module
** Scripted GUI calls CTK and Qt classes
** Some functions currently supported by helper applications
*** storescp, storescu
*** dcmdump, img2dcm, dump2dcm
- Code is in slicer4 repository
** [DICOM.py scripted module](http://viewvc.slicer.org/viewvc.cgi/Slicer4/trunk/QTScriptedModules/Scripts/DICOM.py?view=log)
** [DICOMLib helper classes](http://viewvc.slicer.org/viewvc.cgi/Slicer4/trunk/QTScriptedModules/DICOMLib/)
- Will be released as part of 3D Slicer 4.0 at RSNA in late November 2011

  1. Issues
- Query result selection not implemented (all query results retrieved - need to narrow query to get single subject)
- ctkDICOMModel + QTreeView is cramped
** doesn't fit well in slicer module layout
** would be nice to revisit columns be in
** maybe include the thumbnails?
- Preview image window is not sorted geometrically
- There is no support in ctkDICOM generally for geometric sorting or mapping of series into volumes
- Would be good to have more header data in database (currently not enough to reconstruct a valid header when exporting new series)
- Can't currently search in local database using search terms like in query interface
- Can't delete from the ctkDICOMDatabase (would like to delete by patient/study/series and optionally clean up files)
- ctkDICOMModel holds on to sqlite database meaning that ctkDICOMIndexer is very slow to insert
** workaround in slicer4 requires manually disabling the model in certain slots
- Several operations are blocking and provide no Qt level feedback to the user (e.g. import)
- Retrieve operation is blocking, but could be done in background.
- Seems like some transfer operations could be multi-threaded for efficiency
- Several of the operations can't be interrupted / canceled
- No C-GET support (or WADO?)
- Would like to have sample server that works so typical user can download and test slicer/ctk DICOM
** server needs to be in promiscuous mode
** could use C-GET to bypass NAT
** could run dcmqrscp locally
** could have people install other dicom code
** could install [XNAT Gateway](http://docs.xnat.org/XNAT-DICOM+Gateway)
- Users need help understanding configuration options (both inside ctkDICOM and on their servers)
- Can ctkDICOM help developers manage UID allocation?

- Issues with current slicer4 version
** Some ctkDICOM widgets are hacked since not all signals/configurations are available (for example, findChildren is used to hide or connect to subwidgets)
** Helper app cleanup: crash of main app leaves orphan storescp process
** Files need to be reparsed by ITK
** Formatting of exported series (and Slicer Data Bundle) is not correct
** How can slicer data structures be mapped to and stored as native DICOM objects?  (Annotations, xforms, models, labelmaps...)  If we did store them in a 'standard' way, does anyone else support reading from the 'standard'?
** QSettings of ctkDICOM widgets have no namespacing (like 'DatabaseDirectory')
** Slow queries due to Patient+Study query to populate ctkDICOMDatabase of query results

  1. Implementation Wishlist
- DcmSCP / DcmSCU subclasses for STORE and maybe GET
- ctkDICOM Core classes with signals and slots for configure, feedback, interrupt, logging...
- ctkDICOM Widget classes that can be flexibly assembled by applications
- Better layout options for widgets
- Database with all header tags
- Previews in ctkDICOMModel
- Integrate query with model (ctkDICOMQueryModel)
- Migrate slicer4 python functionality to ctk C++
- Helper classes for well formed exports and SCs (correct UIDs)

  1. Hackfest Progress
- DcmSCP / DcmSCU subclasses for STORE and maybe GET
** *integrated CGET from DCMTK master in a way it will build against DCMTK 3.6 - now works with ctkDICOMAppWidget!*
** *realized storescp executable isn't so bad*
- ctkDICOM Core classes with signals and slots for configure, feedback, interrupt, logging...
** *Developed signal architecture for query retrieve*
- ctkDICOM Widget classes that can be flexibly assembled by applications
** *Can use internal widgets*
- Better layout options for widgets
** ''New model functionality in 
- Database with all header tags
** *TODO*
- Previews in ctkDICOMModel
** *leave for the application to do for now*
- Integrate query with model (ctkDICOMQueryModel)
** *plans for progress signals and interruptible query*
- Migrate slicer4 python functionality to ctk C++
** *TODO*
- Helper classes for well formed exports and SCs (correct UIDs)
** *TODO*