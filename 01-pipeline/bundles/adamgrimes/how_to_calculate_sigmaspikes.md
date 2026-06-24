# SOURCE: https://www.adamhgrimes.com/how-to-calculate-sigmaspikes/


# How to calculate SigmaSpikes?


#### AdamHGrimes

I've received a few questions about how to calculate a measure I have referred to many times here on my blog and in my published research that I call SigmaSpikes. I've disclosed the calculation in several places, but the question keeps popping up, so maybe I need to do it more clearly! First, a little history on how I came up with the measure, or, well, reinvented the wheel:

I think most of us who are involved with markets for any length of time begin to realize that volatility is important. (Yes, that statement is a dramatic understatement.) I did a lot of my early semi-quant work in a vacuum, so I didn't know what everyone else had already done; I created really cool and useful tools that were--ultimately--things that everyone else was already using. Though I kind of smile at my naivety now, I think that process was an important part of my development and learning, so it wasn't wasted time.

When I began to think about volatility, I came up with the idea that different markets traded with different volatility levels (true), that it would be a good idea to have some way to compare volatility across markets (very true), and that each market probably had a base volatility level I could expect it to return to. (The last idea is not true in any practical or meaningful way, but two out of three wasn't bad.) My first attempt was to look at each day's move as a multiple of the average range of the market over some time window. I played with different time windows and decided that a month was about right for how I traded--any longer, and it would be too slow to respond to any change in volatility, and much shorter was so unstable that it wasn't useful. I settled on 20 trading days as a nice round number and used it for my baseline calculations.

The next evolution was to use true range instead of range. This is a small difference, but it really is better: for one, it automatically catches overnight gaps and considers them in the volatility of the market. Another point that is often overlooked is that ATR allows us to use "close only" data series in range calculations, and I was also beginning to use some economic data in my work that had no range associated with each period, just a single datapoint.

Here's an important point, and it's probably the most complex of this post: "time leakage" is a real problem in any kind of testing or development. If you create a system and even slightly reference a seemingly insignificant datapoint you could not have had at the time, your system results will likely look very good, but they'll also be completely invalid. We must be very careful to only use data we would have had at the time. The best way to measure this volatility ratio seemed to me to measure against yesterday's ATR, because we don't know what today's was until the close of the bar. A very big day today will inflate the baseline, making that big day seem smaller, by comparison, than it would have been to a trader at the time. So, I offset the calculation to measure today's range against yesterday's 20 day average range.

[box type="info"] This question frequently comes up on trading forums: a "return", in finance, is just a percent change. This is standard language in any academic or mathematical finance, but not so much in the literature of technical analysis. A return is simply a percent change, so a daily return is the % change for the day.)[/box]

At some point, I began to think that returns were a better way to think about market price. Once you make that leap, standard deviation of returns is an accepted measure of volatility, and is trivially easy to calculate. So, I settled on the idea of looking at each day's return as a multiple of the 20 day standard deviation, with the measure offset one day, and that's what I use today.

Since then, I discovered that practically every options trader and risk management system in the world uses this exact calculation (or some slight variation) in their work. It's a very useful measure, but is by no means unique to my work or perspective. It is, however, a very useful took for looking at market action and price changes, quickly assessing volatility, and removing much of the emotional component associated with large price moves over a period of time. More on that, perhaps, in a future post.

There are a number of ways to do this calculation, but here, in bullet points, is what you're trying to do:

- Calculate daily returns as: return = today's close / yesterday's close - 1

- Calculate standard deviation of daily returns over a 20 day window. In quasi-Excel langauge:: stdev = stdev( returns , 20)

- Calculate today's sigma spike: SigmaSpike = today's return / yesterday's stdev