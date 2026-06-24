> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/pivot-points.md).

# Pivot Points

## What Are Pivot Points? <a href="#introduction" id="introduction"></a>

**Pivot Points are significant levels on a chart that traders and investors can use to determine directional movement and potential support/resistance levels.** Pivot Points use the prior period's high, low, and close to estimate future support and resistance levels. In this regard, Pivot Points are predictive or leading indicators.&#x20;

There are at least five different versions of Pivot Points. This article will focus on Standard Pivot Points, Demark Pivot Points, and Fibonacci Pivot Points.

Pivot Points were originally used by floor traders to set key levels. Like modern-era day traders, floor traders dealt with a fast-moving environment and short-term focus. At the beginning of the trading day, floor traders would look at the previous day's high, low, and close to calculate a Pivot Point for the current trading day. With this Pivot Point as the base, further calculations were used to set support 1, support 2, resistance 1, and resistance 2. These levels would then be used to assist their trading throughout the day.

## Timeframes for Pivot Points <a href="#timeframes" id="timeframes"></a>

Pivot Points for 1-, 5-, 10-, and 15-minute charts use the prior day's high, low, and close. In other words, Pivot Points for today's intraday charts would be based solely on yesterday's high, low, and close. Once Pivot Points are set, they do not change and remain in play throughout the day.

<figure><img src="/files/nYrjS5acQljPacrRsBF1" alt="Chart from StockCharts.com showing pivot points on a 10-minute chart"><figcaption><p>Example of pivot points on a 10-minute chart.</p></figcaption></figure>

Pivot Points for 30-, 60-, and 120-minute charts use the prior week's high, low, and close. These calculations are based on calendar weeks. Once the week starts, the Pivot Points for 30-, 60-, and 120-minute charts remain fixed for the entire week. **The Pivots do not change until the week ends, and new ones can be calculated.**

<figure><img src="/files/o0WRjSbfCl4jTIcNkhxX" alt=""><figcaption><p>Pivot points on a 60-minute chart.</p></figcaption></figure>

Pivot Points for daily charts use the prior month's data. Pivot Points for June 1 would be based on the high, low, and close for May. They remain fixed for the entire month of June. New Pivot Points would be calculated on the first trading day of July. These would be based on the high, low, and close for June.

<figure><img src="/files/nrUgncOTTbBEX4sdiwZ1" alt="Chart from StockCharts.com showing pivot points on a daily chart"><figcaption><p>Pivot Points on a daily chart. </p></figcaption></figure>

Pivot Points for weekly and monthly charts use the prior year's data.

## Standard Pivot Points <a href="#standard_pivot_points" id="standard_pivot_points"></a>

Standard Pivot Points begin with a base Pivot Point. This is a simple average of the high, low and close. The middle Pivot Point is shown as a solid line between the support and resistance pivots. Keep in mind that the high, low and close are all from the prior period.

{% code overflow="wrap" %}

```
Pivot Point (P) = (High + Low + Close)/3

Support 1 (S1) = (P x 2) - High

Support 2 (S2) = P  -  (High  -  Low)

Resistance 1 (R1) = (P x 2) - Low

Resistance 2 (R2) = P + (High  -  Low)
```

{% endcode %}

The chart below shows the Nasdaq 100 ETF (QQQ) with Standard Pivot Points on a 15-minute chart. At the start of trading on June 9, the Pivot Point is in the middle, the resistance levels are above, and the support levels are below. These levels remain constant throughout the day.

<figure><img src="/files/OChXUfbx8e7ceFBCo8JT" alt=""><figcaption><p>Example of standard Pivot Points on a 15-minute chart.</p></figcaption></figure>

## Fibonacci Pivot Points <a href="#fibonacci_pivot_points" id="fibonacci_pivot_points"></a>

Fibonacci Pivot Points start just the same as Standard Pivot Points. Fibonacci multiples of the high-low differential from the base Pivot Point are added to form resistance levels and subtracted to form support levels.

{% code overflow="wrap" %}

```
Pivot Point (P) = (High + Low + Close)/3

Support 1 (S1) = P - {.382 * (High  -  Low)}

Support 2 (S2) = P - {.618 * (High  -  Low)}

Support 3 (S3) = P - {1 * (High  -  Low)}

Resistance 1 (R1) = P + {.382 * (High  -  Low)}

Resistance 2 (R2) = P + {.618 * (High  -  Low)}

Resistance 3 (R3) = P + {1 * (High  -  Low)}
```

{% endcode %}

The chart below shows the Dow Industrials SPDR (DIA) with Fibonacci Pivot Points on a 15-minute chart. R1 and S1 are based on 38.2%, R2 and S2 are based on 61.8%, and R3 and S3 are based on 100%.

<figure><img src="/files/5RNxKoKYOY5QjpaRsMpz" alt="Chart from StockCharts.com showing Fibonacci Pivot Points on a 15-minute chart"><figcaption><p>Example of Fibonacci Pivot Points on a 15-minute chart.</p></figcaption></figure>

## Demark Pivot Points <a href="#demark_pivot_points" id="demark_pivot_points"></a>

Demark Pivot Points start with a different base and use different formulas for support and resistance. These Pivot Points are conditional on the relationship between the close and the open.

{% code overflow="wrap" %}

```
If Close < Open, then X = High + (2 x Low) + Close

If Close > Open, then X = (2 x High) + Low + Close

If Close = Open, then X = High + Low + (2 x Close)

Pivot Point (P) = X/4

Support 1 (S1) = X/2 - High

Resistance 1 (R1) = X/2 - Low
```

{% endcode %}

The chart below shows the Russell 2000 ETF (IWM) with Demark Pivot Points on a 15-minute chart. There is only one resistance (R1) and one support (S1). Demark Pivot Points do not have multiple support or resistance levels.

<figure><img src="/files/XNKJqPnES2gXUXvK7XL6" alt="Chart from StockCharts.com showing Demark Pivot Points on a 15-minute chart"><figcaption><p>Example of Demark Pivot Points on a 15-minute chart.</p></figcaption></figure>

## Setting the Tone <a href="#setting_the_tone" id="setting_the_tone"></a>

The Pivot Point sets the general tone for price action. This is the middle line of the group that is marked (P). A move above the Pivot Point is positive and shows strength. Keep in mind that this Pivot Point is based on the prior period's data. It is put forth in the current period as the first important level. A move above the Pivot Point suggests strength with a target to the first resistance. A break above the first resistance shows even more strength with a target to the second resistance level.

<figure><img src="/files/UYEMpFL4tIwMgmBQrQMi" alt="Chart from StockCharts.com showing the different pivot points"><figcaption><p>When price moves above the Pivot Point, it's positive and shows strength. </p></figcaption></figure>

The converse is true on the downside. A move below the Pivot Point suggests weakness with a target to the first support level. A break below the first support level shows even more weakness with a target to the second support level.

## Support and Resistance <a href="#support_and_resistance" id="support_and_resistance"></a>

Support and resistance levels based on Pivot Points can be used like traditional support and resistance levels. The key is to watch price action closely when these levels come into play. If prices decline to support and then firm, traders can look for a successful test and bounce off support. It often helps to look for a bullish chart pattern or indicator signal to confirm an upturn from support.&#x20;

Similarly, if prices advance to resistance and stall, traders can look for a failure at resistance and decline. Again, look for a bearish chart pattern or indicator signal to confirm a downturn from resistance.

<figure><img src="/files/tlJLqnVWprgeghzk3QdC" alt="Chart from StockCharts.com showing support and resistance levels based on pivot points"><figcaption><p>An example of support and resistance levels based on Pivot Points.</p></figcaption></figure>

The second support and resistance levels can also identify potentially overbought and oversold conditions. A move above the second resistance level would show strength but also indicate an overbought situation that could lead to a pullback. Similarly, a move below the second support would show weakness but suggest a short-term oversold condition that could lead to a price bounce.

<figure><img src="/files/mZvyuWLkMUOyHs3YH3KM" alt="Chart from StockCharts.com showing second support and resistance levels identifying overbought and oversold conditions"><figcaption><p>Example of second support and resistance levels identifying overbought and oversold conditions.</p></figcaption></figure>

## The Takeaway <a href="#conclusion" id="conclusion"></a>

**Pivot Points offer chartists a methodology for determining price direction and setting support and resistance levels. Price direction is determined by looking at the current period's price action relative to the pivot point: starting above or below the pivot point** **or crossing it in either direction during trading.** The set support and resistance points come into play after determining price direction. While originally designed for floor traders, the concepts behind Pivot Points can be applied across various timeframes.

As with all indicators, confirming Pivot Point signals with other aspects of technical analysis is important. A [bearish candlestick reversal pattern](/table-of-contents/chart-analysis/candlestick-charts/candlestick-bearish-reversal-patterns.md) could confirm a reversal at second resistance. An oversold [Relative Strength Index](/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi.md) (RSI) could confirm oversold conditions at second support. An upturn in MACD could be used to confirm a successful support test.

On a final note, sometimes the second or third support/resistance levels are not seen on the chart. This is because their levels exceed the price scale on the right. In other words, they are off the chart.

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

Pivot Points can be found as an **Overlay** on the SharpCharts Workbench. Standard Pivot Points are the default setting, and the parameters box is empty. Place an “F” in the parameters box to apply Fibonacci Pivot Points. Place a “D” in the box to apply Demark Pivot Points. It is even possible to display all three at the same time.

***

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line"> [Click here](https://stockcharts.com/sc3/ui/?s=$SPX\&p=D\&b=5\&g=0\&id=p75918574596\&listNum=30\&a=236469237) for a live chart with all three Pivot Points. You can then remove the ones you do not want.

***

<figure><img src="/files/UqwFkbxXFyqNPuY5Ix6l" alt=""><figcaption><p>Example of Pivot Points in SharpCharts.</p></figcaption></figure>

<figure><img src="/files/NMheuM0XiQotMRroA6lL" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Learn More.** For more details on the parameters used to configure Pivot Points overlays, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#pivot_points) in the Support Center.
{% endhint %}

## Additional Resources <a href="#recommended_books" id="recommended_books"></a>

### Recommended Books <a href="#recommended_books" id="recommended_books"></a>

#### [A Complete Guide to Technical Trading Tactics](https://a.co/d/74c4mav)

by John Person

<div align="left"><figure><img src="https://school.stockcharts.com/lib/exe/fetch.php?media=technical_indicators:pivot_points:store_person_technicaltradingtactics.jpg" alt=""><figcaption></figcaption></figure></div>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/pivot-points.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
