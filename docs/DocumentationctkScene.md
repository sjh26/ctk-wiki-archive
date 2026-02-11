---
title: Documentation/ctkScene
---

1. What is a Scene
1. Generically, a scene is composed of objects that fill a portion of space and time
#* Objects have a position in space
#* Objects have an orientation in space
#* Objects have a range in time
#* Given a point in physical space and time, it should be possible to determine if an object contains it or not.
#* An object should contain at least one point in space and time
#** The concept of units is paramount in a scene.
#** Units describe the spatial and chronological scale of an object
1. A scene represents a hierarchy of object in space and time.
#* Objects have a single parent (except a root object) and may have one or more children objects
#** That is, a scene is a tree of objects
#* Moving a parent object in space or time should (by default) cause its children to experience the same movement in space and time
#* The coordinate system for root objects is defined as "real-world" space.   It is an absolute space.
#* A scene may have multiple roots
#** It is not necessary to represent everything in space from a single root.
#** One or more roots are used to contain the physical/temporal objects relevant to a particular task.
#* Objects implicitly include their child objects
#** When querying the time/space extent of an object (e.g., to determine if a point is inside of it or to determine its bounding box) that query typically also includes its child objects in its computations.
#* Most queries to and responses from objects should be with respect to real-world space (i.e., the coordinate system of the root object).
#** For example, querying an object if it contains a physical point is done using real-world coordinates (i.e., a coordinate system common to all objects in its tree).

1. Use Cases
There are three broad categories of technical use-cases for scenes:  Algorithms,
Storage, and Display

1. Algorithms
  1. Register an arbitrary object (including its children) with another object
  1. Use one object to define an ROI for an operator
  1. Fit an object (in a parametric form) to another object (i.e., adjust the parameters of a spherical harmonics representation of a spleen to make it fit an image of a spleen)
  1. Abstract surgical simulation (computational geometry: add, subtract, etc).
  1. Compute tumor change over time
  1. Compose multiple 2D ultrasound images, taken over time, into a 3D volume
1. Storage
  1. Represent a surgical environment
  1. Vascular network having 100s of blood vessels in a hierarchy
  1. Group a collection of scans from a single patient as well as the segmentations derived from those scans
  1. Group a collection of scans from multiple patients
  1. Group a collection of scans taken over time (decades)
  1. Save a scene in one application, and load it into another
1. Display
  1. Display registration results as a checkerboard image
  1. Multiple 2D and 3D display of the same scene
  1. Display driven by one object, but containing representations of other objects (e.g., segmentation results are shown as a color overlay on a slice)
  1. Object tracking - point-of-view control as an object's transform is changed by an external tracker (e.g., virtual endoscopy)
  1. Rendering the same object in different ways in different displays
  1. Updates to an object in one display immediately affect other displays

  1. Examples
1. Open-Source !OpenInventor: open source version of Open Inventor from Sgi which we use in OpenXIP
1. Commercial !OpenInventor: two commercial versions which are used to implement XIP-based products
#* Mercury: http://www.vsg3d.com
#* !SystemsInMotion: http://www.coin3d.org
1. OpenSG
#* http://opensg.vrsource.org/trac
1. !OpenSceneGraph
#* http://www.openscenegraph.org/projects/osg
1. OpenRM
#* http://www.openrm.org
1. NVSG
#* http://developer.nvidia.com/object/nvsg_home.html
1. OpenMAF / VME
#* http://www.biomedtown.org/biomed_town/MAF/MAF2%20Floor/documentation%20room/doc/maf-2-2%20main%20wiki/VME/?searchterm=VME
1. MRML (Slicer)
#* http://www.slicer.org/slicerWiki/index.php/Slicer3:Data_Model
3 ITK and IGSTK: !SpatialObjects
#* http://www.itk.org/ItkSoftwareGuide.pdf  (ITK Software Guide, Chapter 5: Spatial Objects, pp. 101-138)
#* Companion: !SpatialObjectViewers = http://www.na-mic.org/Wiki/images/f/fd/Na-Mic-SLC05-SpatialObjects.ppt
#* Used in IGSTK: http://public.kitware.com/IGSTKWIKI/index.php/IGSTK:Tutorial#IGSTK_Components
1. MITK: !DataTree/!DataStorage
#* http://www.mitk.org/wiki/Publications?action=AttachFiledo=gettarget=MITK-SPIE-2004-1.pdf
#* http://dx.doi.org/10.1016/j.media.2005.04.005
#* http://hdl.handle.net/1926/14
#* http://docs.mitk.org/nightly-qt4/group__DataStorage.html



1. Implementations in Code
For ctkScenes there are perhaps three possible implementations.  They are discussed next.

Not discussed explicitly, but highly important, is the consideration of interactions.   There will be different interactions styles for a view of a scene.  It might be necessary to have "service actors" / "handlers" that exist only to sustain certain interactions.   An interaction might not change only a parameter of the scene for a particular view (e.g., move the camera), but it might actually modify an object.

  1. Implementation 1) Views of Scenes
The quantum of encapsulation in the View. A CTK View is a module that can take as input standards CTK Data Objects ( I here postulate CTK will have a unique Data Object Model) and return a render window.  In addition, the View exposes some interaction styles, that must be connected to actual interactions, and a number of View Settings, that the application must capture and pass to the View (typically via a GUI).  Each view run a separate thread, and connects with the rest of the application through a limited set of public APIs.  a Facade class prevents any access to internal methods, and makes easier the wrapping into scripting languages. So for a programmer writing a CTK-based application a View is something he can use as it is or not, but cannot be modified (except of course changing the code of the view itself).  Which visualisation library is used inside each view is immaterial.  The View programmer has the responsibility to transform the CTK Data Objects into Actors compatible with VTK, Open Inventor or whatever he plans to use for that view. Similarly, it is his responsibility to transform the rendering output of the visualisation library into a CTK Render Window.  In the picture below the CTK View would be the blue box.

[1. a possible design pattern for ctk](1. a possible design pattern for ctk)(Figure)(Image:ctk_view_encapsualtion.gif.md)

  1. Implementation 2) Scene of Actors
The quantum of encapsulation is a scene of actors. CTK provides classes that automatically compose data objects into actors and these into scenes, and expose such scene in a way that is neutral to the visualisation library.  Each application programmer is responsible to decide what to do with this scene, but in principle CTK could also provide additional modules for interactive rendering.  The scene composer module is the red box, and the interactive rendering module is the brown box.

  1. Implementation 3) Scene of Objects
A scene contains objects that have the features as described at the top of this page.  A scene specifically excludes graphics primitives such as vtkActors or openGL triangle strips, etc.   A scene also specifically excludes algorithms.     Instead visualization-library-specific primitives are stored and manipulated by observing the objects in scenes.  These visualization-library-specific capabilities are isolated to the "view".    Algorithms / logic / interactors are limited to the "controllers."  This approach follows a model-view-controller design pattern.   It is illustrated in the following two figures.

[2. An illustration of how the model-view-controller design pattern can be applied to a ctkScene.](2. An illustration of how the model-view-controller design pattern can be applied to a ctkScene.)(900px|Figure)(Image:ctkMVCDesignPattern.png.md)

[3. Revision to Figure 1 based on the MVC design shown in Figure 2.   Actors are removed from being part of the scene.](3. Revision to Figure 1 based on the MVC design shown in Figure 2.   Actors are removed from being part of the scene.)(Figure)(Image:ctk_view_encapsualtion-Revsized.gif.md)

  1. Implementation 4) A scene in Qt (Pat's suggestion)
The scene could be implemented as a QtObject.   That is, the scene should not be part of ITK or VTK, but instead should be part of Qt.   Qt already has excellent tree and property management capabilities.    The challenge will be managing dependencies on VTK and ITK.   A design of a QtScene that can be used by ITK or VTK independently or together has been suggested so that ITK developers won't need to use/learn/compile VTK and vice versa.

qtScene would manage the spatial location and parent-child relations of the qtSceneObjects.  The qtSceneObjects would only store tokens (i.e., they would not contain the actual object's data).   ITK or VTK adaptor classes would then take an qtSceneObject's token, optionally do the necessary I/O, apply the transform from the qtScene, and return the associated itk/vtk data object.   Via the adaptor classes, we can fulfill the basic API of a scene, e.g., implement member functions to test if a point is or isn't inside an object and its children, change the color of an object.   We would be able to take advantage of qt's "wonderful" property management capabilities, signals and slots, etc.

In this design, an application does not have to link to the QtGui library.  It can use QtCore and have access to an enormous amount of convenience functions for string manipulation, file i/o, regex, plugin support, property systems, signals/slots, etc.

  1. Gianluca's suggestion (Implementations in Files)
A scene should also be represented in file format.   This file format will be used to exchange information across toolkits.

Perhaps CTK should only adopt a file format, and not create classes - there are so many off-the-shelf scene graph-based toolkits already, some very good.

    1. XIP XML Scene
1. XML is a good choice for an easy to parse scene graph file. Ideally this XML file could be parsed and translated to object instances from any scene graph library. The XML format should be organized in different sections to facilitate parsing in a fault-tolerant way. This is because a C++ scene graph object that has been modified by a software developer may get out of sync from the corresponding description found in the scene graph file.
1. The structure of such XML scene graph file format must not change drastically if a user loads a scene graph file, makes a simple change to the scene graph and saves it again. It should be possible to use a diff-and-merge tool like the ones used for source code in order to see where specific changes occurred. This is a must-have in order to be able to work on large projects with multiple developers.
1. The file must allow for the inclusion of information stored in separate files, in the form of nodes that load "sub-graphs". This is the equivalent of #include files in C++ code, and it is another must-have in large projects with multiple developers.
1. The format should include, at least optionally, additional presentation information about each scene graph object so that a Visual Programming environment can save and restore the way a developer has arranged scene graph objects within the workspace (position, grouping, etc.)

The above considerations have already been implemented in the new XML-based XIP scene graph file format - except for (1): so far they have looked primarily into Open Inventor, and there are still open questions about whether this format is general-purpose enough. 

  1. Marco's suggestion
We would have an advantage with Implementation #2 only if the brown box could be entirely replaced by an existing visualisation library; unfortunately I suspect this is not the case:

- Most scengraph libraries treat only vector data + textures; extensions are needed for example to render volumes

- Most complex interaction styles cannot be encoded in the scenegraph, and need to be programmed with direct calls to the visualisation library.

- No visualisation library could provide you out-of-the-box mechanism to modify CTK data objects from interaction.

This means in most realistic cases the application programmer should anyway cross the brown box and code directly with the visualisation library calls. 

This is why we consider Implementation #1 the most interesting for CTK.  If you are an application programmer you use pre-packged View modules, and you just have to pass your data object, attache your interaction devices to the pre-defined interaction styles, and expose in your GUI the View settings, and the render window: done.  If you need a special View, then of course you need to dirt your hands with a visualisation library, but this would happen anyway.  CTK community could provide template of View modules to be programmed with VTK, Open Inventor, OpenSG, etc. to make life easier.

  1. Stephen's suggestion
Combining implementation #3 and #4 allow a ctkScene and algorithms that process it to be implemented independently of the visualization library.  The mapper is specific to the visualization library and also manages interactions.   This design pattern is used in MITK (I believe), IGSTK, SOViewers, and probably others.

By closely following the model-view-controller design pattern, we will be able to 
1. Interface with different visualization libraries by using different mappers
1. Interface with other toolkits (XIP, IGSTK, ITK, ...)
1. Develop algorithms without caring how the objects being processed are displayed (and without having to link with a visualization library)
1. Have different displays potentially use different actors for each object (managed by the mapper)
1. Have different displays potentially use the same actor for the same object (managed by the mapper)
1. Create Interactive Actors that are tied to controller logic (i.e., that process the scene data structure) and via that controller logic manipulate the object's parameters/properties.
1. Create Interactive Actors that are tied to display parameters (e.g., camera position)
1. Have object properties that are shared across views (e.g., color) by storing them as SpatialObjectProperties
1. Have object properties that are specific to particular views by storing them in the mapper

In Maverick we wrapped the mavScene into Qt, and it had some great benefits - could tie a scene to a qtVTKDisplay simply by connecting signals and slots. Could list the objects in a scene by a qtSceneBrowser widget, etc etc.    In short, it became possible to define some very powerful qt widgets that operated on the entire scene.


  1. Ivos and Marcos remarks
As for the MITK team, we traditionally like the definition of a scene given at the top of this page and the mode-view-controller pattern. Both is pretty close to what is used within MITK (except for some extensions, which would be great to have) and therefore could nicely be integrated from CTK.

But caution (correct me, if I am wrong): The Open Inventor definition of a scene is different! Nodes in an Open Inventor scene graph are not necessarily objects (called shape nodes there), but can also be lights, materials (e.g. color), transforms (matrices), switches etc. Thus, the definition a scene is composed of objects that fill a portion of space and time is not compatible with Open Inventor (a material node does not fill a portion of space). Maybe it is possible (and desirable) to combine both ideas of defining a scene graph: the more data-centered approach defined above and the visualization-centered approach of Open Inventor. But we should be careful that we are talking about the same things. 

  1. Steve's Comments
A few points from our experience when redesigning MRML a few years ago:


- Object model and data structures for the scene:

A core issue for MRML was the on-disk and in-memory representation of complex data types that are part of the scene.  Since we use both VTK and ITK extensively, we considered creating a toolkit-independent object layer with adaptors to both toolkits... but we quickly realized that this meant building not only a new object layer but two complete adaptors.  Instead, we standardized on VTK for our MRML Scene layer and have an interface to ITK (a pretty slick one - it uses the ITK I/O factory to give pointer access to the image data).

By sticking, in particular, with vtkPolyData we have been able to represent things like diffusion tractography fiber bundles with tensors-per-vertex and annotated brain surface models.  These are hard data structures to write and debug, and also by using VTK as the object model it plugs easily into the rest of the application.  Note that MRML *does not* describe the GUI and it *does not* even link to OpenGL.  It merely uses VTK for the data structures and the rich set of I/O and data manipulation utilities.  Since CTK will have VTK available, the same considerations apply.

One way of interpreting this approach is that it is essentially Pat's suggestion (Implementation 4), but using VTK (mostly vtkCommon) as the basis for the internal data structures.  From there you can have an ITK adaptor and/or a Qt signals/slots interface as Stephen has shown in mavScene.  Using QtCore's tree data structures and other tools to organize the vtkObject instances may be an ideal combination.


- Descriptions of Image Acqusition

We should distinguish between "objects that fill space" and "physical observations of objects using particular imaging devices and protocols" -- we typically have the latter and are trying to calculate the former.  The ctkScene described on the wiki doesn't (yet) talk about the importance of having the scene be able to describe the image acquisition, clinical information, or other real-time info.  Image acquisition info is basically what comes from the DICOM header like the imaging device and protocol.  In general we should also be able to represent data on things like fMRI stimulus presentation and physiological response if ctkScene apsires to have complete information necessary for a wide range of image analysis tasks.


- The "physical scene" vs. the "semantic scene"

The current ctkScene description focuses on objects in space, but there is also a lot of non-physical information that we typically embed in the scene - things like anatomical labels and annotations.  In MRML we allow /model hierarchies/ independent of /transform hierarchies/ (e.g. the "skeletal system" as opposed to the "hand").  The former might be used for visualization, while the latter can be used for positioning child objects relative to parent objects.