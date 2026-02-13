---
title: CTK DICOM Web Services
---

- Investigate web service approach (WG27)
** Pros: Easily go accross firewall, leverage caching from commercial app
** Approach:
*** Improve DCMTK
*** Kick the tires of the dcm4che implementation

  1. Useful links
Presentation: ["Image Access Everywhere, DICOM Web Services"](http://medical.nema.org/dicom/CP/Conference-2013/Presentations/Post-Conf-Day-1/D1-0935F-Philbin-by-Tarbox-Image%20Access%20Everywhere.pptx) James F Philbin

dcm4che: [Version 4.1.0.Alpha3 (and above) ](http://sourceforge.net/projects/dcm4che/files/dcm4chee-arc4/4.1.0.Alpha3/)

  1. DICOM Supplements
[DICOM Part 18: Web Access to DICOM Persistent Objects (WADO)](http://medical.nema.org/Dicom/2011/11_18pu.pdf)

[ftp://medical.nema.org/medical/dicom/final/sup161_ft.pdf Web Access to DICOM Persistent Objects by RESTful Services (WADO-RS); supplement 161]

[ftp://medical.nema.org/medical/dicom/Final/sup163_ft3.pdf Store Over the Web by RESTful Services (STOW-RS); supplement 163]

[ftp://medical.nema.org/medical/dicom/final/sup166_ft5.pdf Query based on ID for DICOM Objects by RESTful Services (QIDO-RS); supplement 166]

[ftp://medical.nema.org/medical/dicom/supps/PC/sup170_pc.pdf Server Options RESTful Services; supplement 170 (pc)]

Not directly related is [ftp://medical.nema.org/medical/dicom/final/sup157_ft2.pdf Supplement 157, "Multi-Frame Converted Legacy Images"] , which is a more convenient way of handling large stacks of planar images (i.e. convert multiple single-slice images into a single multi-dimensional image).