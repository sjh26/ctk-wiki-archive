---
title: Documentation/Interfacing Via OpenGL
---

*This is a development idea for discussion and experimentation at the [2010 Hackfest](2010 Hackfest)(May,)(CTK-Hackfest-May-2010.md)*

  1. Possible vtkXIPActor (or vtkOpenInventorActor)
    1. Proof of Concept
- A link between vtk and xip could be done by following the example of the [vtkOpenGLScriptedActor](vtkOpenGLScriptedActor)(http://www.slicer.org/slicerWiki/index.php/Slicer3:Python:ScriptedActor).  In this example:
** vtk sets up the rendering context as it normally does during a call to the Render() method on a vtkOpenGLRenderWindow
** the actor's Render() method is responsible for calling the OpenGL API (in this case using PyOpenGL.
- It should be possible to encapsulate OpenInventor scene graphs inside a similar structure.

    1. Open issues
- Mapping vtk events into OpenInventor events so that it is possible to interact with the XIP scene
- Mapping xip inputs (like volume data) generically to a "Set*" methods on the vtk object.

    1. Possible Usage
 vtkXIPActor *xipActor = vtkXIPActor::New();
 xipActor-SetSceneGraph("XIPSampleScene.iv");
 renderer-AddActor(xipActor);
 renderWindow-Render();