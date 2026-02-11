---
title: Documentation/Widget testing
render_with_liquid: false
---

1. Overview
Testing of both CTK widgets and application built on top of CTK could leverage the capabilities offered by the [QtTesting library](QtTesting library)(http://www.paraview.org/Wiki/Testing_design) developed by [Paraview](Paraview)(http://www.paraview.org) folks.

br /
**How added the testing framework to CTK :**
- Turn the variable *CTK_USE_QTTESTING* into *ON*.
br /
**If the option **CTK_USE_QTTESTING** is enabled, the build system will :**
1. Download external project QtTesting
1. Compile the CTKQtTesting Library
#* Including the class :
#***ctkEventTranslaterPlayerWidget* : Widget used by the Unit Test - [Image](Image)(http://www.commontk.org/index.php/File:CtkEventTranslatorPlayerWidget.png)
#***ctkQtTestingUtility* : Class used by the application - inherits from pqTestUtility
#***ctkXMLEventObserver* : Recover the Event and write the .xml file.
#***ctkXMLEventSource* : Read the .xml file and create the events.
1. For CTKWidget - CTKVisualizationWidget - CTKCoreWidget :
#* Include the event translator and player required for custom widgets. (Located in the same folder as their associated widget sources)
1. If **BUILD_TESTING** is enabled: widgets EventTranslatorTests will be compiled.
#**These tests will use *ctkEventTranslaterPlayerWidget* and ensure that events associated with widgets can be properly recorded and played.*
br /
**{{note}}** br /
Option **CTK_USE_QTTESTING** will be automatically enabled if **BUILD_TESTING** is ON

1. Adding the testing framework into your application
Adding the testing framework will allow users to recover script, but also a easy way to create tutorial or to test all the widget.br /
You can see the application exemple created in CTK to have an exemple:

    1. How
Follow these steps to add this testing framework to your application.
1. Create a variable ctkQtTestingUtiliy - can be added to your mainWindow class.
#* And initialize this variable as following :
pre
this-TestUtility = new ctkQtTestingUtility(this);
this-TestUtility-addEventObserver("xml", new ctkXMLEventObserver(this));
this-TestUtility-addEventSource("xml", new ctkXMLEventSource(this));/pre
{{Note}} You can have your own *EventObserver* and *EventSource*
1. Create a button Record, and link it to the ctkQtTestUtility slot *record*
1. Create a button Play, and link it to the ctkQtTestingUtility slot *play*
pre
QObject::connect(Ui.RecordButton, SIGNAL(clicked(bool)), this, SLOT(record()));
QObject::connect(Ui.PlayBackButton, SIGNAL(clicked(bool)), this, SLOT(play()));
/pre

    1. Limits
Note that there are still severals limits to this testing framework :
1. The ctkVTKRenderView had to have the same size between the record and the playback.
#* To solve the issue, ctkTestingUtility record all the application property - size, state, font ... - and before a playback, if these property are differents, ask the user if he wants to load the settings.br /{{Note}} We are working on this limit to find a better solution.
1. All the CTK Widgets are not yet tested - Below the [summary table](summary table)(http://www.commontk.org/index.php/Documentation/Widget_testing#Player.2FTranslators_Widget_Testing) -

1. Issues found on QtTesting
*** QSpinBox/QDoubleSpinBox :** 
** A long click on the up/down arrow - just one click even if the value change severals times. 
** Fast click - Double click - no effect.
** clik on the up/down arrow just after editing the spin Box - no effect.
*Solve : Contribut to the QtTesting by modified the pqSpinBoxEventTranslator* {{Doing}} br/
Here the link to my Github for the [QSpinBox](QSpinBox)(https://github.com/benjaminlong/QtTesting/tree/88-IssueQSpinBox)br/
Here the link to my Github for the [QDoublSpinBox](QDoublSpinBox)(https://github.com/benjaminlong/QtTesting/tree/88-IssueQDoubleSpinBox)


*** In pq3DView :**
** The scroll button has no effect - Implemented for ctk.
** Shift between the current/Expected image.
*Solve : new Implementation with the ctkVTKRenderViewEventTranslator and the ctkVTKRenderViewEventPlayer :* {{Done}}
1. *Change the normalization into a normalization by the widget center.*
1. *Implemented the scroll action*
1. *Add a better rounded when we cast from double to int to not have shift issue.*


*** QComboBox when it is editable :**
** The hight-event "set_sting" crash if we edit the comboBox. 
*** ***Exemple :** If we have an item "foo", we are going to edit the comboBox with "f", but the item "f" doesn't exist, and the player will crash.*
*Solve : ...* {{Not Done}}

1. Building
    1. Milestones
1. Integrate QtTesting has an external projects {{Done}}
1. Add unit test to all the widget - Below, the [summuray table](summuray table)(http://www.commontk.org/index.php/Documentation/Widget_testing#Player.2FTranslators_Widget_Testing) -
  1. Implement *ctkEventTranslaterPlayerWidget* {{Done}}
  1. Create custom translator/player if needed {{Doing}}
  1. Implement widgets EventTranslatorTests {{Doing}}
1. Create an Application test - [ctkQtTesting](ctkQtTesting)(http://www.commontk.org/index.php/File:CtkQtTestingScreenShot.png) - {{Done}}

    1. Player/Translators Widget Testing
Summury table, to know each widgets' state.br /
The state can be *Done* : {{Done}} , *Done with QtTesting issue* : {{Done}}{{Doing}} , *in progress* : {{Doing}} , or *without unit test*: {{Not Done}}.

{| class="wikitable alternance" style="text-align:left; width:100%; border:1px solid black;"
|-  valign=top
| style="width:50%;" |
{|class="wikitable alternance" style="text-align:left; width:100%; border:1px solid black;"
|+ ***CTKWidgets***
|-
! scope=col style="background:#cde6f8;"| Widgets
! scope=col style="background:#cde6f8;"| State
! scope=col style="background:#cde6f8;"| Priority
! scope=col style="background:#cde6f8;"| Notes
|-
|ctkActionsWidget
|{{Done}}
|
|
|-
|ctkAddRemoveComboBox
|{{Done}}
|
|
|-
|ctkAxesWidget
|{{Done}}
|
|*Translator/player implemented*
|-
|ctkBasePopupWidget
|NA
|
|*ctkPopupWidget inherit of it. See ctkPopupWidget*
|-
|ctkButtonGroup 
|{{Done}}
|
|
|-
|ctkCheckableComboBox
|{{Done}}
|
|
|-
|ctkCheckableHeaderView
|{{Done}}
|
|
|-
|ctkCheckBoxPixmaps
|{{Not Done}}
|
|*Not used in Slicer*
|-
|ctkCheckablePushButton
|{{Done}}
|
|*Not used in Slicer*
|-
|ctkComboBox
|{{Done}}
|
|
|-
|ctkCompleter
|NA
|
|
|-
|ctkCollapsibleButton
|{{Done}}
|
|
|-
|ctkCollapsibleGroupBox
|{{Done}}
|
|
|-
|ctkColorDialog
|{{Done}}
|
|
|-
|ctkColorPickerButton
|{{Done}}
|
|
|-
|ctkConsole
|{{Done}}
|
|*May have a problem with the command*
|-
|ctkConfirmExitDialog
|{{Not Done}}
|
|
|-
|ctkCoordinatesWidget
|{{Done}}
|
|
|-
|ctkCrosshairLabel
|{{Not Done}}
|
|
|-
|ctkDateRangeWidget
|{{Not Done}}
|
|*Problem with QDateTimer* 
|-
|ctkDirectoryButton
|{{Done}} - TO VERIFY
|
| bgcolor="f4db9e" |*Value OK but no dialog*
|-
|ctkDoubleRangeSlider
|{{Done}}
|
|
|-
|ctkDoubleSlider
|{{Done}}
|
|
|-
|ctkDynamicSpacer
|NA
|
|
|-
|ctkErrorLogStatusMessageHandler
|NA
|
|*Not a Widget*
|-
|ctkErrorLogWidget
|{{Not Done}}
|
|
|-
|ctkExpandButton
|{{Done}}
|
|
|-
|ctkFileDialog
|{{Done}}
|
|
|-
|ctkFittedTextBrowser
|NA
|
|*This widget just display text.*
|-
|ctkFlowLayout
|NA
|
|*Layout are not tested through the event translator/player mechanism*
|-
|ctkFontButton
|{{Done}}
|
|
|-
|ctkIconEnginePlugin
|NA
|
|*Plugin are not tested through the event translator/player mechanism*
|-
|ctkLayoutManager
|NA
|
|
|-
|ctkMaterialPropertyPreviewLabel
|NA
|
|
|-
|ctkMaterialPropertyWidget
|{{Done}}
|
|
|-
|ctkMatrixWidget
|{{Done}}
|
| * no visuel effects *
|-
|ctkMenuButton
|{{Not Done}}
|
|''Use in Slicer ?
|-
|ctkMenuComboBox
|{{Done}}
|
| bgcolor="#efabab" |'' Developer should make sure menus have a parent. See https://bugreports.qt.nokia.com/browse/QTBUG-20929
|-
|ctkModalityWidget
|{{Done}}
|
|
|-
|ctkPathLineEdit
|{{Done}}
|
| bgcolor="#efabab" |* Note that the first time the listview is displayed, it will show on the top left corner of the screen.*
|-
|ctkPixmapIconEngine
|NA
|
|
|-
|ctkPopupWidget
|{{Done}}
|
|
|-
|ctkQImageView
|NA
|
|
|-
|ctkRangeSlider
|{{Done}}
|
|
|-
|ctkRangeWidget
|{{Done}}
|
|
|-
|ctkScreenshotDialog
|{{Not Done}}
|
|
|-
|ctkSearchBox
|{{Done}}
|
|
|-
|ctkSettings
|NA
|
|
|-
|ctkSettingsDialog
|{{Done}}
|
|
|-
|ctkSettingsPanel
|{{Done}}
|
|*See ctkSettingsDialog*
|-
|ctkSignalMapper
|NA
|
|*This object is not a widget and doesn't have to be tested through the event translator/player mechanism*
|-
|ctkSimpleLayoutManager
|NA
|
|
|-
|ctkSliderWidget
|{{Doing}}
|
|**Translator and player if popup**
|-
|ctkTestApplication
|NA
|
|*This is a utility class. Shouldn't be tested using the event translator/player mechanism*
|-
|ctkThumbnailListWidget
|{{Not Done}}
|
|
|-
|ctkThumbnailWidget
|{{Not Done}}
|
|
|-
|ctkToolTipTrapper
|NA
|
|*This is a utility class. Shouldn't be tested using the event translator/player mechanism*
|-
|ctkTransferFunctionBarsItem
|{{Not Done}}
|
|
|-
|ctkTransferFunctionControlPointsItem
|{{Not Done}}
|
|
|-
|ctkTransferFunctionGradientItem
|{{Not Done}}
|
|
|-
|ctkTransferFunctionItem
|{{Not Done}}
|
|
|-
|ctkTransferFunctionScene
|{{Not Done}}
|
|
|-
|ctkTransferFunctionView
|{{Not Done}}
|
|
|-
|ctkTreeComboBox
|{{Done}}
|
| **Note: This won't work if there multiple items with a similar name. This is not an issue in Slicer since selection is based on string**
|-
|ctkWidgetsUtils
|NA
|
|*This is a utility class. Shouldn't be tested using the event translator/player mechanism*
|-
|ctkWorkflowAbstractPagedWidget
|{{Not Done}}
|
|
|-
|ctkWorkflowButtonBoxWidget
|{{Not Done}}
|
|
|-
|ctkWorkflowGroupBox
|{{Not Done}}
|
|
|-
|ctkWorkflowStackedWidget
|{{Not Done}}
|
|
|-
|ctkWorkflowTabWidget
|{{Not Done}}
|
|
|-
|ctkWorkflowWidget
|{{Not Done}}
|
|
|-
|ctkWorkflowWidgetStep
|{{Not Done}}
|
|
|}
| style="width:50%; "text-align: center; " |
{| class="wikitable alternance" style="text-align:left; width:100%; border:1px solid black;"
|+ ***CTKVisualizationVTKWidgets***
|-
! scope=col style="background:#cde6f8;"| Widgets
! scope=col style="background:#cde6f8;"| State
! scope=col style="background:#cde6f8;"| Priority
! scope=col style="background:#cde6f8;"| Notes
|-
|ctkVTKAbstractMatrixWidget
|{{Done}}
|
|*See ctkVTKMatrixWidget*
|-
|ctkVTKAbstractView
|{{Done}}
|
|*See ctkVTKRenderView*
|-
|ctkVTKChartView
|{{Not Done}}
|
|
|-
|ctkVTKDataSetArrayComboBox
|{{Done}}
|
|
|-
|ctkVTKDataSetModel
|{{Done}}
|
|
|-
|ctkVTKMagnifyView
|{{Not Done}}
|
| *Not used in Slicer*
|-
|ctkVTKMatrixWidget
|{{Done}}
|
| *See ctkVTKMatrixWidget - There is no need for specific translator  player*
|-
|ctkVTKRenderView
|{{Done}}
|
| bgcolor="#f4db9e" | ''Translator/Player implemented br / What we want :br / - Wheel event {{Done}} br / - Better normalization {{Done}} br / - Not working if the renderView has a different size
|-
|ctkVTKScalarBarWidget
|{{Done}}{{Doing}}
|
|bgcolor="#f4db9e" |*QSpinBox issue + key "."(pad) on the line edit*
|-
|ctkVTKScalarsToColorsUtils
|{{Not Done}}
|
|
|-
|ctkVTKScalarsToColorsView
|{{Not Done}}
|
|
|-
|ctkVTKScalarsToColorsWidget
|{{Not Done}}
|
|
|-
|ctkVTKSliceView
|{{Done}}
|
|*Since it's based on QVTKWidget - See ctkVTKRenderView translator  player*
|-
|ctkVTKSurfaceMaterialPropertyWidget
|{{Doing}}
|
|
|-
|ctkVTKTextPropertyWidget
|{{Done}}
|
|
|-
|ctkVTKThresholdWidget
|{{Not Done}}
|
|
|-
|ctkVTKThumbnailView
|{{Not Done}}
|
|
|-
|ctkVTKVolumePropertyWidget
|{{Doing}}
|
|
|-
|ctkVTKWidgetsUtils
|NA
|
|
|}
{| class="wikitable alternance" style="text-align:left; width:100%; border:1px solid black;"
|+ ***CTKDICOMWidgets***
|-
! scope=col style="background:#cde6f8;"| Widgets
! scope=col style="background:#cde6f8;"| State
! scope=col style="background:#cde6f8;"| Priority
! scope=col style="background:#cde6f8;"| Notes
|-
|ctkDICOMAppWidget
|{{Not Done}}
|
|
|-
|ctkDICOMDatasetView
|{{Not Done}}
|
|
|-
|ctkDICOMDirectoryListWidget
|{{Not Done}}
|
|
|-
|ctkDICOMImage
|{{Not Done}}
|
|
|-
|ctkDICOMImportWidget
|{{Not Done}}
|
|
|-
|ctkDICOMItemTreeModel
|{{Not Done}}
|
|
|-
|ctkDICOMListenerWidget
|{{Not Done}}
|
|
|-
|ctkDICOMQueryResultsTabWidget
|{{Not Done}}
|
|
|-
|ctkDICOMQueryRetrieveWidget
|{{Not Done}}
|
|
|-
|ctkDICOMQueryWidget
|{{Not Done}}
|
|
|-
|ctkDICOMServerNodeWidget
|{{Not Done}}
|
|
|-
|ctkDICOMThumbnailGenerator
|{{Not Done}}
|
|
|-
|ctkDICOMThumbnailListWidget
|{{Not Done}}
|
|
|}
{| class="wikitable alternance" style="text-align:left; width:100%; border:1px solid black;"
|+ ***qMRMLWidgets***
|-
! scope=col style="background:#cde6f8;"| Widgets
! scope=col style="background:#cde6f8;"| State
! scope=col style="background:#cde6f8;"| Priority
! scope=col style="background:#cde6f8;"| Notes
|-
|qMRMLCaptureToolBar
|{{Doing}}
|
|
|-
|qMRMLCheckableNodeComboBox
|{{Done}}
|
|
|-
|qMRMLClipNodeWidget
|{{Done}}
|
|
|-
|qMRMLCollapsibleButton
|{{Done}}
|
|
|-
|qMRMLColorListView
|{{Done}}
|
|
|-
|qMRMLColorPickerWidget
|{{Doing}}
|
|
|-
|qMRMLColorTableComboBox
|{{Done}}
|
|
|-
|qMRMLColorTableView
|{{Done}}
|
|
|-
|qMRMLDisplayNodeWidget
|{{Done}}
|
|
|-
|qMRMLEventBrokerWidget
|{{Done}}
|
|
|-
|qMRMLLabelComboBox
|{{Done}}
|
|
|-
|qMRMLLayoutWidget
|{{Doing}}
|
|
|-
|qMRMLLinearTransformSlider
|{{Done}}
|
|
|-
|qMRMLListWidget
|{{Done}}
|
|
|-
|qMRMLMatrixWidget
|{{Done}}
|
|
|-
|qMRMLNavigationView
|{{Done}}
|
|
|-
|qMRMLNodeComboBox
|{{Done}}
|
|
|-
|qMRMLRangeWidget
|{{Done}}
|
|
|-
|qMRMLROIWidget
|{{Done}}
|
|
|-
|qMRMLScalarInvariantComboBox
|{{Done}}
|
|
|-
|qMRMLSceneFactoryWidget
|{{Done}}
|
|
|-
|qMRMLSceneViewMenu
|{{Done}}
|
|
|-
|qMRMLScreenShotDialog
|{{Done}}
|
|
|-
|qMRMLSliceControllerWidget
|{{Doing}}
|
|
|-
|qMRMLSliceWidget
|{{Doing}}
|
|
|-
|qMRMLThreeDViewControllerWidget
|{{Done}}
|
|
|-
|qMRMLThreeDView
|{{Doing}}
|
|
|-
|qMRMLThreeDWidget
|{{Doing}}
|
|
|-
|qMRMLTransformSliders
|NA
|
|
|-
|qMRMLTreeView
|{{Doing}}
|
|
|-
|qMRMLVolumeInfoWidget
|{{Done}}
|
|
|-
|qMRMLVolumeThresholdWidget
|{{Done}}
|
|
|-
|qMRMLWindowLevelWidget
|{{Doing}}
|
|
|}
|}

1. Screenshots
gallery widths=300 px heights=200px perrow=3
Image:CtkQtTestingScreenShot.png|Simple application with recording / playing Qt testing capabilities
Image:CtkEventTranslatorPlayerWidget.png|Little exemple of the widget testing 
/gallery