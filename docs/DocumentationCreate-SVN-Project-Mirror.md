---
title: Documentation/Create SVN Project Mirror
---

[to CTK Documentation](to CTK Documentation)(Back)(Documentation.md)

- Setup the 'svn-mirror' branch

pre
mkir PythonQt
cd PythonQt
git init
git svn init -T https://pythonqt.svn.sourceforge.net/svnroot/pythonqt/trunk/ --no-minimize-url
git svn fetch 
git gc
git remote add origin git@github.com:commontk/PythonQt.git
git branch -M svn-mirror
git push origin svn-mirror:refs/heads/svn-mirror
/pre

- .. and the 'patched' branch

pre
git checkout -b patched
/pre

- hack, hack, hack

pre
git push origin patched:refs/heads/patched
/pre

- Rebase the 'svn-mirror' branch

pre
git checkout svn-mirror
git svn rebase
/pre

pre
Before:

          A---B---C patched
         /
    D---E svn-mirror
/pre

pre
After:

          A---B---C patched
         /
    D---E---F---G svn-mirror
/pre

- Rebase 'patched' branch on top of 'svn-mirror' branch

pre
git rebase patched svn-mirror
/pre

pre
Before:

          A---B---C patched
         /
    D---E---F---G svn-mirror
/pre

pre
After:
                  A'---B'---C' patched
                 /
    D---E---F---G svn-mirror
/pre