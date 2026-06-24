> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/connorsrsi.md).

# ConnorsRSI

## What Is the ConnorsRSI? <a href="#introduction" id="introduction"></a>

ConnorsRSI is a momentum oscillator developed by Larry Connors and the team at Connors Research. It's used to identify overbought/oversold conditions in shorter trading timeframes. The traditional 14-period RSI indicator developed by Welles Wilder reacts too slowly to be useful for short-term trading; Connors Research sought to improve on this indicator, making it more suitable for shorter timeframes.

They initially developed their RSI(2) strategy, which used a 2-period RSI and moved overbought/oversold levels out to 90 and 10, but this approach still resulted in more false signals than desired. The team's subsequent efforts resulted in developing a brand-new composite indicator.

ConnorsRSI combines the momentum measurement of RSI with components that measure the duration of the trend and the magnitude of the price change, to create a more reliable short-term RSI indicator.

<figure><img src="/files/Aln3bVC8VY5cRVRVwB6T" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Learn More.** [Traditional RSI Indicator](/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi.md) | [Connors' RSI(2) Trading Strategy](/table-of-contents/trading-strategies-and-models/trading-strategies/rsi-2.md)
{% endhint %}

## Calculating the ConnorsRSI <a href="#calculation" id="calculation"></a>

ConnorsRSI is calculated by taking the average of its three components.

```
ConnorsRSI(3,2,100) = (RSI(3) + RSI(Streak,2) + PercentRank(100)) / 3
```

## ConnorsRSI Components <a href="#connorsrsi_components" id="connorsrsi_components"></a>

The ConnorsRSI indicator is made up of three components:

### **Relative Strength Index**

The first component is a simple 3-period RSI of price. This component measures price momentum on a scale of 0-100.

### **Up/Down Streak Length**

The second component is a 2-period RSI of the up/down streak length. It measures the duration of the trend.

The up/down streak is essentially the number of days in a row that the security's closing price has been higher (up) or lower (down) than the previous day's close. If a stock closes above its previous close three days in a row, then the up/down streak is +3. If it has closed below its previous close for 2 days, then its streak is -2. If it does not change price between one period and the next, then the streak is reset to 0.

Applying the 2-period RSI to this streak value converts it to a bound oscillator where values must be in the range of 0-100.

### **Magnitude of Price Change**

The third component ranks the most recent period's price change against the price change of the other periods in the specified timeframe (100 periods by default).

Essentially you determine the percentage of previous price changes that are lower than the most recent one. For example, if you specify a 20-day timeframe, and 7 of those 20 price change values are lower than today's price change, then 7 / 20 = 0.35 = 35%.

Again, defining this as a percentage restricts the component to a scale of 0-100. If today's price change was large and positive, the value of this component will be closer to 100; large negative price changes will result in a value closer to 0.

## ConnorsRSI Calculation <a href="#connorsrsi_calculation" id="connorsrsi_calculation"></a>

Once the three components have been calculated; the three values are added together and divided by 3. The resulting ConnorsRSI value ranges between 0 and 100. Connors recommends parameters of 3, 2, and 100 for the three components, but these parameters can be adjusted to meet your trading needs.

## Interpreting the ConnorsRSI <a href="#interpretation" id="interpretation"></a>

The ConnorsRSI indicator is typically used to identify overbought and oversold conditions in shorter trading timeframes.

While the traditional RSI typically defines 70 and 30 as the overbought and oversold levels, ConnorsRSI is more volatile and faster-moving, and requires more extreme levels to be set. Connors recommends using 90 and 10 for overbought/oversold levels, but these can be adjusted to meet your analysis needs. For more volatile securities, some chartists even use 95 and 5.

As with other overbought/oversold indicators, a security dropping below the oversold threshold indicates a buying opportunity, and a security rising above the overbought threshold indicates a pullback may be in its future. Whenever a security reaches either extreme, it is a signal to look closely at technical conditions for that security, including trend, volume, and other indicators.

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

Traditional RSI reaches extreme overbought/oversold levels very frequently when looking at shorter-term timeframes. The incorporation of components that measure the duration of the trend and the magnitude of the price change, as well as setting the overbought/oversold levels further out, help make ConnorsRSI more suitable for shorter-term trades. Despite the increased volatility in short-term trading, ConnorsRSI typically generates fewer trading signals than traditional RSI for this timeframe. When ConnorsRSI reaches an extreme level, it is more likely to actually be overbought/oversold. However, as with any indicator, it may occasionally produce false signals. As with all indicators, traders should use ConnorsRSI in conjunction with other indicators and analysis techniques.

***

## Charting With the ConnorsRSI Indicator <a href="#charting_with_the_connorsrsi_indicator" id="charting_with_the_connorsrsi_indicator"></a>

The ConnorsRSI indicator can be charted on StockChartsACP after installing our free Advanced Indicator Pack. Please see our [StockChartsACP Plug-Ins article](https://help.stockcharts.com/charts-and-tools/stockchartsacp#stockchartsacp_plug-ins) in the Support Center for more information on installing this plug-in.

Once the plug-in is installed, the ConnorsRSI indicator can be added from the Chart Settings panel for your StockChartsACP chart. The indicator can be positioned above, below, or behind the security's price plot.

![](https://school.stockcharts.com/lib/exe/fetch.php?media=technical_indicators:connorsrsi:crsiinacp.png)

By default, the indicator uses a 3-period RSI of price, a 2-period RSI of the up/down streak, and a 100-period timeframe for ranking the price change, but these parameters can be adjusted to meet your technical analysis needs.

## Scanning for ConnorsRSI <a href="#scanning_for_connorsrsi" id="scanning_for_connorsrsi"></a>

StockCharts members can screen for stocks based on ConnorsRSI values. Below are some example scans that can be used for ConnorsRSI-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://help.stockcharts.com/scanning-and-alerts/technical-scans/advanced-scan-workbench).

Members can also set up alerts to notify them when a ConnorsRSI-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://help.stockcharts.com/scanning-and-alerts/technical-alerts/technical-alert-workbench).

### ConnorsRSI Oversold in Uptrend <a href="#connorsrsi_oversold_in_uptrend" id="connorsrsi_oversold_in_uptrend"></a>

This scan reveals stocks that are in an uptrend with oversold ConnorsRSI. First, stocks must be above their 200-day moving average to be in an overall uptrend. Second, ConnorsRSI must cross below 10 to become oversold.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 40000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Daily Close > Daily SMA(200,Daily Close)] 
AND [Daily ConnorsRSI(3,2,100) <= 10]
```

### ConnorsRSI Overbought in Downtrend <a href="#connorsrsi_overbought_in_downtrend" id="connorsrsi_overbought_in_downtrend"></a>

This scan reveals stocks that are in a downtrend with overbought ConnorsRSI turning down. First, stocks must be below their 200-day moving average to be in an overall downtrend. Second, ConnorsRSI must cross above 90 to become overbought.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 40000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Daily Close < Daily SMA(200,Daily Close)] 
AND [Daily ConnorsRSI(3,2,100) >= 90]
```

{% hint style="info" %}
For more details on the syntax to use for ConnorsRSI scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#connorsrsi) in the Support Center.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/connorsrsi.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
