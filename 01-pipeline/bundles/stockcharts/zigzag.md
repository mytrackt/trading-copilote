> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/zigzag.md).

# ZigZag

## What Is the ZigZag Overlay? <a href="#introduction" id="introduction"></a>

The ZigZag feature is not a technical indicator per se but rather a means to filter out smaller price movements. A ZigZag overlay set at 10 would ignore all price movements less than 10%; only price movements greater than 10% would be included on the ZigZag line. Filtering out smaller movements allows you to see the forest instead of just trees.&#x20;

<figure><img src="/files/lEhjrGhXifVipdim61BE" alt=""><figcaption><p>It's easy to see why this overlay is named ZigZag.</p></figcaption></figure>

It is important to remember that the ZigZag feature has no predictive power, because it draws lines based on hindsight. The predictive power comes from applications such as Elliott Wave, price pattern analysis, or indicators. You can also use the ZigZag (Retrace) feature to identify Fibonacci retracements and projections.

***

## ZigZag Calculation <a href="#calculation" id="calculation"></a>

The price data used for ZigZag is dependent on the chart “type.” Line and dot charts, based on the close, will plot the ZigZag based on closing prices. Charts with High-Low-Close bars (HLC), Open-High-Low-Close (OHLC) bars, or candlesticks, which show the period's high-low range, will plot the ZigZag based on this high-low range. A ZigZag based on the high-low range is more likely to change course than a ZigZag based on the close because the high-low range will be much larger and produce bigger swings.

The ZigZag line is overlaid on the price plot, connecting only data points where the price has increased or decreased by at least the specified percentage. Traditionally, a 5% change is used as the threshold, but this percentage can be changed based on your analysis needs.

{% hint style="success" %}
**Cool Tip:** ZigZag and ZigZag (Retrace) can also be plotted on indicator panels, to filter out noise on technical indicators like the RSI.
{% endhint %}

### Adjusting the Sensitivity of ZigZag

While 5% is the traditional percent change threshold for ZigZag, StockCharts' ZigZag features automatically choose a percentage that makes sense for that particular security.

<figure><img src="/files/fmhUVySWqEsXpSDoTwvk" alt=""><figcaption></figcaption></figure>

Some securities produce too few ZigZag lines at 5%, so the default is set lower (e.g., 3.75% for DIS in the chart above). Some securities produce too many ZigZag lines at 5%, so the default is set higher (e.g., 7.81% in the STX chart below). The ZigZag parameter can be seen in the upper left corner of the chart.&#x20;

<figure><img src="/files/NAag5mo91YKvSeVVkHYf" alt=""><figcaption></figcaption></figure>

If you want to adjust the automatically chosen percentage, you can do this in the settings for the ZigZag overlay. A ZigZag with 5 in the parameter box will filter out all movements less than 5%. A ZigZag(10) will filter out movements less than 10%. So, if a stock traded from a reaction low of $100 to a high of $109, it would be a 9% move—there wouldn't be a line because the move was less than 10%. If the stock advanced from a low of $100 to a high of $110 (+10%), there would be a line from $100 to $110. If the stock continued to $112, this line would extend to $112 (100 to 112). The ZigZag would not reverse until the stock declined 10% or more from its high. From a high of $112, a stock would have to decline 11.2 points (or to a low of $100.8) to warrant another line.&#x20;

## Interpreting ZigZag

Chartists can use **ZigZag** to identify trends and help set Elliott Wave counts. **ZigZag (retrace)** can be used to identify Fibonacci retracements and projections.

### Identifying Trends

Since the ZigZag feature filters out small day-to-day price changes, focusing only on price moves that reach a certain threshold, it can be a valuable way to spot trends through the noise.&#x20;

The Citigroup (C) chart below shows a line chart with a 7% ZigZag. The early June bounce was ignored because it was less than 7%. The pullbacks in late June were similarly ignored, because they were much less than 7%.

<figure><img src="/files/j4jHE5jLKYo4a3BswS2a" alt="Chart from StockCharts.com showing a 7% ZigZag"><figcaption><p>Using a 7% ZigZag to filter out choppy price movements and spot trends. </p></figcaption></figure>

**CAUTION:** You may notice that the last ZigZag line is up even though the security advanced just 1.89% ($54.98 to $56.02). This is a temporary line. The security would have to move to $58.83 for a 7% gain to warrant a permanent ZigZag line. Should it fail to reach the 7% threshold on this bounce and decline to below $55, the temporary line would disappear, and the prior ZigZag line would continue from the late August high.

### Setting Elliott Wave Counts <a href="#elliott_wave_counts" id="elliott_wave_counts"></a>

The ZigZag feature can filter out small moves and simplify Elliott Wave counts. The chart below shows the S\&P 500 SPDR ETF (SPY) with a 6% ZigZag to filter moves less than 6%. After some trial and error, 6% was deemed the threshold of importance. An advance or decline greater than 6% was deemed significant enough to warrant a wave for an Elliott count. Keep in mind that this is just an example. The threshold and wave count are subjective and dependent on individual preferences. Based on the 6% ZigZag, a complete cycle was identified from March 2009 until July 2010. A complete cycle consists of eight waves, five up and three down.

<figure><img src="/files/ngEnvKBHFDV4ppL2uo7A" alt="Chart from StockCharts.com showing ZigZag with Elliott Waves"><figcaption><p>ZigZag with Elliott Waves.</p></figcaption></figure>

{% hint style="info" %}
**Learn More.** [Elliott Wave Theory](/table-of-contents/market-analysis/elliott-wave-analysis-articles/introduction-to-elliott-wave-theory.md)
{% endhint %}

### Identifying Retracements and Projections <a href="#retracements_and_projections" id="retracements_and_projections"></a>

SharpCharts users can choose between the normal **ZigZag** and **ZigZag (retrace)**. The normal ZigZag shows lines when prices move at least a specific percentage. The ZigZag (retrace) feature connects those reaction highs and lows with labels that measure the prior move. The numbers on the dotted lines reflect the difference between the current ZigZag line and the ZigZag line immediately before it.&#x20;

For example, the chart below shows Altera (ALTR) with the 10% ZigZag (retrace) feature. Three ZigZag lines are labeled (1, 2, and 3). The dotted line connecting the low of Line 1 with the low of Line 2 shows a box with 0.638. This means Line 2 is 0.638 (63.8%) of Line 1. A number below 1 means the line's price change is smaller than the prior line. The dotted line connecting the high of Line 2 with the high of Line 3 shows a box with 1.646. This means Line 3's price change is 1.646 (164.6%) of Line 2. A number above 1 means the line's price change is larger than the prior line.

<figure><img src="/files/chwNrwyTAqAvuA17Y1T0" alt=""><figcaption></figcaption></figure>

As you may have guessed, seeing these lines as a percentage of the prior lines makes it possible to assess Fibonacci projections. The August decline (Line 2) retraced around 61.8% of the June–July advance (Line 1). This is a classic Fibonacci retracement. The advance from early September to early November was 1.646 times the August decline. In this sense, the ZigZag (Retrace) can be used to project the length of an advance. Again, 1.646 is close to the Fibonacci 1.618, the Golden Ratio used in many projection estimates.

{% hint style="info" %}
**Learn More.** [Fibonacci Retracements](/table-of-contents/chart-analysis/chart-annotation-tools/fibonacci-retracements.md)
{% endhint %}

***

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The ZigZag and ZigZag (Retrace) overlays filter price action and do not have any predictive power. The ZigZag lines simply react when prices move a certain percentage. Chartists can apply an array of technical analysis tools to the ZigZag. Chartists can perform basic trend analysis by comparing reaction highs and lows. Chartists can also overlay the ZigZag feature to look for price patterns that might not be as visible on a normal bar or line chart. The ZigZag has a way of highlighting the important movements and ignoring the noise. When using the ZigZag feature, don't forget to measure the last line to determine if it is temporary or permanent. This line is temporary if the current price change is less than the ZigZag parameter but becomes permanent if the price change is greater than or equal to the ZigZag parameter.

***

## Charting with ZigZag and ZigZag (Retrace) <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

### Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

These overlays can be added to your SharpChart from the **Chart Settings** section of the SharpCharts Workbench. ZigZag and ZigZag (retrace) can be overlaid on the security's price plot or on an indicator panel.

[Click here for a live version of this ZigZag chart.](https://stockcharts.com/sc3/ui/?s=%24COMPQ\&a=2222531966\&p=D\&yr=0\&mn=8\&dy=0\&id=p94388714277)

<figure><img src="/files/OAk9XNbT61Ww1brZQcXv" alt=""><figcaption></figcaption></figure>

[Click here for a live version of this ZigZag (Retrace) chart.](https://stockcharts.com/sc3/ui/?s=%24COMPQ\&a=2222531755\&p=D\&yr=0\&mn=8\&dy=0\&id=p12440384804)

<figure><img src="/files/FLjMdcYWB7hoRRAreEv6" alt=""><figcaption></figcaption></figure>

The parameters window will appear empty after selecting the ZigZag or ZigZag (retrace) feature from the dropdown menu. Five (5%) is the default parameter, but this can change depending on a security's price characteristics. Once the ZigZag feature is applied, you can adjust the parameter to suit your charting needs (as shown in the example below, where ZigZag (Retrace) has been adjusted to use 6.5% as its threshold). A lower number will make the feature more sensitive, while a higher number will make it less sensitive.&#x20;

<figure><img src="/files/XKrJoTBl3VobyPXhgb1T" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Learn More.** For more details on the parameters used to configure ZigZag overlays, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#zigzag) in the Support Center.
{% endhint %}

### Using with StockChartsACP

These overlays can also be added from the Chart Settings panel for your StockChartsACP chart.  ZigZag and ZigZag (retrace) can be overlaid on the security's price plot or on an indicator panel.

[Click here for a live version of this ZigZag chart.](https://schrts.co/aDVHfnJs)

<figure><img src="/files/RTUhRm0s9W250ecC9TGx" alt=""><figcaption></figcaption></figure>

[Click here for a live version of this ZigZag (retrace) chart.](https://schrts.co/EcchpTVS)

<figure><img src="/files/umfTuC9Avlg6QJgt3v5H" alt=""><figcaption></figcaption></figure>

By default, both overlays automatically select an appropriate Percentage threshold for that particular security. To set your own custom Percentage, uncheck the "Auto Percentage" box and enter the desired threshold in the Percentage field.

## Additional Resources <a href="#additional_resources" id="additional_resources"></a>

### ChartSchool Articles <a href="#chartschool_articles" id="chartschool_articles"></a>

[**Swing Charting**](/table-of-contents/trading-strategies-and-models/trading-strategies/swing-charting.md)\
Learn how to use the ZigZag overlay when swing trading.

### Recommended Books <a href="#recommended_books" id="recommended_books"></a>

Robert Prechter's [*Elliott Wave Principle*](https://a.co/d/1cnd1eE) introduces the fundamental concepts and techniques of Elliott Wave Theory and serves as a comprehensive yet accessible handbook for traders interested in this market forecasting technique.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/zigzag.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
