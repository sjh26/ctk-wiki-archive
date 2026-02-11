---
title: Documentation/CLI In Context
render_with_liquid: false
---


This page lists some example and notes on different integration of CLI modules in different frameworks including CTK (see [Documentation/Command_Line_Interface](Documentation/Command_Line_Interface)(Documentation/Command_Line_Interface.md) for a general overview of CLI modules). The first interoperability testing was done during the [third](third)(http://www.creatis.insa-lyon.fr/Interoperability_workshop) VPH NoE Imaging workshop hold in Lyon, France on October 22-23, 2012. It will be continued in consecutive hackfests. The aim is to try to plug in CLI modules in CLI compatible frameworks and come up with possible improvement of the CLI standard, advice to CLI module and CLI framework developers.

  1. Events
- [Hackfest](Hackfest)(CTK)(CTK-Hackfest-Nov-2011.md) in Sophia Antipolis, France in November 2011
** Preliminary work to integrate CLI into GIMIAS
- [Hackfest](Hackfest)(CTK)(CTK-Hackfest-Jul-2012.md) in Boston, USA in July 2012
** Preliminary work to integrate CLI into MITK
- [3rd VPH NoE Imaging workshop](3rd VPH NoE Imaging workshop)(http://www.creatis.insa-lyon.fr/Interoperability_workshop) in Lyon, France on October 22-23, 2012
** [Interoperability tests](Interoperability tests)(First)(#First_Interoperability_tests.md) with CTK, GIMIAS, NiftyView and Slicer
- [Hackfest](Hackfest)(CTK)(CTK-Hackfest-Dec-2012.md) in Bologna, Italy on December, 2012
** Preliminary work to integrate CLI into medInria, MAF3
** Semi-Automatic framework CLI integration tests
- [NA-MIC summer project week](NA-MIC summer project week)(http://www.na-mic.org/Wiki/index.php/2013_Summer_Project_Week)
** [Integration of CLI modules into MeVisLab](Integration of CLI modules into MeVisLab)(http://www.na-mic.org/Wiki/index.php/2013_Summer_Project_Week:CLI_modules_in_MeVisLab)
- [Hackfest](Hackfest)(CTK)(CTK-Hackfest-Nov-2013.md) in London, UK on November, 2013
** [Interoperability tests](Interoperability tests)(Second)(#Second_Interoperability_tests.md): GIMIAS's Command Line Plugins in CTK's Command Line Module Explorer, CTK's Command Line Modules in Taverna Workbench

  1. First Interoperability tests
These first tests mainly concern the integration of niftyreg (registration algorithms from UCL). The different stages of integration are: load, execute and results. Meaning that the CLI module can be loaded. executed and provides the same results as if it was run only from the command line. The problems we encountered were:

- GIMIAS does not support to have a `default` element different that `None` for the output, not sure about the `advanced` option for the `parameters` element 
- niftyreg was using `fileExtensions` with stars (`*.nii`) which is not supported by neither GIMIAS nor Slicer (the star is directly used in the file name)
- The default output folder should be set to the user folder and not the running one, otherwise the CLI module can crash because they were denied access to write in that folder (for example `Program Files` under Windows)
- What to do with CLI modules that have dependencies on shared libraries with the platform but of different versions? Platforms should have the option to only use the libraries shipped with the CLI module
- Platforms should align the way they treat data since if two load data differently, the same CLI module could give different results

It would be interesting to create test CLI modules for these integration tests. For example one that exposes all possible types of options, one running a simple algorithm without any dependencies (as niftyreg) and one with dependencies.

Some thoughts on the tested platforms:
- Niftyview has nice controls on the way CLI modules are found and loaded (control on the `XML` validation)
- Slicer has a nice display of the loaded and non loaded CLI modules (appear in red, there could be more explanation why the loading failed)

Test datasets:

The test datasets [source_2down.nii](source_2down.nii)(https://drive.google.com/file/d/0B3kBRNGHGeP0bGFjZlZNcHJLNEU/edit?usp=sharing) and [target_2down.nii](target_2down.nii)(https://drive.google.com/file/d/0B3kBRNGHGeP0N2gzZTVYV2JTX28/edit?usp=sharing) were obtained from [BrainWeb](BrainWeb)(http://brainweb.bic.mni.mcgill.ca/brainweb) and [ADNI](ADNI)(http://adni.loni.usc.edu/).

Here are the snapshots of niftyreg on the different platforms (collected over many events):

gallery caption="niftyreg on the different platforms" widths="400px" heights="300px" perrow="3"
Image:Niftyreg-ctk.png|CTK command line module explorer 
Image:Niftyreg-slicer.png|3D Slicer
Image:Niftyreg-niftyview.png|NiftyView (based on MITK Workbench)
Image:Niftyreg-gimias.png|GIMIAS
Image:medinria-cli-niftyreg.png|MedInria 
Image:Niftyreg-MeVisLab.png|MeVisLab (see [screencast](screencast)(https://www.youtube.com/watch?v=FSCrmiWEcbA))
Image:Niftyreg-MITK-Workbench.png|MITK Workbench
/gallery

  1. Second Interoperability tests
- GIMIAS's Command Line Plugins in CTK's Command Line Module Explorer

This interoperability test was done under Windows 8. Similar steps can be performed in other platforms.

Typically, GIMIAS's Command Line Plugins (CLPs) are located in folder **GIMIAS_install_dir\commandLinePlugins**. However, the DLL dependencies of these CLPs are located in **GIMIAS_install_dir**. This is a problem when attempting to use GIMIAS's CLPs in CTK's Command Line Module Explorer (CLME), as the CLME will fail to load the CLPs. 

This can be easily solved by copying GIMIAS's CLPs in a different folder, let's say **CLP_folder**, along with its DLL dependencies (for finding out the DLL dependencies of a CLP, a program such as [Dependency Walker](Dependency Walker)(http://dependencywalker.com/) can be used).

After creating **CLP_folder** and copying the necessary files in it. Start CTK's CLME, go to menu "Module" and choose "Options". In "Module Settings" go to "Search Paths", and then add **CLP_folder** to the search paths. Press "OK" and the CLME will scan **CLP_folder** and load the CLPs. 

If the loading process fails, you are probably missing a DLL dependency, close the CLME and go to the cache folder (**user_directory\AppData\Local\CommonTK\CommandLineModuleExplorer\cache** on MS Windows). Clear the content of that directory, add the additional DLL to **CLP_folder** and then start the CLME again.

If a CLP shows up in the list with a warning sign, place the mouse on top of the CLP's name and look at the warning message. Most likely the XML that defines the CLP has a compatibility problem with the CLME, which means that is does not adhere to the [CTK XML Schema](CTK XML Schema)(http://www.commontk.org/docs/html/ctkCmdLineModule.xsd). See the definition of the Schema, correct the XML of the CLP, clear CLME's cache folder as described in the previous paragraph, and start the CLME again.

After following these steps, you will be able to see and use your CLP in the CLME. **This means that you can share your GIMIAS's CLP with any CTK user at any time, by just sharing your CLPs executable file and its DLL dependencies**.

The following image shows GIMIAS's CLPs loaded in CTK's CLME. The "Create a DICOM Series" CLP is selected. The "Settings" dialog is also shown, indicating how to add the CLPs directory to the CLME's search paths. Notice that some CLPs are shown with a warning sign, so their XML definitions has to be corrected.

[400px](400px)(File:GIMIAS_CLPs_on_CTK_CLME.png.md)

- CTK's Command Line Modules in Taverna Workbench

[Taverna Workbench](Taverna Workbench)(http://www.taverna.org.uk/download/workbench/) is an open source Workflow Management System written in Java. GIMIAS's Command Line Plugins (CLPs) can be used in Taverna Workbench for creating medical imaging workflows composed of several filters. In order to be able to do this, the **Center Computational Imaging and Simulation Technologies in Biomedicine (CISTIB)** at the [University of Sheffield](University of Sheffield)(http://www.shef.ac.uk/) has created a Taverna Workbench plugin for GIMIAS.

General instructions on how to install GIMIAS Command-Line Taverna Plugin can be found [here](here)(https://drive.google.com/file/d/0B3kBRNGHGeP0dE53THFMYjdsdDQ/edit?usp=sharing).

In this interoperability test, a CTK Command Line Module was created and tested with GIMIAS Command-Line Taverna Plugin. The sample plugin is called **CopyPlugin**. It is a simple code to open a VTK ASCII file containing a PolyData, and save the contents of the file on another VTK file. The plugin code can be accessed [here](here)(https://drive.google.com/file/d/0B3kBRNGHGeP0bVZVWHZkS1NydnM/edit?usp=sharing).

The result was successful, which means that **GIMIAS's CLPs and CTK's Command Line Modules can be combined to create processing workflows in Taverna Workbench !!**. 

The following image shows the CopyPlugin running on CTK's Command Line Module Explorer.

[400px](400px)(File:COPYPLUGIN_CTK_CLME.png.md)

The CopyPlugin Command Line Module Explorer can also be imported into GIMIAS, see the following image

[400px](400px)(File:COPYPLUGIN_CTK_GIMIAS.png.md)

The following image shows a simple workflow that includes the CopyPlugin, after being imported using GIMIAS Command-Line Taverna Plugin.

[400px](400px)(File:CTL_CLM_TAVERNA.png.md)

GIMIAS's CLPs and CTK's Command Line Modules can be combined into the same Taverna workflow. See the following image where a Marching Cubes GIMIAS's CLP is used along with the CopyPlugin, a CTK Command Line Module.

[400px](400px)(File:GIMIAS_CTK_WORKFLOW.png.md)

