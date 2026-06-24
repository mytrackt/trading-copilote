> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/prings-special-k.md).

# Pring's Special K

## What Is Pring's Special K Indicator? <a href="#introduction" id="introduction"></a>

Created by Martin Pring, Special K is a momentum indicator that combines short-, intermediate-, and long-term velocity into one complete series, thereby giving us truly summed cyclicality. It has two functions. They are:

1. Identify primary trend reversals at a relatively early stage.
2. Use that information to time short-term pro-trend price moves.&#x20;

The illustration below displays all three trends in an overlaid momentum format.

<figure><img src="/files/TtbjQOsIlGIunsJ9djFB" alt="Diagram illustrating short-, intermediate-, and long-term trends"><figcaption><p>Short-, intermediate-, and long-term trends.</p></figcaption></figure>

Below you see the (green) primary trend and the (orange) Special K (the short-term trend shown in the previous chart).

<figure><img src="/files/PqgRsjXnvee8pjIdEYXv" alt=""><figcaption><p>Primary trend and Special K.</p></figcaption></figure>

In an ideal world, the Special K peaks and troughs more or less simultaneously with the price at bull and bear market turning points. In most situations, that happens. When it does, you need to identify these turning points as quickly as possible, after the fact. The formula assumes that prices are revolving around the four-year business cycle. As a result, when a linear uptrend, such as the 1990s secular bull market in equities develops, the Special K leads turning points. Alternatively, when the cycle is truncated, as was the case for the 1987 crash, the indicator is late. In the charts below, most of the time, the price and Special K reverse simultaneously.

***The prime function of the Special K then is to identify primary trend turning points.*** Since this indicator also includes short-term data in its calculation, a subsidiary benefit lies in the identification of smaller trends, for trading purposes, and putting that in context with the direction and maturity of the primary trend. Let's consider both those aspects, starting with primary trend identification.

## Calculating Pring's Special K <a href="#calculation" id="calculation"></a>

The Special K is the sum of several different weighted averages of different rate-of-change calculations. The periods and weightings were selected based on years of market observations.

```
               
  Special K = 10 Period Simple Moving Average of ROC(10) * 1
            + 10 Period Simple Moving Average of ROC(15) * 2
            + 10 Period Simple Moving Average of ROC(20) * 3
            + 15 Period Simple Moving Average of ROC(30) * 4
            + 50 Period Simple Moving Average of ROC(40) * 1
            + 65 Period Simple Moving Average of ROC(65) * 2
            + 75 Period Simple Moving Average of ROC(75) * 3
            +100 Period Simple Moving Average of ROC(100)* 4
            +130 Period Simple Moving Average of ROC(195)* 1
            +130 Period Simple Moving Average of ROC(265)* 2
            +130 Period Simple Moving Average of ROC(390)* 3
            +195 Period Simple Moving Average of ROC(530)* 4
```

Note that at least 725 data points are required to accurately calculate this indicator. If less data is available, then the final line of the calculation is skipped.

## Identifying Long-Term Price Movements With Special K <a href="#identifying_long-term_price_movements" id="identifying_long-term_price_movements"></a>

With the benefit of hindsight, it's easy to spot the Special K turning points and relate them to primary trend peaks and troughs, as shown by the vertical arrows in the charts below. Unfortunately, since traders and investors work in real-time, they don't have the luxury of hindsight. The following are several techniques that help in spotting primary trend turning points using the Special K:

1. Since the Special K is a jagged indicator, it lends itself best to trend line construction. For example, if a trend line of nine months or more is violated, that usually means the Special K's primary trend has reversed and when the indicator changes trend so usually does the price.
2. It is normal to run a moving average through the Special K. The default is a 100-day smoothed by a 100-day SMA. Crossovers of the average typically signal a reversal in the direction of the primary trend. Occasionally, as with all moving average situations, whipsaws are triggered. When combined with a trend line break, though, a stronger and more reliable signal is triggered. Examples at the 2003 and 2009 bottoms for US equities are shown in the first chart above, where MA crosses and trendline violations develop more or less simultaneously.
3. Occasionally, the Special K traces out price patterns. When they are confirmed by some kind of trend reversal in the price itself, this usually represents a valid indication of a reversal in the prevailing primary trend. The GLD chart below offers two examples.

<figure><img src="/files/Kl6waMfz7XQJ2ebftY0r" alt=""><figcaption></figcaption></figure>

[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?s=SPY\&p=D\&st=1995-01-01\&en=2010-04-01\&id=p27191194097\&a=351268055)

***

<figure><img src="/files/J2fNHyxK6t99w6x0sT9M" alt=""><figcaption></figcaption></figure>

[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?s=$CRB\&p=D\&st=1995-01-01\&en=2014-01-01\&id=p91095913553\&a=351269321)

***

<figure><img src="/files/zle1ZL0dxQHImzFGh3l9" alt=""><figcaption></figcaption></figure>

[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?s=GLD\&p=D\&st=2008-01-02\&en=2013-05-06\&id=p98657791953\&a=351279812)

***

It's important to note that calculating the initial plot of the Special K involves several years of data. To really appreciate the long-term perspective offered by this indicator, around 5–10 years of additional data are required. That way, it's possible to see if the security in question is experiencing the expected cyclical swings. Most do, but occasionally you will find some that do not.

## Identifying Pro-Trend Short-Term Buy and Sell Signals <a href="#identifying_pro-trend_short-term_buy_and_sell_signals" id="identifying_pro-trend_short-term_buy_and_sell_signals"></a>

It's important for short-term traders to understand that trades executed in the direction of the main trend are more likely to be successful than those generated in a counter-cyclical way. An objective method of determining the direction of the primary trend is to use the Special K. Obviously, we can tell with the benefit of hindsight where the actual Special K peaks and troughs formed but, in real time, we do not have this luxury. One solution is to determine its position relative to its 10-day MA. Positive readings (i.e., above the MA) would indicate a primary bull market and vice versa.

When the direction of the primary trend has been determined to be bullish, trades from the long side would be initiated when the Special K itself crosses above its 10-day MA. These are shown with orange, upward arrows on the chart below. Trades would that being when the Special K is below its long-term MA and crosses below its 10-day MA. The chart below shows such a system for the Dow Jones UBS Commodity Index. The green vertical line represents the start of a bull market phase as defined by the Special K/10-day MA relationship.

\ <img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line">[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?s=DJP\&p=D\&st=2008-02-14\&en=2010-07-24\&id=p13988319489\&a=351486397)

<figure><img src="/files/Jgc5WO51EDRAvQnx7Mdr" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Note:** No buy signals are generated during the bearish periods, only sell signals (brown, downward arrows). The “Example Sell Point” was subpar because it developed during a bull market, but, unfortunately, the system was still in a bearish mode because the Special K was below its 10-day MA. This illustrates how this approach is far from perfect. As with all technical indicators, rather than blindly using this approach as a mechanical system, it's better to use pro trend signals as an alert and then use other indicators as a filter in a “weight of the evidence” approach.

\- Martin Pring
{% endhint %}

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Special K is available as an indicator for SharpCharts. The first line in the indicator is the raw Special K value. The second line is a double-smoothed moving average of the raw Special K value, which acts as a signal line.

The indicator can be positioned above, below or behind the underlying price plot. Placing the Special K directly behind the price plot accentuates the movements relative to the price action of the underlying security.

Users can adjust the signal line settings by changing the numbers in the Parameters box. The two parameters specify the number of periods in the two simple moving averages used for smoothing. The default parameter values are 100,100. Users can also apply “Advanced Options” to add a horizontal line.

<figure><img src="/files/5lIVf8D8oD9O3HOepdzH" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/1LdHSPBrTXd9eyuic4Gu" alt=""><figcaption></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Special K Bullish Short-Term Cross <a href="#special_k_bullish_short-term_cross" id="special_k_bullish_short-term_cross"></a>

This scan reveals stocks where Special K is above its signal line. A bullish signal is triggered when Special K crosses over its 10-day moving average.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [Special K > Special K Signal(100,100)]
AND [Special K x SMA(10,Special K)]
```

### Special K Bearish Short-Term Cross <a href="#special_k_bearish_short-term_cross" id="special_k_bearish_short-term_cross"></a>

This scan reveals stocks where Special K is below its signal line. A bearish signal is triggered when Special K crosses below its 10-day moving average.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [Special K < Special K Signal(100,100)]
AND [SMA(10,Special K) x Special K]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax for Special K scans, please see our [Scan Syntax Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#pring_s_special_k) in the Support Center.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/prings-special-k.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
