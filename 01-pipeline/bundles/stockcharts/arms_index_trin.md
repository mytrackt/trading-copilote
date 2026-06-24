> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/market-indicators/arms-index-trin.md).

# Arms Index (TRIN)

## What Is the Arms Index (TRIN)? <a href="#what_is_the_arms_index_trin" id="what_is_the_arms_index_trin"></a>

The Arms Index, also known as the TRIN or Short-Term TRading INdex, is a breadth indicator developed by Richard W. Arms in 1967. The index is calculated by dividing the Advance-Decline Ratio by the Advance-Decline Volume Ratio. Typically, these breadth statistics are derived from NYSE or Nasdaq data, but the Arms Index can be calculated using breadth statistics from other indices such as the S\&P 500 or Nasdaq 100. Because it acts as an oscillator, the indicator is often used to identify short-term overbought and oversold situations. A moving average can also be applied to smooth the data series. The terms Arms Index and TRIN are used interchangeably in this article.

## How Do You Calculate the TRIN? <a href="#how_do_you_calculate_the_trin" id="how_do_you_calculate_the_trin"></a>

{% code overflow="wrap" %}

```
(advances / declines) / (advancing volume / declining volume)
```

{% endcode %}

* Advances: number of stocks in the index that closed up on the day
* Declines: number of stocks in the index that closed down on the day
* Advancing Volume: total volume of advancing stocks
* Declining Volume: total volume of declining stocks

<figure><img src="/files/i5tgAgicp9dzPsaS75Te" alt=""><figcaption></figcaption></figure>

## How Do You Interpret the TRIN? <a href="#how_do_you_interpret_the_trin" id="how_do_you_interpret_the_trin"></a>

As a ratio of two indicators, the Arms Index reflects the relationship between the AD Ratio and the AD Volume Ratio. The TRIN is below one when the AD Volume Ratio is greater than the AD Ratio and above one when the AD Volume Ratio is less than the AD Ratio. Low readings (below one) show relative strength in the AD Volume Ratio. High readings (above one) show relative weakness in the AD Volume Ratio.

In general, strong market advances are accompanied by relatively low TRIN readings because up-volume overwhelms down-volume to produce a relatively high AD Volume Ratio. Because of this, the TRIN appears to move “inverse” to the market. A strong up day in the market usually pushes the Arms Index lower, while a strong down day often pushes the Arms Index higher.

[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?s=%24TRIN\&p=D\&yr=0\&mn=6\&dy=0\&id=p99175247298\&a=198185641)

<figure><img src="/files/TR16o3Ds4jzdLKHmGbG5" alt=""><figcaption></figcaption></figure>

As you can see in the calculation above and the corresponding chart below, the AD Volume Ratio surged to 7.17 as up-volume far exceeded down-volume. This produced a TRIN value well below one (0.42). Similarly, relatively high TRIN readings usually accompany strong declines because down-volume swamps up-volume. In the example above, the AD Volume Ratio plunged to 0.05 as down-volume crushed up-volume. This produced a TRIN value well above one (3.00). Extreme readings in the AD Volume Ratio usually produce extreme TRIN readings.

## Chart Scaling <a href="#chart_scaling" id="chart_scaling"></a>

The Arms Index can be displayed with a [semi-log scale](/table-of-contents/glossary/glossary-s.md#semi-logarithmic_percentage_scaling) or an arithmetic scale. Log scaling shows an equal distance for an equal percentage of movements. Arithmetic scaling shows an equal distance for each unit on the scale. On a log scale, a move from 0.50 to one (+100%) will be the same distance as a move from one to two (+100%). This is reflected in the dotted blue lines on the chart below. On an arithmetic scale, a move from 0.50 to 1 (+0.50) will be half the size of a move from one to two (+1).

[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?s=%24TRIN\&p=D\&yr=0\&mn=6\&dy=0\&id=p71043540510\&a=198758182)

<figure><img src="/files/5THnlVgO1G6c0yk2TEZ1" alt=""><figcaption></figcaption></figure>

The log scale evens out the fluctuations of the Arms Index. Notice how spikes above two on the arithmetic scale look out of proportion relative to the overall fluctuations. The data itself is not different. It's presented differently. There is no right or wrong answer when it comes to scaling. It depends on your preferences.

## Overbought/Oversold <a href="#overbought_oversold" id="overbought_oversold"></a>

Overbought and oversold levels for the Arms Index depend on the historical range and the smoothing (if any). An unmodified Arms Index will be more volatile and require a larger range to identify [overbought/oversold](/table-of-contents/glossary/glossary-o.md#overbought) conditions.&#x20;

The chart below shows daily closing values for the NYSE Short-Term Trading Arms Index ($TRIN) with a log scale. Surges above three are deemed oversold, and dips below 0.50 are deemed overbought. The NY Composite is in a larger uptrend because it is above its rising 100-day moving average. As such, oversold levels are preferred to generate bullish signals toward the bigger uptrend. The green dotted lines show oversold levels in early September, early October, early November, and early December, which amount to effectively one per month.

[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?s=%24TRIN\&p=D\&st=2009-08-01\&en=2009-12-31\&id=p05466335211\&a=442655879)

<figure><img src="/files/8ZAEvQ153i5jJfVuKmyR" alt=""><figcaption></figcaption></figure>

The next chart shows the Nasdaq Short-Term Trading Arms Index ($TRINQ) as a 10-day simple moving average (SMA). This moving average smoothes the data series, and a smaller range is needed to generate overbought/oversold signals. Notice that the range is narrower, with oversold above 1.20 and overbought below 0.80. With the Nasdaq above its rising 100-day moving average, oversold signals are preferred to trade in line with the bigger trend. There were oversold readings in June, August, September, and October.

<figure><img src="/files/EjVo7lM1Pg2eALRAdvdL" alt=""><figcaption></figcaption></figure>

[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?s=%24TRINQ\&p=D\&st=2009-08-01\&en=2009-12-31\&id=p17004935024\&a=206222025)

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

The Arms Index is a volatile breadth indicator that can generate overbought and oversold signals. Even though it generates plenty of signals, it is preferable to trade in the direction of the underlying trend. Short-term traders can use the unmodified Arms Index to generate short-term signals or apply a 10-day SMA to generate more medium-term signals. The Arms Index is just one indicator; chartists should employ other aspects of technical analysis to confirm or refute signals generated.

## Charting the Arms Index on SharpCharts <a href="#sharpcharts" id="sharpcharts"></a>

StockCharts.com users can plot the Arms Index for the NYSE ($TRIN) and Nasdaq ($TRINQ). If you prefer a log scale, as in the example below, you should start with the Arms Index as the main symbol. This places the indicator in the main charting window, and you can check the “log scale” option below the chart. To show the indicator as a moving average, select “invisible” as the chart type and then add a moving average as an overlay.

<figure><img src="/files/PSYOPQ5B1laQZdyFom6u" alt=""><figcaption></figcaption></figure>

You can also add horizontal lines as individual overlays to differentiate with colors and line styles to define overbought and oversold levels. You could add multiple horizontal lines by entering comma-separated values in the parameters box (0.80,1,1.20). You can plot the underlying index by selecting “price” in the indicator drop-down menu and entering the desired index symbol. [Click here](https://stockcharts.com/h-sc/ui?s=%24TRINQ\&p=D\&yr=0\&mn=6\&dy=0\&id=p17004935024\&a=206222025) for a live chart with the Arms Index.

<figure><img src="/files/CnBOzCnuLuufheeVjzr1" alt=""><figcaption></figcaption></figure>

## FAQs TRIN <a href="#trin_faqs" id="trin_faqs"></a>

<details>

<summary>What is the Arms Index (TRIN)?</summary>

The Arms Index, also known as TRIN or Short-Term TRading INdex, is a breadth indicator developed by Richard W. Arms in 1967, designed to identify short-term overbought and oversold situations in the market.

</details>

<details>

<summary>What do advances and declines represent?</summary>

Advances refer to the number of stocks in the index that closed up on the day, while declines denote the number of stocks that closed down on the day.

</details>

<details>

<summary>Can the Arms Index be applied to various stock indices?</summary>

Yes. While typically based on NYSE or Nasdaq data, the Arms Index can be calculated using breadth statistics from other indices such as the S\&P 500 or Nasdaq 100.

</details>

<details>

<summary>What does it mean when the TRIN is above or below one?</summary>

A TRIN below one indicates relative strength in the AD Volume Ratio, while a TRIN above one shows relative weakness in the AD Volume Ratio. Low readings suggest strong market advances and high readings suggest strong declines.

</details>

<details>

<summary>What are the overbought and oversold levels for the Arms Index?</summary>

Levels can vary depending on historical range and smoothing. An unmodified Arms Index may consider surges above three as oversold and dips below 0.5 as overbought. However, with modifications, these ranges might change.

</details>

<details>

<summary>How frequently does the Arms Index produce signals?</summary>

While the Arms Index can generate numerous signals, it's crucial to trade in the direction of the underlying trend. An unmodified Arms Index provides short-term signals, but applying a 10-day SMA can produce more medium-term signals.

</details>

<details>

<summary>Should traders rely solely on the Arms Index for making trading decisions?</summary>

The Arms Index is a useful indicator, but chartists should use other aspects of technical analysis to confirm or refute signals generated by the Arms Index for a more comprehensive analysis.

</details>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/market-indicators/arms-index-trin.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
