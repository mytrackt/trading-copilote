> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/ttm-squeeze.md).

# TTM Squeeze

## What Is the TTM Squeeze Indicator? <a href="#introduction" id="introduction"></a>

TTM Squeeze is a volatility and momentum indicator introduced by John Carter of Trade the Markets (now Simpler Trading), which capitalizes on the tendency for price to break out strongly after consolidating in a tight trading range.

The volatility component of the TTM Squeeze indicator measures price compression using [Bollinger Bands](/table-of-contents/technical-indicators-and-overlays/technical-overlays/bollinger-bands.md) and [Keltner Channels](/table-of-contents/technical-indicators-and-overlays/technical-overlays/keltner-channels.md). If the Bollinger Bands are completely enclosed within the Keltner Channels, it indicates a low volatility period. This is known as the squeeze. When the Bollinger Bands expand and move back outside of the Keltner Channel, the squeeze is said to have “fired”— volatility increases, and prices are likely to break out of that tight trading range in one direction or the other. The on/off state of the squeeze is shown with small dots on the zero line of the indicator—red dots indicate the squeeze is on, and green dots indicate the squeeze is off.

The TTM Squeeze indicator also uses a momentum oscillator to show the expected direction of the move when the squeeze fires. This histogram oscillates around the zero line. Increasing momentum above the zero line indicates an opportunity to purchase long, while momentum falling below the zero line indicates a shorting opportunity.

<figure><img src="/files/pRGTtjTRhj5eZksSH7MA" alt=""><figcaption></figcaption></figure>

## Calculating TTM <a href="#calculation" id="calculation"></a>

There are two components of the TTM Squeeze indicator to calculate: the squeeze on/off dots and the momentum histogram.

### Squeeze On/Off Dots <a href="#squeeze_on_off_dots" id="squeeze_on_off_dots"></a>

First, calculate Bollinger Bands for the security. Carter uses the standard Bollinger Band settings of 20 periods and 2 standard deviations, but these parameters can be adjusted to meet your trading needs.

Second, calculate Keltner Channels for the security. Carter uses 20 periods for the moving average and ATR, and 1.5 for the ATR multiplier, but these parameters can be adjusted as well.

{% hint style="warning" %}
**Note:** Carter uses the original Keltner Channels formula developed by Chester W. Keltner in 1960, so that is the formula StockCharts uses to calculate the Keltner Channels for the TTM Squeeze indicator. Elsewhere on the StockCharts website, the updated Keltner Channels formula developed by Linda Raschke in the 1980s is used.
{% endhint %}

Once the values for the upper and lower Bollinger Bands and Keltner Channels have been calculated, the formula for determining the state of the squeeze is simple. If both of the following conditions are true, then the squeeze is on for that period:

```
Upper Bollinger Band < Upper Keltner Channel
Lower Bollinger Band > Lower Keltner Channel
```

If they are not both true (one or both Bollinger Bands fall outside of the Keltner Channel), then the squeeze is off for that period.

### Momentum Histogram <a href="#momentum_histogram" id="momentum_histogram"></a>

The TTM Squeeze indicator also includes a smoothed momentum oscillator to indicate the possible direction of the breakout. StockCharts' implementation of the TTM Squeeze uses the following steps to produce the momentum oscillator.

First, calculate the Donchian midline for the specified number of momentum periods (20 is used by default):

```
(Highest high in 20 periods + lowest low in 20 periods) / 2
```

Second, calculate the SMA of the close for the specified number of momentum periods (so by default, a 20-period SMA of price).

Third, calculate the delta between the close and the average of the Donchian midline and SMA values using the following formula:

```
Close - ( (Donchian midline + SMA) / 2 )
```

Finally, use linear regression on the delta values to smooth them. The formula for linear regression is beyond the scope of this article, but it essentially looks for the “line of best fit” given the available data. The momentum histogram values show how far above or below the average the price is expected to be.

## Interpretating TTM <a href="#interpretation" id="interpretation"></a>

The TTM Squeeze indicator has both volatility and momentum components. The Squeeze dots signal when volatility conditions are right to buy; the momentum histogram indicates the direction (long or short) in which to trade.

While volatility levels are low, the squeeze dots will be red. When volatility increases and the Bollinger Bands expand until they are outside of the Keltner Channels, the squeeze has “fired” and the squeeze dots will be green. Carter recommends buying on the first green dot after one or more red dots.

The momentum histogram helps to determine the direction in which to trade. If the momentum is above the zero line and rising (light blue bars), buy long; if the histogram is below the zero line and falling lower (dark red bars), that indicates a shorting opportunity.

The histogram bars are color coded for ease of interpretation. Bars above the zero line are blue and below the zero line are red. In addition, a bar that is lower than the previous bar will be a darker color (dark blue or dark red), and a bar that is higher than the previous bar will be a lighter color (light blue or light red).

Price moves after a squeeze fires tend to last for 8-10 bars. When the histogram changes direction and starts moving back towards the zero line, that is a signal to sell.

The momentum histogram can also be used to determine specific exit points. Carter recommends selling when you've had two bars in the new color. For example, if the squeeze fires and the bars are light blue (above the zero line and increasing), he recommends selling when you see two dark blue bars (above the zero line and decreasing) in a row.

The TTM Squeeze indicator can be used in many timeframes. Many chartists look at the same security in multiple timeframes for confirmation. For example, if a squeeze is firing on both a daily and an hourly chart at the same time, that is a stronger signal than a squeeze that is only firing in one timeframe.

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The TTM Squeeze indicator measures both volatility and momentum to spot trading opportunities based on volatility changes in a security. The volatility component of the indicator (the squeeze dots) signals potential breakouts after periods of low volatility. The momentum histogram indicates the likely direction of the breakout and can help to determine exit points.

As with all indicators, traders should use the TTM Squeeze indicator in conjunction with other indicators and analysis techniques.

***

## Charting with the TTM Squeeze Indicator <a href="#charting_with_the_ttm_squeeze_indicator" id="charting_with_the_ttm_squeeze_indicator"></a>

The TTM Squeeze indicator can be added to SharpCharts and ACP charts.

### Using with SharpCharts

The TTM Squeeze is available on SharpCharts in the “Indicators” section. The indicator can be positioned above, below, or behind the security's price plot.&#x20;

<figure><img src="/files/hOUwt96OSR0G00EoXYwK" alt=""><figcaption></figcaption></figure>

Once chosen, the default settings will appear in the parameters box (20,2.0,20,1.5,20,20). By default, the indicator uses standard Bollinger Band (20,2.0) and original Keltner Channel (20,1.5,20) settings, as well as a 20-period momentum histogram, but the number of periods and other settings can be adjusted to meet your technical analysis needs.

<figure><img src="/files/zwlEP9YGjyG51TBlHm99" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Learn More.** For more details on the parameters used to configure TTM Squeeze indicators, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference) in the Support Center.
{% endhint %}

### Using with StockChartsACP

The TTM Squeeze indicator can be charted on StockChartsACP after installing our free Advanced Indicator Pack. Please see our [StockChartsACP Plug-Ins article](https://help.stockcharts.com/charts-and-tools/stockchartsacp/stockchartsacp-plug-ins) in the Support Center for more information on installing this plug-in.

Once the plug-in is installed, the TTM Squeeze indicator can be added from the Chart Settings panel for your StockChartsACP chart. The indicator can be positioned above, below, or behind the security's price plot.

<figure><img src="/files/teyB9kAu9xhr8lBbas3q" alt=""><figcaption></figcaption></figure>

By default, the indicator uses standard Bollinger Band and original Keltner Channel settings and a 20-period momentum histogram, but the number of periods and other settings can be adjusted to meet your technical analysis needs.

## Scanning for TTM Squeeze <a href="#scanning_for_ttm_squeeze" id="scanning_for_ttm_squeeze"></a>

StockCharts members can screen for stocks based on TTM Squeeze values. Below are some example scans that can be used for TTM Squeeze-based signals. Copy and paste the scan text into the Scan Criteria box in the [Advanced Scan Workbench](https://help.stockcharts.com/scanning-and-alerts/technical-scans/advanced-scan-workbench).

Members can also set up alerts to notify them when a TTM Squeeze-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://help.stockcharts.com/scanning-and-alerts/technical-alerts/technical-alert-workbench).

### TTM Squeeze Signal to Go Long <a href="#ttm_squeeze_signal_to_go_long" id="ttm_squeeze_signal_to_go_long"></a>

This scan reveals stocks where the TTM Squeeze has fired and the TTM Squeeze Histogram is above zero and rising. This is a signal to go long. This scan is just a starting point. Further refinement and analysis are required.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [TTM Squeeze(20,2.0,20,1.5,20) is true]
AND [yesterday's TTM Squeeze(20,2.0,20,1.5,20) is false]
AND [TTM Squeeze Hist (20) > 0]
AND [TTM Squeeze Hist (20) > yesterday's TTM Squeeze Hist (20)]
```

### TTM Squeeze Signal to Short <a href="#ttm_squeeze_signal_to_short" id="ttm_squeeze_signal_to_short"></a>

This scan reveals stocks where the TTM Squeeze has fired and the TTM Squeeze Histogram is below zero and falling. This is a signal to buy short. This scan is just a starting point. Further refinement and analysis are required.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [TTM Squeeze(20,2.0,20,1.5,20) is true]
AND [yesterday's TTM Squeeze(20,2.0,20,1.5,20) is false]
AND [TTM Squeeze Hist (20) < 0]
AND [TTM Squeeze Hist (20) < yesterday's TTM Squeeze Hist (20)]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax for RVOL scans, please see our [Scan Syntax Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference) in the Support Center.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/ttm-squeeze.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
