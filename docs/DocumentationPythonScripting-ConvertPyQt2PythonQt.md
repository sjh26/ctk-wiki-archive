---
title: Documentation/PythonScripting ConvertPyQt2PythonQt
render_with_liquid: false
---


This document aims at describing which steps are required to migrate PyQt code to PythonQt.

As an example, we will consider the implementation of PythonQt matplotlib backend.

- PyQt should be changed into PythonQt

- QDialog.exec() method isn't available in PythonQt. Use QDialog.open() as a workaround

- QFontDatabase is not available. There is workaround

- There are no equivalent for pyqtSignature, pyqtProperty

- QString is not available. Python string are mapped with QString.

