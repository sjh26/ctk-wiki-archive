---
title: Contributing to CTK
---

The present document aims at describing how a developer should contribute to CTK. 

- The source code of CTK is currently hosted on Github. See http://github.com/commontk/CTK

- It's also assumed the developer is familiar with git [http://git-scm.com/](http://git-scm.com/). There are countless amount of resources available online. A good start point could the list presented on [CMake/git page](CMake/git page)(http://www.cmake.org/Wiki/Git/Resources).

- We use a topic-based workflow as documented [here](here)(http://public.kitware.com/Wiki/Git/Workflow/Topic) and thus define integration branche(s):
** **master** Development; starting point for new features (default)

!--
- We use a topic-based workflow as documented [here](here)(http://public.kitware.com/Wiki/Git/Workflow/Topic) and thus define integration branches:
** **master** Release preparation; starting point for new features (default)
** del**next** Development; new features published here first /del

- We also accept commit following the more classic rebase workflow. See [http://unethicalblogger.com/2010/04/02/a-rebase-based-workflow.html](http://unethicalblogger.com/2010/04/02/a-rebase-based-workflow.html)
--

1. Prerequisites
- [Create an account on github.com](Create an account on github.com)(https://github.com/signup/free)
- Fork http://github.com/commontk/CTK
- Introduce yourself
 $ git config --global user.name "Your Name"
 $ git config --global user.email "you@yourdomain.com"
- Use correct line endings ([more info](more info)(http://help.github.com/dealing-with-lineendings/))
 [Linux](Linux)(On) $ git config --global core.autocrlf input
 [Windows](Windows)(On) $ git config --global core.autocrlf true

1. Checkout your fork
 cd MyProject
 git clone git@github.com:**MYACCOUNT**/CTK.git
 cd CTK
 git remote add origin git@github.com:**MYACCOUNT**/CTK.git
 git remote add upstream git@github.com:commontk/CTK.git

1. Publishing your branch
- Having your own fork CTK allows you to backup and publish your work avoiding the *urge to merge* [http://public.kitware.com/Wiki/Git/Workflow/Topic#Urge_to_Merge](http://public.kitware.com/Wiki/Git/Workflow/Topic#Urge_to_Merge)
 git checkout -b YYY-new-feature
 hack, hack, hack, add, commit
 git push origin topic1:refs/heads/YYY-new-feature

- Note that codeYYY/code reference an issue entered in the tracker.

- As a shortcut, you could also enter the following. Some useful script are also available [here](here)(http://git-wt-commit.rubyforge.org/):
 git config branch.topic1.remote origin
 git config branch.topic1.merge refs/heads/YYY-new-feature

- Then, from the topic branch *YYY-new-feature*, you could just enter the following to backup/publish your work:
 git push

- From there, you have two options:
** Send an email on the developer list referencing your topic
** Submit a pull request [https://help.github.com/articles/using-pull-requests](https://help.github.com/articles/using-pull-requests)

- To delete a branch from your fork:
 git push origin :YYY-new-feature

1. Checkout a branch from a different fork
- You may want to collaborate with an other developer and work conjointly on a feature.
- Let's say, *jcfr* published the branch *awesome_feature* on his fork. You should do the following to check out his branch:
 git remote add jcfr git://github.com/jcfr/CTK.git
 git fetch jcfr
 git checkout -b awesome_feature refs/remotes/jcfr/awesome_feature
or 
 git checkout -b awesome_feature jcfr/awesome_feature
- You should now have a local branch named awesome_feature. You can now add, commit and publish your work.

1. Sync your topic branch
- If a collaborator previously checked out your published branch, committed some changes, then published a revised branch on his github fork, you may want to grab its changes.
- Different ways:
1) If you didn't work on your branch, you could do the following:
 git fetch jcfr
 git checkout my_topic
 git merge jcfr/my_topic

2) If you worked on your branch while your collaborator was working, you may want to select only the commit your collaborator pushed on his fork: 

 git fetch jcfr
 git checkout my_topic
 git cherry-pick sha1   # sha1 identifying a specific commit

1. Integrate your new feature
After it has been validated and tested, your changes could be integrated to **master** following two approaches:

- Direct integration

 git fetch upstream                             # Retrieve change from upstream repository
 git checkout master                            # Checkout your local "master" branch
 git reset --hard upstream/master               # Make sure your local branch is up-to-date.
 git merge new_feature --log --no-ff            # Merge locally to "master" - Your changes are now integrated
 git push upstream                              # Publish your change on the official repository
 git push origin                                # Publish your change on your fork

- Pull request integration

!--
- Initially, your feature should be integrated to **next**.
- To integrate your change to **next**, you could follow the steps listed below. More details are also available [here](here)(http://public.kitware.com/Wiki/Git/Workflow/Topic#New_Topic).
 git fetch upstream                             # Retrieve change from upstream repository
 git checkout next                              # Checkout your local "next" branch
 git merge upstream                             # Make sure your local branch is up-to-date.
 git merge new_feature                          # Merge locally to "next" - Your changes are now integrated
 git push upstream                              # Publish your change on the official repository
 git push origin                                # Publish your change on your fork

- After it has been validated and tested, it could be integrated to **master**. More details [here](here)(http://public.kitware.com/Wiki/Git/Workflow/Topic#Mature_Topic).
 Repeat the command listed above changing "next" into "master"
--

!--
1. Tutorial
The idea behind the tutorial is the following, it will guide you through the basic step allowing to:
- Step1 - Fork and clone the tutorial repository
- Step2 - Create a new feature from **master** branch
- Step3 - Add and commit a file representing the feature
- Step4 - Merge the feature into the **next** branch
- Step5 - Refine your feature by doing an additional commit
- Step6 - Merge again with *'next*
- Step7 - Merge feature with **master**

The 'tutorial feature' you will create could be correspond to a TXT file containing either a proverb, sentence, thought of the day, proverb, ... 
- For the sake of the tutorial, let's make sure the text you create for the first commit contain an "error" (missing the author name, spell mistake, ...).
- The second commit will intent to fix the "error"

For example:
- Commit1
** Filename: ghandi.txt
** Content: "Be the change you want to see in the world." Mahatma Gandhi
** CommitMsg: Added Mahatma Gandhi proverb about change
- Commit2:
** New content: "Be the change you want to see in the world." Mahatma Gandhi, Indian philosopher, internationally esteemed for his doctrine of nonviolent protest, 1869-1948
** CommitMsg: Specified who is Mahatma Gandhi

You will find a repository named GitTutorial here: http://github.com/commontk/GitTutorial

- Step1

- Step2

- Step3

- Step4

- Step5

- Step6

- Step7
--

1. Git Commit Style
- Write very descriptive and concise first line summary of your commit
** try to stick to 50 characters max (no more than 65)
** do not use 'COMP' 'ENH' etc.  (these cut into your 50 characters)
** summary should be a complete English sentence starting with a capital letter (terminating period is optional). Ideally the sentence should be using present tense ("Add" vs "Added", "Fix" vs "Made fixes"...)
- Include a blank line after the summary and then a more detailed multi-line description (72 character max line length)
- In the body of the commit message, include #123 where 123 is the issue number.  If a final commit fixes the issue, include "Fixes #123" or "Closes #123" in the commit message.
- Use codegit merge --log --no-ff topicname/code (this keeps the logs messages of the merged branch)

1. CTK Coding Style
The overall policy is to follow the coding conventions of the parent classes unless there is an accepted CTK exception to improve consistency or usability (to account for inconsistency in the parent class system).  

- If you are writing a widget that inherits from QObject, all your code should follow Qt coding conventions.
** Use the [Private Implementation approach ("PIMPL")](Private Implementation approach ("PIMPL"))(http://www.commontk.org/docs/html/CorePimpl.html) **except** make the member variables of your private class begin with a capital letter.  This means that when you create a widget using the QtDesigner, you must rename the widget to a local name that begins with a capital letter (since this will be an instance variable in your private implementation).

- Use *virtual* keyword also in derived class. Doing so improve readability of the code.

- Use const reference if it applies. For example:
syntaxhighlight lang="cpp-qt"
 void setName(const QString newName); // better
 void setName(QString newName); // poor
/syntaxhighlight

- Use *comment line* separator. For example:
syntaxhighlight lang="cpp-qt"
...

//----------------------------------------------------------------------------
void Foo::setName(const QString newName)
{
  Q_D(Foo);
  d-Name = newName;
}

//----------------------------------------------------------------------------
QString Foo::name() const
{
  Q_D(const Foo);
  return d-Name;
}
...
/syntaxhighlight

- The following statements *for*, *while*, *switch*, *if*, *else*, *try*, *catch* should, most of time, be multi-line. The brackets should also be indented with 2 spaces.  For example:
syntaxhighlight lang="cpp-qt"


//----------------------------------------------------------------------------
bool Foo::doSomething(int count)
{
  // Better
  for(int i=1; i  count; ++i)
    {
    if (i == 100)
      {
      qDebug()  "i = 100";
      break;
      }
    }

  // Poor
  for(int i=1; i  count; ++i)
    if (i == 100) { qDebug()  "i = 100"; break; }
}

/syntaxhighlight
- Within CMakeLists.txt files, source/header file names should be sorted alphabetically. It also applies with inclusion order in header/implementation files
- [Prefer to use normalised signal/slot signatures](Prefer to use normalised signal/slot signatures)(http://marcmutz.wordpress.com/effective-qt/prefer-to-use-normalised-signalslot-signatures/)

1. FAQ
- What the meaning of *fatal: The current branch master is not tracking anything.* ?