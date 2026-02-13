---
title: DICOM de-identification tool overview
---

1. Specific use cases and requirements for de-identification
    1. Requirements
- Client side processing
- Offline processing
- Platform and browser independent
- Provided as commandline tool?
- In-application processing should be possible?
** e.g. in MITK and Slicer?
- Specify conditions like if tag value is equal to XYZ then remove all private tags except of tag list

Some issues, which anonymization tools often have, found on the [Plastimatch homepage](http://plastimatch.org/dicom_comparison.html), also providing a comparison:

- Some date fields cannot be changed (duh)
- It is not possible to preserve relative dates (for example, we would like to set StudyDate to Jan 1, 2000, but preserve the fact that StructureSetDate occurred 35 days later)
- Private tags are always deleted (on our GE scanner, these contain important acquisition details)
- Comments, diagnosis descriptions, or other fields cannot be reset (may contain protected information)
- It is not possible to modify strings (for example, the physician might type smith-final into the StructureSetName field, and we would like to delete smith but preserve final )
- UIDs are not changed, or relationships between UIDs are not preserved (duh)

    1. Usecases
- ## Available tools for DICOM de-identification
{| class="wikitable"
! Toolname
! Language
! Available as cmd line?
! Features
! URL
|-
| Clinical Trial Processor
| Java
|
| 
| http://mircwiki.rsna.org/index.php?title=CTP-The_RSNA_Clinical_Trial_Processor
|-
| DICOM Cleaner
| Java
| 
|
| http://www.dclunie.com/pixelmed/software/webstart/DicomCleanerUsage.html
|-
| DICOM Confidential
| Java
|
| 
| http://sourceforge.net/projects/privacyguard/
|-
| DICOM Browser
| Java
| [Yes](http://nrg.wustl.edu/software/dicom-browser/instructions/batch-anonymizations/)
| Script based processing: Assignment / Deletion / Constraint and condition based / Built-in functions / Generators / user defined variables
| http://nrg.wustl.edu/software/dicom-browser/
|-
| GDCM Anon
| C++
| Yes
|
| http://gdcm.sourceforge.net/html/gdcmanon.html
|-
| DCMTK
| C++
|
| 
| 
|-
| DICOM anon
| Python
| Yes
| 
| https://github.com/cbmi/dicom-anon
|-
|}