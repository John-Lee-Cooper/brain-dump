# git

## setup

* [Download git for OSX](http://git-scm.com/download/mac)
* [Download git for Windows](http://msysgit.github.io/)
* [Download git for Linux](http://git-scm.com/book/en/Getting-Started-Installing-Git)

### Create a new repository

```bash
mkdir <new_directory>
cd <new_directory>
git init
```

### Checkout a repository

`git clone /path/to/repository`

when using a remote server, your command will be  

`git clone username@host:/path/to/repository`

## Workflow

Your local repository consists of three _trees_.
The first one is your _Working Directory_ which holds the actual files.
The second one is the _Index_ which acts as a staging area.
Finally, the _HEAD_ points to the last commit you've made.

### Add files to _Index_

`git add <file_path> ...`

or

`git add -A`

### Commit files to _HEAD_

`git commit -m <commit_message>`

Your changes are now in the __HEAD__ of your local working copy.

### Pushing changes to remote repository

`git push [origin] [branch]`

If you have not cloned an existing repository and want to connect your repository to a remote server:

`git remote add origin <server>`

## Branching

Branches are used to develop features isolated from each other.
The _master_ branch is the default branch when you create a repository.
Use other branches for development and merge them back to the master branch upon completion.

### Create a new branch and switch to it

`git checkout -b <branch>`

### Switch to branch

`git checkout <branch>`

### Delete a branch

`git branch -d <branch>`

### A branch is _not available to others_ unless you push the branch to your remote repository

`git push origin <branch>`

### Update your local repository to the newest commit

`git pull`

This will _fetch_ and _merge_ remote changes.

### To merge another branch into your active branch (e.g. master)

`git merge <branch>`

## Resolving Conflicts

Git tries to auto-merge changes during pulls and merge.
Unfortunately, auto-merging is not always possible, resulting in _conflicts_.
You are responsible for merging _conflicts_ manually by editing the files shown by git.
After changing, you need to mark them as merged with
`git add <filename>`

Before merging changes, you can also preview them by using
`git diff <source_branch> <target_branch>`

## Logging

### View repository history

`git log`

### To see only the commits of a certain author

`git log --author=bob`

### To see a log where each commit is one line:

`git log --pretty=oneline`

### To see an ASCII tree of all the branches, with the names of tags and branches:

`git log --graph --oneline --decorate --all`

### To see only which files have changed:

`git log --name-status`

### Create a new tag

It's recommended to create tags for software releases.
`git tag <tagname> <commit-id>`

### replace local changes

`git checkout -- <filename>`

This replaces the changes in your working tree with the last content in HEAD.
Changes already added to _index_, as well as new files, will be kept.

### To drop all local changes and commits, fetch the latest history from the server and point your local master branch at it

`git fetch origin`
`git reset --hard origin/master`

## useful hints

built-in git GUI
`gitk`
use colorful git output
`git config color.ui true`
show log on just one line per commit
`git config format.pretty oneline`
use interactive adding
`git add -i`

# Git Scenarios

## Scenario with add

You just want to add files with specific extension in your staging area. Of course you can add all the files one by one. But you can use *.<extension_name> to include all files with that extension. Following command will add all python files.

`git add *.py`

You want to add files with specific extension and also want to specify directory name then you can run the following command. The following command will add all python files from sub directories of models/ directory.

`git add models/\*.py`

## Scenario with clean

You created some new files or folders in your branch. After some time you realized that you don’t want those files or folders. You need your working tree clean.

These are untracked files in git.  Untracked files are those which you didn’t add already using git add

To make your working tree clean you can run the following command to delete all files and directories that are not tracked by git.

`git clean -df`

To see which files will be removed before removing then you can run:

`git clean -dn`

## Scenario with rm

You can delete your tracked file using this command.

`git rm <file-path>`

If your file is in staging area then you have to add the force flag.

`git rm <file-path> -f`

You want to delete files from git repository but not from your file system then run:

`git rm --cached <file-path>`

## Scenario with branch

You have made a typo in your branch name or you want to change your branch name, then the following command will change your branch name.

`git branch -m <old-branch-name> <new-branch-name>`

You want to change the current branch name, then you can just run:

`git branch -m <new-branch-name> `

If you’ve already pushed the branch with old name, then there are a couple of extra steps required. You need to delete the old branch from the remote and push up the new one.

`git push [remote-name] --delete <old-branch-name> `

`git push [remote-name] <new-branch-name> `

## Scenario with log

Git log shows a lot of information but you just need to see commit id and message. Then you can run the following command.

`git log --oneline`

The first seven character in above output is the shorthand commit id and then we have our commit message. The commit id is shorthand because the full commit id is forty hexadecimal characters that specify a 160-bit SHA-1 hash. 

If you want to see the commit message of a specific author, say John Doe, then you can run:

`git log --author="John Doe"`

## Scenario with stash

You are working in a branch and made some changes. Now, you want to just see the output or code of that branch before you made those changes. Then you can run stash command to make your working tree clean.

`git stash`

If you want your changes back then you have to run:

`git stash pop`

If you don’t want those changes back then you have to run:

`git stash drop`

**Bonus** You changed some files in wrong branch. Then you can stash your changes and checkout to your desired branch and run git stash pop there. You will get your changes in your desired branch.

## Scenario with checkout

You want to switch to a branch. Then you can just run:

`git checkout <branch-name>`

If you already changed some file in your current branch, then be sure to stash your changes or commit the changes. . If you don’t stash or commit those changes, it will also reflect in your switched branch which you may not want or need.

You have a branch name development and you want to make a branch from development and switch to your new branch directly. Then you can run:

`git checkout -b <new-branch-name>`


You can also checkout using commit id. You can use shorthand commit id safely if your project isn’t very large.

`git checkout <commit-id>`

This will fall in detached head state in git. Head is simply a reference to the current commit (latest) on the current branch. Generally, Head in git can point to a branch or a commit. When Head points to a branch, git doesn’t complain. But when head points to a commit, but not a branch then it goes to a detached head state.

You want to develop a feature from this detached head state then you have to make a branch from this state and develop your feature there.

`git checkout -b <your-new-branch-name>`

## Scenario with commit

Say you had following uncommitted files in the start:

    FileA.txt
    FileB.txt

You make some changes in them and then make the commit by following command:

`git commit -m ‘First Commit’`

After the commit, you realize that you need to make some further changes in FileB.txt. Instead of making a new commit after changing FileB.txt, use the --amend flag to update the previous commit.  This command will prompt you, opening your git default text editor where you can edit the commit message if you need to.

`git commit --amend`

If you just added some files or fixed a bug but don’t want to add another commit message then you can use following git command with --no-edit flag.

`git commit --amend --no-edit`

Here one thing is very important to remember that amending the last commit rewrites the commit history. It means your commit id will change when you amend a commit.

If you already pushed your code in the remote repository and then you realized that you have to amend your commit message then after amending, you have to make a force push:

`git push [remote-name] <branch-name> -f`

## What if the commit I want to amend is not the last one, but an older commit instead?

In this case you have to retrieve the hash of the commit you want to amend.  To get the list of the parent commits of your HEAD, just run:

`git log or git log --graph --oneline`

You should get something similar to this:

* c8i01dj6 — Added method to retrieve barcode to Product model
* 5ti2k3n9 — Deleted file products.json
* 3g46klo0 — Bug fix — added missing parameter

Say you want to amend the commit 3g46klo0. Once you’ve added your changes to the stage, run:

`git commit --fixup 3g46klo0`

This command will not amend the commit directly. Rather, it will create a new commit with the same message of the want to amend preceded by the fixup! prefix.  To rewrite the history to squash the two “Bug fix” commits:

`git rebase master -i --autosquash`

## Scenario: Pushed a few changes that were not supposed to be commited

It is easy to accidentally push a few files that were not supposed to be committed. Let’s say you pushed some a .pem file. One thing that you might try in order to remove the pushed .pem from the remote repo is:

    Pull the latest code from the repo.
    Delete the .pem file
    Create another commit with the deleted .pem file
    Push the changes back to remote repo

Unfortunately, this approach doesn't completely removed the .pem from git. Git keeps a track of all the files you commit. So anyone can dig into the history of git commits and access the .pem file.

However, git allows you to modify history. So the solution would be to move back to your previous commit and force push.

`git reset HEAD~n` lets you move back to your previous n commits. So `git reset HEAD~2` takes you back two commits and show you the changes in them.

`git reset HEAD --hard` will clean all those changes.  Say you want to remove the last commit (i.e ‘Add .pem file’)

First you will go back two commits by running the command:

`git reset HEAD~1`

Next you can remove those two commits using the command:

`git reset HEAD --hard`

Then simply push the code to remote and your .pem file will be deleted from history as well.

[Warning: Force pushing to remote is VERY RISKY as it modifies the git history on the remote branch. As a rule of thumb you should never force push to master/stage branches. Make sure you are only force pushing to the branch that you own and you understand why you are doing it]


## Scenario: Share a piece of dependent code that cannot be pushed right away

If you face a situation where you need to share some changes in the code base that you have made with your co-worker but you cannot yet push your changes to the remote repository, you can use the patch command of git. Here is how it works:

After you have made all the changes you can run the following command:

`git diff > filename.patch`

git diff > filename.patch will create a file that will contain all uncommitted the changes you have made so far in the code base. Then you can simple share this file with your coworker via slack, email, etc.

You coworker will simply download you patch file and run the following command:

`git apply filename.patch`

This will apply all the code changes you have made in the code base on your coworker’s copy of the code.
## Scenario with reset

You want to discard your last some commits. Then you can use git reset to discard those commits. There are three flag for git reset that you should know.

    --soft
    --mixed
    --hard

Let’s assume you want to discard the changes until added two.txt which has commit id 96b037c

Now, let’s run git reset command with --soft flag.

`git reset --soft 96b037c`

`git reset --soft will make orphan all the commits after that commit id (e.g. 96b037c) but the files will not be deleted. The files will be in the staging area.`

Orphaned commit means there is no direct path from a ref to access them. These orphaned commits can usually be found and restored using git reflog Git will permanently delete any orphaned commits after it runs the internal garbage collector. By default, git is configured to run the garbage collector every 30 days.

So, if you run git status you will see the following output.

If you run git log --oneline you will see that previous commits are deleted.

If you run reset command with --mixed flag then your commits will be orphaned and the files will not be in staging area but the files will be found in the file system. If you don’t specify any flag in reset then git will use --mixed flag as default.

If you run git status then you will see the following output.

If you want to permanently delete the files then you can run reset command with --hard flag.

A good practice you can follow that you first run reset command with --soft flag and see the affected files. If you are sure that you don’t want those changes then you can run the reset command with --hard flag.

You should never use git reset <commit-id> when any snapshots after <commit-id> have been pushed to a public repository. Removing a commit that other team members have continued developing poses serious problems for collaboration.

## Scenario with revert

You are working in a public repository and you want to undo a commit. Then you can run the following command.

`git revert <commit-id> --no-commit`

After running the above command, you can check the affected files using git status . Then you have to make a commit using git commit -m "commit-message" .

`git revert will not orphan a commit. It will just undo the changes of your reverted commit id.`

Let’s assume you want to revert the last commit. Then after reverting your status will look like following image.

Before the last commit six.txt file was not added, so it is deleted and five.txt is changed back to it’s previous state. Now, after committing your commit history will look like this.

You want to revert multiple commits within a range then you can run the following command.

`git revert <oldest-commit-id>..<recent-commit-id> --no-commit`

If you want to revert multiple commits that are not within a range then you have to provide every commit id that you want to revert.

`git revert <commit-id-1> <commit-id-2> --no-commit`

## Scenario with cherry-pick

You are working in a branch and you need a commit(e.g. a bug fix commit) from another branch to work in your current branch. Then you can use cherry-pick command to get that commit in your current branch. It is also helpful if you committed in the wrong branch and want the commit in another branch.

First, you have to switch to the branch that has the commit. Copy the commit id of that commit and switch back to your own working branch. Then run the following command to get the commit in your working branch.

`git cherry-pick is like copying something from a folder and pasting it in another folder. So, it will not delete the commit from where you cherry picked and in destination branch commit id will also be different.`

`git cherry-pick <commit-id>`

--------------------------------------

git reset --hard HEAD— Discard staged and unstaged changes since the most recent commit.
  Specify a different commit instead of HEAD to discard changes since that commit.
  --hard specifies that both the staged and unstaged changes are discarded.

git checkout my_commit— Discard unstaged changes since my_commit.
  HEAD is often used for my_commit to discard changes to your local working directory since the most recent commit.
  checkout is best used for local-only undos. It doesn’t mess up the commit history from a remote branch that your collaborators are depending upon!
  If you use checkout with a branch instead of a commit, HEAD is switched to the specified branch and the working directory is updated to match. This is the more common use of the checkout command.

git revert my_commit —Undo the effects of changes in my_commit. revert makes a new commit when it undoes the changes.
  revert is safe for collaborative projects because it doesn’t overwrite history that other users’ branches might depend upon.

--------------------------------------

## I’ve made a lot of changes, how can I select only the bits I want to commit?

In order to create commits that include only related changes, you may want to select the parts of the code you want to add to the commit, rather than adding everything. To do so, you just have to run:

`git add -p`

This command will prompt you a question for each part of the code (hunk) you changed. For each question / set of changes, you can reply

  (y) to add the changes to the stage,
  (n) to not add them,
  (q) to quit the adding process,
  (a) to add the changes and all the following changes in the same file,
  (d) to discard changes and all the following changes in the same file,
  (s) to split the set of changes in smaller sets and get a new question for each of them or
  (e) to edit the diff.

## Store username / password in git config:

`git config credential.helper store; git pull`

--------------------------------------

## Rules

1. Create a Git repository for every new project
2. Create a new branch for every new feature
3. Use Pull Requests to merge code to Master

## Git Links

[Using Git Tags To Version Coding Tutorials](https://medium.com/@emmawedekind/using-git-tags-to-version-coding-tutorials-cf9ff28fad4f)  
[How to Host Your Website On Github Pages For Free](https://medium.com/swlh/how-to-host-your-website-on-github-pages-for-free-3302b0fe8956)  
[Intro to Interactive Rebasing in Git and Customizing Vim Preferences](https://medium.com/@lucaspenzeymoog/intro-to-interactive-rebasing-in-git-and-customizing-vim-preferences-b6e2f0309e31)  
[git-and-github-tutorial](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)  
[Understanding the GitHub flow](https://guides.github.com/introduction/flow/)  
[git - the simple guide](http://rogerdudler.github.io/git-guide/)  
[Git Tutorial: Basics](https://www.atlassian.com/git/glossary)  
[The Git Parable](http://tom.preston-werner.com/2009/05/19/the-git-parable.html)  
[A successful Git branching model](http://nvie.com/posts/a-successful-git-branching-model/)  
[Git - GUI Clients](http://git-scm.com/downloads/guis)  
[What is Git how to use it why to use it](https://levelup.gitconnected.com/what-is-git-how-to-use-it-why-to-use-it-explained-in-depth-76a5066abaaa?source=linkShare-8a8b134a2c85-1550717474)  
[Master your git productivity – Ewan Jones](https://medium.com/@ewanjones_23689/master-your-git-productivity-a717fd4adf77?source=safariShare-8a8b134a2c85-1559349881)  
[Use Git More Efficiently: A Simple Git Workflow](https://medium.com/@negarjf/use-git-more-efficiently-a-simple-git-workflow-c4e650289ec8)  
[How to use Git submodules](http://blog.joncairns.com/2011/10/how-to-use-git-submodules/)  
[30 Git CLI options you should know about - Christophe Porteneuve](https://medium.com/@porteneuve/30-git-cli-options-you-should-know-about-15423e8771df)  
[Git commit practices your future self will thank you for - victoria.dev](https://victoria.dev/blog/git-commit-practices-your-future-self-will-thank-you-for/)  
