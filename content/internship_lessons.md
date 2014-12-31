Title: Lessons from my internship
Date: 2013-09-22 10:20
Modified: 2014-11-29 10:20
Category: Programming
Tags: Programming
Authors: Alex Lord
Summary: I loved my internship, here's what I would do different

This summer I did an internship at EMC Isilon and I absolutely loved it. As amazing as it was, though, it was also quite the learning experience and I’d like to share some of the things I learned with you. 

First, though, some simple metrics:

Over the course of the summer, I wrote almost 13,000 lines of code, but only about 7,500 actually made it into the published beta. Of that 7,500 almost 2,000 are static HTML. In addition to that, I also wrote about 1,500 lines of docstrings. I factored out about 4,500 lines of code and nearly 1,000 straight strings (help text, descriptions, comments, docstrings). A huge chunk of that factored out code is CSS/HTML but a big part is also refactoring my Python and Javascript code.

On average, I wrote 173.33 lines of code per day, 5 days a week, for 15 weeks. In the course of that, I learned about--and now consider myself proficient in--13 new Python and Javascript libraries and learned how to profile a project that uses many different libraries, languages, and protocols.  I learned how to make C modules for Python and how to manage pulling and pushing data from multiple servers and databases. Most important of all I then had people actually start using my tool. PS. deploying things is a pain in the ass. 

What all that boils down to is that I built and deployed a working full stack web application. More importantly I lead a small team (another developer and myself) and owned the project.

That sounds pretty awesome, right? And it was, but part of that learning experience was doing things wrong. Really really wrong. 

The following are four lessons from this summer which I consider the most important of everything I learned. I believe these will be useful to all programmers. 

###Never assume you will be the only programmer on a project.

When I was given my project, I was told that I would be the only developer working on it. That my department didn’t have the people with the skills or the time to work on the project with me. And I made the mistake of believing them.

If you could go and look at the revision history of my projects documentation you can actually see the day I was told that someone else was going to work on my code. Documentation goes from,

```
#  TODO Fix this
```
and
```
“””
no return value, modifies some object variables
“””
```
to
```
some_call(request)  #  Modifies request.url variable
```
and
```
"""
This function executes all the potential actions from the management/users
page. This function modifies database values found in the user table.

NOTE: Only admins are allowed to execute user modifications.

Expected actions:
    Activate: Activates a user.Deactivated users can take no actions.
    
    Deactivate: Deactivates a user.

    ChangeRole: Changes the role of a user. For more on roles go to access_control.py
    
    ChangePostWarning: This changes the warning text that a user sees when they attempt to bypass the review process.
    “””
```
I actually felt pretty ashamed of how bad my documentation was when I watched another developer struggle with my code base. I realized just how many assumptions I made and how much I relied on having created the code to read it. Names that I thought were self documenting weren’t. Docstrings that I assumed contained enough information didn’t. 

This also carries over into other assumptions as well. For example, I never set a style standard for the project, go me. Even if your language comes with a set of style guides (PEP8) you still need to specify what styles to follow because not everyone is going to be familiar with the language. In fact, you should assume no one is going to be familiar with the language. Even better is when you specify an automated tool that displays breaks in style. Examples being pep8 and flake8 for python.  

The biggest assumption was that the code’s workflow was clear just from function calls. When someone comes into your code base, they aren’t going to see the overall structure, side effects, and purpose of your module (package, class, file, whatever). If you don’t want to wait for them to reverse engineer your work (read, spend a looooon time) you will have to spell it out for the. No, that doesn’t make them a bad developer. 

Finish the deployment early, run all of your normal tests against the deployed environment before opening it to the public. 
    
There are actually two mistakes that I made in the process of learning this lesson. The first mistake is that I waited until the last day of my internship to try to deploy the project. The second is that I didn’t run my unit tests against the deployed project. I missed two configuration errors and a line of code that had a hard coded value which was supposed to read from a config file.

I had spent so long working on logic errors that I completely forgot that there is a class of bugs that come not from the code but from the environment that your code works in. Never assume that because something worked in the test environment that it will work in the deployment environment. 

Lines of code are not a good indication of the health of a project.

I purposely started this post by talking about total lines of code followed by a breakdown of lines that actually made it into the final product. 13,000 sounds impressive until you realize how much time I spent modifying and removing bugging, unclear, complicated, and useless lines. I also have a very verbose coding style. For example, if a function like this one,
```
result = post_document(post, post_comments, post_history, flags)
```

would word wrap (PEP8 specifies that lines shouldn’t be longer than 80 characters) I would change the function to look like,
```
result = post_document(
    post, 
    post_comments, 
    post_history, 
    flags)
```
Each of which would get counted as a line of code according to SVN. I should probably use a tool to get a more accurate account of lines of code but I spent enough time just getting SVN to not count comments and blank lines.

When my project was at it’s largest (almost 10,000 lines), it was also at it’s most bug-ridden. After refactoring, pushing common code into functions, and common problems into modules it was much easier to see the big and small picture.

Speaking of verbose code, I’ve found a characteristic of coding style that I now want to strive for in all of my projects. I’m calling it the ‘minimum number of verbose lines of code’. Not very catchy, perhaps, but it does make the code base much easier to maintain by balancing the horizontal and vertical reading requirements for the code. To me, this is how a programmer accomplishes their number one engineering goal (reduce project complexity as much as possible).

User testing (even something as simple as sitting someone down on your computer and watching them play with things) is incredibly important. You need to do this multiple times with different people.
 
Go read two books right now. ‘The Design Of Everyday Things’ by Donald Norman and ‘Don’t Make Me Think’ by Steve Krug. No really, I’ll wait.

You’re back? Ok, I’ll just give a quick summary.  Your user facing code sucks and you have no way to tell how it sucks. It’s too intuitive for you to use tools you created.

It doesn’t matter if you’re making a console application (Can you guess what the Linux command “free” does just from the name?), a web application, or a operating system API, someone is going to use your code (hopefully). And that means you need to watch people use your system and you need to pay special attention to where they struggle. You need to do this in rounds because you’ll have UI errors that can only happen after you’ve fixed the original gaping wounds.

These four lessons were the most important to my growth as a developer, but they’re hardly all I learned this summer. Here are some more specific lessons that may not apply to all developers, but are still good things to be aware of.

In dynamic programming languages, naming things is vitally important. You don’t have a type to tell you what the variable contains. The variable names are your only lifeline. Don’t be the Titanic: have enough lifeboats.

This video explains my stance on this better than I ever could:

LINK/IMBED--->  https://www.youtube.com/watch?v=YklKUuDpX5c 

Basically, your name needs to be as specific as you can possibly make it to try to make the code as self documenting as possible. You don’t have a type to self document.

In Python, if you misname something and the name you accidently put in is a live variable name, you’re gonna have a bad time. My fix is to get a plugin that highlights each name that’s in scope of the current word you are typing.

This is pretty self explanatory. If you have a variable named ‘url’ and ‘uri’ in the same scope and you accidently use the wrong one, you’re going to have to run the program and have it crash (or, even worse, run correctly with bad values) before you catch the bug.

If you have:
```
from library import thing1
from library import thing 2
....
from library import things more than 3
```
Then just import the damn library. I have several files with 10-30 lines of imports that could be done with much less and I haven’t gone back to refactor that problem out because it will require me to modify thousands of lines of code. It’s just not worth the effort at this point, I have other low hanging fruit to fix. But this is still a good thing to keep in mind for future projects.

Even if your application doesn’t have performance as a primary concern, you will run into performance problems. Make sure to stress test.

This example is specific to web application, but the concept applies to all software.

Your stress test can be as simple as creating 25 VMs that all just request your website’s home page. Try putting way more data into your database(s) than you think your project will ever contain and see how each page responds. Test your software in a broken state: i.e., disconnect databases, disconnect the internet, etc.

You will need a tutorial for all non-trivial software. Users will miss giant red banners at the top of the screen.

No really, they will literally miss the giant bright red banners at the top of their screen. And not just one of your users, a large chunk. A person may be smart, but people in general tend to be pretty dumb.

Have a test server that is a exact copy of the production server. This way you can test a deployment before you actually deploy it.

...not that I would have pushed bad code to the production server or anything...

If you set up the test server in a VM all you have to do is copy over the production server and set up a new DNS configuration for the production server.

Virtual machines make life so much easier, especially when it comes to being able to spawn a new server that’s a carbon copy of your production server. Just make sure it doesn’t utilize the production database(s). 

If your website is going to have more than one Javascript or CSS file, learn how to bundle them.

The number one thing you can do to increase your first visit performance is to bundle and compress Javascript and CSS files. [According to Yahoo.com, the number one performance gain you should work on is the load time for a user’s first visit](http://developer.yahoo.com/performance/rules.html ).  In Flask, [you can do this by using flask-assets]( http://elsdoerfer.name/docs/flask-assets/ ). 

After bundling and compressing my Javascript and CSS files, my web application went from a 300ms first access under “heavy” load to 75ms first visit. Not bad considering that the Google homepage takes almost a second for first visit.

If you run into a line of code that you wrote and you still need to take a second to figure it out, you need a comment.

This is pretty self-explanatory. If you’re struggling with your own code then you should expect anyone else that reads that code to feel like their brain is being hit by a porcelain brick. 

Never assume a service will be running.

I can’t go into the specifics for this one, but I believe it’s sufficient to say that you should never assume a service, a server, or even a local daemon will be running (or running correctly). Never trust, always verify. Especially because if your code breaks because another website is down, people won't care that it wasn’t your fault.

If you’ve made it this far, then I think a pat on the back is in order. Feel free to disagree with, correct, or further educate me. I’m at least good enough to be a professional programmer, but I’m not going to even pretend that I’m a true expert on this subject. If there’s one thing that truly sunk in this summer, while I was surrounded by truly smart and knowledgeable individuals, it’s that in the grand scheme of things, I am a baby in this profession still.




