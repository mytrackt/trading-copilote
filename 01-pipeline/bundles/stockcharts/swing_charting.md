> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/swing-charting.md).

# Swing Charting

What do Point & Figure charts, Kagi charts, Renko charts, Filtered Waves, and ZigZag have in common? They are all related to swing charting in some way.&#x20;

## What Is Swing Charting?

Swing charting follows a simple concept: additional information to the chart is made when a new price swing penetrates the level of the prior swing in the same direction. The basis of this type of charting is the filter. Once prices have moved by the distance specified by this filter, a new line is drawn next to the previous one. In a nutshell, it is a chart that shows up and down price movement of a minimum size, regardless of the time it takes.

Swing charts work similarly to a breakout system. A new high made after so many days is a buy signal, while a sell signal occurs when a new low is made after so many days. This has been written about for years by Gann, Merrill, Livermore, Donchian, Hochheimer, Wilder, and Keltner, all of whom used some form of swing charting.

Many swing-based systems use volatility as the basis for determining the parameters for the swing filter. This way, as the current volatility increases, the number of days used to calculate the swing filter decreases.

## Swing Charting Techniques

One of the simpler swing systems was Donchian's Four-Week Rule: buy when the current price goes above the highs of the previous four full weeks, but sell (go short) when the price falls below the lows of the last four whole weeks. That's it. Guess what? In 1970, Dunn and Hargitt Financial Services rated it the best of the popular systems of the day.

There are a host of different swing charting techniques. Some use three consecutive new highs as an upmove and will remain as such until three consecutive new lows. The list is endless, but the concept is the same.

Arthur Merrill first wrote about filtered waves in his book, *Filtered Waves*, in 1977. His swing filter was merely a percentage of price movement. This technique removes actual price from the decision and can work on almost any time series. For all you engineers, it is just an amplitude filter; it helps remove undesirable information.

ZigZag is used by many charting programs, including StockCharts.com, for this filtered wave type of charting.

A simple example is to display price data identifying only moves of 5% or greater.

<figure><img src="/files/QyrpC4y9Tw7kwWDcOI1V" alt=""><figcaption><p>Hewlett-Packard Co. (HPQ) Swing example chart from StockCharts.com</p></figcaption></figure>

It filters out all the small price variations, showing only 5% or greater moves.

A caveat, however, is that the last leg of ZigZag will change as the most recent price changes until prices are reversed by the filter amount (5% in the above chart). The critical item is the turning point, which is the point at which prices have reached at least the filter amount since they reversed. If you see a turning point, then prices have already moved at least the filtered amount in the opposite direction. (Please re-read this paragraph until it sinks in.)

Below is the same price data but with a 10% filter being used. Notice how it removed some of the smaller waves.

<figure><img src="/files/5x85CcFiOvYPztPh2sNj" alt=""><figcaption><p>Hewlett-Packard Co. (HPQ) Swing example chart from StockCharts.com</p></figcaption></figure>

Below is a chart using the exact same data, but with a filter of 15%. That is, only moves of 15% or greater are shown by ZigZag. Notice that the small up-move in the last few days of the previous charts is gone. This is because prices have not moved upward by 15% since the down leg started.

<figure><img src="/files/75kdsBsDYgTnPLcqhE6U" alt=""><figcaption><p>Hewlett-Packard Co. (HPQ) Swing example chart from StockCharts.com</p></figcaption></figure>

Swing charting is a viable tool for trading and making investment decisions, as it assists you in staying with the trend, limiting losses and following well-defined rules.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/swing-charting.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
