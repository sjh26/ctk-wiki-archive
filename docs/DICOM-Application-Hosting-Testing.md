---
title: DICOM Application Hosting Testing
render_with_liquid: false
---


1. SOAP API Testing
This sections on SOAP API Testing summarizes experiences gathered at the [in Sophia Antipolis](in Sophia Antipolis)(hackfest)(CTK-Hackfest-Nov-2011.md) in November 2011.

    1. High - level test suites
That's what I can see so far:

- WSDL compliance: Test if the host and app accept the official method signatures
- Functional testing: Test the "logic" of the host and app (proper state transitions, correct notification messages, etc.)

    1. Possible solutions
- Use [SoapUI](SoapUI)(http://www.soapui.org/) and its command line support to integrate it with ctest.
** Automatically generate tests for WSDL compliance using the official WSDL file
** Create manual functional tests within the SoapUI GUI and put the project file in the CTK git repository

      1. SoapUI
**Requires**

- Either host the SoapUI executable somewhere or look for it if testing is enabled
- Java Runtime on the test system
- Some CMake magic

**Pros** 

- Rely on proven Java libraries to generate the RPC stuff and mock classes for server and client code from the WSDL file.
- No C++ involved, create test cases in the GUI
- No programming knowledge required to add or modify tests

      1. SoapUI Experiences
Just some pieces of information we (Michael C.) gathered during the Sophia-Antipolis Hackfest

- The soapUI project files are located under the dah-testing-soapui branch. I have put two xml files there: HostService-SoapUI.xml and Application-SoapUI.xml under Plugins\org.commontk.dah.core\Resources that correspond to the SoapUI projects and that needs to be imported in SoapUI.
- I have changed the enpoint that we use normally in the examples. (This is under the tab Service Enpoints when you double click on your project). I have tried for example to send a cancel request to the HostedApp plugin by simulating some requests from the hosting system. I received a notification that a message was received on the HostedApp but i didn't get the answer of my request: I am probably missing something in the way I set the endpoints...
- I recommend to use the trial version of SoapUI if you are willing to do some tests. The editing of your soap message  is much simpler in the pro version.

  1. Integration Testing
In contrast to a conventional Web services architecture, DICOM Application Hosting uses Web services for bidirectional communication between the hosting system and the hosted applications. This limits the use of general SOAP testing suites to relatively simple SOAP message conformance tests. For example, testing the method "notifiyStateChanged" of the host interface requires that "setState" of the application interface has been called before - thus, the test has to be a service provider itself, which is not supported by general high level SOAP testing suites (please correct and add links, if you know testing solutions that allowing this).

