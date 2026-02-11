---
title: Making a Release
---

{{banner
| text = [For the latest version of this page, visit the CTK GitHub wiki.](For the latest version of this page, visit the CTK GitHub wiki.)(https://github.com/commontk/CTK/wiki/Release-Process)}}

A core developer should use the following steps to create a release ttYYYY-MM-DD/tt of CTK

ol

  liMake sure that all CI tests are passing/li

  li
    pDownload the source/p
    precd /tmp  \
git clone git@github.com:commontk/CTK  \
cd CTK
/pre
  /li

  li
    pList all tags sorted by version/p
    pre$ git fetch --tags  \
git tag -l | sort -V
/pre
  /li

  li
    pChoose the next release version number/p
    pre$ release=YYYY-MM-DD/pre
  /li
  
  li
    pTag the release/p
    pregit tag --sign -m "CTK ${release}" ${release} master/pre
    psmallWe recommend using a [GPG signing key](GPG signing key)(https://help.github.com/articles/generating-a-new-gpg-key/) to sign the tag./small/p
  /li

  li
    pPublish the release tag/p
    pregit push origin ${release}/pre
  /li
/ol