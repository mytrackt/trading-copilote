> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-average-ribbon.md).

# Moving Average Ribbon

## What Is the Moving Average Ribbon? <a href="#what_is_the_moving_average_ribbon" id="what_is_the_moving_average_ribbon"></a>

A Moving Average Ribbon is a graphical representation of multiple moving averages with varying look-back periods plotted on the same chart. It appears like a ribbon moving across the chart, hence its name.

<figure><img src="/files/piuH732GylLEYkkyVUZ3" alt="Chart from StockChartsACP displaying moving average ribbon overlaid on a price chart"><figcaption><p>Example of Moving Average Ribbon overlaid on a price chart.</p></figcaption></figure>

***

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line">[Click here for a live version of this chart.](https://schrts.co/YZpRPttm)

***

These moving averages can be analyzed separately or as a group for trend identification and trend change signals.

{% hint style="info" %}
**Learn More.** [Moving Averages](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md)
{% endhint %}

***

## How Do You Calculate Moving Average Ribbons? <a href="#how_do_you_calculate_moving_average_ribbons" id="how_do_you_calculate_moving_average_ribbons"></a>

There are no special formulas here; the Moving Average Ribbon is a quick and easy method to add multiple moving averages to your chart.

Determine the number of moving averages (MAs) to add and the number of periods for each. In StockChartsACP, this is accomplished by specifying the number of periods in the shortest MA, the increment in periods between each MA, and the total number of MAs in the ribbon. You may also specify the type of moving average (simple or exponential). For example, you may want 8 EMAs on your daily chart in 10-period increments, with the shortest being a 10-day EMA and the longest being an 80-day EMA.

Each moving average in the ribbon is calculated using the standard SMA or EMA formulas. For more details on those calculations, please see our Moving Averages article in ChartSchool.

***

## How Do You Interpret Moving Average Ribbons? <a href="#how_do_you_interpret_moving_average_ribbons" id="how_do_you_interpret_moving_average_ribbons"></a>

Since the Moving Average Ribbon is just a collection of moving averages, the interpretation is similar to that used with one or two moving averages. With single moving averages, you can look at the direction of the moving average and whether it is above or below the price bars. With two moving averages, you can look for crossovers of the short-term MA over the long-term MA and vice versa. The ribbon allows you to look at these relationships for multiple moving averages at once:

* If all the averages move in the same direction, this indicates a strong trend. The longer- and shorter-term lines are all in agreement about the direction of the trend. If all the moving average lines in the ribbon move upward, prices increase in all timeframes, and the security is likely in an uptrend.
* If the shorter-term lines cross above the longer-term lines, this signals a new uptrend; a downtrend is indicated when shorter-term moving average lines cross below the longer-term ones. Chartists can also look for price bars to cross above or below the various moving average lines in the ribbon.

The ribbon's width—the distance between the moving average lines in the ribbon—can also provide information for traders:

* When all moving average lines are running in parallel (the lines are evenly spaced over time), this indicates a strong trend.
* If the ribbon is expanding (the moving average lines are getting farther apart over time), this could mark the end of the current trend.
* If the ribbon is contracting (the moving average lines are getting closer together or even crossing), this can indicate the start of a new trend.

The responsiveness of the ribbon can be adjusted by changing the type of moving average (EMAs respond more quickly than equivalent SMAs), and by changing the number of periods in the moving averages (MAs with fewer periods will react more quickly than those with more periods).

{% hint style="info" %}
**Learn More.** [Trade With Moving Average Ribbons](/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies/guppy-multiple-moving-average-an-ma-ribbon-designed-to-tip-the-markets-hand.md)
{% endhint %}

***

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

A moving average ribbon allows you to see at a glance what's happening in both the long- and short-term by looking for trends and crossovers across various look-back periods. In addition, ribbon width expansions and contractions can indicate trend strength and possible trend changes. As with all technical indicators, traders should use the Moving Average Ribbon overlay with other indicators and analysis techniques.

***

## Charting with Moving Average Ribbons <a href="#charting_with_moving_average_ribbons" id="charting_with_moving_average_ribbons"></a>

Moving Average Ribbons can be created on both SharpCharts and StockChartsACP charts.

### Using with StockChartsACP <a href="#using_with_stockchartsacp" id="using_with_stockchartsacp"></a>

Chartists can build their own ribbon by adding several moving averages to their chart one at a time, but there is a quicker way in StockChartsACP: the Moving Average Ribbon overlay.

This overlay can be added from the Chart Settings panel for your StockChartsACP chart. Moving Average Ribbons can be overlaid on the security's price plot or on an indicator panel.

<figure><img src="/files/x66J3jzclGojeNBjve0M" alt="Chart from StockChartsACP displaying the moving average ribbon overlaid on a price chart of SPY"><figcaption><p>The Moving Average Ribbon overlay applied to a chart using StockChartsACP.</p></figcaption></figure>

***

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line">[Click here for a live version of this chart.](https://schrts.co/ViAhWEzX)

***

By default, the overlay uses 10 SMAs, spaced 5 periods apart, ranging between 20 and 65 periods. The type of moving average (Simple or Exponential), the number of periods in the shortest moving average, the increment (Step) of periods between each line, and the number of moving averages can all be adjusted to meet your technical analysis needs.

The line colors default to rainbow order with the shortest moving average set to red, the second shortest set to orange, and so on, but these line colors can also be adjusted.

### Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

While the SharpCharts Workbench does not offer a built-in Moving Average Ribbon indicator, it is relatively easy to create your own ribbon on SharpCharts by adding multiple moving averages, each with a different number of periods and different color.

The example below shows the same ribbon as in the StockChartsACP example above. Click the link below the chart to see how this ribbon was configured in SharpCharts.

<figure><img src="/files/D6xdYoREH2woIx5DQgBh" alt="Chart from StockCharts.com displaying the moving average ribbon overlay"><figcaption><p>Example of the Moving Average Ribbon overlay applied to SharpCharts.</p></figcaption></figure>

***

[Click here for a live version of this chart.](https://stockcharts.com/sc3/ui/?s=SPY\&p=D\&yr=1\&mn=0\&dy=0\&id=p34602251938\&a=961500269)

***

{% hint style="info" %}
**Learn More.** For more details on the parameters used to configure moving average overlays, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#simple_moving_average_sma-1) in the Support Center.
{% endhint %}

***

## Moving Average Ribbon FAQs <a href="#moving_average_ribbon_faqs" id="moving_average_ribbon_faqs"></a>

<details>

<summary>What are the most common settings for a Moving Average Ribbon?</summary>

A common setting for a Moving Average Ribbon is to use 6 to 8 moving averages of different lengths, such as 10, 20, 30, 40, 50, and 60 periods. However, the best settings for a Moving Average Ribbon will vary depending on the market being analyzed and the trader's personal preferences.

</details>

<details>

<summary>What moving averages can I use in a Moving Average Ribbon?</summary>

You can use Simple Moving Averages (SMAs) or Exponential Moving Averages (EMAs) in a Moving Average Ribbon, depending on your preference and the specific analysis you are conducting.

</details>

<details>

<summary>How can the Moving Average Ribbon assist in signaling a new uptrend or downtrend?</summary>

A new uptrend is signaled when shorter-term moving average lines cross above the longer-term ones. On the contrary, a downtrend is indicated when shorter-term moving average lines cross below the longer-term ones.

</details>

<details>

<summary>How can I adjust the responsiveness of the Moving Average Ribbon?</summary>

The responsiveness of the Moving Average Ribbon can be adjusted by changing the type of moving average and the number of periods in the moving averages. Exponential Moving Averages (EMAs) respond more quickly than Simple Moving Averages (SMAs), and moving averages with fewer periods will react more quickly than those with more periods.

</details>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-average-ribbon.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
