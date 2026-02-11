---
title: Documentation/Command Line Interface
render_with_liquid: false
---


1. What are CLI modules?
"CLI (commandline interface) modules" are standalone tools (for instance, a segmentation algorithm) that offer a commandline interface and a **--xml** switch that outputs a *machine-readable kind of --help* (XML description of their supported parameters, values, hints, etc.).  This makes it possible to use such CLIs as some kind of "plugins" for rich GUI applications that offer visualization and **automatically generated GUI panels** for parameter adjustment.  Also, the whole data handling is left to the host application (which may e.g. implement a batch processing pipeline, running the CLI systematically on all relevant data for a particular study), and it becomes possible to use the **same algorithm in various different host applications and contexts**, by agreeing on a common standard for the --xml output.

  1. CTK Support for CLI Modules
CTK provides an API for interfacing with such self-describing command line modules, and the XML schema for the parameter description and most of the supported feature set for a module has been adopted from the Slicer Execution Model (the first host where this idea originated).

The API provided by CTK allows the management, GUI generation, and asynchronous execution of such modules in a toolkit-independent and interoperable way. Application writers can rely on the provided libraries and their API to quickly integrate command line modules into their applications.  CTK also comes with an example application, called ctkCommandLineModuleExplorer which can be used to load different kinds of modules, to verify their correctness, to run - and finally inspect their output.

;More information on CTK's support for CLI modules:
: There is [a well-written page in the Doxygen docs](a well-written page in the Doxygen docs)(http://www.commontk.org/docs/html/CommandLineModules_Page.html) (and a [group for the classes](group for the classes)(http://www.commontk.org/docs/html/group__CommandLineModules__Group.html)), as well as [separate wiki page](separate wiki page)(a)(Documentation/CLI Support in CTK.md).

  1. Example Applications
CLI modules are already supported by a number of host applications, e.g. 3D Slicer, NiftyView / MITK Workbench, GIMIAS, MedInria, MeVisLab, nipype and more.  You can see some examples on the [In Context](In Context)(CLI)(Documentation/CLI_In_Context.md) page.

  1. Background Information / Specs
Currently, the CLI module standard is documented as [Slicer's Execution Model](Slicer's Execution Model)(http://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Developers/SlicerExecutionModel).  There is an [XML schema definition](XML schema definition)(https://github.com/commontk/CTK/blob/master/Libs/CommandLineModules/Core/Resources/ctkCmdLineModule.xsd) ([auto-generated pretty-printed documentation](auto-generated pretty-printed documentation)(http://www.commontk.org/docs/html/ctkCmdLineModule.xsd)) that was created retroactively, and not all existing modules strictly follow the spec.  However, one problem is that the schema definition does not facilitate to specify that e.g. the order of author and description elements is irrelevant, so the schema is more strict than the actual implementation in some respects (and less strict in some other).

You are welcome to join the [ctk-developers mailing list](ctk-developers mailing list)(http://www.commontk.org/index.php/Getting_Started#CTK_mailing_list) for discussing related questions.

TODO: The standard (Slicer execution model description) should probably be moved to the CTK domain.

  1. Creating your own CLI modules
There is a ["SlicerExecutionModel"]("SlicerExecutionModel")(https://github.com/Slicer/SlicerExecutionModel) project at GitHub that shall help you with implementing new CLIs, e.g. by offering means to **automatically parse commandline arguments** based on the XML spec.

The Slicer documentation also contains instructions on [how to extend Slicer via CLI modules](how to extend Slicer via CLI modules)(http://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Developers/Modules) or other means.

If you want to implement a Python-based solution, you might also be interested in [the code available on GitHub](the code available on GitHub)(https://github.com/commontk/ctk-cli) and [the Python Package Index](the Python Package Index)(https://pypi.python.org/pypi/ctk-cli) that was developed as part of the [CLI integration in MeVisLab](CLI integration in MeVisLab)(http://www.na-mic.org/Wiki/index.php/2013_Summer_Project_Week:CLI_modules_in_MeVisLab) during the NA-MIC summer project week 2013.

  1. Examples of CLI Modules
Wherever feasible, Slicer developers are encouraged to encapsulate functionality as CLI modules.
- [Source code of Slicer's CLI Modules](Source code of Slicer's CLI Modules)(https://github.com/Slicer/Slicer/tree/master/Modules/CLI)
- Many [Slicer extensions](Slicer extensions)(http://slicer.kitware.com/midas3/slicerappstore?os=winarch=amd64revision=23777category=search=layout=layout) provide command line modules (unfortunately, ATM, it is not possible yet to query only CLI modules, but there are now [auto-generated lists](auto-generated lists)(http://wiki.slicer.org/slicerWiki/index.php/User:UpdateBot/Issue-2843-Consolidated-Extension-List) that can be [filtered by type=cli](filtered by type=cli)(http://wiki.slicer.org/slicerWiki/index.php/User:UpdateBot/Issue-2843-Consolidated-Extension-List/4.4#cli)).
- The [NITRC.org project for 3D Slicer](NITRC.org project for 3D Slicer)(http://www.nitrc.org/projects/slicer) lists associations to software packages that interoperate with Slicer, and many of these consist of one or more CLI modules.
- [niftyreg](niftyreg)(http://sourceforge.net/projects/niftyreg/) contains registration algorithms (from UCL, hosted on SF.net).

