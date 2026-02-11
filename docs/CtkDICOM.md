---
title: CtkDICOM
---

1. ctkDICOM
Showcase application showing the DICOM retrieve and browse functionality of different CTK components.

  1. Basic functionality
- Provide a database managing Patient, Study and Series information
** sql schema of header data
** Import local files
*** Recursive traversal of directories
*** Parsing of DICOMDIR files (WIP@DKFZ)
*** Manage local database: delete files, re-index, (vacuum or other db admin as needed)
** Query and Retrieve data from PACS
*** Search by different criteria
*** Configure PACS settings
*** Background listener that feeds into database
*** Efficient Study/Series move requests (integrate incremental queries into ctkDICOMModel)
** Thumbnail preview of selected series
** Quick single slice view 
*** Zoom/pan
*** Level window
** Search interface for local database (like Q/R search terms)
** Helper code for attaching new volume data into proper DICOM format and into database
** Store user code (send)
** Export from database to external directory (possibly with DICOMDIR)

- Structure Code for maximum reuses
** Utilize and enhance DcmSCU/DcmSCP code for core networking and contribute back to dcmtk where possible
** Provide ctk classes a Q_OBJECT wrappers around DcmSCU/P code
*** Core for non-GUI helpers
*** Widgets for QWidget subclasses
** All Q_OBJECT code should provide a rich property/invokable API plus plenty of signals and slots of that applications using the code can have customizability and user feedback
** Example helper applications like ctkDICOM, ctkDICOMIndexer, etc should be both demonstrations of the API and useful utilities in their own right

- Provide testing environment
** store/query/move/get tests
** example server (dcmqrscp)
** instructions for creating promiscuous server with cget so any user machine can test ctkDICOM networking