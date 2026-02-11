---
title: Tools: Application launcher/Build Instructions
---

1. Prerequisites: Build Qt statically
  1. Qt 4.8.6
!--
    1. Linux
    1. Mac
--

    1. Windows
- Download the source: http://packages.kitware.com/download/item/6174/qt-everywhere-opensource-src-4.8.6.zip
- Extract archive into codeC:\D\Support\qt-static-release-i386-4.8.6/code
** Note: *On windows, the library is built in the source tree. To avoid confusion, let's make sure the source directory is properly named*
- Download ftp://ftp.qt.nokia.com/jom/jom.zip
- Extract archive into codeC:\D\Support\jom/code
- Add "C:\D\Support\jom" to PATH
- Start codeVisual Studio 32 bits Command Prompt/code
pre
 cd C:\D\Support\qt-static-release-i386-4.8.6
 configure.exe -confirm-license -static -release -opensource -arch windows -no-exceptions -no-accessibility -no-sql-db2 -no-sql-ibase -no-sql-mysql -no-sql-oci -no-sql-odbc -no-sql-psql -no-sql-sqlite -no-sql-sqlite2 -no-sql-ibase -no-sql-tds -no-qt3support -no-xmlpatterns -no-multimedia -no-audio-backend -no-phonon -no-phonon-backend -no-webkit -no-script -no-scripttools -no-declarative -no-gif -no-libtiff -no-libmng -no-openssl -no-dbus -no-opengl -no-openvg -nomake demos
/pre
- Build
pre
 jom
/pre

  1. Qt 4.7.4
- code-no-stl/code flag shouldn't be used. See http://qt-project.org/forums/viewthread/9716/#55456

    1. Linux
- Download the source
 cd Dashboards/Support
 wget http://packages.kitware.com/download/item/7521/qt-everywhere-opensource-src-4.7.4.tar.gz
 tar -xzvf qt-everywhere-opensource-src-4.7.4.tar.gz

- Configure
pre
./configure -prefix /home/kitware/Dashboards/Support/qt/qt-everywhere-opensource-static-release-4.7.4 -confirm-license -static -release -opensource -no-largefile -no-exceptions -no-accessibility -no-sql-db2 -no-sql-ibase -no-sql-mysql -no-sql-oci -no-sql-odbc -no-sql-psql -no-sql-sqlite -no-sql-sqlite2 -no-sql-sqlite_symbian -no-sql-tds -no-qt3support -no-xmlpatterns -no-multimedia -no-audio-backend -no-phonon -no-phonon-backend -no-svg -no-webkit -no-javascript-jit -no-script -no-scripttools -no-declarative -no-gif -no-libtiff -no-libmng -no-openssl -no-nis -no-cups -no-dbus -no-opengl -no-openvg -nomake demos -no-gtkstyle
/pre

- Build and install
 make sub-src  make install

    1. Mac
- Download the source
 cd Dashboards/Support
 curl -O http://packages.kitware.com/download/item/7521/qt-everywhere-opensource-src-4.7.4.tar.gz
 tar -xzvf qt-everywhere-opensource-src-4.7.4.tar.gz

- Configure
pre
./configure -prefix /Users/kitware/Dashboards/Support/qt-everywhere-opensource-static-build-4.7.4/ -confirm-license -arch x86_64 -static -release -opensource -no-largefile -no-exceptions -no-egl -no-accessibility -no-sql-db2 -no-sql-ibase -no-sql-mysql -no-sql-oci -no-sql-odbc -no-sql-psql -no-sql-sqlite -no-sql-sqlite2 -no-sql-sqlite_symbian -no-sql-tds -no-qt3support -no-xmlpatterns -no-multimedia -no-audio-backend -no-phonon -no-phonon-backend -no-svg -no-webkit -no-javascript-jit -no-script -no-scripttools -no-declarative -no-gif -no-libtiff -no-libmng -no-openssl -no-nis -no-cups -no-dbus -no-opengl -nomake demos -sdk /Developer/SDKs/MacOSX10.5.sdk/
/pre

- Build and install
 make sub-src -j3  make install

    1. Windows
- Download the source: http://packages.kitware.com/download/item/7520/qt-everywhere-opensource-src-4.7.4.zip
- Extract archive into codeC:\D\Support\qt-static-release-i386-4.7.4/code
** Note: *On windows, the library is built in the source tree. To avoid confusion, let's make sure the source directory is properly named*
- Download ftp://ftp.qt.nokia.com/jom/jom.zip
- Extract archive into codeC:\D\Support\jom/code
- Add "C:\D\Support\jom" to PATH
- Start codeVisual Studio 32 bits Command Prompt/code
pre
 cd C:\D\Support\qt-static-release-i386-4.7.4
 configure.exe -confirm-license -static -release -opensource -arch windows -no-exceptions -no-accessibility -no-sql-db2 -no-sql-ibase -no-sql-mysql -no-sql-oci -no-sql-odbc -no-sql-psql -no-sql-sqlite -no-sql-sqlite2 -no-sql-ibase -no-sql-tds -no-qt3support -no-xmlpatterns -no-multimedia -no-audio-backend -no-phonon -no-phonon-backend -no-webkit -no-script -no-scripttools -no-declarative -no-gif -no-libtiff -no-libmng -no-openssl -no-dbus -no-opengl -no-openvg -nomake demos
/pre
- Build
pre
 jom
/pre

  1. Qt 4.7.0
    1. Linux
- Download the source
 cd Dashboards/Support
 wget http://get.qt.nokia.com/qt/source/qt-everywhere-opensource-src-4.7.0.tar.gz
 tar -xzvf qt-everywhere-opensource-src-4.7.0.tar.gz

- Configure
pre
./configure -prefix /home/jchris/Dashboards/Support/qt-static-release-4.7.0 -confirm-license -static -release -opensource -no-largefile -no-stl -no-exceptions -no-accessibility -no-sql-db2 -no-sql-ibase -no-sql-mysql -no-sql-oci -no-sql-odbc -no-sql-psql -no-sql-sqlite -no-sql-sqlite2 -no-sql-sqlite_symbian -no-sql-tds -no-qt3support -no-xmlpatterns -no-multimedia -no-audio-backend -no-phonon -no-phonon-backend -no-svg -no-webkit -no-javascript-jit -no-script -no-scripttools -no-declarative -no-gif -no-libtiff -no-libmng -no-openssl -no-nis -no-cups -no-dbus -no-opengl -no-openvg -nomake tools -nomake demos -no-gtkstyle
/pre

- Build and install
 make  make install

    1. Mac
- Download the source
 cd Dashboards/Support
 curl-O http://get.qt.nokia.com/qt/source/qt-everywhere-opensource-src-4.7.0.tar.gz
 tar -xzvf qt-everywhere-opensource-src-4.7.0.tar.gz

- Configure
pre
./configure -prefix /Users/jjomier/Workspace/qt-static-release-4.7.0 -confirm-license -cocoa -universal -static -release -opensource -no-largefile -no-stl -no-exceptions -no-egl -no-accessibility -no-sql-db2 -no-sql-ibase -no-sql-mysql -no-sql-oci -no-sql-odbc -no-sql-psql -no-sql-sqlite -no-sql-sqlite2 -no-sql-sqlite_symbian -no-sql-tds -no-qt3support -no-xmlpatterns -no-multimedia -no-audio-backend -no-phonon -no-phonon-backend -no-svg -no-webkit -no-javascript-jit -no-script -no-scripttools -no-declarative -no-gif -no-libtiff -no-libmng -no-openssl -no-nis -no-cups -no-dbus -no-opengl -no-openvg-nomake tools -nomake demos
/pre

- Build and install
 make  make install

    1. Windows
- Download the source: http://get.qt.nokia.com/qt/source/qt-everywhere-opensource-src-4.7.0.zip
- Extract archive into C:\Dashboards\Support\qt-static-release-4.7.0
** Note: *On windows, the library is built in the source tree. To avoid confusion, let's make sure the source directory is properly named*
pre
 cd C:\Dashboards\Support\qt-static-release-4.7.0
 configure.exe -confirm-license -static -release -opensource -arch windows -no-stl -no-exceptions -no-accessibility -no-sql-db2 -no-sql-ibase -no-sql-mysql -no-sql-oci -no-sql-odbc -no-sql-psql -no-sql-sqlite -no-sql-sqlite2 -no-sql-ibase -no-sql-tds -no-qt3support -no-xmlpatterns -no-multimedia -no-audio-backend -no-phonon -no-phonon-backend -no-webkit -no-script -no-scripttools -no-declarative -no-gif -no-libtiff -no-libmng -no-openssl -no-dbus -no-opengl -no-openvg -nomake tools -nomake demos
/pre
- Build
pre
 nmake
/pre

1. Build the launcher
  1. Linux
 cd ~/Projects
 git clone git://github.com/commontk/AppLauncher.git
 mkdir AppLauncher-Release
 cd AppLauncher-Release
 cmake -DQT_QMAKE_EXECUTABLE:FILEPATH=/home/jchris/Dashboards/Support/qt-static-release-4.7.0/bin/qmake -DBUILD_TESTING:BOOL=ON -DBUILD_TYPE:STRING=Release ../AppLauncher

  1. Mac
 cd ~/Projects
 git clone git://github.com/commontk/AppLauncher.git
 mkdir AppLauncher-Release
 cd AppLauncher-Release
 cmake -DQT_QMAKE_EXECUTABLE:FILEPATH=/home/jchris/Dashboards/Support/qt-static-release-4.7.0/bin/qmake -DBUILD_TESTING:BOOL=ON -DBUILD_TYPE:STRING=Release -DCMAKE_OSX_ARCHITECTURES:STRING="i386"../AppLauncher

- Note that an extra cmake variable has been specified: **-DCMAKE_OSX_ARCHITECTURES:STRING="i386"**

  1. Windows
1. Package the launcher
  1. Linux
  1. Mac
  1. Windows
Don't build the package via Visual Studio, but from the command line
 "c:\Program Files\CMake 2.8\bin\cpack.exe" -G TGZ

1. Versioning
See https://github.com/commontk/AppLauncher#maintainers-how-to-make-a-release-

!--
Since there all development occurs on codemaster/code, each time version is updated, two commits will be required.

  1. Release-candidate
    1. Step1
codeRC/code corresponds to the release candidate number. It is greater or equal to one.

- In codeCMakeLists.txt/code, 
** set codeCTKAppLauncher_VERSION_IS_RELEASE/code to code1/code
** uncomment and set codeCTKAppLauncher_VERSION_RC/code to codeRC/code

- ... and if this is the first release candidate, update at least one these variables:
** codeCTKAppLauncher_MAJOR_VERSION/code
** codeCTKAppLauncher_MINOR_VERSION/code
** codeCTKAppLauncher_BUILD_VERSION/code

- Commit message: codeCTKAppLauncher X.Y.Z-rcRC/code

    1. Step2
- Generate packages based on SHA associated with step1.

    1. Step3
- In codeCMakeLists.txt/code, set codeCTKAppLauncher_VERSION_IS_RELEASE/code to code0/code
- Commit message: codeBegin post-X.Y.Z-rcRC development/code

  1. Release
    1. Step1
- In codeCMakeLists.txt/code, 
** set codeCTKAppLauncher_VERSION_IS_RELEASE/code to code1/code
** comment codeCTKAppLauncher_VERSION_RC/code and reset to code1/code

- Commit message: codeCTKAppLauncher X.Y.Z/code

    1. Step2
- Generate packages based on SHA associated with step1.
- Tag the repository:
  git tag -s -m "CTKAppLauncher X.Y.Z" vX.Y.Z

    1. Step3
- In codeCMakeLists.txt/code, set codeCTKAppLauncher_VERSION_IS_RELEASE/code to code0/code
- Commit message: codeBegin post-X.Y.Z development/code

--