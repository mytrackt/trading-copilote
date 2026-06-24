> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/narrow-range-day-nr7.md).

# Narrow Range Day NR7

Narrow range patterns come from Toby Crabel's book, *Day Trading with Short Term Price Patterns & Opening Range Breakout*. Even though the book, which was published in 1990, is currently out of print, many of its ideas are still effective. In particular, the NR4 (Narrow Range 4) and NR7 (Narrow Range 7) patterns are quite popular with short-term traders. The philosophy behind the pattern is similar to the Bollinger Band Squeeze, that is, a volatility expansion often follows a volatility contraction. Narrow range days mark price contractions that often precede price expansions. Even though Crabel traded mainly futures, traders can apply these techniques to stocks, indices and ETFs.

## Strategy <a href="#strategy" id="strategy"></a>

This strategy starts with the day's range, which is simply the difference between the high and the low. Crabel used the absolute range, as opposed to the percentage range, which would be the absolute range divided by the close or the midpoint. Because we are only dealing with four and seven days, the difference between the absolute range and percentage range is negligible.

Crabel focused on two different narrow range timeframes: four days and seven days. An NR4 pattern would be the narrowest range in four days, while an NR7 would be the narrowest range in seven days. It is a very short-term pattern designed to initiate a trade based on an “opening range breakout,” which is another term from Crabel's book. The opening range breakout (ORB) is based on the price range in the first five minutes of trading, which is too short of a term for this article. Instead, chartists can look for an upside breakout when prices move above the high of the narrow range day and a downside breakdown when prices move below the low of the narrow range day.

<figure><img src="/files/CRhtDf9eUjKE4DhszImi" alt=""><figcaption><p>Chart 1  -  Narrow Range Days</p></figcaption></figure>

<figure><img src="/files/QIXtsHG5mV7sY8BYe1nm" alt=""><figcaption><p>Chart 2  -  Narrow Range Days</p></figcaption></figure>

Because this is a short-term setup, it is important that the trade starts working right away. Failure to continue in the direction of the signal is the first warning. After a buy signal, a move below the low of the narrow range day would be negative. Conversely, a move above the high of the narrow range day would negate a sell signal.

Chartists also need to consider profit targets and stop-losses. Crabel took profits quite quickly, usually at the close of the first trading day or on the first profitable close. Again, this is very short-term-oriented and might not be suitable for all traders. Alternatively, profits can be taken near the next resistance level or a percentage target could be used. For stops, chartists can use the Parabolic SAR to trail stops or base their stops on the Average True Range (ATR). For example, the stop-loss on a long position could be set two Average True Range values below current prices and trailed higher.

#### **Bull Signal Recap:**

1. Identify NR4 or NR7 day.
2. Buy on move above high of narrow range day high.

#### **Bear Signal Recap:**

1. Identify NR4 or NR7 day.
2. Sell on move below low of narrow range day low.

## Trading Example <a href="#trading_example" id="trading_example"></a>

The trading example shows Morgan Stanley with twelve signals in less than three months. The blue arrows show the NR7 candlesticks and the thin blue lines mark the high-low of the range. A next day move above the high is bullish, while a next day move below the low is bearish. Notice that NR7 days formed back-to-back on three different occasions. While not always the case, these back-to-back NR7 days did not result in different signals, they simply affirm the existing signal from the prior NR7 breakout. With nine signals in total, traders could have to watch price action closely, exercise judgment and manage stops.

<figure><img src="/files/ath4VrWSfoLoZDyLxr33" alt=""><figcaption><p>Chart 3  -  Narrow Range Days</p></figcaption></figure>

## SharpCharts Alternatives <a href="#sharpcharts_alternatives" id="sharpcharts_alternatives"></a>

SharpCharts does not offer an indicator that shows the day's range or identifies NR4 and NR7 days. However, it is possible to scan for NR4 or NR7 days using the Advanced Scan Workbench to write the code, an example of which is provided in the next section. On SharpCharts, chartists can use a 1-period Average True Range (ATR) to imitate or estimate the “range” and visually identify “NATR7” readings, which means ATR is its narrowest in seven days. While this NATR7 will not produce the exact same signals, many will overlap with the basic NR7 readings. More importantly, the Average True Range does show when the range is contracting or expanding.

<figure><img src="/files/l9b3mcbl3GgbsETIQbq4" alt=""><figcaption><p>Chart 4  -  Narrow Range Days</p></figcaption></figure>

## Tweaking <a href="#tweaking" id="tweaking"></a>

Most chartists will want to qualify NR7 signals, as they are quite frequent. A typical stock will produce dozens of NR7 days in a twelve-month period; a daily scan of US stocks will often return hundreds of stocks with NR7 days. Chartists can increase or decrease the number of narrow range periods to affect the results. A decrease from NR7 to NR4 would increase the number of stocks fitting the criteria, while an increase from NR7 to NR20 would decrease the number of candidates. In general, the number of stocks meeting the criteria will increase as the narrow range period decreases and decrease as the narrow range period increases.

Chartists can also add other indicators to further qualify signals. In fact, it is often a good idea to add a trend indicator and an overbought/oversold indicator. Adding a trend indicator ensures that trades are in the direction of a bigger trend. Adding an overbought/oversold oscillator identifies pullbacks or bounces to improve the risk-reward ratio.

The chart below shows McDonalds with the 1-period Average True Range (ATR) to mimic NR7 signals, the Aroon indicators to define the bigger trend and the Commodity Channel Index (CCI) to define overbought/oversold conditions. A bullish signal occurs when Aroon Up is above Aroon Down (uptrend), the 5-day low for CCI is below -100 (oversold) and the range moves to a seven day low (turning point). Bearish signals occur when Aroon Down is above Aroon Up (downtrend), the 5-day high for CCI is above +100 (overbought) and the range moves to a seven day low (turning point).

<figure><img src="/files/QtZ7KmeQVJRWJFwKuJot" alt=""><figcaption><p>Chart 5  -  Narrow Range Days</p></figcaption></figure>

There were two signals in late November. The first signal did not work, but there was another a few days later that marked a good bottom.

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The NR7 day is based on the premise that range contractions are followed by range expansions. In this regard, the indicator is neutral when it comes to future price direction. As with Bollinger Bands, chartists must employ other tools for a directional bias. Because NR7 days are relatively commonplace and the range is small by definition, the chances of whipsaw are above average. A break above the NR7 high can fail and be followed by a break below the NR7 high. Keep the bigger picture in mind and be wary of sell signals within a bullish pattern, such as a falling flag or at a support test. This article is designed as a starting point for trading system development. Use these ideas to augment your trading style, risk-reward preferences and personal judgments. [Click here](https://stockcharts.com/h-sc/ui?s=IBM\&p=D\&yr=0\&mn=6\&dy=0\&id=p11241870721\&listNum=30\&a=262493168) for a chart of IBM with the Average True Range (ATR), Aroon indicators and Commodity Channel Index (CCI).

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### NR7 in Uptrend After Pullback <a href="#nr7_in_uptrend_after_pullback" id="nr7_in_uptrend_after_pullback"></a>

This scan reveals stocks that have just had an NR7 day during an uptrend (as indicated by the Aroon indicator values) and whose CCI values indicate an oversold condition.

```
  [type = stock] 
  and [country = us] 
  and [daily sma(20,daily volume) > 100000] 
  and [daily sma(60,daily close) > 20] 
  and [Range < 1 day ago Min (6, Range)] 
  and [today's high < yesterday's high]
  and [today's low > yesterday's low]
  and [Min (5, CCI(10)) < -100] 
  and [Aroon Up (63) > Aroon Down(63)]
```

### NR7 in Downtrend After Pullback <a href="#nr7_in_downtrend_after_pullback" id="nr7_in_downtrend_after_pullback"></a>

This scan reveals stocks that have just had an NR7 day during a downtrend (as indicated by the Aroon indicator values) and whose CCI values indicate an overbought condition.

```
  [type = stock] 
  and [country = us] 
  and [daily sma(20,daily volume) > 100000] 
  and [daily sma(60,daily close) > 20] 
  and [Range < 1 day ago Min (6, Range)] 
  and [today's high < yesterday's high]
  and [today's low > yesterday's low]
  and [Max (5, CCI(10)) > 100] 
  and [Aroon Up (63) < Aroon Down(63)]
```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/narrow-range-day-nr7.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
