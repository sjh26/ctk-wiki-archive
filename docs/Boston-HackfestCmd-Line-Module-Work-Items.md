---
title: "Boston Hackfest:Cmd Line Module Work Items"
---

1. Boston Hackfest Work Items
      1. First Step
- Improve XSD validation file `{{Done}}`
** Fixup existing Slicer CLI
- Add support for hidden parameters `{{Done}}`
** Suggestion: Just map hidden attribute with "visible" property ?
- Add support for application specific parameters
** Suggestion: via a generic, custom, application, advanced... element ?
- Synchronize between QtGUI and ctkCmdLineModuleDescription `{{Not_Done}}` (invalid)
- Add support to "restore defaults" `{{Done}}`
- Slicer integration ( Julien )
** Use CTK mechanism
** Derive QUILoader for custom qMRMLWidgets initialization (setMRMLScene)
** Customize XSL file

      1. Future work
- Progress Report `{{Done}}`
** Suggestion: Using QFuture
- Rename ctkCmdLineModule* into ctkCommandLineModule* `{{Not_Done}}`
- Command Line XML designer tool
** Left side: XML editor, right side: generated GUI to give immediate feedback from XML