# SOURCE: https://www.adamhgrimes.com/defend-bad-statistics/


# Market stats: how to catch a common error


#### AdamHGrimes

Financial markets are highly uncertain, and every decision we make is ruled by the iron fist of probability. For traders and investors, statistics, whether expressed explicitly or learned implicitly from long contact with the market, are one of our most important tools for understanding the market. In my last post, I looked at a particularly common statistical error: the idea that the direction of the first day of the month or quarter sets the tone for that month (or quarter). In this post, I hope to accomplish two things:

- To understand how easily "future information" can contaminate statistical studies, and how even a subtle bias can introduce serious distortions.

- To suggest one simple condition--asking yourself if the statistic could possibly have been executed in the market as a trade--can protect us from all errors like this.

The specific error around the first day of the month effect is common. I've certainly made it myself in tests and analysis enough times to know that it is something always worth checking for, and I've seen it in stats people use for many technical factors like moving average crosses, seasonality, trend indicators, buying/selling at 52 week highs, the January effect, and many others. Anytime a statistic depends on the market moving in a certain direction, this error can rear its ugly head.


### Day of the week effect?

In my last post , I looked at the stats around the first day of the month, but it might be easier to understand if we re-cast it as the "day of the week effect". Here are (erroneous) stats that show that the return for each day of the week (1 = Monday, 2 = Tuesday, etc.) is a strong influence on the weekly return. For instance, if Wednesday is down, there is a high probability the entire week is down. For comparison, looking first at all weeks (2,856) in the S&P 500 cash index, going back to 1962, the average weekly return was 0.15% with a standard deviation of 2.14%, and 56.1% of all weeks were positive.

Here are statistics for the weekly returns, based on whether any Day of the Week (left column) was up or down for the week. We seem to find a very strong effect, and that's our first warning that something is amiss:


### Market data is abstract. Think of physical "things" to simplify problems.

To find the mistake, it helps to think of each week as a physical card. On one side of the card, there are five boxes, each of which has a positive or negative number (the daily return). Flip the card over, and you will find a single number that is the return for the week; though not strictly correct, let's just simplify slightly and say the weekly return is all the daily returns added together. (You can't add percentage returns, so this is not quite right. The correct math takes into account the compounding effect of money ((Add 1 to each day's return, multiply them together, and subtract 1 from the result.)), or uses continuously compounded (log) returns, but that's a complication we don't need for this blog post.) Here is what a few of the cards cards might look like:

So, put the 2,856 cards in a bag and randomly draw one out. You will find each of the five boxes is more or less just as likely to have a positive or negative number (i.e., each day is just about as likely to be up as down). If you did this a lot, you'd find that the numbers are slightly more likely to be positive than negative--about 52.7% of the days are up--but you would have to look at a lot of cards to see that. At first glance, it just looks like we have a mix of positive and negative days in each small box.

For this exercise, let's focus on box 1, which is the return for the first trading day of the week. Imagine pulling a few cards out, looking at that day, and finding, just like any of the boxes, some are up and some are down. Ok, now put all the cards back in the bag; things are about to get interesting.

Now, dump all the 2,856 cards out on the floor, and separate them into two piles based on one factor: if that day 1 is positive put it in the pile on your left, and if day 1 is negative, put it in the pile on your right. Now, do you see what has happened here? Your selection process has guaranteed that at least one of the days will be positive for the week for every card in the left hand pile, and there's the mistake.

If you now turn the cards over and average the weekly number for every card in each pile. you'll discover that the pile on your left has a lot more weeks that were positive, and the pile on your right has most weeks in the red. When one out of five days is guaranteed to be positive, the week will overwhelmingly be biased to be positive. While this might not seem that this error would create a large bias in the test, it does. Market data is random enough that even a very light "thumb on the scale" is enough to seriously distort the results.


### One test can catch many errors

How do we avoid errors like this? Well, the standard I apply to any test is simple: Always ask how could you trade the given effect. In this case, we are looking at weekly returns, which means buying or selling on a Friday and exiting the following Friday (except in shortened weeks); this is the only way we can capture the weekly return as traders. However, we don't know if we should have bought or sold on Friday until we see what the following Monday does! This trade would have been impossible to execute, so the statistic is suspect.

In this case, a better test, and one that would be tradable, would be to define the week in one of two ways: either from the close of the day being examined to the next Friday, or maybe doing a rolling week, always 5 trading days out. In the case of the original test, the month should be defined from the close of the day being examined to the end of the month, and a test like this will find no bias. If you're curious, here is a comparison of the two methods for the first day of the week effect:

This is a sneaky error, and it's one I've made many times myself. Though the test--thinking about whether the tendency was tradable on the timeline--will work, it takes some careful thought as mistakes are not always apparent at first glance. Be ruthless in examining the information you use and be even more vigilant with your own thinking. Bad statistics lead to biases and poor decisions.