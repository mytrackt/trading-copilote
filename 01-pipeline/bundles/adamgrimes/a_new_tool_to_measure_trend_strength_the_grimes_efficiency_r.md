# SOURCE: https://www.adamhgrimes.com/a-new-tool-to-measure-trend-strength-the-grimes-efficiency-ratio/


# A new tool to measure trend strength: the Grimes Efficiency Ratio


#### AdamHGrimes

Is a market trending or not? Even this simple question, which is at the heart of most of our thinking about markets, is not easy to answer. Definitions of trend are often subjective, depend on both timeframe (e.g., daily or intraday) and reference period (i.e., how far are we looking back?), and are generally somewhat unsatisfactory, in one way or another. I have been working to improve that situation, and I want to share some of my work with you today.


## Calculating the Grimes Efficiency Ratio

One of the best ways to track intraday strength among several markets is to calculate the closing price as a percentage of the day's range; it is intuitive that markets near the high of the day would be stronger, and those near the low would be weaker. When we look at other periods or want to evaluate trend strength over a period of time, the task is a little harder. One solution is to pick an arbitrary lookback period, and calculate the closing price as a percentage of the total (high to low) range prices covered over that time. This measure is the heart of the tool I am calling the Grimes Efficiency Ratio (GER). The chart below shows the closing price as a percentage of the last 20 ((I chose 20 as a starting point since it represents about a month's lookback. Also, it corresponds, roughly, to the vertical grid lines on the chart, so it's easier for you to evaluate visually.)) trading days' range for every bar on the chart:

This is obviously a noise measure that can flip from 1.0, meaning the close is the high price achieved in the last month, to 0.0 on a single bar. It's very difficult to extract useful information from something this noisy, but look what happens when we smooth it a bit, averaging the close as % range measure for each of the past 20 trading days:

Now we're getting somewhere. Take a look at the line, and remember that it measures trend strength over, roughly, the width of the vertical lines. When the red line is low, the trend is strongly down; when it is in the middle, the market has been in a trading range over the past month. First step is to see if this tool seems to do what we think it does, and it passes a simple visual inspection.


## How to use the GER

Initially, there are a few ways I would consider using this tool:

- Use it as a filter for rules-based strategies, but more work would need to be done to see if it is predictive. It does a great job of describing past trend conditions, but regimes change quickly, and a tool like this might do more harm than good.

- Rather than using as an entry filter, use to managing existing positions. For instance, perhaps a trailing stop could tighten faster as the GER falls.

- Rank multiple markets by GER and use it as an input in selecting best markets to trade.

- Use middle-ranked GER markets (which we would presume to be in trading ranges or consolidations) as breakout candidates or at least as a place to look for further screening.

- Use markets that have recently shown an extremely high or low GER, and now show a more moderate level, as potential pullback trades.

My point here is just to give you some ideas and some ways to think about a tool like this. There's a lot more to be done, but these ideas might be a good starting points. While we're at it, here's something different.


## A counter-intuitive use of the GER

Market psychology swings back and forth between extremes. We all know this, and some standard examples come to mind: a soaring market that crashes (extreme of trend direction), a quiet market that explodes with new volatility (volatility contraction), or a market that exhausts itself in a last-gasp, mighty trend thrust--these are common examples of extremes. Another extreme is simply the alternation between trending (without considering direction) and trading range. This tool captures this rhythm visually, but there's more...

This tool was created to measure trend strength, but there is an edge to fading extremes of trends. The GER can be used in as an overbought/oversold indicator; the table above shows the results of fading an extreme level of the GER, only taking one trade every two weeks, on a basket of 50 stocks. Pay attention to the first column, which shows the outperformance over the baseline drift return: a staggering 3.74% over the next 20 trading days for the buy signal. This is a basket of stocks, and it's normal to see a sell signal not perform as well, but we might have a little juice on the shorting side too. ((Consider statistical significance , which you can read in the "p=" column. Buys appear to be significant and sells do not, but, again, that asymmetry does not invalidate the tool, here at first glance.))


## Here's the code

Here is the code, in EasyLanguage format, with some comments. inputs: lookback(20); vars: rng(0), crng(0), sumrng(0); rng = highest(h, lookback) - lowest(l, lookback); crng = iff(rng > 0,((c - lowest(l, lookback)) / rng), 0); //calculate close as % of range, catch divide by zero error sumrng = average(crng, lookback); plot1(sumrng);If you make use of this, please let me know . I will continue to work on it and tweak it, and I just might find an interesting use for it.

(Note that there is an indicator called the Kaufman Efficiency Ratio, but it is quite different. It looks at the price change over a period of time, divided by the sum of the absolute price movements over that period. The idea here is to look at how far the market moved against how much it jiggled around, but the KER does not consider highs and lows. The GER represents a significantly different perspective, as it's essentially an averaged percentile of price.)


## Other examples

I will leave you with a few other examples on other markets: