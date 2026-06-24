> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/candlevolume.md).

# CandleVolume

## What Are CandleVolume Charts? <a href="#introduction" id="introduction"></a>

As its name implies, CandleVolume charts merge volume into candlesticks. This allows chartists to analyze price action and volume with one look at the price chart. CandleVolume charts are similar to [EquiVolume charts](/table-of-contents/chart-analysis/chart-types/equivolume.md) but offer more information because candlesticks are used instead of high-low boxes. This means chartists can see the open and close for each period, as well as the high and the low. CandleVolume charts can be used just like normal charts. Chartists can look for candlestick patterns and classical chart patterns, such as triangles and wedges, to generate signals.

## Calculating CandleVolume Charts <a href="#calculation" id="calculation"></a>

A CandleVolume candlestick comprises five components—open, high, low, close, and volume. As with [normal candlesticks](/table-of-contents/chart-analysis/candlestick-charts/introduction-to-candlesticks.md), the open and close form the candlestick's body, while the high and low form the upper and lower shadows.&#x20;

Volume determines the width of the candlestick. Wide candlesticks form when volume is high, while narrow candlesticks form when volume is low. The chart below shows basic black and white (filled and hollow) candlesticks based on CandleVolume. Wide and hollow candlesticks form when the close is well above the open and volume is high. Wide and filled candlesticks form when the close is well below the open and volume is high. Narrow candlesticks form when volume is relatively low.

<figure><img src="/files/N7IT2lU9lJmrJh8F4xlH" alt="Chart displaying wide and narrow hollow and filled CandleVolume charts from StockCharts.com"><figcaption><p>CandleVolume chart shows wide and narrow hollow and filled candlesticks.</p></figcaption></figure>

You can also colorize candlesticks and volume bars to identify up and down periods. The chart below shows a colorized version of the chart of the same stock over the same period as the above chart.&#x20;

<figure><img src="/files/n5f4xCezSJ0fDskQhMgS" alt="Chart showing a colorized version of a CandleVolume chart from StockCharts.com"><figcaption><p>Colorized version of CandleVolume chart.</p></figcaption></figure>

In the Chart Attributes section below the chart, you can check the **Color Prices** and **Color Volume** box to colorize. A hollow candlestick still means the close was above the open, and a filled candlestick means the close was below the open. The red candlestick means the close was below the prior close, while a black candlestick means the close was above the prior close. The same applies to the red and green volume bars.

When calculating CandleVolume charts, note that volume is normalized to show it as a percentage of the look-back period. For a four-month daily chart, each day's volume would be divided by total volume for the look-back period (four months). As such, the width of each box represents the percentage of total volume for the look-back period. Big-volume days occupy more space on the x-axis (horizontal) than low-volume days.&#x20;

The date axis is usually not uniform on CandleVolume charts with varying widths. Some weeks will extend longer because of wide candlesticks, while others will be shorter because of narrow candlesticks.&#x20;

The chart below shows Pfizer (PFE) with normal candlesticks and a normal x-axis.&#x20;

<figure><img src="/files/4oZSMg43IqhBhLzce761" alt="Chart displaying CandleVolume with normal candlesticks and normal x-axis"><figcaption><p>CandleVolume chart with normal candlesticks and normal x-axis.</p></figcaption></figure>

In the next chart (see below), the CandleVolume changes the x-axis because volume was much higher in June than in prior months.

<figure><img src="/files/5u9MO9IAOvG7VZ8EEyqd" alt="Example of a CandleVolume chart with different candlestick widths resulting in changes in the x-axis from StockCharts.com"><figcaption><p>CandleVolume chart with different candlestick width resulting in changes in the x-axis.</p></figcaption></figure>

## Candlestick Reversal <a href="#candlestick_reversals" id="candlestick_reversals"></a>

CandleVolume charts can be used to validate candlestick reversal patterns. A candlestick reversal pattern on high volume carries more weight than one on low volume.&#x20;

The first chart below shows Transocean (RIG) forming a wide hammer in mid-April. The second chart shows RIG forming a wide bearish engulfing in mid-May. The third chart shows price action after these patterns.

<figure><img src="/files/0JzVmDI4kCnquAXktmfr" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/pWrLYriQDlmWe0VjX4l1" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/EDHyLxGsCznn0JG69Rra" alt=""><figcaption></figcaption></figure>

## Breakout Validation <a href="#breakout_validation" id="breakout_validation"></a>

Volume is important in chart analysis, especially in validating support and resistance breaks. Volume is fuel—an upside breakout on high volume is more bullish than a breakout on low volume.&#x20;

An upside breakout on high volume shows strong demand that is less likely to fade away. The chart below shows Google (GOOG) with a CandleVolume chart ending on April 19. Notice how the stock broke above resistance with a wide hollow candlestick. This shows high volume (strong demand) on the breakout. The second chart shows what happened next. Not all setups pay off quite this well, but CandleVolume can help separate the pretenders from the contenders.

<figure><img src="/files/51FGm10Rbrgrj2dXkqZR" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/3qS8QAmVGwwYUlfzOENN" alt=""><figcaption></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

CandleVolume charts put price action and volume together for easy visual analysis. Because these candlesticks share the same features as normal candlesticks, chartists can use them to validate candlestick patterns. CandleVolume charts can also be used to affirm a support test or validate a resistance level. A bounce off support with a wide candlestick is stronger than a bounce with a narrow candlestick. The same is true for a decline from resistance. Basically, almost anything done on normal candlestick charts can be applied to CandleVolume charts. [**Click here**](https://stockcharts.com/h-sc/ui?s=SPY\&p=D\&yr=0\&mn=4\&dy=0\&id=p12849814557\&a=307087146) for a live CandleVolume chart.

***

## CandleVolume and SharpCharts <a href="#candlevolume_and_sharpcharts" id="candlevolume_and_sharpcharts"></a>

In SharpCharts you can find CandleVolume under **Chart Type** in the **Attributes** area of the Chart Settings. There is also a volume setting in the Attributes area. You can choose to have volume off, separate, or as an overlay. Volume can also be skipped (off) because it's reflected on the CandleVolume chart.&#x20;

The example below shows the checkbox for selecting **Color Volume**, which you can use to display the up and down days of volume bars in different colors. You can choose your colors for both price bars and volume using **Up Color** and **Down Color**, or choose Auto to use the default colors.

<figure><img src="/files/TBdhSwOBpvgI4JshTCkT" alt="SharpCharts settings for CandleVolume charts in StockCharts.com"><figcaption><p>SharpCharts settings for CandleVolume charts.</p></figcaption></figure>

<figure><img src="/files/s2wcKgYSiE1QiytWw5PA" alt=""><figcaption></figcaption></figure>

## Further Study <a href="#further_study" id="further_study"></a>

| <p><a href="https://a.co/d/es5dtV2"><strong>Candlestick Charting Explained</strong></a><br>Gregory Morris</p> | <p><a href="https://a.co/d/2RmNjj1"><strong>Japanese Candlestick Charting Techniques</strong></a><br>Steve Nison</p> |
| ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| ![](/files/s2a0rFv8cM71busdrS9N)                                                                              | ![](/files/bzsLTkl3r9JRNL4AOR0U)                                                                                     |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/candlevolume.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
