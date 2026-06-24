# SOURCE: https://www.adamhgrimes.com/a-new-look-at-measuring-trend-days/


# A new look at measuring trend days


#### AdamHGrimes

For intraday traders, trend days can offer outsized rewards. For some styles of traders, much of the work of trading is focused on capturing trend days, and most of the profits for the month may come from one or two trend days, with most of the other days showing small gains and losses that more or less net out. (This is not true for all intraday traders.) Many traders find the best results when they reduce trading activity on non-trend days (and might see even bigger improvements if they did not trade on non-trend days altogether), but it is vitally important to identify trend days when the do occur.


## What do trend days look like?

Over the years, I've worked on various ways to identify trend days and to predict when conditions are ripe for a trend day. This is not as easy as it sounds. Subjectively, it is easy. Here are a few trend days in the S&P futures. Trend days generally:

- Open and close at opposite ends of the day.

- See few major intraday reversals. Most trend days are clean trends.

- Have a larger range than other days.

- Occur about once a month.

Here are a few examples of trend days on 1 minute bars. Note minimal retracements against the trend:

You're probably getting the point, but contrast those last two charts with these. These are "not trend" days in the S&P:

Subjectively, it's pretty easy to label trend or not trend days. As far as predicting trend days, there are a number of things that can be useful. (That's a future blog post.) The focus today is on identifying and labeling trend days objectively. I've worked on this off and on for many years with varying degrees of success. Ideas like taking largest range of past 10 days and saying the body of the candle has to >85% of the day's range--ideas like that work, but I recently stumbled across a simpler way that might be better.

On my trading platform I have a chart that runs 1 minute ES bars with an audio alert every time the market makes a new high or low of the day. You'd be surprised how much information you can get from this simple idea. Without looking at the screen, I know if "she" says "S&P High" a lot, we're having a strong market day. Also, if she is quiet and then starts saying "S&P Low" a lot, something happened. This is a great way to build some market intuition, and a really useful tool for reading the market when you can't stare at the screen every day.


## A new (?) way to measure intraday trend strength

The breakthrough came when I thought "let's just count how many times one minute ES bars make new highs or low on the day during the regular session. What would that look like?" You can find what that looks like in the spreadsheet at the end of this post, and it looks pretty interesting. The columns are:

- Date

- NH: The number of 1 minute ES bars that make "new highs" on the day. Note that this has nothing to do with A/D style new highs.

- NL: Number of 1 minute ES bars that make new lows on the day.

- SignedTrend: NH - NL. This will be large and positive if there were more highs than lows, large and negative if many new lows, and smaller if the day made both highs and lows frequently.

- Trend: The absolute value of SignedTrend, and maybe a measure of trend day. This number ranges from 0-64 in this sample (5 years of 1 minute data).

- Label: I made breaks at 99th, 95th, 90th, and 75th percentiles, and labeled "strongest trend", "strong trend", "trend", and "possible trend", respectively.

I'm not sure these labels are exactly right, and there could be more work to do here. For instance, only looking at the net number might miss some detail--there could be a better way to look at this, but I do like the simplicity of this approach. Any complication will have to add a lot of value, in my opinion, to be worth moving away from the simplicity of the data. Maybe the break points aren't in the right place for my labels? There are other ideas like that to consider, but I offer this here for you to look at and think about. It's also likely that someone has done something like this before, but I don't remember seeing this. There are only so many ways to slice the data, but sometimes simplest is best. Sometimes simplicity can be very elusive. At the very least, it's an interesting perspective on measuring intraday trend strength. I'll follow up with another post on this in the future, and look forward to some of your thoughts and perspectives in the comments. [gview file="https://adamhgrimes.com/wp-content/uploads/2015/04/ES-Trend-Days.xls"]