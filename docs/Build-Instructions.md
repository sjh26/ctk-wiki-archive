---
title: Build Instructions
---

The following instructions are valid as of October 2012 (if something is incorrect, please [report an issue](https://github.com/commontk/CTK/issues/new)).

  1. Prerequisites
- git version 1.6.5 or later
- Qt version 4.x or 5.x
- CMake 3.0 or later

  1. Download
{|
! Anonymous checkout behind a firewall
! CTK developer with write access
|-
|
 git clone https://github.com/commontk/CTK.git
|
 git clone git@github.com:commontk/CTK.git
|}

  1. Build with CMake
 mkdir CTK-superbuild
 cd CTK-superbuild
 ccmake ../CTK
 make

    1. CMake Configuration
- For Qt5, set ttQt5_DIR/tt to ttC:\Qt\5.15.2\msvc2019_64\lib\cmake\Qt5/tt
- For Qt4, set ttQT_QMAKE_EXECUTABLE/tt (ttqmake/tt is usually found in the ttbin/tt folder)
- turn on the parts of CTK you want to build

    1. How to use CTK ?
See the [Examples](http://www.github.com/commontk/Examples) project that illustrates how CTK can be integrated into applications.

1. Contribute
  1. Simple Git
See also https://docs.github.com/en/get-started/using-git

    1. Checkout
- checkout
 git clone git@github.com:commontk/CTK.git
(or use anonymous option listed above)

    1. Update
 git pull --rebase

    1. Commit
- commit (commit is to local version, push sends it to upstream server)
 git add changed files
 git commit -m message
 git push

  1. Intermediate Git
- check update before merging (look at diff):
 git fetch
 git diff origin master
 git rebase

- If you have changes pending that you aren't ready to commit, you can't rebase on top of them unless you do this:
 git stash
 git pull --rebase
 git stash pop

- to get the code from a branch 
 git clone repository dir
 cd dir
 git checkout origin/branchname

1. Links
List of needed tools and libraries used when building CTK:
- [Git](http://git-scm.com/download): To download source code
- [Qt](https://www.qt.io/download-open-source): Dependency required.
- [CMake](http://www.cmake.org/cmake/resources/software.html): Cross-platform build system
- [Patch for Windows](http://gnuwin32.sourceforge.net/packages/patch.htm): Needed to apply patches to external thirdparty libraries source code

Optional:
- [Python](http://www.python.org/download/): If you plan to use Scripting
- [DoxyGen](http://www.stack.nl/~dimitri/doxygen/download.html#latestsrc): To generate documentation from source code on your machine
- [GraphViz](http://www.graphviz.org/Download.php): To generate documentation from source code on your machine