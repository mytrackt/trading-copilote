> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/mass-index.md).

# Mass Index

## What Is the Mass Index? <a href="#introduction" id="introduction"></a>

Developed by Donald Dorsey, the Mass Index uses the high-low range to identify trend reversals based on range expansions. In this sense, the Mass Index is a volatility indicator that does not have a directional bias. Instead, the Mass Index identifies range bulges that can foreshadow a reversal of the current trend.

<figure><img src="/files/AVdLIxa3o4m5DxtTbK6p" alt=""><figcaption></figcaption></figure>

## Mass Index Calculation <a href="#sharpcharts_calculation" id="sharpcharts_calculation"></a>

There are four parts involved in the Mass Index calculation:

```
Single EMA = 9-period exponential moving average (EMA) of the high-low differential 

Double EMA = 9-period EMA of the 9-period EMA of the high-low differential

EMA Ratio = Single EMA divided by Double EMA

Mass Index = 25-period sum of the EMA Ratio
```

The calculation is fairly straightforward. First, the Single EMA provides the average for the high-low range. Second, the Double EMA provides a second smoothing of this volatility measure. Using a ratio of these two exponential [moving averages](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) normalizes the data series. This ratio shows when the Single EMA becomes large relative to the Double EMA. The final step, a 25-period summation, acts like a moving average to further smooth the data series. Overall, the Mass Index rises as the high-low range widens and falls as the high-low range narrows. A spreadsheet example is shown below.

<figure><img src="/files/JyCV4vejPGcW7vFD8jOM" alt=""><figcaption><p>Spreadsheet 1</p></figcaption></figure>

Some of the spreadsheet values are off by a penny because the exponential moving average calculation extends back less than three months. Calculations in SharpCharts extend back two years, which makes the exponential moving average calculation more robust.

Click below to download this spreadsheet example.

{% file src="/files/nxiGFBTKKVBcodW0v2ur" %}

## Interpreting the Mass Index <a href="#signals" id="signals"></a>

### Trend Reversal Signals

Donald Dorsey looked for “reversal bulges” to signal a trend reversal. According to Dorsey, a bulge occurs when the Mass Index moves above 27. This initial bulge does not complete the signal, however. Dorsey waited for this bulge to reverse with a move back below 26.50. Once the reversal bulge is complete, traders should use other analysis techniques to determine the direction of the next move. Ideally, a downtrend followed by a reversal bulge would suggest a bullish trend reversal. Conversely, an uptrend followed by a reversal bulge would suggest a bearish trend reversal.

<figure><img src="/files/Z6XjkCNXU7rMR9PD8kXM" alt=""><figcaption><p>Reversal bulge signals in an uptrend</p></figcaption></figure>

The example above shows Advanced Auto Parts Inc. with the Mass Index producing two reversal bulges over a 12-month period. In both cases, the trend was up when the Mass Index moved above 27, which means a bearish reversal was expected. The first signal foreshadowed a trading range. The second signal is still developing.&#x20;

Chartists looking for signals will most likely have to relax Dorsey's requirements for the reversal bulge because the Mass Index rarely exceeds 27. It takes exceptional volatility to push the index above this level.

### Adjusting the Signal Threshold <a href="#tweaking" id="tweaking"></a>

Chartists can lower the threshold for a reversal bulge to generate more signals. One size does not fit all when it comes to volatility. In other words, chartists may need to compare Mass Index levels over time to identify historical highs and lows. A move that nears the high end of the historical range would suggest a volatility bulge that could foreshadow a reversal.

The chart below shows International Paper with the Mass Index moving above 26 twice. Even though the Mass Index touched 27 in August 2011, the 26 level seems more appropriate for a reversal bulge. Additionally, keep in mind that August 2011 was an extremely volatile period for the entire stock market and this reading looks like an outlier. The trend was down when the Mass Index moved above 26 in August 2011 and May 2012. This suggested that a bullish reversal would follow and chartists could then use other analytical techniques to identify such a reversal.

<figure><img src="/files/BoiN7Yza02EBRkEVtTGw" alt=""><figcaption><p>Reversal bulge signals in a downtrend</p></figcaption></figure>

### Generating Directional Signals

The bottom indicator in the chart above is the [TRIX oscillator](/table-of-contents/technical-indicators-and-overlays/technical-indicators/trix.md), which is the one-period rate-of-change for the triple smoothed exponential moving average. The TRIX is like the smoothed version of MACD. Once the reversal bulge is in place and the trading bias established, chartists can use the TRIX (or similar indicators, such as the [MACD](/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator.md) or [PPO](/table-of-contents/technical-indicators-and-overlays/technical-indicators/percentage-price-oscillator-ppo.md)) to generate a directional signal.&#x20;

Because the trends were down when these reversal bulges occurred in the International Paper example above, the trading bias was bullish and only bullish signals were considered. The green arrows show when the TRIX moved above its signal line to signal an upturn in prices.

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The Mass Index uses the high-low differential to provide a smoothed volatility measure. The indicator typically fluctuates in the mid-20s; readings near the high end of the historical range suggest increasing volatility, which increases the chances for a trend reversal. Although Dorsey set the bulge threshold at 27, chartists should consider a lower threshold to produce more signals. Keep in mind that the Mass Index does not have a directional bias. The directional bias depends on the existing trend. As with all indicators, chartists should use other analysis techniques to complement the Mass Index.

***

## Charting with the Mass Index <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

### Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Mass Index can be set as an indicator above, below or behind a security's price plot. Once the indicator is chosen from the dropdown menu, a Mass Index indicator is added to the chart with the default setting of 25 summation periods. Users can adjust the summation periods by changing the number in the Parameters box. Chartists can also add one or more horizontal lines using the Overlay setting for the Mass Index indicator. In the example below, a blue line was added at 26.5 and a red line at 27, to set the thresholds for the reversal bulge signal.&#x20;

[Click here for a live version of this chart.](https://stockcharts.com/sc3/ui/?s=QQQ\&id=p02675086103)

<figure><img src="/files/GuDJcYTDwbbmH2rXtEJE" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/S5Qxc72ZLRACNlmMiVIM" alt=""><figcaption><p>SharpCharts Settings for the Mass Index</p></figcaption></figure>

{% hint style="info" %}
**Learn More:** For more details on the parameters used to configure Mass Index indicators, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#mass_index) in the Support Center.
{% endhint %}

### Using with StockChartsACP <a href="#suggested_scans" id="suggested_scans"></a>

This indicator can be added from the Chart Settings panel for your StockChartsACP chart. The indicator can be positioned above, below, or behind the security's price plot.

<figure><img src="/files/wJBT3xFiKdYor0PUVYLg" alt=""><figcaption></figcaption></figure>

[Click here for a live version of this chart.](https://schrts.co/tyTRpMhN)

By default, the indicator uses 25 summation periods. This parameter can be adjusted to meet your technical analysis needs.

## Scanning for the Mass Index <a href="#suggested_scans" id="suggested_scans"></a>

StockCharts members can screen for stocks based on Mass Index values. Below are some example scans that can be used for Mass Index-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when a Mass Index-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-al/al).

### Mass Index Bullish Reversal <a href="#mass_index_bullish_reversal" id="mass_index_bullish_reversal"></a>

This scan searches for stocks that are trading below their 200-day moving average to define a long-term downtrend. A bullish reversal is identified when Mass Index moves below 26.5.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [Daily Close < Daily SMA(200,Daily Close)]
AND [26.5 x Daily MASS(25)]
```

### Mass Index Bearish Reversal <a href="#mass_index_bearish_reversal" id="mass_index_bearish_reversal"></a>

This scan searches for stocks that are trading above their 200-day moving average to define a long-term uptrend. A bearish reversal is identified when Mass Index moves below 26.5.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [Daily Close > Daily SMA(200,Daily Close)]
AND [26.5 x Daily MASS(25)]
```

{% hint style="info" %}
**Learn More:** For more details on the syntax for Mass Index scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#mass_index_mass) in the Support Center.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/mass-index.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
