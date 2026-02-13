---
title: Interoperability
---

The Common Toolkit also strives to solve interoperability issues between different toolkits at various levels.

See our [integration levels table](CTK-Integration-Levels-Overview.html) to get an overview how CTK may be used to ease the integration of third-party functionalities as well as your own.

**Currently, CTK offers five levels of interoperability / integration:**

- [DICOM Application Hosting (Part 19)](Documentation/DicomApplicationHosting.html)
: Implements DICOM Part 19 specifications (work in progress)
- [Command Line Interface](Documentation/Command-Line-Interface.html)
: Allows the integration of command line programs and a limited form of communication
- [Event Bus](Documentation/CTK-Plugin-EventAdmin-local.html)
: A OSGi EventAdmin implementation using the CTK Plugin Framework
- [Service Oriented Architectures](Documentation/Plugin-Framework.html)
: Create modular components with a service oriented approach using the CTK Plugin Framework
- Classic C++
: Use the libraries provided by CTK by directly linking to it.