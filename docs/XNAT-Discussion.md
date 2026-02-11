---
title: XNAT Discussion
---

1. General ideas
      1. CTK XNAT Library
- Pull out the XNAT data structures from the plug-in and create a CTK library (there have been requests for that) {{Done}}
- Use virtual methods in ctkXnatObject subclasses for fetching the data (i.e. move the fetch methods from ctkXnatConnection to the subclasses) (It seems this exists already ? - Flo) {{Done}}
- Support asynchronous operations in ctkXnatObject? {{Doing}}
- Support editing Xnat data and committing it back to the server (?) {{Done}}
- Think about user access rights and how to handle read-only access within setters of ctkXnatObject sub-classes
- Use ctkException as a base class for ctkXnatException {{Done}}
- Create (asynchronous) Qt models for displaying data in list, tree and table widgets
- Thinks about possibilities to generate GUI masks for editing or creating XNAT data objects
- Add a simple example application which reuses Xnat related Widgets from a (new) CTK library and allows to query a Xnat server {{Done}}
- Add querying support (https://wiki.xnat.org/display/XNAT16/Query+the+XNAT+Search+Engine+with+REST+API)

      1. qRestAPI library
- emit resultReceived signal in the qRestAPI class {{Not_Done}} (invalid)

    1. Ideas from the London Hackfest
- ctkXnatServer: should it be an ctkXnatObject, or should we keep it at all. We keep it for now. Maybe adding for meaningful metadata about the server to justify the name, or maybe to rename it to ctkXnatRootObject or similar.
** We went for ctkXnatSession as the class name {{Done}}
- Create a separate class for storing ctkXnatObject properties and share it between XNAT objects shared across projects. Make the ctkXnatConnection maintain a cache / map of ID-property object pairs.
- Possibility to set the parent in the xnat object constructor, as well by the setParent function. {{Done}}
- Check if the create/save functions could be unified to a single save function. {{Done}}
- Save all the properties of the xnat objects. {{Done}}
- Introduce a 'dirty' flag in ctkXnatObject that describes if the properties or the set of children has been modified. Not the children themselves. The save function should check this flag and not re-save the object again if it is not dirty.
- Introduce a modificationTime member in ctkXnatObject. The save function should update this. The reload function should check this property and retrieve the properties only if the 'remote' modification time is newer than our 'local'.
- Reload support. See previous point.

- Session support. Create a session when the user logs in. Use the returned session ID for the subsequent requests. If the session expires meanwhile, an exception should be thrown and processed in the client. The login dialog should be popped up or thing like that. {{Done}}

- Registering C++ classes to XML schema types. {{Done}}
- Download location. {{Not_Done}} (already works)
- Zip/unzip support. Add QuaZip external project or copy MiniZip files to the XNAT library sources.

    1. Ideas from the Heidelberg Hackfest
- Constants for common XNAT properties
- Modify the fetch methods to work on the cache and update the cache if necessary
- Cache
** Use QHashQString, ctkXnatObject*
** Create ctkXnatObject::globalId() for use in the cache