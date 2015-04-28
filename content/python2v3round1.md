Title: Python2 vs Python3, Round 1
Date: 2015-04-27
Category: Programming
Tags: python,python3,porting
Authors: Alex Lord
Summary: The future_builtins module.

#Hello World,

This is going to the be the first in a three part series on the changes between Python 2.7 and Python 3.4. This first blog post is going to focus on what’s different in the builtin functions and other language changes.

I originally started writing this post with a grand plan of how the series was supposed to proceed. And just as all plans go my didn’t survive the first contact with the enemy (whoever the enemy is in this case). So I’ll just keep it simple and state that I want to talk about the differences between Python2’s and Python3’s builtins, How to deal with the dependency problem porting to Python3 can cause, and an example of porting a simple package from python2 to python3.

# A Plea To The Audience

The focus of this series is to talk about what's new in Python3 for those at are used to Python2. A secondary goal is to help maintainers be both Python2 and Python3 
compatible.

To start with you should not support both Python2.x and Python3.x. [If you want to see how much of a hassle it can be for some projects go read about mercurial’s experience porting to 3](http://mercurial.selenic.com/wiki/SupportedPythonVersions#Python_3.x_support). Supporting both is somewhere between hauling Sisyphus with his boulder and walking on a slightly broken toe. If you are building something new just build it in Python3. [If you inherit a python2.x code base there are some very compelling reasons in 3.5 to port.](https://docs.python.org/3/library/asyncio-task.html) There are very few to no reasons to support both version unless you’re making a community package that lives and dies off both 2 and 3.

[If you are a package maintainer for something used by a lot of people](http://flask.pocoo.org/) then there are ways to shore up your code and survive the onslought of porting bugs.

With all of that said

# future_builtins Will Save Your Ass

If you use repr, filter, hex, map, oct, or zip in your code base than the future_builtins module will keep your bacon in your behind. From the documentation

“This module provides functions that will be builtins in Python 3.0, but that conflict with builtins that already exist in Python 2.x.”

    ascii(arg) -- Returns the canonical string representation of an object.
    
    filter(pred, iterable) -- Returns an iterator yielding those items of iterable for which pred(item) is true.
           
    hex(arg) -- Returns the hexadecimal representation of an integer.
    
    map(func, *iterables) -- Returns an iterator that computes the function using arguments from each of the iterables.
    
    oct(arg) -- Returns the octal representation of an integer.
    
    zip(iter1 [,iter2 [...]]) -- Returns a zip object whose .next() method returns a tuple where the i-th element comes from the i-th iterable argument.


##An Easy Trap to Fall Into

Let's start off by talking about a trap. As with most python traps, it's an import issue. 

    import future_builtins # oh you sad, sad import statement you.

It might seem reasonable, as it did to me, to just import the future_builtins module to get all of the future builtins. Importing all the things is always a good idea or so the internet tells me. Yes, python, give me all the future please.

The only problem with this is that the future_builtins module doesn't, upon importing it, change the behavior of the builtins in question.

###Python2.7
    import future_builtins
    test_list = ["a", "b", "c", "pyladies"]
    filter(lambda x: len(x) > 1, test_list)
    ['pyladies']
    from future_builtins import filter
    filter(lambda x: len(x) > 1, test_list)
    <itertools.ifilter object at 0x10c0af750>


This is a classic bait and switch. We’re promised the future and were told that we needed to ask our question more clearly.

It’s of equally important note that the __future__ module does something very similar.

    print "a"
    a
    import __future__
    print "a"
    a
    from __future__ import print_function
    print "a"
        File "<stdin>", line 1
            print "a"
                    ^
    SyntaxError: invalid syntax

So remember, world, that in the python2 universe if you want the future you need to specifically request portions of the future.

##A Simple Work Around

Ok, that’s a lie. You can specifically request all of the future by using the * operator.

    from future_builtins import *

If you have a library or package which has to support both python 2.x and python 3.x I highly suggest you add

    try:
        from future_builtins import *
    except ImportError:
        # Py3 is already the future
        pass

To make your life more sane. Which is slightly insane because having to write try ... except blocks around imports is slightly insane by most language standards. 

##ascii (also known as “Unicode is hard, escape all the things.”)

If you try to just use ascii in python2.7 you’ll actually get a type error.

    ascii
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'ascii' is not defined

So it’s a bit of a misnomer to say that ascii has a conflict with a python2.7 builtin. In python3 ascii is the replacement for repr's old functionality

    ascii(object)
    As repr(), return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by repr() using \x, \u or \U escapes. This  generates a string similar to that returned by repr() in Python 2.

This doesn’t make a lick of difference for most Python objects.

    repr(unittest)
    "<module 'unittest' from '/usr/lib/python3.4/unittest/__init__.py'>"

    repr(unittest)
    "<module 'unittest' from '/usr/lib/python2.7/unittest/__init__.pyc'>"

Unless, of course, you want to program in languages which aren’t American English. [Wait, why would anyone want to do that?](https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers)

###Python2.7

    class  example:
        def __repr__(self):
            return "漢字"

    repr(example)
    '<class __main__.example at 0x10f89f530>'
       
    example()
    漢字
    ascii(example())
    '\xe6\xbc\xa2\xe5\xad\x97'
    from future_builtins import ascii
    repr(example)
    '<class __main__.example at 0x10f89f530>'

For me it was surprising when importing ascii didn't modify the behavior of repr in python2.7. In retrospect python2 strings and python3 strings get along as well as Caesar and the Roman Senate and it should not be surprising that converting python2 functions to match python3 string outputs would be avoided in the same way that a debtor avoids debt collectors.

###Python3.4

    class  example:
        def __repr__(self):
            return "漢字"
       
    example()
    漢字
    ascii(example())
    '\\u6f22\\u5b57'

One interesting note is that python3.4 and 2.7 chose different character escapes. So really, ascii is only useful if you need to support 2.6 code or you're 2.7 code isn't using unicode strings.

### Interesting Aside

Just as a side note non-ascii characters are now legal class and function name characters in Python3. 


#### Python 3.4

    class  例:
        def __repr__(self):
            return "漢字"
       
    例
    <class '__main__.例'>
    例()
    漢字

####Python2.7

    class  例:                                                                      
    File "<stdin>", line 1                                                                            
    class  例:                                                                                      
           ^                                                                                        
    SyntaxError: invalid syntax     

##filter
[If you haven't used filter much (I hadn't before writing this, which is why I like writing these blog posts) here's a quick little tutorial to get you up to speed.](http://www.u.arizona.edu/~erdmann/mse350/topics/list_comprehensions.html)

###Python 2.7 with


    test_list = ["a", "b", "c", "pyladies"]
    filter(lambda x: len(x) > 1, test_list)
    ['pyladies']
    from future_builtins import filter
    test_list = ["a", "b", "c", "pyladies"]
    filter(lambda x: len(x) > 1, test_list)
    <itertools.ifilter object at 0x10c0af750>
    dir(filter(lambda x: len(x) > 1, test_list))
    ['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'next']

###Python 3.4

    test_list = ["a", "b", "c", "pyladies"]
    filter(lambda x: len(x) > 1, test_list)
    <filter object at 0x1096e2128>
    dir(filter(lambda x: len(x) > 1, test_list))
    ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    for elem in filter(lambda x: len(x) > 1, test_list):
    print(elem)
    pyladies

So there's a couple interesting things going on here. The first of which is that the old filter directly returned a list and the new filter returns an object. Specifically, the new filter returns a generator. Returning a full list means that in the worst case filter forces you to hold every element in the target iterable twice. This is about as terrible as my first hair cut when I first move to Seattle. From both a memory and speed standpoint since it means filter is a O(n^2) memory and O(n^2) run time algorithm. Filter is why we can’t have nice things.

Returning a generator means that you can just return items from the original list. This does mean that if your items are mutable you do have to worry about a generator manipulating the targeted iterable.

The one tradeoff of using a generator is that you can't iterate over the object twice.

    def print_items(a):
        for item in a:
            print(item)
    a = filter(lambda x: len(x) > 1, test_list)
    print_items(a)
    pyladies
    print_items(a)

###Fun note

if you run this on python you will be sad. 

    [str(n) for n in range(10**100)]

If you run this on python2.7 you will still be sad.

    map(str, range(10**100))

If you run that previous statement on python3.4 or run the next example in python2 you will be unsad.
     
    from future_builtins import map
    map(str, range(10**100))

If you run this you will also be un-sad.

    (str(n) for n in range(10**100))


##hex

Hex is fundamentally unchanged in most use cases. What has changed is the [magic method](http://www.rafekettler.com/magicmethods.html) used to get an integer from an object to convert into hex.

[“Works like the built-in hex(), but instead of __hex__() it will use the __index__() method on its argument to get an integer that is then converted to hexadecimal.”](https://docs.python.org/2/library/future_builtins.html)

###example class

For the rest of the hex section this is the example class I used and manipulated.

    class example():
    def __hex__(self):
        return "a"
    def __index__(self):
         return 1

### Misunderstanding __hex_

Just as a note when I first started writing this section I had hex return an integer

    def __hex__(self):
        return 0
        
Which lead to this bit of fun

    hex(example())
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    TypeError: __hex__ returned non-string (type int)

And this is where I learned that the object which is making the __hex__ function is in charge of properly returning a hexadecimal object. Which isn’t a whole lot more complex but it is about the same thing as requiring you to dance before flushing a toilet.

### How is index Different?

index expects an integer or a long and will actually do the transition (since it's simple once you know you have a int) for you.

    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    TypeError: __index__ returned non-(int,long) (type float)
    
    class example():
        def __index__(self):
            return 1
    hex(example())
    '0x1'

This is a pretty clear cut and simple difference. that python3's hex implementation is just better.

##map

[When I was first finding the map function this SO was what really made it stick for me.](https://stackoverflow.com/questions/672172/how-to-use-python-map-and-other-functional-tools) Map is very similar to filter. In fact, if you run this code snippet on Python3

    map_test_list = [1, 2, 3, 4, 5]
    filter_sequence = filter(lambda x: True,    map_test_list)
    print([elem for elem in filter_sequence])
    [1, 2, 3, 4, 5]
    map_sequence = map(lambda x: x, map_test_list)
    print([elem for elem in map_sequence])
    [1, 2, 3, 4, 5]
    
you can see that they are very similar. The first major difference is that map's function takes an [inorder](https://stackoverflow.com/questions/486039/in-order-tree-traversal) traversal of multiple (any number) of iterables which are passed to map. [Generally speaking it's considered more 'pythonic' to use generator, list, or dictionary comprehensions but map, filter, and the other function key-words exist for those who coming from the functional world to Python.](https://stackoverflow.com/questions/1247486/python-list-comprehension-vs-map) I’ve also found that the inorder traversal portion of map makes it less useful than comprehensions.

That being said, what’s different?

    map_test_list = [1, 2, 3, 4, 5]
    map_test_list2 = [6, 7, 8, 9, 10]
    map(lambda x, y: (x + y), map_test_list, map_test_list2)
    [7, 9, 11, 13, 15]

###Python 2.7

    map_test_list = [1, 2, 3, 4, 5]
    map(lambda x: x, map_test_list)
    [1, 2, 3, 4, 5]

###Python 3.4

    map_test_list = [1, 2, 3, 4, 5]
    map(lambda x: x, map_test_list)
    <map object at 0x102dc83c8>

Again, the big change from python2 to 3 is that map returns a generator so that things are lazy loaded to keep sadness at bay.

##oct

[“Works like the built-in oct(), but instead of __oct__() it will use the __index__() method on its argument to get an integer that is then converted to octal.”](https://docs.python.org/2/library/future_builtins.html)

Everything that was said about hex also applies to oct. If you haven't read that section, go read it.

##zip

zip has also been changed to return a generator. This effectively means that zip now acts exactly like python2’s itertools.izip. 

    test_list1 = [1, 2, 3, 4, 5]
    test_list2 = [6, 7, 8, 9, 10]
    zip(test_list1, test_list2)
    <zip object at 0x102dc7848>

A side note is that, for some reason I don't understand, izip was taken out of python3.

    izip
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    NameError: name 'izip' is not defined

I my eye's keeping izip would make porting to 3 easier so I'm not sure why it was removed even if it doesn't have any functional difference between

### Make Your Life Easier By

    try:
        from itertools import izip as zip
    except ImportError:
        # Already the future.
        pass


#Conclusion

If you have a python2 code base and want to start the process of porting to python3 then the future_builtins module is your friend (as well as the uncovered __future__ module).

Maintaining both python2 and python3 compatibility is not your friend. If you have to deal with this not friend, use the future_builtins (and __future__) module to save your bacon.

Of the changes made, hex and oct are the same changes applied to different builtins (using the __index__ magic method rather than the __hex__ or __oct__ methods). filter, map, and zip all now return generators rather than lists (which reduces the amount of tears shed by programmers world round). Lastly, ascii has the same behavior as python 2.6's repr.

I hope you’ve enjoyed reading this or at least found this post informative. Thank you, World, for reading and as always I'd love to hear your feedback.














