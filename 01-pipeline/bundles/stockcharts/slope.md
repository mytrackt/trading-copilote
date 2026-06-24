> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/slope.md).

# Slope

## What Is the Slope Indicator? <a href="#introduction" id="introduction"></a>

The slope indicator measures the rise-over-run of a linear regression, which is the line of best fit for a price series. Fluctuating above and below zero, the Slope indicator best resembles a [momentum oscillator](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#momentum_oscillators) without boundaries. It is not well suited for overbought/oversold levels, but can measure the direction and strength of a trend. It can also be used with other indicators to identify potential entry points within an ongoing trend.

## Calculating the Slope <a href="#calculation" id="calculation"></a>

Slope is based on a linear regression (line of best fit). Even though the formula for a linear regression is beyond the scope of this article, a linear regression can be shown using the Raff Regression Channel in SharpCharts. This indicator features a linear regression in the middle with equidistant outer trend lines. Slope equals the rise-over-run for the linear regression. Rise refers to the price change. Run refers to the timeframe. A 20-day Slope would be the rise-over-run of a 20-day linear regression. If the rise is 4 points and the run is two days, then the slope would be 2 (4/2 = 2). If the rise is -6 points and the run is 2, then the slope would be -3 (-6/2 = -3). In general, an advancing period has a positive slope and a declining period has a negative slope. The steepness depends on the sharpness of the advance or decline.

<figure><img src="/files/FJ15FGqhtTuZ8tFk43fc" alt=""><figcaption><p>Slope - Chart 1</p></figcaption></figure>

Chart 1 shows SPY with three different 20-day periods (orange, yellow, blue). A 20-day [Raff Regression Channel](/table-of-contents/chart-analysis/chart-annotation-tools/raff-regression-channel.md) is shown for each 20-day period. The linear regression, in the middle, represents the “line of best fit” for the 20 data points. The dotted lines mark the end of the 20-day period and the value of the slope at that price point. The first period is relatively flat and the slope is barely positive. The second period is up and the slope is clearly positive. The third period is down and the slope is negative. Keep in mind that the Slope changes as old data points are dropped off and new data points are added.

## Trend Identification <a href="#trend_identification" id="trend_identification"></a>

Slope can be used to [quantify the trend](/table-of-contents/chart-analysis/trend-lines.md). A positive slope is by definition an uptrend. Similarly, a negative slope defines a downtrend. Chart 2 shows the Dow Industrials with a 52-week Slope (one year). The red dotted lines show the Slope turning negative, while the green dotted lines show the slope turning positive. The 52-week Slope was positive for around two years (2006-2007) and then turned negative in February 2008. Even though the Dow bottomed in March 2009 and moved sharply higher, the 52-week Slope did not cross back into positive territory until September 2009. Notice that the slope does not predict the trend. Instead, it follows the trend or the price points. This means there will be some lag.

<figure><img src="/files/0bGUGcfwz1ONBgprwrFo" alt=""><figcaption><p>Slope - Chart 2</p></figcaption></figure>

## Trend Strength <a href="#trend_strength" id="trend_strength"></a>

Directional movement can also be important when analyzing the slope. A negative and rising slope shows improvement within a downtrend. A positive and falling slope shows deterioration within an uptrend. Chart 3 shows the Nasdaq 100 ETF (QQQQ) with the 100-day Slope. A 20-day simple moving average was added to identify upturns and downturns. A Slope is rising when above its 20-day SMA and falling when below. Four key crossovers are identified on this chart (green/red arrows). Notice that the crossovers occurred before the Slope turned negative or positive. This is like a leading indication for the Slope. Also, notice the bounce after the negative cross in July 2008 and the retest after the positive cross in January 2009. These early slope reversals foreshadowed a move into positive territory or a trend change, but you should not expect an extended move after every moving average crossover. The 100-day Slope moved below its 20-day SMA in August 2009, yet QQQQ kept moving higher. A declining and positive Slope reflects less steepness in the advance. Notice how the 100-day Slope remained positive as QQQQ continued higher from September 2009 to January 2010.

<figure><img src="/files/ElO3Qe7aDcRJe0273ibD" alt=""><figcaption><p>Slope - Chart 3</p></figcaption></figure>

## Trade Bias <a href="#trade_bias" id="trade_bias"></a>

Slope alone cannot be used to participate in an ongoing trend, but it can be used with other indicators to identify potential entry points. In particular, Slope can be used for trend identification to establish a trading bias. A positive slope dictates a bullish bias, while a negative Slope dictates a bearish bias. Once a trading bias is established, a momentum oscillator can be used to identify potential entry points. The choice of momentum oscillator is really a personal preference. The example with Apple uses the 100-day Slope with 10-day [Williams %R](/table-of-contents/technical-indicators-and-overlays/technical-indicators/williams-r.md). The look-back period for the Slope should be significantly longer than the look-back period for the momentum oscillator. The Slope defines the bigger trend, while the momentum oscillator represents a subset of that trend. Chart 4 shows the 100-day Slope moving above zero in July to establish a bullish bias. Only bullish signals are considered for the momentum oscillator. These include oversold readings, centerline crossovers, or signal line crossovers. Williams %R does not have a signal line, but [MACD](/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator.md) and PPO do. The blue dotted lines show when 10-day Williams %R moves below -80% to become oversold. Notice that these readings correspond with short pullbacks in the stock. Except for the last oversold reading in early December, Apple resumed its uptrend soon after these oversold readings.

<figure><img src="/files/hieNVjO6YcuZHiXWEV1c" alt=""><figcaption><p>Slope - Chart 4</p></figcaption></figure>

## Relative Strength <a href="#relative_strength" id="relative_strength"></a>

The Slope of two (or more) securities can be compared to identify relative strength and relative weakness. The chart below shows Amazon (AMZN) with the S\&P 500. Both securities are shown with the 20-day Slope (black). The blue vertical line marks a point in early November when Amazon had a positive Slope and the S\&P 500 had a negative Slope. Amazon was clearly outperforming the S\&P 500 at this time. In fact, when the S\&P 500 bottomed in early November, Amazon led the way higher with a move from 117 to 143. Notice that Amazon moved higher even as the Slope moved lower. The Amazon Slope turned negative in mid-December and the S\&P 500 Slope was still positive. This situation repeated the second week of January. Based on the Slope comparison, Amazon went from relative strength in November to relative weakness in December and January. During these two months, the 20-day linear regression for Amazon was sloping down while the 20-day linear regression for the S\&P 500 was sloping up.

<figure><img src="/files/SYMKs3ho5vSYJmvxbKIF" alt=""><figcaption><p>Slope - Chart 5</p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

Slope measures the rise-over-run of a linear regression. In general, an uptrend is present when Slope is positive and a downtrend exists when the slope is negative. The timeframe depends on the number of days. 10 days covers a short-term trend, 100 days a medium-term trend, and 250 days a long-term trend. As with typical trend-following indicators, Slope lags price and reverses after an actual top or bottom. This does not, however, detract from its usefulness. Trend identification and trend strength are important tools, even for traders. As with moving averages, Slope can be used with momentum indicators to participate in an ongoing trend. [Click here](https://stockcharts.com/h-sc/ui?s=DIA\&p=D\&yr=0\&mn=8\&dy=0\&id=p93531652664\&listNum=30\&a=191771207) for a live chart with the Slope indicator.

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

Slope can be found near the bottom of the indicator list on SharpCharts. The default parameters (20) can be changed to suit the desired timeframe. Like all indicators, Slope can be positioned above the price plot, behind the price plot or below the price plot. In addition, users can click the green arrow next to advanced options to apply a moving average or another indicator to Slope.

<figure><img src="/files/Z0kkBJ5zIU349eWYimxv" alt=""><figcaption></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Oversold in an Uptrend <a href="#oversold_in_an_uptrend" id="oversold_in_an_uptrend"></a>

This scan reveals stocks that are oversold (short-term Williams %R below -80) in a medium-term uptrend (positive 100-day Slope).

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 5]

AND [Daily Slope(100,Daily Close) > 0]
AND [Daily Williams %R(10) < -80]
```

### Overbought in a Downtrend <a href="#overbought_in_a_downtrend" id="overbought_in_a_downtrend"></a>

This scan reveals stocks that are overbought (short-term Williams %R above -20) in a medium-term downtrend (negative 100-day Slope).

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 5]

AND [Daily Slope(100,Daily Close) < 0]
AND [Daily Williams %R(10) > -20]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax to use for Slope scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#slope_slope) in the Support Center.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/slope.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
