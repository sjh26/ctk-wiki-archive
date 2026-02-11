---
title: Documentation/WidgetPlans
render_with_liquid: false
---


1. Background
The ctkGUI library will need to provide a set of Qt extension widgets geared for scientific and medical uses.

Some of these widgets exist in a variety of Qt-based packages which may be drawn upon if the license permits.  Other widgets will be recreated from scratch based on corresponding widgets in other toolkits.  This page collects some ideas and examples of the types of widgets that are needed.  Please add ideas to the lists below.

'''
  1. General Purpose Widgets
'''

- **Menu Button**

- **Range Widget** (pick a min/max with one widget) (like window/level and threshold used here: http://www.slicer.org/slicerWiki/index.php/Modules:Volumes-Documentation-3.4)

- **Extent Widget** (pick a 3D subvolume)  (see example http://www.kwwidgets.org/Wiki/Image:KWWidgetsCompositeWidgetsOverview.png)

- **Color Pickers and dialogs** (single color)

- **Color table editor** (lookup table list of named colors) (http://www.kwwidgets.org/Wiki/Image:VtkKWColorPickerDialog_Classes.png)

- **Path List Browser** (i.e. a widget that manages a list of paths like LD_LIBRARY_PATH) (see http://www.slicer.org/slicerWiki/index.php/File:Slicer3.4-module-path-dialog.png)

- **File Browser Widget** (embeddable in a more complex dialog)

- **Load/Save Button**

- **Thumbwheel** and other ways to pick scalar values (http://www.kwwidgets.org/Wiki/Image:KWWidgetsCoreWidgetsOverview.png)

- **workflow/wizard frameworks** (http://www.kwwidgets.org/Wiki/Image:EMSegmentationModuleWizardAnimated.gif)

- **error/info log window** / notification framework (http://www.kwwidgets.org/Wiki/Image:KWWidgetsLogDialog.png)

- **script console** (like tkcon / ipython) (http://opencircuitdesign.com/xcircuit/giffiles/tkcon.gif)

- **animation controller** (vcr buttons start/pause/loop...) (see example http://www.kwwidgets.org/Wiki/Image:KWWidgetsCompositeWidgetsOverview.png)

- **collapsible frames** (http://www.slicer.org/slicerWiki/index.php/Modules:MainApplicationGUI-Documentation-3.4#Slicer_Viewers)

- **stopwatch**

- **image gallery**

- **database browsers**

- **Undo/Redo** Buttons/Comboboxes

- **Data repository / scene overview** (show all objects, easy modification of visibility, visualization properties  ...)

- **Application Settings Dialog** (with Registry abstraction)


'''
  1. Scientific Widgets
'''

- **Parametric Function Editor** (http://www.kwwidgets.org/Wiki/Image:KWWidgetsTransferFunctionEditors.png)

- **1D and 2D Histogram** ((like image histogram here: http://www.slicer.org/slicerWiki/index.php/Modules:Volumes-Documentation-3.4 -- note the window/level in the background and the range widget on the bottom that can be used to zoom)

- **Matrix Display/Edit** widget (for numerics)

- **various plots/graphs/tables**...

- **gauges and dials**
 

'''
  1. Visualization Widgets
'''

See examples at: http://www.kwwidgets.org/Wiki/Image:KWWidgetsVTKWidgetsOverview.png

- **Render window** with overlays and corner annotations (http://www.slicer.org/slicerWiki/index.php/Modules:MainApplicationGUI-Documentation-3.4#Slicer_Viewers)

- **Material properties editor**

- **Transfer function editors**

- **Volume Rendering Parameter Editor**

- **Light editor**

- **Camera parameters widget**

- **4x4 matrix editor** (http://www.slicer.org/slicerWiki/index.php/Modules:Transforms-Documentation-3.4)

'''
  1. 2D/3D Interaction Widgets
'''

See example images from the CTK_Widgets_snaps.zip file attached to this page.  Each of these widgets has a 3D interactor (a.k.a. 3D Widget, manipulator, or 3D Gadget) linked to a 2D widget that shows the numerical parameters being manipulated.  

See also the VTK Widget examples: http://www.vtk.org/Wiki/VTK_Widget_Examples


- **Rotation widget**

- **Translation widget**

- **Isotropic-scaling widget**

- **ROI widget**

- **Probing widget**

- **Distance meter widget**

- **Selection widget**

See also the way these manipulators are implemented in Autodesk's Maya animation and modeling software:

- http://download.autodesk.com/us/maya/2010help/index.html?url=Transforming_objects_Use_manipulators.htm,topicNumber=d0e65921

- See also the http://download.autodesk.com/us/maya/2010help/index.html?url=Transforming_objects_Use_the_Universal_Manipulator.htm,topicNumber=d0e66424


'''
  1. Medical Imaging Widgets
'''

- **DICOM header browser** (http://www.slicer.org/slicerWiki/index.php/File:AddVolume.png)

- **Image Viewer** (with window/level, pan/zoom, corner annotations, lightbox modes...) (http://www.na-mic.org/Wiki/index.php/File:Annotated_Lightbox.png http://www.na-mic.org/Wiki/index.php/File:Case01-BF-axial.jpg)

- **PACS-like browser** (Modality/Patient/Study/Series/Image hierarchy with image preview) (http://www.clubpacswestmi.net/final.png)

- **Transform hierarchy editor** (http://www.slicer.org/slicerWiki/index.php/Modules:Data-Documentation-3.4)

- **Fiducial Landmark point list widget** (x,y,z,name, color, type, visibility flag...) (http://www.slicer.org/slicerWiki/index.php/Modules:Fiducials-Documentation-3.4)

- **Image comparison tools** (checkerboards, overlays, cross-fade, side-by-side linked zoom...) (http://www.na-mic.org/Wiki/index.php/File:Annotated_Lightbox.png http://www.na-mic.org/Wiki/index.php/File:Case01-BF-axial.jpg)

 

'''

  1. Application Specific Widgets
    1. fMRI
- Voxel Time Course Graphs [http://www.commontk.org/images/5/5c/Slicer2-fmri-montage.png](http://www.commontk.org/images/5/5c/Slicer2-fmri-montage.png)
- Design Matrix / Paradigm Editor

    1. Diffusion MRI
- Tractography Options [http://www.slicer.org/slicerWiki/index.php/Modules:FiducialSeeding-Documentation-3.6](http://www.slicer.org/slicerWiki/index.php/Modules:FiducialSeeding-Documentation-3.6)
- Fiber Bundle Properties [http://www.slicer.org/slicerWiki/index.php/Modules:DTIDisplay-Documentation-3.6](http://www.slicer.org/slicerWiki/index.php/Modules:DTIDisplay-Documentation-3.6)

  1. References
'''

Built-in Qt Widgets:

http://doc.trolltech.com/4.5/gallery-plastique.html

Qt Add-On Widgets:

http://www.qt-apps.com

http://www.libqxt.org/

http://www.qtsoftware.com/products/appdev/add-on-products/catalog/4

http://qwt.sourceforge.net/

Other Examples:

http://www.kwwidgets.org/Wiki/KWWidgets/Screenshots

http://www.digitalfanatics.org/e8johan/projects/widgets/

