---
title: Documentation/CLI Modules
render_with_liquid: false
---


graphviz
digraph g {
graph [= "LR"
](= "LR"
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
"xmlFile" [= "f0 CLI XML (.xml)| f1"
shape = "record"
](= "f0 CLI XML (.xml)| f1"
shape = "record"
)(
label);
"uiFile" [= "f0 CLI UI (.ui) | f1"
shape = "record"
](= "f0 CLI UI (.ui) | f1"
shape = "record"
)(
label);
"gui" [= "f0 Qt GUI | f1"
shape = "record"
](= "f0 Qt GUI | f1"
shape = "record"
)(
label);
"ctkCLIModuleDescription" [= "f0 ctkCLIModuleDescription| f1"
shape = "record"
](= "f0 ctkCLIModuleDescription| f1"
shape = "record"
)(
label);
"vtkMRMLParametersNode" [= "f0 vtkMRMLParametersNode| f1"
shape = "record"
](= "f0 vtkMRMLParametersNode| f1"
shape = "record"
)(
label);
"xmlFile":f1 - "uiFile":f0 [= 0
](= 0
)(
id);
"xmlFile":f1 - "ctkCLIModuleDescription":f0 [= 1
](= 1
)(
id);
"xmlFile":f1 - "vtkMRMLParametersNode":f0 [= 2
](= 2
)(
id);
"uiFile":f1 - "gui":f0 [= 3
](= 3
)(
id);
"gui":f1 - "ctkCLIModuleDescription":f1 [= 4
](= 4
)(
id);
"ctkCLIModuleDescription":f1 - "vtkMRMLParametersNode":f1 [= 5
](= 5
)(
id);
}

