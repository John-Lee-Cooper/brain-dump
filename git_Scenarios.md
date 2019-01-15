# Git Scenarios

## Scenario with add ##

You just want to add files with specific extension in your staging area. Of course you can add all the files one by one. But you can use *.<extension_name> to include all files with that extension. Following command will add all python files.

>  `git add *.py`

You want to add files with specific extension and also want to specify directory name then you can run the following command. The following command will add all python files from sub directories of models/ directory.

>  `git add models/\*.py`

## Scenario with clean ##

You created some new files or folders in your branch. After some time you realized that you don’t want those files or folders. You need your working tree clean.

These are untracked files in git.  Untracked files are those which you didn’t add already using git add

To make your working tree clean you can run the following command to delete all files and directories that are not tracked by git.

>  `git clean -df`

To see which files will be removed before removing then you can run:

>  `git clean -dn`

## Scenario with rm ##

You can delete your tracked file using this command.

>  `git rm <file-path>`

If your file is in staging area then you have to add the force flag.

>  `git rm <file-path> -f`

You want to delete files from git repository but not from your file system then run:

>  `git rm --cached <file-path>`

## Scenario with branch ##

You have made a typo in your branch name or you want to change your branch name, then the following command will change your branch name.

>  `git branch -m <old-branch-name> <new-branch-name>`

You want to change the current branch name, then you can just run:

>  `git branch -m <new-branch-name> `

If you’ve already pushed the branch with old name, then there are a couple of extra steps required. You need to delete the old branch from the remote and push up the new one.

>  `git push [remote-name] --delete <old-branch-name> `

>  `git push [remote-name] <new-branch-name> `


## Scenario with log ##

Git log shows a lot of information but you just need to see commit id and message. Then you can run the following command.

>  `git log --oneline`

The first seven character in above output is the shorthand commit id and then we have our commit message. The commit id is shorthand because the full commit id is forty hexadecimal characters that specify a 160-bit SHA-1 hash. 

If you want to see the commit message of a specific author, say John Doe, then you can run:

>  `git log --author="John Doe"`

## Scenario with stash ##

You are working in a branch and made some changes. Now, you want to just see the output or code of that branch before you made those changes. Then you can run stash command to make your working tree clean.

>  `git stash`

If you want your changes back then you have to run:

>  `git stash pop`

If you don’t want those changes back then you have to run:

>  `git stash drop`

**Bonus** You changed some files in wrong branch. Then you can stash your changes and checkout to your desired branch and run git stash pop there. You will get your changes in your desired branch.

## Scenario with checkout ##

You want to switch to a branch. Then you can just run:

>  `git checkout <branch-name>`

If you already changed some file in your current branch, then be sure to stash your changes or commit the changes. . If you don’t stash or commit those changes, it will also reflect in your switched branch which you may not want or need.

You have a branch name development and you want to make a branch from development and switch to your new branch directly. Then you can run:

>  `git checkout -b <new-branch-name>`


You can also checkout using commit id. You can use shorthand commit id safely if your project isn’t very large.

>  `git checkout <commit-id>`

This will fall in detached head state in git. Head is simply a reference to the current commit (latest) on the current branch. Generally, Head in git can point to a branch or a commit. When Head points to a branch, git doesn’t complain. But when head points to a commit, but not a branch then it goes to a detached head state.

You want to develop a feature from this detached head state then you have to make a branch from this state and develop your feature there.

>  `git checkout -b <your-new-branch-name>`

## Scenario with commit ##

Say you had following uncommitted files in the start:

    FileA.txt
    FileB.txt

You make some changes in them and then make the commit by following command:

>  `git commit -m ‘First Commit’`

After the commit, you realize that you need to make some further changes in FileB.txt. Instead of making a new commit after changing FileB.txt, use the --amend flag to update the previous commit:

>  `git commit --amend`

If after some time you realize that you also need to modify the commit message of the last commit. you can also do that by using the amend flag using:

>  `git commit —amend -m ‘First Commit Modified’`

If you just added some files or fixed a bug but don’t want to add another commit message then you can use following git command with --no-edit flag.

>  `git commit --amend --no-edit`

Here one thing is very important to remember that amending the last commit rewrites the commit history. It means your commit id will change when you amend a commit.

If you already pushed your code in the remote repository and then you realized that you have to amend your commit message then after amending, you have to make a force push:

>  `git push [remote-name] <branch-name> -f`

## Scenario: Pushed a few changes that were not supposed to be commited ##

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

>  `git reset HEAD~1`

Next you can remove those two commits using the command:

>  `git reset HEAD --hard`

Then simply push the code to remote and your .pem file will be deleted from history as well.

[Warning: Force pushing to remote is VERY RISKY as it modifies the git history on the remote branch. As a rule of thumb you should never force push to master/stage branches. Make sure you are only force pushing to the branch that you own and you understand why you are doing it]


## Scenario: Share a piece of dependent code that cannot be pushed right away ##

If you face a situation where you need to share some changes in the code base that you have made with your co-worker but you cannot yet push your changes to the remote repository, you can use the patch command of git. Here is how it works:

After you have made all the changes you can run the following command:

> `git diff > filename.patch`

git diff > filename.patch will create a file that will contain all uncommitted the changes you have made so far in the code base. Then you can simple share this file with your coworker via slack, email, etc.

You coworker will simply download you patch file and run the following command:

>  `git apply filename.patch`

This will apply all the code changes you have made in the code base on your coworker’s copy of the code.
## Scenario with reset ##

You want to discard your last some commits. Then you can use git reset to discard those commits. There are three flag for git reset that you should know.

    --soft
    --mixed
    --hard

Let’s assume you want to discard the changes until added two.txt which has commit id 96b037c

Now, let’s run git reset command with --soft flag.

>  `git reset --soft 96b037c`

>  `git reset --soft will make orphan all the commits after that commit id (e.g. 96b037c) but the files will not be deleted. The files will be in the staging area.`

Orphaned commit means there is no direct path from a ref to access them. These orphaned commits can usually be found and restored using git reflog Git will permanently delete any orphaned commits after it runs the internal garbage collector. By default, git is configured to run the garbage collector every 30 days.

So, if you run git status you will see the following output.

If you run git log --oneline you will see that previous commits are deleted.

If you run reset command with --mixed flag then your commits will be orphaned and the files will not be in staging area but the files will be found in the file system. If you don’t specify any flag in reset then git will use --mixed flag as default.

If you run git status then you will see the following output.

If you want to permanently delete the files then you can run reset command with --hard flag.

A good practice you can follow that you first run reset command with --soft flag and see the affected files. If you are sure that you don’t want those changes then you can run the reset command with --hard flag.

You should never use git reset <commit-id> when any snapshots after <commit-id> have been pushed to a public repository. Removing a commit that other team members have continued developing poses serious problems for collaboration.

## Scenario with revert ##

You are working in a public repository and you want to undo a commit. Then you can run the following command.

>  `git revert <commit-id> --no-commit`

After running the above command, you can check the affected files using git status . Then you have to make a commit using git commit -m "commit-message" .

>  `git revert will not orphan a commit. It will just undo the changes of your reverted commit id.`

Let’s assume you want to revert the last commit. Then after reverting your status will look like following image.

Before the last commit six.txt file was not added, so it is deleted and five.txt is changed back to it’s previous state. Now, after committing your commit history will look like this.

You want to revert multiple commits within a range then you can run the following command.

>  `git revert <oldest-commit-id>..<recent-commit-id> --no-commit`

If you want to revert multiple commits that are not within a range then you have to provide every commit id that you want to revert.

>  `git revert <commit-id-1> <commit-id-2> --no-commit`

## Scenario with cherry-pick ##

You are working in a branch and you need a commit(e.g. a bug fix commit) from another branch to work in your current branch. Then you can use cherry-pick command to get that commit in your current branch. It is also helpful if you committed in the wrong branch and want the commit in another branch.

First, you have to switch to the branch that has the commit. Copy the commit id of that commit and switch back to your own working branch. Then run the following command to get the commit in your working branch.

>  `git cherry-pick is like copying something from a folder and pasting it in another folder. So, it will not delete the commit from where you cherry picked and in destination branch commit id will also be different.`

>  `git cherry-pick <commit-id>`

