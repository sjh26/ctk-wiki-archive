---
title: "Documentation/DicomApplicationHosting:DataExchangeDevelopment"
render_with_liquid: false
---


1. DICOM Specifications uncertainties
First the implementation showed some dark areas on how to stick to the official definition. These comments have been (or will be very soon) forwarded to Lawrence Tarbox for advice and correction.
- Some inconsistencies in the naming of parameters and functions (capitalization mostly). But these are benign, they just need polishing on an updated version.
- It is not always clear in the definition that some data are a *ArrayOf[Type](Type)*. For instance, section 9.2, definition of the AvailableData type lists these parameters:
** *ObjectDescriptors�:�ObjectDescriptor[]��An�array�of�ObjectDescriptor�data�structures [...](...)*�
** *Patients�:�Patient[]��An�array�of�Patient�data�structures*.
Replacing the term *ArrayOfPatients* by Patient[] leads to confusion as what is an array, and does one need to wrap arrays with this *ArrayOf[Type](Type)* wording.
- *ArrayOf[Type](Type)* has been very obscure to us. Especially since we had poor notions of WSDL notations we can't really challenge this notation, and the w3c definition creates a gray area http://www.w3.org/TR/wsdl#_wsdl :
cite
Array types should extend the Array type defined in the SOAP v1.1 encoding schema (http://schemas.xmlsoap.org/soap/encoding/) (regardless of whether the resulting form actually uses the encoding specified in Section 5 of the SOAP v1.1 document). Use the name ArrayOfXXX for array types (where XXX is the type of the items in the array).  The type of the items in the array and the array dimensions are specified by using a default value for the soapenc:arrayType attribute.  At the time of this writing, the XSD specification does not have a mechanism for specifying the default value of an attribute which contains a QName value.  To overcome this limitation, WSDL introduces the arrayType  attribute (from namespace http://schemas.xmlsoap.org/wsdl/) which has the semantic of providing the default value.  If XSD is revised to support this functionality, the revised mechanism SHOULD be used in favor of the arrayType attribute defined by WSDL.
/cite

- Why do the example schemas in appendices of the specifications use the microsoft schemas and not the official W3C WSDL schemas?

Have a look at the QtSoap limitations to see an illustration of the doubts there still are on this Array issue.

  1. Outstanding features
- No model exchange yet. That is not planned until we get the simple data exchange right.
- Only the back end (both client and server)has been worked on, the actual example server and client don't feature data exchange yet.
- the only outstanding function is **releaseData**.


  1. Dirty hacks and unpolished methods
Due to speed of coding and the impatience to see something come out of the specifications some corners have been cut.
- Worst of all: there is a non uniform use of statically and dynamically allocated memory in the data binding helper classes. As a result it's not always clear who is responsible for handling the memory. This should be the first place to look at if someone is thinking of doing an example implementation of the data exchange specs. If there are segmentation faults, they come from there, most likely.

- Most of the inconsistencies in naming have been corrected by Sasha on the 20th of September, but some may still lurk somewhere, don't be afraid to check them.



    1. QtSoap limitations
- There is no constructor nor accessor for *long* simple types in QtSoap, only *int*s are covered. For the sake of quick implementation and early testing ObjectLocator.length and ObjectLocator.offset have been casted to *int* at Soap-C++ translation time. If someone knows how to transfer Soap long object with QtSoap, please give us a hand.
- Ok, not sure about this one: QtSoapArrays are constructed using the *arrayType* attribute from supposedly http://schemas.xmlsoap.org/wsdl/. But it restricts the possible types to a few set, plus *QtSoapType::Other*. This may not be compatible with the *ArrayOf[Type](Type)* way of writing arrays. Extended testing with other implementations should be pursued to get this right.

