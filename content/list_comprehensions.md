Title: List comprehensions break my brain 
Date: 2014-10-11 10:20
Modified: 2014-11-29 10:20
Category: Programming
Tags: Programming,Python
Authors: Alex Lord
Summary: but they're fast.

[I asked a question on Stackoverflow and was given this brain cracking set of list comprehensions as an answer.](http://stackoverflow.com/questions/24792257/how-to-write-regular-expressions-to-match-white-space-delimited-multi-line-colum)

```
whitespaces = [i for l in content for i, char in enumerate(l) if char == ' ']

whi_columns = [k for k, v in Counter(whitespaces).iteritems() if v == no_lines]

data_columns = [[line[col].strip() for line in content] for col in columns_defs]
```

Which immediately punted my comprehension out the window. And just to add insult to my injured pride, they worked. 

The first list comprehension,

```
whitespaces = [i for l in content for i, char in enumerate(l) if char == ' ']
```

can be broken into two for loops
```
whitespace_indexes = []
for line in content:
    for char_index, char in enumerate(line):
        if char == ' ':
            whitespace_indexes.append(char_index)
```
The second comprehension,
```
whi_columns = [k for k, v in Counter(whitespaces).iteritems() if v == no_lines]
```

can be broken into a single for loop,
```
for num in Counter(whitespaces).iteritems():
    # Counter will sum up how often a white_space index is present.
    if num[1] == number_of_lines:
        # If a whitespace index shows up for the total number of lines then it’s a column.
        white_columns.append(num[0])
```


And lastly, there was this little beauty which reminded me of a nested ternary conditional
```
data_columns = [[line[col].strip() for line in content] for col in columns_defs]
```
can be expressed as two for loops,
```
data_columns = []
for col in columns_defs:
    sub_list = []
    for line in content:
        sub_list.append(line[col].strip())
        data_columns.append(sub_list)
```
It turns out the comprehension portion of these statements was not the hard part. What I didn’t understand was the comma operator. 

In each of those list comprehensions there’s a section after the `for` keyword which has a comma. That comma returns a tuple. Here’s an example 
```
foo = [1, 2, 3]
bar = [4, 5, 6]
for tuple in foo, bar:
   print(tuple) # tuple == ( [1, 2, 3], [4, 5, 6])
# prints 
# [1, 2, 3]
# [4, 5, 6] 
```
will return the tuple ([1, 2, 3], [4, 5, 6]) in one iteration.

You can have mis-matched tuples which I think is super awesome.

```
foo = [1, 2, 3]
bar = ([4, 5, 6], [7, 8, 9])
for tuple in foo, bar:
   print(tuple) # tuple == ( [1, 2, 3], ([4, 5, 6], [7, 8, 9]))
# prints 
#[1, 2, 3] 
#([4, 5, 6], [7, 8, 9]) 
```
Most of the programmers at work (C programmers who dabble in Python, mainly) Have a hard time initially understanding these comprehensions. Which to me means that these are too complex unless you’re dealing with people well versed in the language. These kinds of list comprehensions really shouldn’t be your first choice. They reduce code readability. You also can’t step through them using PDB which makes debugging them a... challenge. 

But they are very fast. I ran the double for loop example and it’s counter list comprehension through timeit. 
```
alord@alord-desktop:comprehension :) $ python for_loop.py 
2.46502590179
alord@alord-desktop:comprehension :) $ python comprehension.py 
1.67403912544
```
Here’s the code I used:

```
------------------------------------------------- For Loop version ---------------------------------------------------


import timeit

print(timeit.timeit(
"""
content = ['------------------------------------------------------------------------------', 's200_13tb_400gb  1     +3 system, vhs_de 1:0-23,      1      53T /  218T (25% )', '-ssd_48gb-ram             ny_writes, vhs 2:0-23, 3:0-                          ', '                          _hide_spare,   1,3-19,21-25                          ', '                          ssd_metadata   , 4:0-23,                             ', '                                         5:0-23,                               ', '                                         6:0-23,                               ', '                                         7:0-23,                               ', '                                         8:0-23,                               ', '                                         9:0-23,                               ', '                                         10:0-23,                              ', '                                         11:0-23,                              ', '                                         12:0-23,                              ', '                                         13:0-23,                              ', '                                         14:0-23,                              ', '                                         15:0-23,                              ', '                                         16:0-23,                              ', '                                         17:0-23,                              ', '                                         18:2-25                               ', 'Unprovisioned drives: none', '']
whitespace_indexes = []
for line in content:
    for char_index, char in enumerate(line):
        if char == ' ':
            whitespace_indexes.append(char_index)
""",
number=10000))
```
```
---------------------------------------------- Comprehension version ---------------------------------------------

import timeit

print(timeit.timeit(
"""
content = ['------------------------------------------------------------------------------', 's200_13tb_400gb  1     +3 system, vhs_de 1:0-23,      1      53T /  218T (25% )', '-ssd_48gb-ram             ny_writes, vhs 2:0-23, 3:0-                          ', '                          _hide_spare,   1,3-19,21-25                          ', '                          ssd_metadata   , 4:0-23,                             ', '                                         5:0-23,                               ', '                                         6:0-23,                               ', '                                         7:0-23,                               ', '                                         8:0-23,                               ', '                                         9:0-23,                               ', '                                         10:0-23,                              ', '                                         11:0-23,                              ', '                                         12:0-23,                              ', '                                         13:0-23,                              ', '                                         14:0-23,                              ', '                                         15:0-23,                              ', '                                         16:0-23,                              ', '                                         17:0-23,                              ', '                                         18:2-25                               ', 'Unprovisioned drives: none', '']

whitespaces = [char_index for character in
    content for char_index, char in enumerate(character) if char == ' ']
""",
number=10000))
```

so about 1.5 times slower to do the full for loop in this case. 

I will say that after having written this blog post I understand how the comma operator and iteration work much more comprehensively. Every time I’ve seen a comma separated iterator I’ve understood what was happening much faster than this first time. But this first time threw me for such a loop that I stand by my stance that list comprehensions like this reduce readability and require some kind of explanation to be readable. 

So in conclusion, List comprehensions break my brain but they're also fast. 




