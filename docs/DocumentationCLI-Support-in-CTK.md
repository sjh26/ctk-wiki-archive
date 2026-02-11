---
title: Documentation/CLI Support in CTK
render_with_liquid: false
---


Command Line Interface (CLI) support in CTK will primarly focus on providing an API for working with existing CLI modules. Providing utilities and tools for creating CLI modules from scratch is a desired addition but there are no concrete plans for this yet. See [Documentation/Command_Line_Interface](Documentation/Command_Line_Interface)(Documentation/Command_Line_Interface.md) for more general information about CLI modules.

    1. Getting the Code
The code is available in the CTK master:

https://github.com/commontk/CTK

Enable the following CMake options to be able to play with the code:

- **BUILD_TESTING** (for creating CLI test modules)
- **CTK_APP_ctkCommandLineModuleExplorer** (small program allowing you to test-drive CLI modules using the CTK CLI module API, enables all the options below)
- **CTK_LIB_CommandLineModules/Core** (the CTK library providing the core CLI module API)
- **CTK_LIB_CommandLineModules/Frontend/QtGui** (the CTK library providing GUI generation using the Qt widgets)
- **CTK_LIB_CommandLineModules/Backend/LocalProcess** (the CTK library for executing local executable files as command line modules)

    1. API Design
This is a partially overview of the API design, showing the GUI generation process for the Qt front-end.

graphviz
digraph G {
graph [= "TB"
](= "TB"
)(
rankdir);
node [= "16"
shape = "ellipse"
](= "16"
shape = "ellipse"
)(
fontsize);
edge [
](
);
subgraph cluster_0 {
  label = "CTK";
  color = lightGray;
  "xmlFile" [label = "{f0 Command Line Module XML (.xml)| f1}"
  shape = "record"
  ](label = "{f0 Command Line Module XML (.xml)| f1}"
  shape = "record"
  )(
);
  "gui" [label = "{f0 Qt GUI | f1}"
  shape = "record"
  ](label = "{f0 Qt GUI | f1}"
  shape = "record"
  )(
);
  "uiFile" [label = "{f0 CLI UI (.ui) | f1}"
  shape = "record"
  ](label = "{f0 CLI UI (.ui) | f1}"
  shape = "record"
  )(
);
  "ctkCLIModuleDescription" [label = "{f0 ctkCmdLineModuleDescription| f1}"
  shape = "record"
  ](label = "{f0 ctkCmdLineModuleDescription| f1}"
  shape = "record"
  )(
);
}

subgraph cluster_1 {
  label = "3D Slicer";
  color = gray;
  "vtkMRMLParametersNode" [label = "{f0 vtkMRMLParametersNode| f1}"
  shape = "record"
  ](label = "{f0 vtkMRMLParametersNode| f1}"
  shape = "record"
  )(
);
}
"xmlFile":f0:e - "xmlFile":f0:ne [= "XSD file check" ](= "XSD file check" )(label);
"xmlFile":f1 - "uiFile":f0 [= "QtGui XSL file" ](= "QtGui XSL file" )(label);
"xmlFile":f1 - "uiFile":f0 [= "" style=invis](= "" style=invis)(label);
"xmlFile":f1 - "ctkCLIModuleDescription":f0 [label=ctkCmdLineModuleXmlParser](label=ctkCmdLineModuleXmlParser);
"ctkCLIModuleDescription":f1 - "vtkMRMLParametersNode":f0 [label=create](label=create);
"uiFile":f1 - "gui":f0 [= QUiLoader](= QUiLoader)(label);
"gui":f1:e - "vtkMRMLParametersNode":f1:w [= both label=synchronize constraint=false](= both label=synchronize constraint=false)(dir);
}
/graphviz

Overview of some central classes and their scope.

Please see the full [Core API](Core API)(file:///opt/ctk-builds/CTK-debug-gcc/CTK-build/Documentation/html/group__CommandLineModulesCore__API.html) for a list of available classes and their documentation.

      1. ctkCmdLineModuleDescription
C++ API for accessing the command line arguments meta-data defined in the XML description.

This class is *read-only*.

      1. ctkCmdLineModuleReference
A handle to a command line module.

- Get ctkCmdLineModuleDescription class
- Convenient meta-data access (module location etc.)
- Used to crate actual ctkCmdLineModuleFrontend instances from specific ctkCmdLineModuleFrontendFactory implementations

      1. ctkCmdLineModuleFrontend
Represents an invokable command line module and its current parameter values.

Multiple instances for the same ModuleReference may exist.

- Set/Get individual parameter values or all at once
- Reset to default parameters
- Get GUI representation (QObject*)
- Get parameter value change notifications

      1. ctkCmdLineModuleFuture
Returned by the ctkCmdLineModuleManager run method and used to communicate with a running module.

- Run/Abort 
- Status
- Progress reporting
 
      1. ctkCmdLineModuleManager
Responsible for managing and running other ctkCmdLineModule* classes.
 
- Register specific back-ends for handling different types of modules
- Register/Unregister modules
- Get ctkCmdLineModuleReference objects
- Run ctkCmdLineModuleFrontend objects

    1. Customizability
      1. Qt Widget related
See also the [ctkCmdLineModuleFrontendQtGui](ctkCmdLineModuleFrontendQtGui)(http://www.commontk.org/docs/html/classctkCmdLineModuleFrontendQtGui.html) class for customization information.

- Use parameters for the default XSLT file to customize widget class names for argument types
- Use your own XSLT file for custom transformations of XML to UI
- Use your own QUiLoader to control instantiation of certain widget types

      1. General
- Use a custom *factory* to create your own GUI based on a ctkCmdLineModuleDescription instance.

