> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-directional-index-adx.md).

# Average Directional Index (ADX)

## What Is the Average Directional Index (ADX)? <a href="#what_is_the_average_directional_index_adx" id="what_is_the_average_directional_index_adx"></a>

The Average Directional Index (ADX), Minus Directional Indicator (-DI) and Plus Directional Indicator (+DI) represent a group of directional movement indicators that form a trading system developed by Welles Wilder. Although Wilder designed his Directional Movement System with commodities and daily prices in mind, these indicators can also be applied to stocks.

<figure><img src="/files/8MQcP9Vw0AzdOnvg2p2r" alt=""><figcaption></figcaption></figure>

Positive and negative directional movement form the backbone of the Directional Movement System. Wilder determined directional movement by comparing the difference between two consecutive lows with the difference between their respective highs.

The **Plus Directional Indicator (+DI)** and **Minus Directional Indicator (-DI)**, shown in green and red in the chart above, are derived from smoothed averages of these differences and measure trend ***direction*** over time. When +DI is *above* -DI, the trend is up; when +DI is *below* -DI, the trend is down. These two indicators are often collectively referred to as the Directional Movement Indicator (DMI).

The **Average Directional Index (ADX)**, shown in black in the chart above, is in turn derived from the smoothed averages of the difference between +DI and -DI; it measures the ***strength*** of the trend (regardless of direction) over time.

Using these three indicators together, chartists can determine both the **direction** and **strength** of the trend.

Wilder features the Directional Movement indicators in his 1978 book, *New Concepts in Technical Trading Systems*. This book also includes details on [Average True Range (ATR)](/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-atr.md), the [Parabolic SAR](/table-of-contents/technical-indicators-and-overlays/technical-overlays/parabolic-sar.md) system, and [Relative Strength Index (RSI)](/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi.md). Despite being developed before the computer age, Wilder's indicators are incredibly detailed in their calculation and have stood the test of time.

## Calculating the Average Directional Index <a href="#how_to_calculate_average_directional_index" id="how_to_calculate_average_directional_index"></a>

### Directional Movement Calculation

Directional movement is calculated by comparing the difference between two consecutive lows with the difference between their respective highs.

Directional movement is **positive** (plus) when the current high minus the prior high is greater than the prior low minus the current low. This so-called Plus Directional Movement (+DM) then equals the current high minus the prior high, provided it is positive. A negative value would simply be entered as zero.

Directional movement is **negative** (minus) when the prior low minus the current low is greater than the current high minus the prior high. This so-called Minus Directional Movement (-DM) equals the prior low minus the current low, provided it is positive. A negative value would simply be entered as zero.

<figure><img src="/files/1DrqJ6qFvASU9PEYtiWh" alt=""><figcaption></figcaption></figure>

The chart above shows four calculation examples for directional movement. The first pairing shows a big positive difference between the highs for a strong Plus Directional Movement (+DM). The second pairing shows an outside day with Minus Directional Movement (-DM) getting the edge. The third pairing shows a big difference between the lows for a strong Minus Directional Movement (-DM). The final pairing shows an inside day, which amounts to no directional movement (zero). Both Plus Directional Movement (+DM) and Minus Directional Movement (-DM) are negative and revert to zero, so they cancel each other out. All inside days will have zero directional movement.

### Step by Step ADX Calculation <a href="#step_by_step_adx_calculation" id="step_by_step_adx_calculation"></a>

The calculation steps for the ADX, Plus Directional Indicator (+DI) and Minus Directional Indicator (-DI) are based on the Plus Directional Movement (+DM) and Minus Directional Movement (-DM) values calculated above, as well as the Average True Range. Smoothed versions of +DM and -DM are divided by a smoothed version of the Average True Range to reflect the true magnitude of the move.

{% hint style="warning" %}
**Note:** Wilder describes it as the "True Range" (abbreviated as TR) in his formulas, but the calculation method is the same as for the [Average True Range](/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-atr.md) indicator used elsewhere on the site.
{% endhint %}

The calculation example below is based on a 14-period indicator setting, as recommended by Wilder.

1. Calculate the True Range (TR), Plus Directional Movement (+DM) and Minus Directional Movement (-DM) for each period.
2. Smooth these periodic values using Wilder's smoothing techniques. These are explained in detail in the next section.
3. Divide the 14-day smoothed Plus Directional Movement (+DM) by the 14-day smoothed True Range to find the 14-day Plus Directional Indicator (+DI14). Multiply by 100 to move the decimal point two places. This +DI14 is the green Plus Directional Indicator line (+DI) that is plotted along with the ADX line.
4. Divide the 14-day smoothed Minus Directional Movement (-DM) by the 14-day smoothed True Range to find the 14-day Minus Directional Indicator (-DI14). Multiply by 100 to move the decimal point two places. This -DI14 is the red Minus Directional Indicator line (-DI) that is plotted along with the ADX line.
5. The Directional Movement Index (DX) equals the absolute value of +DI14 less -DI14 divided by the sum of +DI14 and -DI14. Multiply the result by 100 to move the decimal point over two places.
6. After all these steps, it is time to calculate the Average Directional Index (ADX) line. The first ADX value is simply a 14-day average of DX. Subsequent ADX values are smoothed by multiplying the previous 14-day ADX value by 13, adding the most recent DX value and dividing this total by 14.

The spreadsheet example shows the calculation in detail. There is a 119-day calculation gap because approximately 150 periods are required to absorb the smoothing techniques.&#x20;

<figure><img src="/files/PzqAQM6eymSrCxj1dris" alt=""><figcaption></figcaption></figure>

Click below to download this spreadsheet example.&#x20;

{% file src="/files/0N0i8U1rPay2XFGTyM4C" %}

### Wilder's Smoothing Techniques <a href="#wilder_s_smoothing_techniques" id="wilder_s_smoothing_techniques"></a>

It's important to understand the effects of all the smoothing involved in the ADX, +DI and -DI calculations. Because of Wilder's smoothing techniques, it can take around 150 periods of data to get true ADX values. Wilder uses similar smoothing techniques with his RSI and Average True Range calculations. ADX values using only 30 periods of historical data will not match ADX values using 150 periods of historical data. ADX values with 150 days or more of data will remain consistent.

The first technique is used to smooth each period's +DM1, -DM1 and TR1 values over 14 periods. As with an exponential [moving average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md), the calculation has to start somewhere so the first value is simply the sum of the first 14 periods. As shown below, smoothing starts with the second 14-period calculation and continues throughout.

```
First TR14 = Sum of first 14 periods of TR1 
Second TR14 = First TR14 - (First TR14/14) + Current TR1 
Subsequent Values = Prior TR14 - (Prior TR14/14) + Current TR1
```

The second technique is used to smooth each period's DX value to finish with the Average Directional Index (ADX). First, calculate an average for the first 14 days as a starting point. The second and subsequent calculations use the smoothing technique below:

```
First ADX14 = 14 period Average of DX 
Second ADX14 = ((First ADX14 x 13) + Current DX Value)/14 
Subsequent ADX14 = ((Prior ADX14 x 13) + Current DX Value)/14
```

## Interpreting the Average Directional Index <a href="#applying_the_average_directional_index" id="applying_the_average_directional_index"></a>

The Average Directional Index (ADX) is used to measure the strength or weakness of a trend, not the actual direction. Directional movement is defined by +DI and -DI. In general, the bulls have the edge when +DI is greater than -DI, while the bears have the edge when -DI is greater. Crosses of these directional indicators can be combined with ADX for a complete trading system.

Before looking at some signals with examples, keep in mind that Wilder was a commodity and currency trader. The examples in his books are based on these instruments, not stocks. This does not mean his indicators cannot be used with stocks, however. Some stocks have price characteristics similar to commodities, which tend to be more volatile with short and strong trends. Stocks with low volatility may not generate signals based on Wilder's parameters. Chartists will likely need to adjust the indicator settings or the signal parameters according to the characteristics of the security.

### Measuring Trend Strength <a href="#trend_strength" id="trend_strength"></a>

At its most basic, the Average Directional Index (ADX) can be used to determine if a security is trending or not. This determination helps traders choose between a trend-following system or a non-trend-following system. Wilder suggests that a strong trend is present when ADX is above 25 and no trend is present when ADX is below 20. There appears to be a gray zone between 20 and 25. As noted above, chartists may need to adjust the settings to increase sensitivity and signals. ADX also has a fair amount of lag because of all the smoothing techniques. Many technical analysts use 20 as the key level for ADX.

<figure><img src="/files/xSW1YWjGjWnUydEL3PCK" alt=""><figcaption></figcaption></figure>

The chart above shows Nordstrom (JWN) with the 50-day SMA and 14-day Average Directional Index (ADX). The stock moved from a strong uptrend to a strong downtrend in April-May, but ADX remained above 20 because the strong uptrend quickly changed into a strong downtrend. There were two non-trending periods as the stock formed a bottom in February and August. A strong trend emerged after the August bottom as ADX moved above 20 and remained above 20.

### Identifying Trend Direction and +DI/-DI Trading Signals <a href="#trend_direction_and_crossovers" id="trend_direction_and_crossovers"></a>

Wilder put forth a simple system for trading with these directional movement indicators. The first requirement is for ADX to be trading above 25. This ensures that prices are trending. Many traders, however, use 20 as the key level. A buy signal occurs when +DI crosses above -DI. Wilder based the initial stop on the low of the signal day. The signal remains in force as long as this low holds, even if +DI crosses back below -DI. Wait for this low to be penetrated before abandoning the signal. This bullish signal is reinforced if/when ADX turns up and the trend strengthens. Once the trend develops and becomes profitable, traders will have to incorporate a stop-loss and trailing stop should the trend continue. A sell signal triggers when -DI crosses above +DI. The high on the day of the sell signal becomes the initial stop-loss.

<figure><img src="/files/avUut0YgoKdKCCwxV4wc" alt=""><figcaption></figcaption></figure>

The chart above shows Medco Health Solutions with the three directional movement indicators. Note that 20 is used instead of 25 to qualify ADX signals. A lower setting means more possible signals. The green dotted lines show the buy signals and the red dotted lines show the sell signals. Wilder's initial stops were not incorporated in order to focus on the indicator signals. As the chart clearly shows, there are plenty of +DI and -DI crosses. Some occur with ADX above 20 to validate signals. Others occur to invalidate signals. As with most such systems, there will be whipsaws, great signals, and bad signals. The key, as always, is to incorporate other aspects of technical analysis. For example, the first group of whipsaws in September 2009 occurred during a consolidation. Moreover, this consolidation looked like a flag, which is a bullish consolidation that forms after an advance. It would have been prudent to ignore bearish signals with a bullish continuation pattern taking shape. By contrast, the June 2010 buy signal occurred near a resistance zone marked by broken support and the 50-62% retracement zone. In this instance, it would have been prudent to ignore a buy signal so close to this resistance zone.

<figure><img src="/files/kBbm9kSotvpCBWcHFJhJ" alt=""><figcaption></figcaption></figure>

The chart above shows AT\&T (T) with three signals over a 12-month period. These three signals were pretty good, provided profits were taken and trailing stops were used. Wilder's [Parabolic SAR](/table-of-contents/technical-indicators-and-overlays/technical-overlays/parabolic-sar.md) could have been used to set a trailing stop-loss. Notice that there was no sell signal between the March and July buy signals. This is because ADX was not above 20 when -DI crossed above +DI in late April.

{% hint style="info" %}
**Learn More:** [Parabolic SAR](/table-of-contents/technical-indicators-and-overlays/technical-overlays/parabolic-sar.md)
{% endhint %}

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The Directional Movement System indicator calculations are complex, interpretation is straightforward, and successful implementation takes practice. +DI and -DI crossovers are quite frequent and chartists need to filter these signals with complementary analysis. Setting an ADX requirement will reduce signals, but this uber-smoothed indicator tends to filter as many good signals as bad. In other words, chartists might consider moving ADX to the back burner and focusing on the Directional Movement Indicators (+DI and -DI) to generate signals. These crossover signals will be similar to those generated using momentum oscillators. Therefore, chartists need to look elsewhere for confirmation help. Volume-based indicators, basic trend analysis and [chart patterns](/table-of-contents/chart-analysis/chart-patterns.md) can help distinguish strong crossover signals from weak crossover signals. For example, chartists can focus on +DI buy signals when the bigger trend is up and -DI sell signals when the bigger trend is down.

## Charting with the ADX <a href="#using_adx_with_sharpcharts" id="using_adx_with_sharpcharts"></a>

### Using with SharpCharts <a href="#using_adx_with_sharpcharts" id="using_adx_with_sharpcharts"></a>

SharpCharts users can plot these three directional movement indicators by selecting **ADX Line (w/+DI and -DI)** from the indicator dropdown list (there is also an option to plot the ADX line only). By default, the ADX line will be in black, the Plus Directional Indicator (+DI) in green and the Minus Directional Indicator (-DI) in red. This makes it easy to identify directional indicator crosses.&#x20;

While ADX can be plotted above, below or behind the main price plot, it is recommended to plot above or below because there are three lines involved. A horizontal line can be added to help identify ADX moves. The chart example below also shows the 50-day SMA and Parabolic SAR plotted behind the price plot. The moving average is used to filter signals. Only buy signals are used when trading above the 50-day moving average. Once initiated, the Parabolic SAR can be used to set stops.&#x20;

[Click here for a live version of this chart.](https://stockcharts.com/sc3/ui/?s=AAPL\&id=p96105200280)

<figure><img src="/files/r1M6K9pLwCpUBaFNAghI" alt=""><figcaption><p>Using ADX and supporting overlays on a SharpChart</p></figcaption></figure>

<figure><img src="/files/stiv18CYhYqCH251Xbve" alt=""><figcaption><p>ADX settings on the SharpCharts Workbench, along with supporting overlays</p></figcaption></figure>

{% hint style="info" %}
**Learn More:** For more details on the parameters used to configure ADX indicators, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#adx_line) in the Support Center.
{% endhint %}

### Using with StockChartsACP

The ADX indicator (either with or without the +DI/-DI lines) can be added from the Chart Settings panel for your StockChartsACP chart. The indicator can be positioned above, below, or behind the security's price plot.

<figure><img src="/files/hB8aJosUFRuwG5OwZINj" alt=""><figcaption></figcaption></figure>

[Click here for a live version of this chart.](https://schrts.co/TenRyRAs)

By default, this indicator is calculated using 14 periods. This parameter can be adjusted to meet your technical analysis needs.

## Scanning for ADX and +DI/-DI <a href="#suggested_adx_scans" id="suggested_adx_scans"></a>

StockCharts members can screen for stocks based on ADX, +DI, and -DI values. Below are some example scans that can be used for ADX-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when a ADX-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-al/al).

### Overall Uptrend with +DI Crossing above -DI <a href="#overall_uptrend_with_di_crossing_above_-di" id="overall_uptrend_with_di_crossing_above_-di"></a>

This scan starts with stocks that average 100,000 shares daily volume and have an average closing price above 10. An uptrend is present when trading above the 50-day SMA. A buy signal is possible when ADX is above 20. This signal materializes when +DI moves above -DI.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 10] 

AND [Daily ADX Line(14) > 20] 
AND [Daily Plus DI(14) crosses Daily Minus DI(14)] 
AND [Daily Close > Daily SMA(50,Daily Close)]
```

### Overall Downtrend with -DI Crossing above +DI <a href="#overall_downtrend_with_-di_crossing_above_di" id="overall_downtrend_with_-di_crossing_above_di"></a>

This scan starts with stocks that average 100,000 shares daily volume and have an average closing price above 10. A downtrend is present when trading below the 50-day SMA. A sell signal is possible when ADX is above 20. This signal materializes when -DI moves above +DI.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 10] 

AND [Daily ADX Line(14) > 20] 
AND [Daily Minus DI(14) crosses Daily Plus DI(14)] 
AND [Daily Close < Daily SMA(50,Daily Close)]
```

{% hint style="info" %}
**Learn More:** For more details on the syntax to use for Average Directional Index, Plus DI and Minus DI scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference) in the Support Center.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-directional-index-adx.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
