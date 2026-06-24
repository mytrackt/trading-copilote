# SOURCE: https://www.adamhgrimes.com/reader-question-how-to-backtest/


# Reader question: how to backtest?


#### AdamHGrimes

Reader Jas asked a question about backtesting:

Good question, and there's no easy answer. I would point your question in a slightly different direction. You're asking about software or firms to do backtesting. Of course, these things exist, and you can always find someone to take your money in return for a service. :) The people doing this work will have slick marketing material and will explain that they use Monte Carlo modelling and non-parametric statistics, and they'll hope you will be dazzled and for over the cash for the test.

But wait.

First, I think you need to make sure you have a solid education in statistics, probability, and backtesting. Yes, I know this is an annoying answer because people just want a solution, but there are so many ways to go wrong with this kind of work--so many pitfalls and so many places a perfectly well-intentioned person can make fatal errors--you have to educate yourself. That education doesn't have to take a lot of time, but a year or so, depending on your background, spent really wrapping your head around statistics is time well spent.

Also, educate yourself on backtesting in general. A good place to start is the module in the trading course Ernie Chan did for us. Why did I ask Ernie to do this? Because I think he is absolutely the best at teaching and communicating these concepts, and he put together a powerhouse of a module that will show you many of the things that can go wrong with backtesting, and will lead you toward asking the right questions. The course is free, so head over there and check it out right now to start.

From there, continue to educate yourself on backtesting techniques. Learn, for instance, what might be wrong with having a rule set, tweaking it based on results, and then running another test. Or adding an indicator, running a test with a few different settings, and then deciding which setting to keep as you work forward. It's very easy to produce a nice backtest, but the goal with all of this rigorous work is to have something that works in the future. That, my friends, ain't easy.

Personally, I got a lot of value out of doing my first simple backtests in Excel. Yes, it's perhaps the worst backtesting environment for a number of reasons, but you can see and manipulate the data and understand your work in a way that is more difficult in software like Stata (which I use), Matlab (which many more people use) or in coded systems written in languages like Python or R (which is probably what you ultimately should be using).

Learn statistics. Understand probability. Understand how backtests can go wrong. Craft simple backtests of simple concepts, and look for an edge, and then test your system. That would be my advice, but check the comments to this post as I'm sure some readers will have other ideas and perspectives. (Word to the wise: I'll delete commercial links from comments.)