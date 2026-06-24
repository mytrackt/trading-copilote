# SOURCE: https://www.adamhgrimes.com/quant-101/


# Quantitative analysis: what it is and why you need to do it


#### AdamHGrimes

I think most traders and investors understand that we live in a world in which markets are becoming ever more competitive. To make money in those markets, you must have an edge, and you have to truly understand your edge. But the question remains: where and how do you find an edge and how can be you sure you understand it? I want to share a little bit of my own experience in this regard, and give you some ideas for doing your own work.

At the beginning, I think it's important to understand the questions we are asking. No matter what your trading/investment methodology is, you are assuming that something is more likely to happen than something else, based on whatever tools you are using. Think about that a minute, because some people are confused on this point. Whatever you do to decide when to get in and out of markets, you are doing so because you think one outcome is more likely than another. If we don't have this understanding, then we can easily fall into a mindset that says "x must happen", "x will happen", or "x has to happen." That way of thinking is dangerous; at best, x is a little bit more likely to happen. So, how do we know that is true?

Quantitative analysis and quantitative tools can seem to be intimidating, but, at their core, they are very simple--all we're doing is looking at a bunch of things that happened in the market, defining some conditions, and seeing if the those conditions have been tied to certain outcomes. We then make a (hopefully small) leap and assume, if we've done our work right, that seeing these conditions in the future will make certain outcomes more likely. Here are some concrete examples of statements we can test. Notice that they each include a condition or set of conditions, and an outcome: Stocks with good earnings stability are likely to go up. Stocks making 52 week highs are likely to go up. After a decline in price, if volatility contracts, stocks are more likely to go down. After making new 20 day highs, a commodity is more likely to continue to go higher. (By the way, some of those statements might be true, and some might be false. They are simply examples.)

How do we answer those questions? Well, there are some semi-sophisticated techniques that you may have encountered in a math class a long time ago like linear regression or principal component analysis. These tools do have their place, but we don't need them for much of work. We can do some pretty deep analysis with these steps:

- Get a bunch of market data together . We need to make some decisions about what timeframe (daily, weekly, 1 minute?), what markets, what time span (recent? 5 years? 50 years?) we want to cover. This stage of getting and managing our data is harder than you might think because we have some thorny issues like dividends and splits for stocks and rolls for futures to consider. In addition, nearly all data sources have some errors, so we're going to need to spend (too much of our) time cleaning and wrangling this data.

- Define a set of conditions . These conditions can include price patterns, other technical factors, tools calculated from price inputs (e.g., MACD), fundamental factors, changes in fundamental factors, economic data, macro factors, sentiment data, etc. The only serious caveat here is that these conditions need to be defined precisely because we are going to test them over hundreds or thousands of occurrences.

- Look for every time the condition occurred in every market we are analyzing.

- See what happened following every occurrence of the conditions.

- Compare what happens after the conditions to all other market data. What we're looking for here is some evidence that our condition set has the power to influence markets.

That's really it, and it's not so intimidating: define a condition; test it, and then look at the results. We can do this with pencil and paper, and, indeed, that is how I started. But, to really do this work, we need good tools. In my next post I'll share some of the tools I have developed and used over the years, starting with that pencil and paper, through Excel spreadsheets, to convoluted combinations of different tools, to, finally, a robust framework written in Python. I'll tell you why I think Python is the right choice for much of this work and for many of my readers, and then we'll dig a lot deeper into what you need to know to use it well.