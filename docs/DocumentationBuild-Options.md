---
title: Documentation/Build Options
render_with_liquid: false
---


1. Semantic grouping
- DICOM
- DICOMApplicationHosting
- Widgets
- PluginFramework

1. Options
- CTK_ENABLE_DICOM
- CTK_ENABLE_DICOMApplicationHosting
- CTK_ENABLE_Widgets
- CTK_ENABLE_PluginFramework
- CTK_ENABLE_EXAMPLES
- CTK_ENABLE_PYTHON_WRAPPING


pre
set(CTK_LIBS
  Core:ON
  PluginFramework:OFF  ..........- CTK_ENABLE_PluginFramework
  Widgets:OFF   ................ - CTK_ENABLE_Widgets (or CTK_ENABLE_DICOM or (CTK_ENABLE_DICOMApplicationHosting and CTK_ENABLE_EXAMPLES))
  DICOM/Core:OFF   ............. - CTK_ENABLE_DICOM or CTK_ENABLE_DICOMApplicationHosting
  DICOM/Widgets:OFF    ......... - CTK_ENABLE_DICOM or CTK_ENABLE_DICOMApplicationHosting
  ImageProcessing/ITK/Core:OFF   - NA
  Scripting/Python/Core:OFF .... - CTK_ENABLE_PYTHON_WRAPPING
  Scripting/Python/Widgets:OFF . - CTK_ENABLE_PYTHON_WRAPPING and CTK_ENABLE_Widgets
  Visualization/VTK/Core:OFF     - NA
  Visualization/VTK/Widgets:OFF  - NA
  )
/pre

pre
set(CTK_PLUGINS
  org.commontk.eventbus:OFF     - NA
  org.commontk.configadmin:OFF  - NA
  org.commontk.eventadmin:OFF   - NA 
  org.commontk.log:OFF          - NA
  org.commontk.log4qt:OFF       - NA
  org.commontk.metatype:OFF     - NA

  # Plug-ins related to DICOM WG23 (Application Hosting)
  org.commontk.dah.core:OFF        - CTK_ENABLE_DicomApplicationHosting
  org.commontk.dah.app:OFF         - CTK_ENABLE_DicomApplicationHosting
  org.commontk.dah.host:OFF        - CTK_ENABLE_DicomApplicationHosting
  org.commontk.dah.exampleapp:OFF  - CTK_ENABLE_DicomApplicationHosting and CTK_ENABLE_EXAMPLES
  org.commontk.dah.examplehost:OFF - CTK_ENABLE_DicomApplicationHosting and CTK_ENABLE_EXAMPLES

  # Misc
  org.commontk.plugingenerator.core:OFF - NA
  org.commontk.plugingenerator.ui:OFF   - NA
  org.commontk.slicermodule:OFF         - NA
  )
/pre

pre
set(CTK_APPLICATIONS
  ctkDICOM:OFF              - CTK_ENABLE_DICOM and CTK_ENABLE_EXAMPLES
  ctkDICOMIndexer:OFF       - CTK_ENABLE_DICOM and CTK_ENABLE_EXAMPLES
  ctkDICOMDemoSCU:OFF       - CTK_ENABLE_DICOM and CTK_ENABLE_EXAMPLES
  ctkDICOMQuery:OFF         - CTK_ENABLE_DICOM and CTK_ENABLE_EXAMPLES
  ctkDICOMRetrieve:OFF      - CTK_ENABLE_DICOM and CTK_ENABLE_EXAMPLES
  ctkDICOMQueryRetrieve:OFF - CTK_ENABLE_DICOM and CTK_ENABLE_EXAMPLES
  ctkExampleHost:OFF        - CTK_ENABLE_DicomApplicationHosting and CTK_ENABLE_EXAMPLES
  ctkExampleHostedApp:OFF   - CTK_ENABLE_DicomApplicationHosting and CTK_ENABLE_EXAMPLES
  ctkEventBusDemo:OFF       - NA
  ctkPluginBrowser:OFF      - CTK_ENABLE_PluginFramework and CTK_ENABLE_EXAMPLES
  ctkPluginGenerator:OFF    - CTK_ENABLE_PluginFramework and CTK_ENABLE_EXAMPLES
  ctkDICOMObjectViewer:OFF  - CTK_ENABLE_Dicom and CTK_ENABLE_EXAMPLES
  ctkSimplePythonShell:OFF  - CTK_ENABLE_PYTHON_WRAPPING and CTK_ENABLE_EXAMPLES
  )
/pre

