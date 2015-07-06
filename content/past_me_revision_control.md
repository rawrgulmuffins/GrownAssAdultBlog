Title: Past Me Meet Revision Control
Date: 2015-07-04
Category: Programming
Tags: RevisionControl,Student,Heroes
Authors: Alex LordThorsen
Summary: The dog ate my source code doesn’t work.

Hello World,

Here’s something a little different. I’m going to talk to Past Me. Specifically I’m going to tell Past Me the things that current me thinks would have made school much easier if Past Me had known about them. This is partially to organize my own thoughts about what’s important for students to learn but I’m trying to also make a resource for new students jumping into the Computer Science rabbit hole. With no further adu.

# Revision control

Past Me, listen here, you need revision control. I’m going to lay down how  [git](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics) works because that’s what I use in my day job but  [there’s a large diversity of revision control systems out there](https://en.wikipedia.org/wiki/Comparison_of_revision_control_software). They will all [save your ass.](https://programmers.stackexchange.com/questions/13614/how-serious-is-losing-the-source-code)


And I do know that revision control will save your ass because three days before Unix Assignment 5 (the one where you implement pipes and recursive shell script execution) you’re going to lose your source code and start over from scratch. The world is a scary place but it’s not as scary as your own mistakes.

There’s all kinds of things that you get from revision control but here’s the fundamental things that a student will care about.

1. You'll never have to worry about the dog eating your source code again.
2. You can radically change your code (even the logical extreme of deleting everything) and you have a way to get everything back.
3. It's super easy to track what changes you made and when you made them.
4. When you work in groups you have actual data of who contributed what and where they did it.
5. No really, you’ll never have to worry about losing code again.
6. If you have a computer with internet access you can download your code in under a minute.

Sold? Alright, sold. Here’s the nitty gritty factoids you’ll need to know, Past Me.

Git comes with a lot of magic commands which can be super useful but realistically for a student the commands you’ll need to know about are

    git init
    git add
    git commit
    git push
    git pull
    git clone 
    git diff

Everything else is added complexity that, while useful, isn't required. And to anyone who know’s git out there, I know I know, I’m not talking about  branches yet. But you, my advanced friend, have never watched a revision control newbie struggle with branching. 

For this example we're going to use [bitbucket](https://bitbucket.org/) to store git repositories not local to our machine. If you want to follow this example on your computer go to [bitbucket](https://bitbucket.org/) and register an account. I love my some github (I would suggest eventually making an account but it's not needed right now) but all source code repositories have to be public on github and if your assignments start showing up in a publicly indexable space you're instructors will take your grades into a dark alley and beat them with a billy club.

Next time you get an assignment for class head over to bitbucket [and create a repository for that assignment.](https://confluence.atlassian.com/display/BITBUCKET/Create+a+repository) This example is going to use a linked list assignment (yay CS145).

    # I normally make a directory to hold all git folders
    $ mkdir ~/git
    $ cd  ~/git
    # Now we're going to retrieve the repository that you created for the assignment
    $ git clone  https://rawrgulmuffins@bitbucket.org/rawrgulmuffins/linked_list_assignment.git
    

Now that we're in this repository we can start modifying code 
 
    $ cd linked_list_assignment
    $ echo "#This is a basic assignment to create a linked list in Python
    " >> README.md

and now comes the fun bits,

    $ git add README.md 
    $ $git status
    On branch master
    
    Initial commit
    
    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)
    
            new file:   README.md
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
                                                                                                                      
            .README.md.swp                                       

This bit of text is telling you in what repository your changes are being stored. There's two [repositories](https://programmers.stackexchange.com/questions/69178/what-is-the-benefit-of-gits-two-stage-commit-process-staging) and two [directories](https://help.github.com/articles/pushing-to-a-remote/) that we care about in this example. We have the working directory (the thing with all your souce files), staged commits directory (stored in the .git directory),  the local .git repository (aka, the .git directory on your local box), and Bitbucket's remote repository. 

The changes to be committed section explains what files are in you [are going to be added to the .git repository](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes). The untracked files tells you what file(s) (in this case .README.md.swp which is a backup created by vim automagically) is not tracked by git and will not be committed to the local repository.

At this point if I wanted to see what [differences](https://en.wikipedia.org/wiki/Diff_utility) there are in the repository I could run

    $ git diff

and nothing would happen. I’m really glad there’s no differences because  there's no previous `README.md` file changes to compare against. But, if we run

    # -a says commit all file changes, -m says this is the commit message
    $ git commit -a -m "First commit. Adding README.md."
    [master (root-commit) 2aee159] First commit. Adding README.md.
    1 file changed, 1 insertion(+)
    create mode 100644 README.md

and then run

    $ echo "I'm a modification." > README.md
    $ git status
    On branch master
    Your branch is up-to-date with 'origin/master'.
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   README.md

    no changes added to commit (use "git add" and/or "git commit -a")
    $ git diff
    diff --git a/README.md b/README.md
    index e69de29..17d5696 100644
    --- a/README.md
    +++ b/README.md
    @@ -0,0 +1 @@
    +I'm a modification.

Now we see git [diff](https://en.wikipedia.org/wiki/Diff_utility) produce a set of changes from the previous modifications to the current. The `+` indicates text added to `README.md` and a `-` means text removed.

If you really want to dive deep into git (which is not my suggestion for first starting out) then checkout [Pro Git](https://www.git-scm.com/book/en/v2).  written by Scott Chacon and Ben Straub. This is where most of my deeper understanding of git (and distributed revision control) comes from.

[Also, github also offers a pretty sweet deal to anyone with a .edu email address. This package includes things like $100 for Digital Ocean VPS time and access to TravisCI for your projects.](https://education.github.com/pack)

If you want to know more about distributed vs central revision control [Joel Spolsky's tutorial on mercurial is very nifty.](http://hginit.com/)

# Go Find Hero’s


There are some really awesome people out on the interwebs and a lot of them talk about being better programmers / engineers. 

[Reading Joel Spolsky's article on the 12 steps for better coding was a life changing experience.](http://www.joelonsoftware.com/articles/fog0000000043.html) I wish that I hadn’t read it during my last quarter of college when I was reaching burnout territory. 

[Jessica McKellar](https://twitter.com/jessicamckellar) has already hosted the [meetup that I want to host in Seattle and she’s probably done it better then I ever well.](http://pythonsprints.com/2013/05/5/bostons-cpython-sprint-new-contributors/)

[Finding out that doom’s source code is open for anyone to read was awesome. Having it change some fundamental ways that I organize code repositories was awesomer.](https://github.com/id-Software/DOOM/tree/master/linuxdoom-1.10)

[Well known projects (like the linux kernal) are being heavily modified by people  like Valerie Aurora](http://blog.valerieaurora.org/2009/03/27/relatime-recap/)

Brett [Cannon’s caniusepython3](https://github.com/brettcannon/caniusepython3) has become my example project that I base all of my python packages off of. Very similar to how I still use [Mason Bially’s Make File every time I work with a C Project.](https://github.com/mason-bially)

There are so many amazing people out in the world doing so many amazing things. I feel like Past Me was so focused on just surviving school that Past Me never took any time to find inspiration.

Hell, there’s a bunch of amazing people doing amazing things in Bellingham Washington that Past Me could have actually paid attention to.

Past Me, find big shoes.

#Listen Up, Past Me

I have a bunch more “Listen up, Past Me” topics I’d like to cover (things like unit testing, data languages, configuration, how to spot a tree structure, How to spot other data structures) so stay tuned.
