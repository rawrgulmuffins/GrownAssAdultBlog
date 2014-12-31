Title: Learning to not hate python regular expressions
Date: 2014-09-29 10:20
Modified: 2014-11-29 10:20
Category: Programming
Tags: Programming,Python,PyCon
Authors: Alex Lord
Summary: It turns out, regular expressions can be super useful

I have a secret to share. It’s not an airplane-sized secret but it’s also not mouse-sized either. More antelope than anything else.

I like regular expressions.

There, I said it. No, I won’t take that back, thank you very much. 

Many programmers out there will be saying, “Well of course you like regular expressions, you’re a programmer.” They will not understand where the other camp comes from and assume that camp is insane. Others of you will hear the quote:

[“Some people, when confronted with a problem, think ‘I know, I'll use regular expressions.’ Now they have two problems.” - Fredrik Lundh](http://regex.info/blog/2006-09-15/247)

And I used to be one of you, two problems people. Trust me, I know how you feel. But I have been shown the light. I have seen the other side of the tunnel and I have discovered that regex can, in fact, solve useful problems. I know that sounds about as appealing as eating a fist full of bark to those two problems people out there, but stick with me on this one.

I got handed this mess about three weeks ago:

`Cluster_Totals:.*?([0-9.]*[KMGTPE])\s*/\s*([0-9.]*[KMGTPE])\(\<\s[0-9.]*\%\)\|\s([0-9.]*[KMGTPE])\/\s([0-9.]*[KMGTPE])`

And it made me sad. Not quite "Pandas are going extinct because they think sex is cootieful" sad. Around "I was looking forward to eating that ice cream before I dropped it" sad. As someone who disliked regular expressions and avoided using it in his own code, this was a nightmare. This is the stuff that Disney witches brew in cauldrons to sprinkle on unsuspecting baby dwarfs to make their beards fall off. I took one look at that mess and almost rewrote 400 lines of code just to avoid one line of regex.

[First of all, if you ever catch yourself saying, “I could rewrite this better from scratch,” then stop what you're doing and apply your open palm to the side of your face. Afterwards, read Joel Spolsky’s blog about starting from scratch to save yourself from more pain.](http://www.joelonsoftware.com/articles/fog0000000069.html)


That article lays out why this is normally a really dumb idea better than I ever will. But I speak a tautology because Spolsky makes me feel as articulate as a drooling rock. 

But second of all (and more importantly), regular expressions are not that scary. The first thing I did that really helped out was finding an interactive source that allowed me to toy with my regular expression and see exactly what matched and didn’t match easily. [In this case I lucked out and found a web application that does just that](https://pythex.org/). I also having beeing using [pythonregex](http://www.pythonregex.com/) Because it showed what running several different python regex methods would produce.

I'm continually amazed at the kind of applications which live on the web currently. Hell, [I found a online java compiler just the other week.](http://www.compileonline.com/compile_java_online.php)

Next, I got a bunch of examples from the data sets that I wanted to get my matches from and put them into my unit tests. I ended up with test strings that looked like:

```
 11|None           |-A-- |  14K|    0|  14K|  32G/  93T(< 1%)|    (No SSDs)    
-------------------+-----+-----+-----+-----+-----------------+-----------------
Cluster Totals:          | 439K|  11M|  12M| 2.2T/ 323T(< 1%)| 2.1G/ 1.4T(< 1%)
```

and produced expected dictionaries that looked like:

`{‘hdd_used’:’2.2T’, ‘hdd_total’:’323T’, ‘ssd_used’:’2.1G’, ‘ssd_total’:’1.4T’} `

or

`{‘hdd_used’:’2.2T’, ‘hdd_total’:’323T’, ‘ssd_used’:None, ‘ssd_total’:’None} `

I can not express how useful writing all of those unit tests were for learning how to properly use regular expressions, especially how regex groups work. Writing the unit tests before the code forced me to think in terms of what input lead to what output and this change in mindset made things vastly easier.

The last thing that I did was to start breaking apart the original regex looking for patterns. As a refresher:

`Cluster_Totals:.*?([0-9.]*[KMGTPE])\s*/\s*([0-9.]*[KMGTPE])\(\<\s[0-9.]*\%\)\|\s([0-9.]*[KMGTPE])\/\s([0-9.]*[KMGTPE])`

The first thing that really popped out was the `([0-9.]*[KMGTPE])` sections and the` Cluster_Totals:.*? `section.

I started splitting the regular expression up into chunks.
```
preamble = Cluster_Totals:.*?
totals_grouping = ([0-9.]*[KMGTPE])\s*/\s*([0-9.]*[KMGTPE])
```
which lead to 
```
regex.compile(preamble + totals_grouping + “(\<\s[0-9.]*\%\)\|\s” + totals_grouping)
```
Which leads me to why I originally had to tackle this regex in the first place. There were many log sets that I was attempting to run this search over which contained data that looked like the example I gave but contained subtle differences in the middle formatting. If the formatting in the middle didn’t match, then the regex would just ignore the match. There were also some cases where the last grouping didn’t exist. So I changed the final result to look like  
```
ssd_regex = regex.compile(preamble + totals_grouping + “.*?” + totals_grouping)
hdd_only_regex = regex.compile(preamble + totals_grouping + “.*?” + \(No SSD\))
```
One little tip that I learned the hard way is to always include a ? at the end of a splat (*) operator unless you want that sucker to soak up every last bit of text it can find. Also, since the splat operator will cause the regex engine to attempt a greedy algorithm to match every character, you’ll significantly increase the computation time of any match or search by not including the ? operator.

I’ve also been using regex to check to see if text from web forms matches the formatting that I’ve been expecting. Example being:

`re.findall("((http|https)://legacy.*/)", field.data)`

It’s a very simple task but it uses significantly less code than if I attempt to do multiple `string.find()` operations. 

[On a similar note, if you have a large blog of text and you don't want to cause a second allocation than `re.finditer(iterable_object)` is awesome.](https://docs.python.org/2/library/re.html#re.finditer)

There we have it. Regex can be about as intimidating as a fire-breathing dragon but once you get close enough, you realize it’s a tiny fire-breathing dragon. 




