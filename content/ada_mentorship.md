Title: What I learned from being a Ada Mentor.
Date: 2015-01-09
Category: Mentorship
Tags: Mentorship,CodingCamps,Management,Teaching
Authors: Alex Lord
Summary: "Soft" skills matter.



[I feel very passionately about narrowing the gender gap](http://blog.codinghorror.com/what-can-men-do/) in the software industry, which is why when EMC Isilon put its support behind the [Ada Developers Academy](http://adadevelopersacademy.org/) ( A year long coders boot camp for women), I volunteered to be a mentor. Having never been a mentor in a corporate setting and only 6 months out of college, I was bright-eyed and came with the best of intentions. 

I want to start off by saying that I really like this program. So much so that I’ve been volunteering a couple hours a week. I think that the mission is a great one. That the Ada Developers Academy is run by fantastic people and that the best thing going for the program is the students. A lot of the programmers who have come out of the program will be (and are) very strong developers. [It's a great example of what coding boot camps can be.](http://www.npr.org/blogs/ed/2014/12/20/370954988/twelve-weeks-to-a-six-figure-job)

With all of that said I wanted to focus this document on what I and my team could do better in the future when it comes to mentoring interns from the Ada Academy. 

I have been a professional academic tutor before in college. In my ignorance, I assumed academic mentoring was the same thing--after all, the title for both positions was “mentor.”

Assuming that I already knew how to mentor was my first big mistake. I made the assumption, based on the title that had been assigned to the task, that I was prepared for this and knew what it took. If present me could go back in time and beat past me up and then leave a note as an explanation, it would read: 

 	“JUST BECAUSE IT’S CALLED MENTORSHIP DOESN’T MEAN IT’S SOMETHING YOU’VE DONE BEFORE.”

In all seriousness though, titles are meaningless. I just want to lay out some of the major differences between the “mentorship” I did for academia and what teaching a very smart, but inexperienced, programmer what it means to be a software developer.

My intern had a project and, for reasons I’ll get into later, I had to learn how to be a project manager. [My previous mentorship gigs](http://www.edcc.edu/lsc/) were very limited in scope (at most an hour of help on a defined project) whereas the internship had the scope of “make them a good software engineer.

That defined project thing really matters. When I mentored someone at Edmonds Community College and Western Washington University, it was for assignments and homework problems. If someone asked me what a network file system was I was supposed to say “that’s beyond the scope of what I’m teaching you.” 

[Explaining how to use NFS, and what it fundamentally is, was required to start on my apprentice’s project.](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/3/html/Reference_Guide/ch-nfs.html) This is not a trivial task from either of our perspectives and learning how to teach not just a specific protocol but what [protocols are](http://fcit.usf.edu/network/chap2/chap2.htm) was daunting.

Because the professors at my schools had already decided what the students learning priorities were (for better or worse), I didn’t have to. This meant I never had to think about how hard or easy it was to learn a topic. Leveling material for students is hard to get right--not quite discovering Calculus hard, but about learning to like who you are hard.

One thing I really struggled with when it came to leveling learning material is deciding how much struggle is too much. Confusion and struggle are not a bad thing in and of themselves. Students learning something foreign or contradictory to their current knowledge base will often be confused and frustrated. That’s not in itself a bad thing. What’s bad is when a student is confused and not making any progress towards lifting the mental fog, or if a student is struggling on a task that they will only do once or twice in their life and will not provide any tangential learning. 

Another major difference is that being a mentor for an intern means you can not lose the trust or the working relationship with said intern. If I had issues with a student as an academic tutor, I could always hand them off to another mentor. There were always too many students to help.

This was very much not the case with the Ada internship. It’s a one on one relationship and you will be working with this person for large chunks of your day, everyday. Gaining trust once it is lost is an Indiana Jones level of adventure.

The length of the internship means you can’t just worry about the apprentice’s learning and growth as a coder. The duration makes an internship just as much about managing motivation and determination as anything else. 

One thing that is immediately clear is that changing technology stacks was not the hardest thing to learn for the apprentices. Initially, the team thought that the transition from Ruby to Python would be the biggest pain point for them, And there was some truth to that Python was their second (or third) language and picking up languages is a skill you get from... well from learning a lot of languages. 

The hardest technological task for the apprentices were going from web development to processing and analyzing data acquired from databases and network attached file systems. It’s very easy to learn how to use data in one fashion (Via http and web forms) without truly learning the underlying concept (data extraction). For me to build up this skill (and I haven’t mastered it yet) I needed to work on a project that required me to work with 3 separate kinds of databases (MySQL, OracleDB, MSSQL), CVS files designated with a http path, web forms,  and JSON serialization (AJAX requests and data to the server).

Another technology pitfall we ran into was not being able to explain to each of interns how much time and effort it takes to get used to a major environmental change. The best examples of this is that our interns switched from OSX and Sublime Text to Ubuntu and Gvim. In retrospect, I think that there’s only so much change someone can make in a short span of time without bogging themselves down. It’s kind of like increasing the amount of weight you can lift. Adding a little weight and growing your capacity is much more effective than adding 45 pounds and lifting something once. 


By far the biggest management challenge was learning how to manage more than just my own work and projects. My boss received a great offer from another company and left halfway through the internship. No one planned for that and there was no management failover to pick up the slack that was left. I tried to fill the gaps, but the biggest problem is that I was a total noob when it came to project management. This gap was compounded by the fact that everyone expected me to succeed no matter what endeavour I took.

I have had a lot of success at Isilon. The problem is that I’ve had a lot of success as a developer at Isilon. The roles of project manager and Software Engineering Teacher are new and unproven roles for me. This is especially poignant because, prior to my current role, I had never worked on teams larger than three people.

One mistake I made was classifying tasks as “easy” when, in reality, we had done them so much it made them trivial. It really caught me off guard how quickly I’ve forgotten what it was like to be brand new. I only started programming about five years ago and I assumed that was a short enough time to see clearly how hard things are to learn. [This kind of language also increases the sense of Isolation that some female developers feel.](http://www.fastcolabs.com/3008216/tracking/minding-gap-how-your-company-can-woo-female-coders)

Have you ever seen anyone juggle five balls? If you’ve never juggled before, then starting off with three is enough of a challenge to keep you occupied for a couple hours. Now imagine if someone gave you five on your very first try and told you that “Five is easy. This should take you, eh, half an hour to get. Then we can go on to the hard stuff.”

Underselling the difficulty of a task also destroys any sense of self accomplishment one gets from a project. I love building and making things because of the way that I feel afterwards. I love being able to go into work and see people using the stuff that I’ve created. I love knowing that in my little corner of the world that I’ve improved things for people. And I hate that I took that away from someone.

It also distances the mentor from the mentee. It creates, or reinforces, a sense of otherness in the relationship. This makes Mentees feel like they are even further from being a full fledged developer. The point of an internship is to try to remove the title of intern. The point is that somewhere along the way the intern becomes a developer and no one really notices until they look close enough. 

Another mistake that my team made was giving the interns one person projects rather than putting them on projects with other developers. The idea behind giving people their own projects is that they get to be their own master and owning something from the ground up lets you experience the whole spectrum of software development. The actuality is that unless people already have real world experience than they normally aren’t ready to own a project whole cloth. 

This style of internship worked really well for me. I loved being able to choose the technical direction and focus of my work and I don’t mind working alone. I had also spent 5 years in college mainly working on projects by myself. This is a great example of why the Golden Rule (treat others as you would like to be treated) is really dangerous. Applying my mental model to a student is not the right approach.

This was a poor choice for the Ada interns because they have a open classroom (everyone studies in the same room) and projects are set up to be highly collaborative. In the Ada program, it’s not cheating to work on a project with another student. In fact, you have to work on a bunch of different projects with other students. Also, because all of the projects are on github you can see exactly who made what changes and when. 

The bigger problem with having the Ada interns work on their own separate project is that the intern’s mentor is not incentivized to create a heavily-structured project for the intern to follow. In order to create a good set of instructions (road map, specification, whatever), you need to have a fairly detailed understanding of what the project entails. More importantly, you need to be there to be able to modify those instructions when they’re wrong. I find it very hard to be able to give good instructions without working on a project and spending a lot of time developing a deep understanding of what it’s trying to accomplish.

If you’re not directly working for a project and you want to give detailed instructions to someone who is still in the learning stage, then you have effectively taken on the responsibilities of their project while still having to meet the time tables for you first project. When one project helps a student out and one project keeps your job then ...

I think this last pain point could have been avoided if I had been a TA at Ada before being a mentor for the first group of students. Spending time in the classroom would have also given me a much better idea of what topics the interns had already known and what topics they had no idea about. That would have saved us a lot of time and hassle trying to calibrate the topics and how to teach them. 

I also feel there needs to be a designated manager who’s in charge of picking up slack if someone leaves or things are going poorly for each internship. I’m a pretty firm believe that if someone hasn’t proclaimed ownership or been assigned ownership of a task, it’s not getting done. That leads me to my next point--no one owned training mentors.

Perhaps it’s because teaching teachers is hard. Maybe it’s because you can only really learn how to teach by doing it. But I felt like I had to learn an awful lot of hard knocks lessons when it came to mentorship and project management. I would have loved to have had my own mentor to talk about what I was doing and to help me get on the right path when I had problems. 

One thing this experience has taught me is that empowerment comes from choosing goals and then meeting goals. Letting someone choose their goals can greatly increase their sense of accomplishment and self worth if they succeed. But that’s a double edge sword. If that person makes a choice and it turns out to be a bad choice, then that can shatter self confidence more than if they had an out. 

When someone is new to something, they need quick wins that stretch their understanding. Knowing when to let students choose those projects is one of the most valuable skills a mentor (or really, any leader) can have. You can delegate authority all you want, but you can never delegate responsibility. When I’m looking at my girlfriend’s homework for Plastic Engineering, I might as well be reading Dothraki. Asking me to pick projects that will quickly increase my learning and understanding of chemistry would be folly at best. Letting someone know that they’re committing folly can be hard.

If you haven’t looked up the sandwich method of communicating criticism, you should. It’s a useful technique that’s useful for all kinds of relationships. The basic idea is that you start off with a positive remark about someone, a criticism of some kind, and then you leave on a positive note. The idea is to be super clear in your communication and to be able to tell someone when you find something wrong, but you also keep their trust and attention with the positive reinforcement and prevent them from feeling attacked. 

Another small note that I’ve found useful recently is to change “Do you have any questions?” to “What questions do you have?” Stating things in such a manner as to make questions the norm makes people feel much more comfortable and it will elicit feedback where you otherwise would get none. Also “Do you have any questions?” makes it sound like the person you’re talking to should obviously never have any questions--that you’re always clear and concise and no one could ever get lost while listening to you.

Asking people for help is by far the quickest way to build trust and build confidence. Asking people for help is also an exercise in vulnerability on your part. Genuinely asking for help forces you to let someone else take the reigns on your idea. It means you can’t exercise tight control over how that idea is shaped, and it means you have to be patient.

Also, while [some people](https://hbr.org/2013/04/the-sandwich-approach-undermin/) think [feedback sandwiches](http://www.wikihow.com/Give-a-Feedback-Sandwich) subverts your feedback to individuals I will state that my personal experience totally contradicts this.

Letting someone else work on your idea means things will not go as quickly as you planned. My first instinct about how long a task will take is almost always wrong. I also am almost always wrong in the “huh, this sure did take longer than I thought” direction.

And this is where I end this monster of a blog post. I think for me, the big takeaways from this point are that interns do real shit. A mentor's job is to decrease the amount of time until a mentee is adding value to a company. If you haven’t been provided a support network, find one. Be very clear in what someone’s goals and responsibilities are. If you can, go watch or volunteer at the location your mentee will be coming from. Ask your mentee for help early and often. 

Thank you all if you’ve made it this far. I would love to hear from you if you disagree with anything in this post and I would love to hear why you disagree with me. I’m still very much learning.
