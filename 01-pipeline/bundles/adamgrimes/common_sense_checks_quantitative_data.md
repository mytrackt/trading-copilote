# SOURCE: https://www.adamhgrimes.com/common-sense-checks-quantitative-data/


# Common sense checks for quantitative data


#### AdamHGrimes

Yesterday I wrote a post that looked at asset returns and how to compound them. That post was in response to a reader's (Anthony's) question, and I want to continue answering more of the question today. Here's the question in its entirety, with the part we're going to address today bolded:

So, Anthony's procedure here is pretty solid. He's (correctly) assumed that consecutive closes might set a stock index up to mean revert, and is investigating that by finding instances of consecutive closes in one direction and then looking at what the market does after. Though we can always refine procedures, it's hard to poke holes in that basic thought process. For simplicity, let's call "SPY was down 2 days in a row" as the signal event for the rest of this post.


## The TLAR test

Ok, so this is only half a joke--TLAR stands for "that looks about right", and is a quick "back of the envelope" type of check we should do with any analysis--it is a way to apply common sense tests to quantitative data. I would do this type of analysis at least two points in the process: first, with the raw data, and second with any final results.

What we're looking for, first of all, are things that just don't make sense or are too good be true (in the case of results.) If your data are daily returns on liquid stocks, do you have a lot of +/- 20% days? Do you have any days that show a return less than -100%? Do you have days with missing data? If you're looking at prices, do you have any negative prices? Do you have anything that looks like this: 101.23, 104.21, 1,021,30, 100.21? Any highs lower than lows? Opens or closes above the high or below the low? Plot a time series of the data and look for anything stupid. These are basic things, but most researchers find too much of their life is spent on wrangling data into submission.

As for results, we want to be on guard for something that looks too good to be true. Did you find a signal in the S&P 500 that wins 80% of the time with a large sample size? Good, you made a mistake so now go find that mistake and learn from it. It takes some experience to know what is too good to be true, but if you ever ignore this common sense check you will be sorry.


## Are these returns reasonable?

So Andrew has found that. following the signal event, SPY had an average return of 0.06% over the next 5 days and 0.41% for the next 20 days. He finds the 5 day return "fine" (probably meaning that he applied some form of common-sense TLAR checking to it and it passed) but he's skeptical of the 20 day return. Question: should he be skeptical? (If you didn't read yesterday's post and you aren't comfortable annualizing returns you really should read that post first!)

So the 20 day return of .41% annualizes to 5.3%. (There are 12.6 20 day periods in a 252 trading day year, so: (1 + 0.41%) ^ 12.6 - 1 = 5.3%.) The 5 day return annualizes to 3.07%. Stocks do tend to go up, and they tend to go up somewhere around 7% a year. We don't know what time period Andrew is looking at, and it's possible that he's focused on a time period in which stocks were flat or down. However, if someone tells you they have a system that will give you 3% - 5% in stocks, yes it passes the TLAR test. It is reasonable, and, based on the magnitude of those returns, there's no reason to be suspicious that an error was made in the analysis. (Note to Anthony: "fudged" probably is not the f-word you were looking for (or that you will use) when you do find errors like this!)


## Is the system good?

I'll follow up soon with one more post on this in which we will consider whether this system looks good enough to trade. Before you read that post, think about what more we might want to know before making that decision. Based on his short question, I don't think Andrew has given us enough information for a full answer, but here's the value for you, the reader: what questions would you ask of Anthony, and, by extension, of the data? What more do we need to know?