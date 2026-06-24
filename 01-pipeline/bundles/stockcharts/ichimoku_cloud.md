> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/ichimoku-cloud.md).

# Ichimoku Cloud

## What Is an Ichimoku Cloud? <a href="#what_is_an_ichimoku_cloud" id="what_is_an_ichimoku_cloud"></a>

The Ichimoku Cloud, also known as Ichimoku Kinko Hyo, is a multi-functional tool that provides various insights into market dynamics. It helps in identifying levels of support and resistance, figuring out the direction of the market trend, measuring momentum, and producing trading signals. Ichimoku Kinko Hyo translates into “one look equilibrium chart.” With one look, chartists can identify the trend and look for potential signals.&#x20;

[Click here for a live version of this chart.](https://stockcharts.com/sc3/ui/?s=VZ\&p=D\&b=5\&g=0\&id=p95956825276\&a=956702515)

<figure><img src="/files/rT77ipgQHQlgs7S7o28a" alt=""><figcaption></figcaption></figure>

The indicator was developed by journalist Goichi Hosoda and published in his 1969 book. Even though the Ichimoku Cloud may seem complicated when viewed on the price chart, it's a rather straightforward indicator; the concepts are easy to understand and the signals are well-defined.

***

## Ichimoku Cloud Calculation <a href="#how_do_you_calculate_an_ichimoku_cloud" id="how_do_you_calculate_an_ichimoku_cloud"></a>

### Calculating the Plots

Four of the five plots within the Ichimoku Cloud are based on the average of the high and low over a given period of time. For example, the first plot is simply an average of the 9-day high and 9-day low. Before computers were widely available, it would have been easier to calculate this high-low average rather than a 9-day moving average. The Ichimoku Cloud consists of five plots.

#### Conversion Line

{% code overflow="wrap" %}

```
Tenkan-sen (Conversion Line): (9-period high + 9-period low)/2))
```

{% endcode %}

The default setting for the Conversion Line is 9 periods and can be adjusted. On a daily chart, this line is the midpoint of the 9-day high-low range, which is almost 2 weeks.

#### Base Line

{% code overflow="wrap" %}

```
Kijun-sen (Base Line): (26-period high + 26-period low)/2))
```

{% endcode %}

The default setting for the Base Line is 26 periods and can be adjusted. On a daily chart, this line is the midpoint of the 26-day high-low range, which is almost one month.

#### Leading Span A

{% code overflow="wrap" %}

```
Senkou Span A (Leading Span A): (Conversion Line + Base Line)/2))
```

{% endcode %}

This is the midpoint between the Conversion Line and the Base Line. The Leading Span A forms one of the two cloud boundaries. It is referred to as "Leading" because it is plotted 26 periods into the future and forms the faster cloud boundary.

#### Leading Span B

{% code overflow="wrap" %}

```
Senkou Span B (Leading Span B): (52-period high + 52-period low)/2))
```

{% endcode %}

On the daily chart, this line is the midpoint of the 52-day high-low range, which is a little less than three months. The default setting for this line is 52 periods, but can be adjusted. This value is plotted 26 periods in the future and forms the slower cloud boundary.

#### Lagging Span

```
Chikou Span (Lagging Span): Close plotted 26 days in the past
```

The Lagging Span line is just the close plotted 26 days in the past. The default setting is 26 periods, but can be adjusted.

{% hint style="info" %}
**Note:** This tutorial will use the English names when discussing the various plots.
{% endhint %}

### Forming the Cloud

As mentioned above, the "clouds" on the chart are formed when the faster Leading Span A plot crosses the slower Leading Span B. The area between the two lines is color-coded. If the faster Leading Span A line is on top, that is bullish and the area between the two lines is shaded in green. If the slower Leading Span B is on top, that is bearish and the area between the two lines is shaded in red.

***

## Interpreting Ichimoku Clouds <a href="#how_do_you_interpret_ichimoku_clouds" id="how_do_you_interpret_ichimoku_clouds"></a>

The five plots in an Ichimoku Cloud overlay can be used very much like moving averages. Chartists can look at the relationship between price and each of the plots, as well as the relationship between various plots, to determine the trend and to spot trading signals.

The chart below shows the Dow Industrials with the Ichimoku Cloud plots. The Conversion Line (blue) is the fastest and most sensitive line. Notice that it follows price action the closest. The Base Line (red) trails the faster Conversion Line, but follows price action pretty well. The relationship between the Conversion Line and Base Line is similar to the relationship between a 9-day moving average and 26-day moving average. The 9-day is faster and more closely follows the price plot. The 26-day is slower and lags behind the 9-day. Incidentally, notice that 9 and 26 are the same periods used to calculate the MACD.

<figure><img src="/files/E44HkyUPoONWYJ4plkd5" alt=""><figcaption><p>Comparing Ichimoku Cloud plots</p></figcaption></figure>

The Leading Span A line shows the midpoint between the 9-period and 26-period lines, while The cloud (Kumo) is the most prominent feature of the Ichimoku Cloud plots and is often used to identify the overall trend. The Leading Span A (green) and Leading Span B (red) form the cloud. The Leading Span A is the average of the Conversion Line and the Base Line. Because the Conversion Line and Base Line are calculated with 9 and 26 periods, respectively, the green cloud boundary moves faster than the red cloud boundary, the average of the 52-day high and the 52-day low. It's the same principle with moving averages. Shorter moving averages are more sensitive and faster than longer moving averages.

### Identifying Trends <a href="#how_can_ichimoku_clouds_help_you_identify_trends" id="how_can_ichimoku_clouds_help_you_identify_trends"></a>

There are two ways to identify the overall trend using the cloud, by comparing the relationship of price to the cloud, and by comparing the relationship of the two lines that form the cloud.&#x20;

First, the trend is up when prices are above the cloud, down when prices are below the cloud, and flat when prices are in the cloud. This is a very straightforward signal to spot on a chart.

Second, the uptrend is strengthened when the Leading Span A (green cloud line) rises above the Leading Span B (red cloud line). This situation produces a ***green cloud***. Conversely, a downtrend is reinforced when the Leading Span A (green cloud line) falls below the Leading Span B (red cloud line). This situation produces a ***red cloud***. Because the cloud is shifted forward 26 days, it also provides a glimpse of future support or resistance.

Chart 2 shows IBM with a focus on the uptrend and the cloud. First, notice that IBM was in an uptrend from June to January as it traded above the cloud. Second, notice how the cloud offered support in July, early October, and early November. Third, notice how the cloud provides a glimpse of future resistance. **Remember, the entire cloud is shifted forward 26 days.** This means it is plotted 26 days ahead of the last price point to indicate future support or resistance.

<figure><img src="/files/3TDKNHfwR733CuqIDGOp" alt=""><figcaption><p>Ichimoku Cloud in an Uptrend</p></figcaption></figure>

Chart 3 shows Boeing (BA) focusing on the downtrend and the cloud. The trend changed when Boeing broke below cloud support in June. The cloud changed from green to red when the Leading Span A (green) moved below the Leading Span B (red) in July. The cloud break represented the first trend change signal, while the color change represented the second trend change signal. Notice how the cloud then acted as resistance in August and January.

<figure><img src="/files/gMk0DfbMb4qOVWW5Ik55" alt=""><figcaption><p>Ichimoku Cloud in a Downtrend</p></figcaption></figure>

### Finding Trading Signals <a href="#how_can_ichimoku_clouds_help_you_identify_trading_signals" id="how_can_ichimoku_clouds_help_you_identify_trading_signals"></a>

The previous section showed some longer-term trend signals that can be gleaned from an Ichimoku Cloud chart. Whether the price is above, below, or in the cloud, and whether the cloud is green or red, can help chartists determine the current trend. But the Ichimoku Cloud overlay can also give shorter-term trading signals.

Price, the Conversion Line, and the Base Line are used to identify faster and more frequent signals. It is important to remember that bullish signals are reinforced when prices are above the cloud, and the cloud is green. Bearish signals are reinforced when prices are below the cloud, and the cloud is red. In other words, bullish signals are preferred when the bigger trend is up (prices above green cloud), while bearish signals are preferred when the bigger trend is down (prices are below red cloud). This is the essence of trading in the direction of the bigger trend. Signals counter to the existing trend are deemed weaker, such as short-term bullish signals within a long-term downtrend or short-term bearish signals within a long-term uptrend.

#### **Conversion-Base Line Crossovers**

During an uptrend, a bullish signal is triggered when the Conversion Line crosses above the Base Line. Similarly, the Conversion Line crossing below the Base Line during a downtrend is a bearish signal.

Chart 4 shows Kimberly Clark (KMB) producing two bullish signals within an uptrend. First, the trend was up because the stock was trading above the cloud and the cloud was green. The Conversion Line dipped below the Base Line for a few days in late June to enable the setup. A bullish crossover signal was triggered when the Conversion Line moved back above the Base Line in July. The second signal occurred as the stock moved towards cloud support. The Conversion Line moved below the Base Line in September to enable the setup. Another bullish crossover signal was triggered when the Conversion Line moved back above the Base Line in October. Sometimes it is hard to determine exact Conversion Line and Base Line levels on the price chart. For reference, these numbers are displayed in the upper left-hand corner of each Sharpchart. As of the January 8 close, the Conversion Line was 62.62 (blue) and the Base Line was 63.71 (red).

<figure><img src="/files/fv6ZbDUcA0cQmZ0u7Vem" alt=""><figcaption><p>Conversion-Base Line Crossover Signal in an Uptrend</p></figcaption></figure>

Chart 5 shows AT\&T (T) producing a bearish signal within a downtrend. First, the trend was down as the stock was trading below the cloud and the cloud was red. After a sideways bounce in August, the Conversion Line moved above the Base Line to enable the setup. This did not last long as the Conversion Line moved back below the Base Line to trigger a bearish signal on September 15th.

<figure><img src="/files/2L3r6eXmytzbrlTfTAey" alt=""><figcaption><p>Conversion-Base Line Crossover Signal in a Downtrend</p></figcaption></figure>

#### **Price-Base Line Crossovers**

During an uptrend, a bullish signal is triggered when price crosses above the Base Line. Similarly, price crossing below the Base Line during a downtrend is a bearish signal.

Chart 6 shows Disney producing two bullish signals within an uptrend. With the stock trading above the green cloud, prices moved below the Base Line (red) to enable the setup. This move represented a short-term oversold situation within a bigger uptrend. The pullback ended when prices moved back above the Base Line to trigger the bullish signal.

<figure><img src="/files/cezUcqGgHKeSd6tE4IZF" alt=""><figcaption><p>Price-Base Line Crossover Signal in an Uptrend</p></figcaption></figure>

Chart 7 shows DR Horton (DHI) producing two bearish signals within a downtrend. With the stock trading below the red cloud, prices bounced above the Base Line (red) to enable the setup. This move created a short-term overbought situation within a bigger downtrend. The bounce ended when prices moved back below the Base Line to trigger the bearish signal.

<figure><img src="/files/2PkT5lKc1PGjCHT7VxIs" alt=""><figcaption><p>Price-Base Line Crossover Signal in a Downtrend</p></figcaption></figure>

#### Ichimoku Cloud Signal Summary <a href="#ichimoku_cloud_signal_summary" id="ichimoku_cloud_signal_summary"></a>

This article features four bullish and four bearish signals derived from the Ichimoku Cloud plots. The trend-following signals focus on the cloud, while the momentum signals focus on the Conversion and Base Lines. In general, movements above or below the cloud define the overall trend. Within that trend, the cloud changes color as the trend ebbs and flows. Once the trend is identified, the Conversion Line and Base Line act similar to MACD for signal generation. And finally, simple price movements above or below the Base Line can be used to generate signals.

**Bullish Signals:**

* Price moves above cloud (trend)
* Cloud turns from red to green (ebb-flow within trend)
* Price Moves above the Base Line (momentum)
* Conversion Line moves above Base Line (momentum)

**Bearish Signals:**

* Price moves below cloud (trend)
* Cloud turns from green to red (ebb-flow within trend)
* Price Moves below Base Line (momentum)
* Conversion Line moves below Base Line (momentum)

***

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

The Ichimoku Cloud is a comprehensive indicator designed to produce clear signals. Chartists can first determine the trend by using the cloud. Once the trend is established, appropriate signals can be determined using the price plot, Conversion Line, and Base Line. The classic signal is to look for the Conversion Line to cross the Base Line. While this signal can be effective, it can also be rare in a strong trend. More signals can be found by looking for price to cross the Base Line (or even the Conversion Line).

It is important to look for signals in the direction of the bigger trend. With the cloud offering support in an uptrend, traders should also be on alert for bullish signals when prices approach the cloud on a pullback or consolidation. Conversely, in a bigger downtrend, traders should be on alert for bearish signals when prices approach the cloud on an oversold bounce or consolidation.

The Ichimoku Cloud can also be used in conjunction with other indicators. Traders can identify the trend using the cloud and then use classic momentum oscillators to identify overbought or oversold conditions.

***

## Charting with Ichimoku Clouds <a href="#charting_with_ichimoku_clouds" id="charting_with_ichimoku_clouds"></a>

### Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Ichimoku Cloud indicator is available on SharpCharts by selecting it as an indicator in the “Overlay” drop-down box. Choose “Ichimoku Cloud” to display the cloud portion only, or choose “Ichimoku Cloud (Full)” to display the Conversion Line, Base Line, and Lagging Span Line along with the cloud.

Default settings are 9 for the Conversion Line, 26 for the Base Line and 52 for the Leading Span B. The Leading Span A is based on the Conversion Line and Base Line. The number for the Base Line (26) is also used to move the cloud forward (26 days). These numbers can be adjusted to suit individual trading and investing styles. Sometimes it is necessary to add extra bars to the chart when increasing the Base Line, which also increases the forward movement of the cloud.

[Click here for a live version of this chart.](hhttps://stockcharts.com/sc3/ui/?s=TGT\&id=p17629306858)

<figure><img src="/files/FQ42oskEBtQqzOlvZgyl" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/4Gcrr1Z9nLlqI9xWyJS4" alt=""><figcaption><p>SharpCharts settings for the Ichimoku Cloud overlay</p></figcaption></figure>

{% hint style="info" %}
**Learn More.** For more details on the parameters used to configure Ichimoku Cloud overlays, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#ichimoku_cloud) in the Support Center.
{% endhint %}

### Using with StockChartsACP <a href="#using_with_stockchartsacp" id="using_with_stockchartsacp"></a>

This overlay can be added from the Chart Settings panel for your StockChartsACP chart. The example below shows the Ichimoku Cloud (Full) overlay, which plots all parts of the overlay. Chartists can instead select the simpler Ichimoku Cloud overlay to plot only the clouds, and not the additional lines.

[Click here for a live version of this chart.](https://schrts.co/wApaQnjD)

<figure><img src="/files/dBnLpa1tEXZUx3MiUOMV" alt=""><figcaption></figcaption></figure>

By default, the overlay is calculated with a 9-period Conversion Line, 26-period Base Line, and a 52-period Leading Span B Line. These parameters can be adjusted to meet your technical analysis needs.

***

## Scanning for Ichimoku Clouds <a href="#scanning_for_ichimoku_clouds" id="scanning_for_ichimoku_clouds"></a>

StockCharts members can screen for stocks based on Ichimoku Cloud values. Below are some example scans that can be used for Ichimoku Cloud-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when a Ichimoku Cloud-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-al/al).

### Ichimoku Uptrend with Close above Base Line <a href="#ichimoku_uptrend_with_close_above_base_line" id="ichimoku_uptrend_with_close_above_base_line"></a>

This scan starts with a base of stocks that are averaging at least $10 in price and 100,000 daily volume over the last 60 days. Stocks are classified in an uptrend as long as Span A is above Span B and the Close is above Span B. A breakout within this uptrend occurs when price moves above the Base Line.

```
[type = stock] AND [country = US]
AND [Daily SMA(60,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 10]

AND [Daily Close > Daily Ichimoku Span B(9,26,52)]
AND [Daily Ichimoku Span A(9,26,52) > Daily Ichimoku Span B(9,26,52)]
AND [Daily Close x Daily Ichimoku Base Line(9,26,52)]
```

### Ichimoku Downtrend with Close below Base Line <a href="#ichimoku_downtrend_with_close_below_base_line" id="ichimoku_downtrend_with_close_below_base_line"></a>

This scan starts with a base of stocks that are averaging at least $10 in price and 100,000 daily volume over the last 60 days. Stocks are classified in a downtrend as long as Span A is below Span B and the Close is below Span A. A continuation of this downtrend could be starting when price crosses below the Base Line.

```
[type = stock] AND [country = US]
AND [Daily SMA(60,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 10]

AND [Daily Close < Daily Ichimoku Span A(9,26,52)]
AND [Daily Ichimoku Span A(9,26,52) < Daily Ichimoku Span B(9,26,52)]
AND [Daily Ichimoku Base Line(9,26,52) x Daily Close]
```

For more details on the syntax to use for Ichimoku Cloud scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#ichimoku_cloud) in the Support Center.

Check out our Support Center article on [Scanning Ichimoku Clouds](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scanning-case-studies/scanning-ichimoku-clouds) for general instructions.

***

## Additional Resources <a href="#additional_resources" id="additional_resources"></a>

### ChartSchool Articles <a href="#chartschool_articles" id="chartschool_articles"></a>

[**Ichimoku Cloud Trading Strategy**](/table-of-contents/trading-strategies-and-models/trading-strategies/ichimoku-cloud-trading-strategies.md) \
Learn how to use the Ichimoku Cloud indicator as a standalone trading system.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/ichimoku-cloud.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
