---
title: Documentation/CLI Modules
---

graphviz
digraph g {
graph [
rankdir = "LR"
];
node [
fontsize = "16"
shape = "ellipse"
];
edge [
];
"xmlFile" [
label = "f0 CLI XML (.xml)| f1"
shape = "record"
];
"uiFile" [
label = "f0 CLI UI (.ui) | f1"
shape = "record"
];
"gui" [
label = "f0 Qt GUI | f1"
shape = "record"
];
"ctkCLIModuleDescription" [
label = "f0 ctkCLIModuleDescription| f1"
shape = "record"
];
"vtkMRMLParametersNode" [
label = "f0 vtkMRMLParametersNode| f1"
shape = "record"
];
"xmlFile":f1 - "uiFile":f0 [
id = 0
];
"xmlFile":f1 - "ctkCLIModuleDescription":f0 [
id = 1
];
"xmlFile":f1 - "vtkMRMLParametersNode":f0 [
id = 2
];
"uiFile":f1 - "gui":f0 [
id = 3
];
"gui":f1 - "ctkCLIModuleDescription":f1 [
id = 4
];
"ctkCLIModuleDescription":f1 - "vtkMRMLParametersNode":f1 [
id = 5
];
}