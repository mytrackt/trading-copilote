> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/six-month-cycle-macd.md).

# Six-Month Cycle MACD

Sy Harding introduced his seasonal MACD strategy in his 1999 book, *Riding the Bear*. The strategy combines the six-month seasonal cycle from the *Stock Trader's Almanac* and momentum using MACD, which was developed by Gerald Appel. Basically, MACD is used to confirm or trigger bullish and bearish signals within the guidelines of the six-month cycle. According to the *Stock Trader's Almanac*, using MACD greatly increased the profitability of the seasonal system and reduced risk.

## Six-Month Cycle <a href="#six-month_cycle" id="six-month_cycle"></a>

Discovered by Yale Hirsch, founder of the *Stock Trader's Almanac*, the six-month cycle defines a bullish cycle running from November to April and a bearish cycle running from May to October. This is where the phrase “sell in May and go away” comes from. While this cycle is certainly not infallible, statistics from the *Stock Trader's Almanac* show the stock market seriously outperforming during the bullish six month period and underperforming during the bearish six-month period. Over the past 50 years, the average gain for the Dow was less than 1% from May to October. In contrast, the average gain was more than 7% from November to April. The chart below shows the S\&P 500 with the six-month cycle over a 10-year period. The red arrows mark the start of May (bearish cycle), and the green arrows mark the beginning of November (bullish cycle).

<figure><img src="/files/w27jOGQr0sJcuHzVaTUV" alt=""><figcaption><p>Chart 1  -  Six Month Cycle MACD</p></figcaption></figure>

## Strategy <a href="#strategy" id="strategy"></a>

Sy Harding made some minor adjustments to the six-month cycle and added the MACD as a timing mechanism. First, Harding started the bullish cycle on October 16th, which is two weeks earlier. Starting the cycle a little earlier makes sense because there have been several October bottoms in the S\&P 500. Second, Harding started the bearish cycle on April 20th, which is almost three weeks later. Third, Harding added MACD to time signals near these cycle dates (October 16th and April 20th). Chartists can move ahead to the next trading date should April 20th or October 16th fall on a weekend.

There is more than one way to trigger a signal. A buy signal is triggered when the bullish cycle starts and MACD is on a bullish signal or, alternately, when MACD turns bullish after the bullish cycle starts. A sell signal is triggered when the bearish cycle starts and MACD is on a bearish signal or when MACD turns bearish after the bearish cycle starts. MACD turns bullish when it moves above its signal line or into positive territory, whichever comes first. MACD turns bearish when it moves below its signal line or into negative territory.

<figure><img src="/files/ooiLcjSJg6IpQnww16Kt" alt=""><figcaption><p>Chart 2  -  Six Month Cycle MACD</p></figcaption></figure>

The chart above shows the S\&P 500 with MACD from March 2011 to February 2012, which encompasses two cycles. The bearish cycle started on April 20th and MACD was already on a bearish signal (below its signal line). The bullish cycle started on October 16th and MACD was already on a bullish signal (above its signal line and in positive territory).

#### **Buy Signal Recap:**

1. Buy on October 16th if MACD is bullish.
2. Wait for bullish MACD signal if MACD is not bullish on October 16th.

#### **Sell Signal Recap:**

1. Sell on April 20th if MACD is bearish.
2. Wait for a bearish MACD signal if MACD is not bearish on April 20th.

## Tweaks <a href="#tweaks" id="tweaks"></a>

Sy Harding tweaked this system even further by anticipating the six-month cycle. While chartists do not really know when a MACD signal will trigger, we can figure out when the six-month cycle will trigger. It is, after all, like clockwork. Knowing that the six-month cycle will turn bearish in May, traders can use the whole month of April to anticipate a sell signal in MACD. Similarly, traders can use the whole month of October to anticipate a buy signal. This requires a lot more discretion and intuition, however. Taking a signal in April or October seems acceptable, but what about signals in late March or late September?

<figure><img src="/files/FqKWh91TNXk0MTt4384P" alt=""><figcaption><p>Chart 4  -  Six Month Cycle MACD</p></figcaption></figure>

The chart above shows SPY from February 2010 to February 2011. MACD moved below its signal line in late April and SPY broke support in early May, both of which produced solid signals. SPY bottomed in early July and formed a higher low in August. MACD moved above its signal line in early September and broke resistance in mid-September. These signals were well before the bullish six-month cycle started, but traders would have faced an overbought market if they had waited until October. Speculation requires anticipation.

Chartists can also consider using weekly charts and weekly MACD. However, only the signal line crossovers would work because the centerline crosses are too infrequent. The chart below shows DIA with weekly MACD, bearish cycles in yellow and bullish cycles in white. There were some good signals, some bad signals, and some non-signals. For example, MACD did not turn down during the bearish cycle period from May 2009 until October 2009.

<figure><img src="/files/I5eIQGK5tfF4FMO0mxbz" alt=""><figcaption><p>Chart 14 -  Six Month Cycle MACD</p></figcaption></figure>

## Final Thoughts <a href="#conclusion" id="conclusion"></a>

The six-month cycle is not infallible. While adding MACD improves the historical results, it does not mean every signal will work. As with every system, there will be good signals, great signals, bad signals and ugly signals. The overall results are based on over 50 years of trading, which means over 100 signals. Most likely, the gains in some of the great signals made up for the losses in the bad signals to produce a positive result overall. Keep in mind that this article is designed as a starting point for trading system development. Use these ideas to augment your trading style, risk-reward preferences and personal judgments.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/six-month-cycle-macd.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
