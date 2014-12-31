Title: PyCon 2014
Date: 2014-03-11 10:20
Modified: 2014-11-29 10:20
Category: Programming
Tags: Programming,Python,PyCon
Authors: Alex Lord
Summary: Everything I remmeber and wrote down from PyCon

So, I went to PyCon US this year. The short of it was that PyCon is amazing. Easily the best organized convention I’ve ever been to. I haven’t been to too many tech conventions, so that may not be saying much. 

PyCon US is partitioned into Tutorials, Talks, and Sprints . This year there were two days of tutorials, three days of talks, and four days of sprints. The tutorials are two blocks of three hours classes. The first two days of talks had a Keynote at 9AM until 10AM and then five different speakers every 45 minutes from 11AM to 5:40 PM. The topics covered everything from machine learning, to garbage collection, to security,  [to analyzing rap lyrics](https://us.pycon.org/2014/schedule/tutorials/). Here's the talk [schedule if you want to get a feel for the topics at the conference.](pycon.org/2014/schedule/talks/) 

[My favorite part of PyCon, however, were the sprints](https://us.pycon.org/2014/community/sprints/). Sprint leaders (mostly project leads, but some weren’t) would describe what the state of their project was and what they would like to accomplish by the end of the four days. A very abbreviated list of projects sprinted on are: `CPython`, `PyPy`, `IPython`, `Apache Allure`, `Twisted`, `SaltStack`, `Mercurial`, `Django`. Many of the core developers for these projects are present at the sprint and are willing to teach or mentor in exchange for some grease work. 

I feel that working on CPython and talking to the core developers was hugely beneficial to my personal development as a programmer. Just being in the same room as the Mercurial sprint taught me a lot about how revision control works and what trade-offs Mercurial has made in comparison to other revision control systems. 

One thing I found pleasantly surprising was the number of not only female attendees at PyCon US, but the number of female speakers. According to the opening statement, PyCon US had a little over 100 talks and 33% of the speakers were female. Many tech conferences boast when they have 1-3 female speakers and a 5-10% female attendance. I was really struck with how open and inviting the conference felt as a whole.

As with all endeavours in my life, I made a couple of large (and in one case, costly) mistakes. The first of which is that I didn’t have a working laptop going into PyCon. I thought (naively) that I could make it without a laptop. But I realized after my first afternoon of tutorials that in order to really learn most of what was being taught, I needed to work through and break the material given to the class. I immediately rented a laptop (which costed an arm and a leg) and never for a second felt like it was a bad investment.

The second mistake I made was not having any business cards. I had 34 business cards to go through when I returned home. Even just one week later I remember the people who gave me a card more than those who didn’t.

I had a rude awakening in Canada when it came to data usage. In America I have a smart phone that can do things. Lots of things that I have gotten very used to having. I thought I could supplement my mobile usage with Wi-Fi. The PyCon Wifi is barely fast enough to load static HTML files. It wasn’t even fast enough to pip install something. I really need to Think about my mobile data usage and Prepare my laptop going to any tech conference. 

 One general project tip I picked up from the development sprints was to always have the current project version as the first thing on the readme file (if not all project files). There were several times where I was working on the wrong version of code because projects either had version numbers in weird places or missing altogether. I also learned that I like it when people name their development branches after the version they’re working towards. 

From here on out I’m going to cover some specific topics and things I learned at PyCon. Some of this may seem very simple to some of you while other pieces are going to be incredible specific and too detailed. These topics are self contained units, you don’t need to read them sequentially or at all to understand the rest. 

###CPython

One thing I picked up at PyCon is that virtual_env makes a set of symbolic links to the referenced Python installation. By installing something to the virtual_env, then it will only be installed to that virtual_env. But installing something to the linked Python instance (say the base instance), then that will also show up in the virtual_env. This can lead to a lot of confusion and make it very hard to figure out what version of a package is actually being used by Python.
Pythonbrew is a Mac exclusive solution to this problem. Python 3.4 comes with a tool called pyvenv which has support for separate Python binaries as well as site and package directories. 
One thing that surprised me was that pip doesn’t install as the current user by default. If installing as the current user is desired then use the --user option.

One talk pointed out that import is, at its core, basically just a implicit namespace (the module name being the namespace unless you use the as syntax) with an exec of the files in the module. This actually helped me really understand a lot of my frustrations with import errors (or errors that happen in a module but are reported as a bad import). Also, this finally cleared up what the difference between what a Python module and package is. A module is a Python source file, a package is a directory of Python source files (modules).
Here’s a cool, though I don’t know how useful, import fact. There’s a buildin function called reload that will re-exec a module. I heard about this when someone was talking about how Django renders server side changes without a http server restart.

[Python (2.7+) comes with an OrderedDict](https://docs.python.org/2/library/collections.html), which is a dictionary that remembers the order in which elements were inserted. I’m assuming that an OrderedDict is just a list of (key, value) pairs that has its access and insert methods

in a C Module. The example use cases for an OrderedDict are XML/HTML processing libraries or parsing HTTP headers. 
One thing I found interesting is that Python lists have a 94% space utilization on average. Dicts on the other hand have a minimum of 33% of their allocated space unused and a maximum of ~50%, which is what is expected from a generic key hash data structure. 
In newer version of CPython (2.6 with object slots, 3.2+ by default, and almost all versions of PyPy by default), objects have less time and space overhead than dicts. Use objects when an arbitrary number of references isn’t required. IE. if a struct would have worked in C then use a NamedTuple or Object. This one really caught me by surprise.

[On a similar note, use the __slots__ attribute if possible ](https://stackoverflow.com/questions/1336791/dictionary-vs-object-which-is-more-efficient-and-why/1336829#1336829).
__dict__ is not necessarily a dictionary even if it exposes (most) of the same methods as a dictionary. 

    "Every problem in computer science can be solved with another layer of indirection." - David Wheeler    

###IPython

A large number of presentations, classes, and open spaces at PyCon came with an IPython notebook. I can’t even begin to explain how excited I am about IPython. It’s an enhanced version of CPython that comes with a large amount of convenience functionality. The big ones that I remember off the top of my head are the ?, ??, %timeit, %%time, %run, %edit, History, interpreter shell commands, and startup files.

My favorite examples are the ? and ?? operators. ? will give present the docstring for any object, ?? will show the source code. 

[More information can be found athte ipython tutorial](http://ipython.org/ipython-doc/stable/interactive/tutorial.html)

Probably one of the best features of IPython, however, is the browser-based IPython notebooks. These are Python interpreters embedded in a web browsable format. IPython notebooks come with a URL and can be hosted as a dynamic page either locally or via a Mod_wsgi enabled web server. Github will host a set of IPython notebooks on their network for free.

[IPython notebooks have support for simple markdown, Latex, CPython code, and a large number of other DLS markups.](http://nbviewer.ipython.org/github/ipython/ipython/blob/master/examples/Notebook/Running%20Code.ipynb) These things are seriously awesome, they’re so intuitive that it’s just easier to [run one on your own then listen to me prattle on about them.](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks)

Probably my favorite part about this is that there is now work being done to have the `IPython` model work for many other languages like, `IHaskell` notebooks, `IGo`, `IScala`, `IClosure`, etc. 

###Sphinx and Hieroglyph

[I didn’t work with Sphinx or Hieroglyph enough to really get a feel for either tool, but I’m very interested in how both of them work.](http://sphinx-doc.org/)  Sphinx is a docfile generation tool which is used to build html, latex (pdf by extension), man pages, xml, or plain text documentation. By producing the first set of documentation all the other kinds of documentation come for free.

From what I’ve seen, Sphinx takes a little bit of configuration and getting used to, so it seems like it’s built for decent sized project to really see the benefits. Next time I write something that needs HTML and a man page I’ll be trying out Sphinx.
    
 I’ll also be trying Hieroglyph next time I give some kind of presentation. It’s a tool that is built on top of Sphinx which generates HTML presentations. 

###Twisted

I have heard of the Twisted project before, but I didn’t really understand what it was or what it might be useful for. I still haven’t used the library (much) but I now understand that out of the box it’s able to parse and construct network protocol connections. It’s useful for sending and receiving standard OSI network protocols (TCIP, SMTP, POP3, IMAP) and comes with support for custom protocols. 
This is not immediately useful to me personally, but given some of the projects I want to work on in the future this will become useful knowledge down the road. 
    And no, asyncio.py does not replace Twisted... or so I was forcefully told.  

###Message passing frameworks
This is one topic that is very immediately useful to me. I’ve been looking into distributed messaging brokers with the intent of finding the system best suited to create a distributed job broker.
    I don’t know much about most of these tools, so I’m just going to list them off in the order in which I’m going to investigate them. The one message broker I’ve used before is RabbitMQ, other then that:  GearMan,  ZeroMQ, Celery, ActiveMQ. I would love to hear peoples thoughts on this topic.

###Machine Learning
    
This is by far the topic that I spent the most time at PyCon learning about. I came into PyCon with almost no understanding of how machine learning works and now I feel like I know just enough to be dangerous to those sitting in close proximity. Basically, bring a large pinch of salt.
    If you’re interested, this is a link to a IPython Notebook which will walk you through the basics of machine learning. Absolutely wonderful tutorial. https://github.com/jakevdp/sklearn_pycon2014

To start off with let’s talk about some practical applications to machine learning, specifically projects that I think are worth pursuing. I would love to take the bugzilla database at my work as a test and training data set and then guess the chance that a new bug is a product bug, configuration bug, or any other number of useful categorizations. The next step would be for all, known and new, product bugs guess what section of code the bug is most likely found in. If I can get a program that has a reasonable amount of accuracy (say 75% for arguments sake) then this would be very useful. I find the concept of having computers accurately predict and categorize fascinating. 

Cool story and all, but how does one actually turn a computer into a more accurate magic 8-ball? The basic idea behind machine learning can be summed up into 5 parts: Acquiring data, feature scaling (making data uniform), choosing an algorithm (sometimes called a model), applying the algorithm to the data (called data fitting), and validation. 

The three hard parts are acquiring the data, feature scaling, and validation. Scikit-learn already comes with a large number of ML algorithms and a processes to fit the data to the algorithm. Acquiring the data is exactly what it sounds like. I’d like to answer how one does data acquisition but the instructor glossed over that detail. Someone in the class asked “how do I learn to gather data” and the instructor’s answer was “go to college.”

Feature scaling is what the database world refers to as normalization. Normally a preprocessor which makes sure the data set the algorithm is going to work on uses the same assumptions. The suggestions given in class were to make sure the data gathering has constraints on it which don’t allow too little, too much, or malformed data. The other major alternative is to take an existing database and chop off the pieces which break the code. 

The example that I was given at PyCon was attempting to do image analysis on a set of thumbnails that all have different resolutions. Running a ML algorithm against a set of images with different resolutions will produce garbage. In the IPython notebook I linked to they use a PCA (principal component analysis) to drop sections of the example database. 

The specific technologies we used in the tutorials were: scikit-learn, Pandas, Numpy, SciPy, and MatPlotLib.  Scikit-learn is built on top of Numpy, SciPy, and MatPlotLib. It’s open source and uses the BSD license. Created make data preprocessing, classification, regression, and clustering an easier proposition. Scikit-learn is the reason why choosing an algorithm and fitting the data to that algorithm is one of the easiest parts of machine learning. The developers of scikit-learn have taken the portion of ML that used to be the hard part and trivialized it. The example page for a Support Vector Machine shows just how simple the process of using the [scikit-learn](http://scikit-learn.org/stable/modules/svm.html) library is:
```
from sklearn import svm

X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y) 
clf.predict([[2., 2.]])
```
Taken from: 
Numpy and SciPy are two Python libraries built to address two of CPython’s (the standard Python implementation) major faults: Speed of computation and memory use. According to these benchmarks (https://stackoverflow.com/questions/7596612/benchmarking-python-vs-c-using-blas-and-numpy) there is very little to no difference between c++ and Python. Both NumPy and SciPy use less memory than native Python data structures but I don’t know what the difference is and I’m having trouble finding documentation that shows conclusive benchmarks. Topic for another time. 

MatPlotLib is a Mathlab-like 2D plotting framework. It makes it very easy to produce visualizations of all the datasets that scikit-learn and Pandas produce. [I’m especially fond of the seaborn extension to MatPlotLib.](http://www.stanford.edu/~mwaskom/software/seaborn/examples/index.html) Seaborn is simple and produces high quality visualizations with little to no effort on the programmer's part. I view it almost as the [Twitter Bootstrap](http://getbootstrap.com/) of data visualization.

There are two major types of machine learning algorithms, supervised and unsupervised. Unsupervised ML algorithms are a set of algorithms that take in a dataset and attempt to group data which is similar. [This SO answer does a pretty good job of explaining the differences](https://stackoverflow.com/questions/1832076/what-is-the-difference-between-supervised-learning-and-unsupervised-learning) but I’m going to try to put it into my own words anyway. 
Supervised means a dataset that contains data and some kind of classification of the data. Normally in supervised learning a human has gone through each portion of the data and set the classification by hand (thus the supervised part).  The dataset is split into a “training” and “test” set, normally a 75% and 25% split respectively. The algorithm “learns” from the training set and then attempts to guess what the right classification is on the training set. The assumption is that the human guess are “correct” often enough that there is something to test against. This makes it very easy to validate a model’s fit of the data. 

Unsupervised means the dataset doesn’t come pre-categorized. So the algorithm attempts to create a set of classifications or categorizes based on patterns it finds in the dataset. This requires much less effort on the part of the programmer but the results are much less trustworthy. In general unsupervised algorithms are much more susceptible to outliers,  poor feature scaling, and ambiguity. They algorithms also tend to be more sensitive to certain kinds of patterns and less sensitive to others. As such the false positive and false negative rate is higher. The verification processes is also more difficult with unsupervised algorithms. 

Sadly the class that was supposed to cover Model verification didn’t get to the topic. This is something that I’ll have to look into at a later time. Here’s a short list of jargon that was thrown out (in very quick succession) of things one can use to verify a model: RMSE, precision, recall score,  f-score, ROC curves, cost curves. What any of that means is a mystery to me (at the time of this writing at least). 
Here are some miscellaneous notes that I found useful but couldn’t quite fit into the rest of this write-up:

###sklearn
_ prefix means that the method or component are uninitialized until after the data fit. 

###supervised 
Large amounts of uncertainty tend to break support vector machines. 
        
###Numpy

numpy array slicing has been overridden. Don’t expect it to act like normal array slicing.

numpy slices return references, not copies. 

Don't use strings. I learned this the hard way. Convert strings to integers if possible. 


###Pandas
`dropna()` is a great way to remove null data.
`Pd.get_dummies` is useful for changing data to an enumerated type.
Passing mixed data to pandas then Panda will insert everything as an object. 

###Conda
I’ve been informed that if I want to do any amount of scientific computing in Python i should use Conda as my package manager. Having never used it myself I don’t know about the validity of this claim. 

`NOTE: `after having used Conda I've come to the conclusion that I prefer to use a default python installation and to manage my own packages by hand. Conda includes a lot of libraries I don't use (all the time, for every project) and it gets hard to manage production deployments when you list of installed packages is in the two hundreds.


###Partitioning is the heart of scaling 

One thing many of the talks focused on (especially the ones that were web focused) is how important it is, for performance reasons, to be able to partition a technology stack. The classic web example of this concept is sticking a web server and database on different servers. The traditional software engineering way of stating this is that low coupling is very important.

For some reason I’ve always paid attention to the security benefits of separating a web server from the database server. I’ve also heard people talk about performance reasons but I’ve never understood that. Doesn’t putting these services on different servers now mean they have to at least deal with network latency? But the thing I never really understood is that the network is not always the system bottleneck. It’s only been my bottleneck because everything I’ve written has been so simple. It is becoming more important now that I want to do things like e-mail a list of users upon some action, change a page’s url and the thousands of references to that page, or build a categorization for the data a user is attempting to submit as a bug report. 

And that made me realize that partitioning a system allows for isolation of hot spots. Partitioning allows me to focus system resources on the overloaded portions of the system. This is the same pattern I follow when I’m attempting to solve a performance problem in code (profile, isolate, refactor) just applied to a system or service rather than functions or classes. 

###Local outreach
[There was an interesting keynote given by Jessica McKellar that talked about teaching Python in schools.](https://www.youtube.com/watch?v=4QOoAw6Su7M) Specifically the sorry state of programming education in the United States and her opinions on how the Python programming language could help that.


###Flask

[Flask is my web framework of choice when I do web development. I went a talk called “Developing Flask Extensions” and came away with some interesting ideas](https://www.youtube.com/watch?v=OXN3wuHUBP0). Probably the biggest thing that I came away with is that the `@app` decorator is the heart of the Flask framework. Extensions to Flask will ultimately change the properties of the `@app` decorator. 

####Some cool extensions that I got to play with are:

`Flask-Debugtoolbar : `This is a flask port of the Django debug toolbar. This thing is seven kinds of amazing. It displays a huge amount of debugging information and makes it very easy to see the state of a web application.

`Flask-WTF :` I’m a big fan of WTForms. This is a flask extension that makes integrating with WTForms a very simple task. If you are writing web applications in Python that will use web forms than `Flask-WTF` is something you should seriously consider. Another option is `Flask-SeaSurf`.

`Flask-Admin `: Another port of a Django feature. This gives many (not all) of the features that the default Django admin page.

These are just the extension that I played with at PyCon. [A much larger (but still not exhaustive) list can be found at](http://flask.pocoo.org/extensions/).

###Subprocessing
This is going to sound dumb to anyone that’s used Python for scripting purposes, but there’s a module called subprocess and it’s awesome. The things one learns...
```
import subprocess
    subprocess.call(['git', 'clone', git_url])
```
###Security

I’m not a security expert and am definitely not a web security expert. But these videos were interesting to me. I’m just going to leave these links here on the chance that you want to know more about these topics. 

[The Sorry State of SSL.](https://www.youtube.com/watch?v=SBQB_yS2K4M) This was a fun (and slightly terrifying) meander through SSL libraries. 

[Quick Wins for Better Website Security](https://www.youtube.com/watch?v=T-5p5ewqhVw). I knew most of these topics previous to the talk (IE, it's pretty basic security) but this is a decent introduction to web security. 

[Building and breaking a Python sandbox](https://www.youtube.com/watch?v=sL_syMmRkoU) . This was one of my favorite talks at PyCon. It does such a fantastic job of showing you the complexity that a "secure" system has to battle against. It's also a really cool way to talk about the internals of the Python language. 

[Shiny, Let's Be Bad Guys: Exploiting and Mitigating the Top 10](https://www.youtube.com/watch?v=nQOahpei6kw). I know that the video time says three hours for this one but you'll be fast forwarding through a lot of it. If you want hands on experience with breaking into systems I highly recommend this tutorial.

If you're at all interested in web security I suggest going to [OWASP](https://www.owasp.org/index.php/Main_Page) and [Qualys SSL Labs](https://www.ssllabs.com/ssltest/)

###Dynamic Code Analysis. 
I’ve always been a fan of Pylint and coverage.py. I believe that they’re very useful tools and produce cleaner code. But I was introduced to a tool called flake8 which is a combination of pep8, pyflakes, and a cyclomatic complexity checker. Pylint freaks out at Mixins and since Flask uses so many mixin’s I’ve been having a hard time using Pylint on flask projects. I’ve been using flake8 as a fallback when Pylint is too strict.
        
##Cool PyCon Talks that didn't fit anywhere
[Here's all the videos](http://pyvideo.org/category/50/pycon-us-2014)

[Augie Fackler, Nathaniel Manista / Deliver Your Software In An Envelope](https://www.youtube.com/watch?v=mTj297sGzxw)

[Alex Gaynor / Fast Python, Slow Python](https://www.youtube.com/watch?v=7eeEf_rAJds)

[Allison Kaptur / Import-ant Decisions](https://www.youtube.com/watch?v=aS5kXzbsLLQ)


So that was my PyCon 2014 experience. I hope you had fun reading. As always I'm open to feedback on both my technical chops and my writing abilities. 

