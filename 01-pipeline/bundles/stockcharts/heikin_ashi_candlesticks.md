> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/heikin-ashi-candlesticks.md).

# Heikin-Ashi Candlesticks

## What Are Heikin-Ashi Charts? <a href="#introduction" id="introduction"></a>

Heikin-Ashi Candlesticks are an offshoot from Japanese candlesticks. Heikin-Ashi Candlesticks use the open-close data from the prior period and the open-high-low-close data from the current period to create a combo candlestick. The resulting candlestick filters out some noise in an effort to better capture the trend.&#x20;

In Japanese, *Heikin* means “average” and *Ashi* means “pace” (EUDict.com). Taken together, Heikin-Ashi represents the average pace of prices. Heikin-Ashi Candlesticks are not used like regular candlesticks. You won't find dozens of bullish or bearish reversal patterns consisting of one to three candlesticks. Instead, Heikin-Ashi candlesticks can be used to identify trending periods, potential reversal points, and classic chart patterns.

## Calculating Heikin-Ashi <a href="#calculation" id="calculation"></a>

Heikin-Ashi Candlesticks are based on price data from the current open-high-low-close, current Heikin-Ashi values, and prior Heikin-Ashi values. Yes, it is a bit complicated. In the formula below, a “(0)” denotes the current period. A “(-1)” denotes the prior period. “HA” refers to Heikin-Ashi. Let's take each data point one at a time.

```
1. The Heikin-Ashi Close is an average of the open, 
high, low and close for the current period. 

<b>HA-Close = (Open(0) + High(0) + Low(0) + Close(0)) / 4</b>

2. The Heikin-Ashi Open is the average of the prior Heikin-Ashi 
candlestick open plus the close of the prior Heikin-Ashi candlestick. 

<b>HA-Open = (HA-Open(-1) + HA-Close(-1)) / 2</b> 

3. The Heikin-Ashi High is the maximum of three data points: 
the current period's high, the current Heikin-Ashi 
candlestick open or the current Heikin-Ashi candlestick close. 

<b>HA-High = Maximum of the High(0), HA-Open(0) or HA-Close(0) </b>

4. The Heikin-Ashi low is the minimum of three data points: 
the current period's low, the current Heikin-Ashi 
candlestick open or the current Heikin-Ashi candlestick close.

<b>HA-Low = Minimum of the Low(0), HA-Open(0) or HA-Close(0) </b>
```

Before moving to a spreadsheet example, note that there's a chicken and egg dilemma. You need the first Heikin-Ashi candlestick before calculating future Heikin-Ashi candlesticks. Therefore, the first calculation uses data from the current open, high, low and close.&#x20;

The first Heikin-Ashi close equals the average of the open, high, low and close ((O+H+L+C)/4). The first Heikin-Ashi open equals the average of the open and close ((O+C)/2). The first Heikin-Ashi high equals the high and the first Heikin-Ashi low equals the low. Even though this first Heikin-Ashi candlestick is somewhat artificial, the effects will dissipate over time (usually seven to 10 periods).&#x20;

<figure><img src="/files/CZgQynJeuEL9oP3Y2ke1" alt="Spreadsheet example of Heikin-Ashi calculations."><figcaption><p>Spreadsheet displaying Heikin-Ashi calculations.</p></figcaption></figure>

StockCharts.com starts its Heikin-Ashi calculations before the first price date, which is visible on each chart. Therefore, the effects of this first calculation will have already dissipated. The chart below shows examples of two normal candlesticks converting into one Heikin-Ashi Candlestick.

<figure><img src="/files/Mew8naoDY5SFWcRyDOE1" alt="Chart from StockCharts.com showing how regular candlesticks convert to Heikin-Ashi candlesticks."><figcaption><p>Example showing how candlesticks convert to Heikin-Ashi candlesticks.</p></figcaption></figure>

## How To Read a Heikin-Ashi Chart <a href="#interpretation" id="interpretation"></a>

Heikin-Ashi Candlesticks are similar to regular candlesticks but differ in some key features. A Heikin-Ashi candlestick is hollow when the HA-close is above the HA-open; conversely, Heikin-Ashi candlesticks are filled when the HA-close is below the HA-open. This is similar to normal candlesticks, filled when the close is below the open and hollow when the close is above the open.

While traditional candlestick patterns don't exist with Heikin-Ashi candlesticks, chartists can derive valuable information from these charts. A long hollow Heikin-Ashi candlestick shows strong buying pressure over two days. The absence of a lower shadow also reflects strength.&#x20;

A long, filled Heikin-Ashi candlestick shows strong selling pressure over two days. The absence of an upper shadow also reflects selling pressure. Small Heikin-Ashi candlesticks or those with long upper and lower shadows show indecision over the last two days. This often occurs when one candlestick is filled, and the other is hollow.

The chart below shows QQQ with Heikin-Ashi candlesticks over four months.

<figure><img src="/files/8P2sb9aLkFL1R2tckLsB" alt="Heikin-Ashi chart from StockCharts.com showing indecisive market, a strong decline, and a strong advance."><figcaption><p>Heikin-Ashi chart showing an indecisive market, a strong decline, and a strong advance.   </p></figcaption></figure>

An indecisive market can sometimes foreshadow a trend reversal. The blue arrows show indecisive Heikin-Ashi Candlesticks formed with two normal candlesticks of opposite colors.&#x20;

The red arrows show a strong decline marked by a series of Heikin-Ashi candlesticks without upper shadows. This means the Heikin-Ashi open marked the high, and the remaining data points were lower.&#x20;

The green arrow shows a strong advance marked by a series of Heikin-Ashi candlesticks without lower shadows. The Heikin-Ashi open marked the low, and the remaining data points were higher.

## Doji and Spinning Tops <a href="#doji_and_spinning_tops" id="doji_and_spinning_tops"></a>

As with normal candlesticks, Heikin-Ashi doji and spinning tops can be used to foreshadow reversals. A Heikin-Ashi doji or Heikin-Ashi spinning top looks similar to a [traditional doji or spinning top](#doji_and_spinning_tops) (see image below).&#x20;

<figure><img src="/files/BQG5BsI73knDA9nLEdkJ" alt="Illustration of doji and spinning top candlesticks"><figcaption><p>Illustration of dojis and spinning tops.</p></figcaption></figure>

Despite much movement from high to low, prices finish near their opening point for little change. This shows indecision that can foreshadow a reversal.

When using Heikin-Ashi candlesticks, a doji or spinning top in a downtrend should not immediately be considered bullish. It shows indecision within the downtrend. Indecision is the first indication of a change in trend direction. You need a confirmation of a directional change (trend reversal). For example, when you spot a doji or spinning top in a downtrend, set a resistance level to base a trend reversal.

The example below shows Caterpillar (CAT) with a spinning top forming in late May (1). The trend is down, so a resistance level is set to define a reversal breakout (confirmation). CAT broke this resistance level a few days later, but the breakout failed—a reminder that not all signals are perfect. The downtrend extended, and CAT then formed two dojis in mid-June. A resistance level was marked after the doji, and CAT broke resistance to confirm a reversal.

<figure><img src="/files/0ehUln2h5QKSVKBoMtQz" alt="Heikin-Ashi chart from StockCharts.com showing spinning tops and dojis indicating reversals but confirmation is only when a breakout occurs."><figcaption><p>Spinning top and dojis represent reversal areas, but trends are confirmed when there's a breakout.</p></figcaption></figure>

Prices extended higher until the stock stalled around 110 in July. Two doji and an indecisive candlestick formed in mid-July (3). Also, a clear support level was established. CAT broke support in late July to start a strong downtrend and confirm the trend reversal. A spinning top formed during this downtrend (4), but there was no upside follow-through or reversal. Confirmation of a trend reversal is important.

## Classic Chart Patterns and Heikin-Ashi <a href="#classic_chart_patterns" id="classic_chart_patterns"></a>

Classic chart patterns and trend lines can also be used on Heikin-Ashi charts. In contrast to normal candlesticks, Heikin-Ashi Candlesticks are more likely to trend with strings of consecutive filled candlesticks and hollow (white) candlesticks.&#x20;

The chart below shows Apache (APA) falling with a string of filled candlesticks in late October. The Heikin-Ashi candlesticks formed a falling wedge, and APA broke resistance with a surge in early November. As the stock consolidated in November, a triangle consolidation took shape. The upside breakout signaled a continuation of the bigger uptrend.

<figure><img src="/files/PwSqJNOUHbS8qWo6iCRU" alt="Example of a Heikin-Ashi chart from StockCharts.com showing a breakout from a falling wedge and triangle pattern."><figcaption><p>Heikin-Ashi chart showing breakouts from falling wedge and triangle patterns </p></figcaption></figure>

The next chart shows Monsanto (MON) with a classic correction in June 2011. The Heikin-Ashi Candlesticks were more than adequate to identify this correction and subsequent breakout. Notice how a falling channel formed as the stock retraced around 61.80% of the prior decline. The big breakout in late June signaled an end to this correction and resumption of the advance.

<figure><img src="/files/gO4QZBZCdRlMHR6un8JR" alt="Heikin-Ashi chart from StockCharts.com showing a breakout from a falling channel which signaled the end of a correction and start of an uptrend."><figcaption><p>Heikin-Ashi chart shows a breakout from a falling channel which signaled the end of the correction and start of an uptrend.</p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

Heikin-Ashi Candlesticks are a versatile tool that can filter noise, foreshadow reversals, and identify classic chart patterns. In fact, all aspects of classical technical analysis can be applied to these charts. Chartists can use Heikin-Ashi Candlesticks to identify support and resistance, draw trend lines or measure retracements. Volume indicators and momentum oscillators also work well. [**Click here**](https://stockcharts.com/sc3/ui/?s=SPY\&p=D\&yr=0\&mn=6\&dy=0\&id=p30728818423\&listNum=30\&a=243449099) for a live Heikin-Ashi chart.

***

## SharpCharts <a href="#sharpcharts" id="sharpcharts"></a>

In SharpCharts you can find Heikin-Ashi under **Chart Type** in the **Attributes** area of the Chart Settings. Use the **Up Color** and **Down Color** settings to change from the default colors for up day and down day price bars.&#x20;

By default, a red-filled candlestick means the close was below the open (filled) and the close was lower than the prior close (red). A black hollow candlestick means the close was above the open (hollow), and the close was higher than the prior close (black).&#x20;

<figure><img src="/files/YXnkQI9gGZsgTdr4qflU" alt="Chart showing traditional candlestick and Heikin-Ashi candlestick charts from StockCharts.com side by side."><figcaption><p>Candlesticks and Heikin-Ashi Candlesticks. </p></figcaption></figure>

<figure><img src="/files/w20pJ0qU1qEUfognvQpi" alt="SharpCharts settings for Heikin-Ashi charts."><figcaption><p>SharpChart settings for Heikin-Ashi charts</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/heikin-ashi-candlesticks.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
