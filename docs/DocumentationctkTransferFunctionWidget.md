---
title: Documentation/ctkTransferFunctionWidget
---

1. ctkTransferFunctionWidget
*Support for VTK functions
Note: The development of the widgets using Qt only has been stopped. We are now orienting the drawing/interaction using VTK Charts. 
**vtkColorTransferFunction
**vtkLookupTable
**vtkPiecewiseFunction
{|
|[thumb|400px|ctkVTKColorTransferFunction](thumb|400px|ctkVTKColorTransferFunction)(File:CtkTransferFunctionWidget.png.md)
|[thumb|400px|ctkVTKLookupTable](thumb|400px|ctkVTKLookupTable)(File:CtkVTKLookupTable.png.md)
|--
|[thumb|400px|ctkVTKPiecewiseFunction](thumb|400px|ctkVTKPiecewiseFunction)(File:CtkVTKPiecewiseFunction.png.md)
|[thumb|400px|ctkVTKCompositeFunction](thumb|400px|ctkVTKCompositeFunction)(File:CtkVTKCompositeFunction.png.md)
|--
|[thumb|400px|ctkTransferFunctionHistogramItem](thumb|400px|ctkTransferFunctionHistogramItem)(File:CtkTransferFunctionHistogramItem.png.md)
|}
*Features
** Move points
** Add points

*To do List
** Limits - First and last point behaviour option: clamping, extrapolate, to 0, ...
** Background item
*** View color background (white for the moment)
** Should each point be a different item..?
** Widget items editor
**** Change sharpness, midpoint, color, opacity
** Preset shapes (bell, ...)
** Possibility to drag item
*** scaling and offsetting items
** support histograms (from vtkData)
** add bar graphic item
** remove items feature
** improve items moves
** vertical gradient