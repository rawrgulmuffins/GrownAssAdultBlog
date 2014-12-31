Title: Dirty Hacky Code
Date: 2013-07-15 10:20
Modified: 2014-11-29 10:20
Category: Programming
Tags: Programming,PeopleManagement
Authors: Alex Lord
Summary: Making sausage and writing code isn't always clean work

[So I was reading a Gamasutra article from 2009 called “Dirty Coding Tricks.”](http://www.gamasutra.com/view/feature/132500/dirty_coding_tricks.php) The whole article is well worth reading for both programmers and non-codejunkies. The last of the nine stories that are covered was so interesting I wanted to quote it on here:

“I was fresh out of college, still wet behind the ears, and about to enter the beta phase of my first professional game project -- a late-90s PC title. It had been an exciting rollercoaster ride, as projects often are. All the content was in and the game was looking good. There was one problem though: We were way over our memory budget.

Since most memory was taken up by models and textures, we worked with the artists to reduce the memory footprint of the game as much as possible. We scaled down images, decimated models, and compressed textures. Sometimes we did this with the support of the artists, and sometimes over their dead bodies.

We cut megabyte after megabyte, and after a few days of frantic activity, we reached a point where we felt there was nothing else we could do. Unless we cut some major content, there was no way we could free up any more memory. Exhausted, we evaluated our current memory usage. We were still 1.5 MB over the memory limit!

At this point one of the most experienced programmers in the team, one who had survived many years of development in the "good old days," decided to take matters into his own hands. He called me into his office, and we set out upon what I imagined would be another exhausting session of freeing up memory.

Instead, he brought up a source file and pointed to this line: static char buffer[1024*1024*2];
"See this?" he said. And then deleted it with a single keystroke. Done!

He probably saw the horror in my eyes, so he explained to me that he had put aside those two megabytes of memory early in the development cycle. He knew from experience that it was always impossible to cut content down to memory budgets, and that many projects had come close to failing because of it. So now, as a regular practice, he always put aside a nice block of memory to free up when it's really needed.

He walked out of the office and announced he had reduced the memory footprint to within budget constraints -- he was toasted as the hero of the project.

As horrified as I was back then about such a "barbaric" practice, I have to admit that I'm warming up to it. I haven't gotten into the frame of mind where I can put it to use yet, but I can see how sometimes, when you're up against the wall, having a bit of memory tucked away for a rainy day can really make a difference. Funny how time and experience changes everything.”

[I love the last example about "storing" extra memory. It reminds me of an old master descending from the mountains and telling their students that "they must learn patients."](https://www.youtube.com/watch?v=Z8VD4JXUozM) I love me some  deception. It’s wonderful because it’s a clear case of creativity and discipline through restrictions. It reminds me of people who have artificial deadlines for projects a week before they’re actually due. It reminds me a lot of my dad who is fond of saying “Go like hell in the beginning and hope you can coast at the end.”

To my ears all of these arbitrary constraints are a kind of personal insurance. They’re risk management but the management portion is just a shot in the dark. Which is why these kind of tricks are also awful to me.

[All of these tricks remind me of 1850 architectes guessing how much support they’d need to build into a bridge. It reminds me of the Tay Rail Bridge built in scotland in 1878.](https://en.wikipedia.org/wiki/Tay_Rail_Bridge)

The Tay Rail Bridge was an early attempt to build a lighter and cheaper bridge. Up until this point most train bridges were built by guessing how much the max weight of a train would be and then multiplying by a couple hundred. This is great from the perspective of safety but terrible of the perspective of building more than one bridge... ever.

Then again most of my project estimates start with "hmmm, that sounds like it'll take a week. Better multiply that by three."
