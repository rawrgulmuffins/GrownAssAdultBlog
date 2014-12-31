Title: Code Complete Getters and Setters
Date: 2013-05-28 10:20
Modified: 2014-11-29 10:20
Category: Programming
Tags: Python,ProgrammingLanguages
Authors: Alex Lord
Summary: I'm really enjoying Code Complete but the book is a little long in the tooth

[I've been reading Code Complete by Steve McConnell recently](http://www.amazon.com/Code-Complete-Practical-Handbook-Construction/dp/0735619670). The books a good read and has contained solid advice for my lowly student self. [I mainly picked up Code Complete because Jeff AtWood raves about it so often.](http://blog.codinghorror.com/)

I'm on chapter eight and I feel like I've been pumping programming iron. Between all of the reading I've been doing, and putting concepts into practice at work, I feel like my programming abilities are being super charged.

With all of that said, code complete is starting to get a little long in the tooth. I’m reading the second edition which was published in 2004 and it shows. I’m finding it deeply ironic that a book that talks about coupling, in the same fashion that most people talk about government corruption, is so tightly coupled to c++/Visual Basic. 

In chapter six "Working Classes" under the section "Good Encapsulation" McConnell says to never expose member data to the public. He then goes on to say that you should always use getters and setters to access that data. The reasoning behind this is to isolate change (you only have to modify the getter or setter rather than all the code which uses them) and to reduce the programs complexity (The calling code shouldn’t need to know the internal workings of the getter / setter to work). The less nuts and bolts (only changing one function) to replace or modify a part the happier you’ll be when you inevitably have to change that code down the road. 

This sounds perfectly reasonable (and is perfectly reasonable if you're using c++, java, c, ada, etc.). The Funny part about this advice is that you have to write much more upfront code in order to make modification heaps easier down the road (The worst case being two functions for every action / attribute). Sometimes you have to spend some time to save more in the end, right? 

McConnells overall point (Encapsulation good) is great for object oriented programming and very relevant. [His sweeping generalization of how to Encapsulate(Don’t expose member data, use getters / setters) isn’t always relevant.](http://stackoverflow.com/questions/6618002/python-property-versus-getters-and-setters)

[The way that dynamic interpreted languages work is a little different](http://dirtsimple.org/2004/12/python-is-not-java.html). Let's use Python as a counter example to McConnell's statement. if I wanted to make a class in Python i'd say
```
class samurai():
    def __init__ (self):
        self.sword = “a freaking Katana.”
jack = samurai()
Black = samurai()
Print (jack.sword)
Print (black.sword)
```

Under McConnell's good encapsulation example this would be terrible because you're directly accessing member data. If this was c++ I’d have to change my print statements if I wanted to modify the .sword attribute (and if you have thousands of .sword access in c++ that’s a lot of copy-replace). And just to be clear I am accessing the public member of the samurai class in this example. But this doesn't actually break encapsulation in Python because you can change the default ([using the @propert and @setter decorators](https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work)) accessor function if you find the need to do so.

```
class samurai():
    @property
    def Sword(self): 
        """ getter which is used by the syntax samurai.sword"""
        #add your new code here! It’s magic!
        Return self.value
        
@sword.setter
    def Sword(self, value):
        """ setter which is used by the syntax samurai.sword = value"""
        #I’m here just for good measure.
        Self.value = value
```

Which means you get the best of both worlds. You don’t have the upfront cost of writing a getter and setter for every attribute  (having written about 200 of those in one sitting for a java project this can be “fun”) and you also get the lower cost of modification / complexity that getters and setters gives you. 

Side note, you can create "read only" attributes by creating a setter that throws an error or does nothing. I prefer my mistakes to die screaming.

```
class samurai():
    def __init__ (self):
        self._sword = “a freaking read only katana”

    @property
    def Sword(self): 
        """ getter which is used by the syntax samurai.sword"""
        #add your new code here! It’s magic!
        Return self._sword
            
    @samurai.setter
    def x(self, value):
        raise NotImplementedError()
```

[The original point of getters and setters was to reduce complexity](http://stackoverflow.com/questions/1554546/when-and-how-to-use-the-builtin-function-property-in-python). Ironically enough sometimes they now add more complexity if you’re language is flexible enough. 

Did I mention that Code Complete is awesome? I think I did but I can’t remember with all the ragging I’ve done recently. 
