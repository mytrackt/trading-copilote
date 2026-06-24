# SOURCE: https://www.adamhgrimes.com/trend-following-futures/


# Testing a trend-following approach in futures


#### AdamHGrimes

In this post, we'll take a look at a common trend-following trading idea: channel breakouts (also called Donchian channels). I want to share with you a way of looking at market tendencies, and structuring tests of those tendencies, that I have found to be very useful and powerful. There are many ways you can expand this idea (look at "event studies" in academic research for examples), but the core idea is very simple.


## Structuring tests

There are many ways to set up tests of market tendencies. One of the most common is to create some type of trading system around the rule, and then to report profitability stats on that system. This approach is everywhere, and you can find many blogs and business built around "stats" and results created in retail-level trading systems. (An example might be something like: "this pattern has occurred 16 times in the S&P in the past 10 years. Investing $10,000 on each signal would have resulted in a profit of $XXXX with a win ratio of Y%") One of the biggest problems is that this type of test does not address the issue of the "baseline" return in the market being considered. How much would I have made had I simply bought and held? At the very least, we need that stat too.

Ideally (actually, essentially), we need to have some measure of statistical significance. A rudimentary statistic would be to compare some measure of volatility for the "system" being considered with the volatility for the buy and hold approach in the same market. Better yet would be an actual measure of statistical significance, but we have to have some measure of how important the results are--simply noise, or likely to be something else?

The real problem, to my way of thinking, is that any system-type test is a joint test of whatever underlying tendency might (or might not) be in the market, with whatever specific rules you imposed on the test. Let's take a very simple entry system. If you want to create a system test, then you have to exit. When, where, and how? Taking a simple X day hold does not solve the problem, because I do not know how you arrived at X. Did 3 days work, but 5 didn't? Did you use a stop? Did you use a trailing stop? All of these decisions have a dramatic impact on the results, and they can hide what we are really trying to test.

I prefer to structure first-level tests as very simple, almost crude, tests of market tendencies. I simply want to define a condition (which is usually simple, but could be a complex condition), and then see what happens in a set of markets after that condition appears. The concept of this type of test is simple: we take a set of market data, and find the baseline return. If we are looking at a group of markets, we find the baseline for each market, and then average them together. (We can also look at them separately, of course.) Next, we go through the market data and find every time the condition occurred, and then record the market's movements for a time window after each event. Last, we compare the signal returns with the baseline return. If we have a valid signal, it should look "different" from the baseline return in some way. This approach generates a lot of data, but it's possible to summarize it for easy comprehension.


## Channel breakouts

The channel breakout is a tried and true approach to trend-following and to trading markets. Many trading programs are built on this concept; it was the basis for the legendary performance of the Turtles, and I even publish a version of a system like this every day in my research for Waverly Advisors . This is a simple, robust system idea that works, so let's dig into it a bit deeper. Take a look at the following chart, which shows channels representing the 20 and 50 day highs and lows applied to the crude oil market. (These are sometimes called Donchian channels, in honor of Richard Donchian, of the pioneers in trend following in futures markets.)

As you can see, shorting at the bottom channel would have been very profitable in this time period (but so would shorting based on any idea whatsoever!) Charts like this always make trend following systems look very attractive, but don't forget the whipsaws and drawdowns--trading a system like this can be difficult psychologically for many traders, even if the system works over a large sample size. Now, take a look at the following chart, which shows a simple test of shorting (buying) the 50 day low (high) in a set of futures markets. I applied one filter: requiring 20 days between entries (though the results are not much changed with or without that filter condition.) I recorded returns out to about a year from each signal event. Here are the results of this test:

The dark blue (red) line is the average return for buys (sells), in percents, for each trading day (x-axis) following the signal event. The dotted grey line is the baseline return, which was pretty close to zero for this sample, and the shaded area is the difference between the signal and baseline returns (excess returns). What we would like to see in this test is that buys go up (they do) and sells go down (they do). We also can get some idea of how long the signal is valid, and might be able to find some inflections, though we should be careful about drawing too many conclusions from such a crude test.

So, the method seems to work in futures markets. I wonder what happens if we try the same thing in stocks? How about currencies? That's a good topic for my next post...