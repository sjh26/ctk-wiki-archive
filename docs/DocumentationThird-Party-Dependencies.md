---
title: Documentation/Third Party Dependencies
---

While the details of the implementation have yet to be finalized, a few of the design principles have been decided by the founding group.  In particular, several core libraries will serve as the foundation.

**Overall object structure will be based on Qt 4.5**

http://www.qtsoftware.com/

See the [Widget Plans page](Widget Plans page)(wiki:WidgetPlans).
See the [Coding Guidelines page](Coding Guidelines page)(wiki:CodingGuidelines).

**DICOM support will be implemented using DCMTK**

http://dicom.offis.de/dcmtk

**Visualization will use VTK**

http://www.vtk.org

**Analysis algorithms will use ITK**

http://www.itk.org

**Software engineering methodology will follow the ITK style (leveraging CMake and friends)**

http://www.cmake.org

**A To-be-determined wrapping tool will support calling CTK from Python, Tcl, Java, C#, etc**


----

**Open Questions**

- Qt Script (javascript) provides a subset of "traditional" VTK-style wrapping.  [PyQt](PyQt)(http://www.riverbankcomputing.co.uk/news) is GPL so not usable in CTK.  What are the other alternatives?  
** Perhaps [PythonQt](PythonQt)(http://pythonqt.sourceforge.net/) - it is LGPL and lighter (less complete) than [PyQt](PyQt)(http://www.riverbankcomputing.co.uk/news).  It is a product of the [MeVisLab](MeVisLab)(http://www.mevislab.de) effort.
** [PySide](PySide)(http://www.pyside.org/about/) appears to be the nokia-sponsored replacement for PyQt.

- What third party widget libraries exist for Qt?  What licenses do they use? (Since the open source version of Qt was GPL until recently, most third party libraries are probably GPL also).  For example, [the QDCWS project](the QDCWS project)(http://sourceforge.net/projects/qdcws/) combines DCMTK with Qt but is GPL (and no longer active, apparently - email to the developer bounced).