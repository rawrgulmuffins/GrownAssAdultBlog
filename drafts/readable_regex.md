Title: The Readable Regex
Date: 10/16/2016
Category: Programming
Tags: regex, searching, readability, code style
Authors: Alex LordThorsen
Summary: Readability Is Maintainability

# Acknowledgement

A lot of what I'm going to write about in here comes from working with my
teammates Ethan Madden, Ed Hodapp, and Max Payton at Isilon. My team has done
a good job of fostering a drive to create excessively readable code and this
essay contains a set of codified methods created by that drive.

# The Readable Regex

There have been times when I have read regular expressions and felt like it
would have been more useful to devine it's hidden meaning by throwing physical
versions of each character into a bowl and stirring until it made sense.

And no, I'm not just compalining about other peoples code. I've done this to
myself. 

# Some Examples

Let's throw some examples on the table for those who haven't had the pleasure
of being introduced. Also to stirr up some anxiety in the unfortunate.

We have this lovely speciment here

    re.compile(r'(^\S.+) +(\d+) +(\d+) +([\-\d]+) +([\-\d]+)\% +(\d+) +(\d+) +([\-\d]+)\% +(.+)', re.MULTILINE)

Not bad, not terrible. An example string that this matches is

    < Insert Example >

This is almost marginally readable and it only took me a solid 5 minutes of
reading the reference manual to figure it all out.

Then we have this bit of minor nightmare fuel

    re.compile(r'^\s*PID\s*USERNAME\s*THR\s*PRI\s*NICE\s*SIZE\s*RES\s*STATE\s*TIME\s*WCPU\s*COMMAND\s*$', re.MULTILINE)
    re.compile('^(?P<pid>[ \d]{5}) (?P<username>.{8,}) +(?P<thr>[\d]{1,5}) (?P<pri>.{3}) (?P<nice>.{4}) (?P<size>.{6}) (?P<res>.{6}) (?P<state>.{6}) (?P<time>.{6}) (?P<wcpu>.{5,6})\% (?P<command>.*)'
    re.compile(r'^\s*PID\s*USERNAME\s*THR\s*PRI\s*NICE\s*SIZE\s*RES\s*STATE\s*C\s*TIME\s*WCPU\s*COMMAND\s*$'
    re.compile(^(?P<pid>[ \d]{5}) (?P<username>.{8,}) +(?P<thr>[\d]{1,5}) (?P<pri>.{3}) (?P<nice>.{4}) (?P<size>.{6}) (?P<res>.{6}) (?P<state>.{6}) +(?P<c>\d{1,2}) (?P<time>.{6}) (?P<wcpu>.{5,6})\% (?P<command>.*)'

I don't know about you but this kind of reads like a compressed word typhoon.

The output it parses is

    < Insert Example >

Just in case you feel like this is all moaning without substance here's the
most complex regular expression I've ever seen in my life

    < Insert MIME protocol regex expression >

This parsers MIME complient e-mails like this contrived example

    <Insert Example>

Now that I've shown you what code car crashes look like let's start building
some safety features into our practice.

# Examples Matter

## Raw regex

Let's make an example regex that reads hard drive SMART data and let's put it
in the style and format that most regular expressions are written with.

    r'^(Carrier board|Internal)\s+(\w+\d+)/([a-z]+\d+)\s+is\s+(.+)\s+FW:([\w\. ]+)\s+SN:([\w\-]+),?\s+(\d+)\s+blks\n$')

without an example this is a doable mess. A seasoned regular expression vetern
can bust out a manual and work through this blabber mouth in a reasonable
amount of time

But if you suddenly add an example (or multiple if you're feeling frisky)

    # Matches:$
    # Carrier board J3/ad3 is SMART mSATA SG9MST3D32GBM01 FW:Ver7.02w SN:SPG134602B7 62533296 blks$
    r'^(Carrier board|Internal)\s+(\w+\d+)/([a-z]+\d+)\s+is\s+(.+)\s+FW:([\w\. ]+)\s+SN:([\w\-]+),?\s+(\d+)\s+blks\n$')

and all of the sudden you can start assosciating the example characters and
groupings with their regular expression counter parts. It becomes easier to
remember what `|` and `\s+` means when there's an example to walk through.

# Human Sized Groupings

Did you mother even tell you not to eat something larger then your face? Just
my mother? Oh, well that's unfortunate. I think it's good advice.

A "bite sized chunks" rule regular makes regular expressions much more
digestable. Often times I find it simpliest just to break each group into it's
own new line


    # Matches:$
    # Carrier board J3/ad3 is SMART mSATA SG9MST3D32GBM01 FW:Ver7.02w SN:SPG134602B7 62533296 blks$
    r'^'
    r'(Carrier board|Internal)'
    r'\s+'
    r'(\w+\d+)'
    r'/'
    r'([a-z]+\d+)'
    r'\s+is\s+'
    r'(.+)'
    r'\s+FW:'
    r'([\w\. ]+)'
    r'\s+SN:'
    r'([\w\-]+)'
    r',?\s+'
    r'(\d+)'
    r'\s+blks\n$')'

One thing that's immediately recongnizable from this new format is what data
will be captured by groups and what patterns are just syntatically important.

This is an improvement but we can still do better.


# Named Groups

    # Matches:$
    # Carrier board J3/ad3 is SMART mSATA SG9MST3D32GBM01 FW:Ver7.02w SN:SPG134602B7 62533296 blks$
    r'^'
    r'(?P<type>Carrier board|Internal)' # Drive Type
    r'\s+'
    r'(?P<id>\w+\d+)'                   # Drive ID
    r'/'
    r'(?P<device>[a-z]+\d+)'            # Full Device Name.
    r'\s+is\s+'
    r'(?P<model>.+)'                    # Model Name
    r'\s+FW:'                           # END OF MODEL
    r'(?P<firmware>[\w\. ]+)'           # Firmware Name
    r'\s+SN:'
    r'(?P<serial>[\w\-]+)'              # Serial Number
    r',?\s+'
    r'(?P<blocks>\d+)'                  # Total Block On Device
    r'\s+blks\n$')'

Suddenly we start to be able to see the individual tree's and the forrest
at the same time.

    r'^(Carrier board|Internal)\s+(\w+\d+)/([a-z]+\d+)\s+is\s+(.+)\s+FW:([\w\. ]+)\s+SN:([\w\-]+),?\s+(\d+)\s+blks\n$')

It takes up one line but the trade offs are that 

    1. you can't tell what any of the logical groupings are
    2. spotting wild cards is a chore
    3. figuring out how wild cards stop is more work then I want to do.
    4. it's hard to tell what parts are symmantically important,
    5. its hard to see how the syntax flows from one section to another.

Lastly the original is just ugly. There's no nice way to say it. 

But you don't have to live with ugly regex. There is another way, another path.
You can live a more beautiful and functional regular expression life by
following the simple steps listed above?

Someday you will thank your readability conciouse past self when frantically
debugging some regular expression soup you generated on auto pilot two years
ago.

