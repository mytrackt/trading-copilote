> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/renko-charts.md).

# Renko Charts

## What Are Renko Charts? <a href="#introduction" id="introduction"></a>

Renko charts originated in Japan. The charts ignore time and focus solely on price changes that meet a minimum requirement. In this regard, these charts are similar to [Point & Figure charts](/table-of-contents/chart-analysis/point-and-figure-charts.md). Instead of X-and O-Columns, Renko charts use price “bricks,” representing a fixed price move. These bricks are sometimes called “blocks” or “boxes.” They move up or down in 45-degree lines with one brick per vertical column. Bricks for upward price movements are hollow, while bricks for falling price movements are filled with a solid color (typically black).

## Construction and Characteristics of Renko Charts <a href="#construction_and_characteristics" id="construction_and_characteristics"></a>

Renko charts are based on bricks with fixed values that filter out smaller price movements. A regular bar, line, or candlestick chart has a uniform date axis with equally spaced days, weeks, and months. This is because there is one data point per day or week. Renko charts ignore the time aspect and only focus on price changes.&#x20;

If the brick value is set at 10 points, a move of 10 points or more is required to draw another brick. Price movements less than 10 points would be ignored, and the Renko chart would remain unchanged.

For example, if you're using the S\&P 500 10-point Renko chart and the S\&P 500 advanced nine points (1840 to 1849), you wouldn't see a new Renko brick drawn on the chart. If the S\&P 500 advanced to 1850 the next day, a new Renko brick would be drawn because the entire move was at least 10 points. This brick would extend from 1840 to 1850 and be hollow or white in this example. Alternatively, if the S\&P 500 declined from 1840 to 1830, a new Renko brick would be drawn, and it would be solid or black.

The two charts below cover a six-month timeframe. The Renko chart sports an irregular date axis. The price action is less choppy because the S\&P 500 Renko chart ignores price moves that are less than 10 points. It remains unchanged until there is a move of at least 10 points.

<figure><img src="/files/WihCEYRK1epcuYnOAogX" alt=""><figcaption><p>Traditional bar chart with a uniform data axis.</p></figcaption></figure>

<figure><img src="/files/TPLgftbMqFolKef0ljti" alt=""><figcaption><p>Renko chart for the same time frame as the bar chart but note the irregular date axis and less choppy price action.</p></figcaption></figure>

## Close Versus High-Low Range <a href="#close_versus_high-low_range" id="close_versus_high-low_range"></a>

Renko charts can be based on closing prices or the high-low range using the “field” setting in SharpCharts. Closing price means there is one data point per period and less volatility. The high-low range puts two data points into play and increases the fluctuations, which results in added bricks.&#x20;

The examples below show Renko charts for the S\&P 500; the box size is 10 points for both. The first chart is based on closing prices, and the second is based on the high-low range. Notice that the Renko chart based on the high-low range fluctuates more than the close-only Renko chart.

<figure><img src="/files/xtYqHXrRoz9woVSTBi17" alt="Renko chart from StockCharts.com based on closing prices."><figcaption><p>Renko chart based on closing prices.</p></figcaption></figure>

<figure><img src="/files/31mzp150lihuXyCUvw6R" alt="Renko charts from StockCharts.com based on the high-low range."><figcaption><p>Renko chart based on the high-low range.</p></figcaption></figure>

## Fixed Value versus ATR <a href="#fixed_value_versus_atr" id="fixed_value_versus_atr"></a>

Chartists can use the “box” settings to set brick size as a specific value or as the [Average True Range](/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-atr.md) (ATR). A specific point value means brick size will remain constant even as new data is incorporated into the chart. In other words, new price data is added every trading day, and the brick size will remain constant. The two charts above have a fixed value, and each brick represents ten points.

In contrast to fixed price bricks, using ATR values results in fluctuating brick sizes. The default ATR is based on 14 periods, and the ATR fluctuates over time. The brick size is based on the ATR value when the chart is created. Should the ATR value change the next day, the new ATR value will be used to set the brick size. Also note that ATR values are based on standard charts, such as close-only, bar, and candlestick. These charts have one data point per period and a uniform x-axis (date axis). The ATR value shown on these charts can differ from the ATR brick value on a Renko chart due to rounding issues.

<figure><img src="/files/DD5LtWhkoJNtYPIo5yAC" alt=""><figcaption></figcaption></figure>

The next two examples show how the ATR value changes when the ending chart date changes. The first chart ends on June 10, and the ATR value is 12.05, which is the value for each Renko brick. The second chart ends on April 15, and the ATR value is 20.55, which is the value for each Renko brick. Notice how the brick value changed as the ATR value changed. The bricks on April 15 have a much higher value than those on June 10.

<figure><img src="/files/wsLGnRB7VeOIH7KuTNlM" alt=""><figcaption><p>Renko chart when the ending ATR value is low.</p></figcaption></figure>

<figure><img src="/files/qTZwdmw6rSTF5lv3OAwB" alt=""><figcaption><p>Renko chart when the ending ATR value is high.</p></figcaption></figure>

## Trends, Support, and Resistance <a href="#trends_support_and_resistance" id="trends_support_and_resistance"></a>

White bricks form when prices rise a certain amount, and black bricks form when prices decline a certain amount.&#x20;

The image below shows a daily S\&P 500 chart with 10-point bricks and a 10-period [simple moving average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md). Note that a 10-period moving average calculation is based on the last 10 Renko values, not the last 10 trading days. An indicator on a Renko chart is based on Renko values and will differ from that on a bar chart. Chartists can typically use shorter moving averages on Renko charts because smaller price movements have been filtered out.

<figure><img src="/files/PIwYRqlvSm6unrPfQTcZ" alt=""><figcaption></figcaption></figure>

Troughs can mark support levels, and peaks can mark resistance levels. You can also look for a two-brick reversal to signal a trend change. Notice how the index fell with five black bricks in August and again in September-October. These declines looked like falling flags. A reversal occurred when two white bricks formed and broke above the short-term resistance level. Chartists can also apply the Fibonacci Retracements Tool to Renko charts.

## The Takeaway <a href="#conclusions" id="conclusions"></a>

Like their Japanese cousins (Kagi and Three Line Break), Renko charts filter the noise by focusing exclusively on minimum price changes. Renko bricks are not added unless price changes by a specific amount. As with Point & Figure charts, it is easy to spot important highs and lows, and identify key support and resistance levels.&#x20;

With this information, chartists can identify uptrends with higher highs and higher lows or downtrends with lower lows and lower highs. As with all charting techniques, chartists should employ other technical analysis tools to confirm or refute their findings on Renko charts.

***

## Renko Charts In SharpCharts <a href="#sharpcharts" id="sharpcharts"></a>

Chartists can create Renko charts by going to the **Attributes** area of the Chart Settings and selecting Renko as the **Chart Type**. Users will then be able to choose between points or ATR, and then set the parameters for these two options in the next box.

The **ATR** setting uses the Average True Range indicator from the symbol's underlying bar chart to determine an “Automatic” value for the Renko chart's box size. Note: This ATR value might change as prices change which can cause the Renko chart to change significantly whenever it is updated.

The **Renko Price Field** can be set at close or high-low range. Chartists looking for more sensitivity can choose the high-low range. Chartists looking to focus on end-of-day price data can choose the close. The brick colors can also be changed using the **Up Color** and **Down Color** drop down menus in the Chart Settings area.

***

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line"> [**Click here**](https://stockcharts.com/sc3/ui/?s=QQQ\&p=D\&st=2013-10-14\&en=2014-06-10\&id=p06455616707\&a=354889631) for a live example.

***

<figure><img src="/files/nRVLVcxTdafIrNRRsJcT" alt=""><figcaption><p>Renko chart for QQQ</p></figcaption></figure>

<figure><img src="/files/UluMji4zusTcXzvRUxph" alt="SharpCharts settings for Renko charts using StockCharts.com"><figcaption><p>SharpChart settings for Renko charts.</p></figcaption></figure>

{% hint style="warning" %}
**Note:** If the phrase “AT LIMIT” appears at the top of a chart, it means that the box size specified would result in a chart that is too large for us to display. In that case, we increase the box size to the smallest size we can successfully display and add the “AT LIMIT” message to the top of the chart.
{% endhint %}

***

## Frequently Asked Questions <a href="#frequently_asked_questions" id="frequently_asked_questions"></a>

<details>

<summary>Why are the Renko bricks changing on my chart?</summary>

If you are using the ATR box size, the box size is computed automatically. However it may change during the day, so the chart may change along with it.

</details>

***

## Further Study <a href="#further_study" id="further_study"></a>

As the name implies, this book goes beyond candlesticks to show chartists other technical analysis techniques that originated in Japan. Nison devotes an entire chapter to Renko charts; additionally, he covers Three Line Break charts, Kagi charts and explains how Japanese traders use moving averages.

| <p><a href="https://a.co/d/4B1HdkV"><strong>Beyond Candlesticks</strong></a><br>Steve Nison</p> |
| ----------------------------------------------------------------------------------------------- |
| ![](/files/we1PnaOLag2ULhNx5MLq)                                                                |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/renko-charts.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
