> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/bollinger-bands.md).

# Bollinger Bands

## What Are Bollinger Bands? <a href="#what_are_bollinger_bands" id="what_are_bollinger_bands"></a>

Developed by John Bollinger, Bollinger Bands® are volatility bands placed above and below a moving average. Volatility is based on the standard deviation, which changes as volatility increases and decreases. The bands automatically widen when volatility increases and contract when volatility decreases. Their dynamic nature allows them to be used on different securities with the standard settings.

[Click here for a live version of this chart.](https://stockcharts.com/sc3/ui/?s=MSFT\&p=D\&b=5\&g=0\&id=p81912915738\&a=952666096)

<figure><img src="/files/nhHlGqvHHiPNNisQ7457" alt=""><figcaption></figcaption></figure>

So, how do you use Bollinger Bands effectively? They can be used to confirm M-Tops and W-Bottoms or to determine the trend's strength. Signals based on the distance between the upper and lower band, including the popular Bollinger Band Squeeze, are identified using the related Bollinger BandWidth indicator.

{% hint style="info" %}
**Learn More:** [Bollinger Band Squeeze](/table-of-contents/trading-strategies-and-models/trading-strategies/bollinger-band-squeeze.md) | [Bollinger BandWidth](/table-of-contents/technical-indicators-and-overlays/technical-indicators/bollinger-bandwidth.md)
{% endhint %}

{% hint style="warning" %}
**Note:** Bollinger Bands® is a registered trademark of John Bollinger.
{% endhint %}

***

## Bollinger Bands Calculation <a href="#how_to_calculate_bollinger_bands" id="how_to_calculate_bollinger_bands"></a>

### Formulas <a href="#formulas" id="formulas"></a>

```
  * Middle Band = 20-day simple moving average (SMA)
  * Upper Band = 20-day SMA + (20-day standard deviation of price x 2) 
  * Lower Band = 20-day SMA - (20-day standard deviation of price x 2)
```

**Bollinger Bands consist of a middle band with two outer bands.** The middle band is a simple moving average that is usually set at 20 periods. A simple moving average is used because the standard deviation formula also uses a simple moving average. The look-back period for the standard deviation is the same as for the simple moving average. The outer bands are usually set 2 standard deviations above and below the middle band.

<figure><img src="/files/zbsl6PjIAph52XQmp1K4" alt=""><figcaption><p>Chart 1</p></figcaption></figure>

This spreadsheet below shows the calculations for the Bollinger Bands in the SPY chart above.

Click below to download this spreadsheet example.

{% file src="/files/X1JHX1iMgLFWQRUyjOv0" %}

<figure><img src="/files/BfttypNCNXpgYGgYjAAM" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Learn More:** [Moving Averages](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) | [Standard Deviation](/table-of-contents/technical-indicators-and-overlays/technical-indicators/standard-deviation-volatility.md)
{% endhint %}

### Adjusting Bollinger Band Settings <a href="#adjusting_bollinger_band_settings" id="adjusting_bollinger_band_settings"></a>

Settings can be adjusted to suit the characteristics of particular securities or trading styles. Bollinger recommends making small incremental adjustments to the standard deviation multiplier. Changing the number of periods for the moving average also affects the number of periods used to calculate the standard deviation. Therefore, only small adjustments are required for the standard deviation **multiplier**. An increase in the moving average period would automatically increase the number of periods used to calculate the standard deviation and would also warrant an increase in the standard deviation **multiplier**. With a 20-day SMA and 20-day standard deviation, the standard deviation multiplier is set at 2. Bollinger suggests increasing the standard deviation multiplier to 2.1 for a 50-period SMA and decreasing the standard deviation multiplier to 1.9 for a 10-period SMA.

## Interpreting Bollinger Bands <a href="#what_do_bollinger_bands_tell_us" id="what_do_bollinger_bands_tell_us"></a>

Bollinger Bands are often used to help confirm trend reversals. M-Tops and W-Bottoms are chart patterns that can indicate a trend reversal; the chart pattern's position relative to the Bollinger Bands helps confirm the chart pattern.

The strength of the trend can also be determined by how closely prices follow the upper Bollinger Band in a strong uptrend, or the lower Bollinger Band in a strong downtrend. This is often referred to as "walking the bands".&#x20;

### Confirming W-Bottom Chart Patterns <a href="#signalw-bottoms" id="signalw-bottoms"></a>

W-Bottoms were part of Arthur Merrill's work that identified 16 patterns with a basic W shape. Bollinger uses these various W patterns with Bollinger Bands to identify W-Bottoms, which form in a downtrends and contain two reaction lows. In particular, Bollinger looks for W-Bottoms where the second low is lower than the first but holds above the lower band. There are four steps to confirm a W-Bottom with Bollinger Bands. First, a reaction low forms. This low is usually, but not always, below the lower band. Second, there is a bounce towards the middle band. Third, there is a new price low in the security. This low holds **above** the lower band. The ability to hold above the lower band on the test shows less weakness on the last decline. Fourth, the pattern is confirmed with a strong move off the second low and a resistance break.

<figure><img src="/files/drAyhf67Ut574RmEIX1o" alt=""><figcaption><p>Chart 2</p></figcaption></figure>

Chart 2 shows Nordstrom (JWN) with a W-Bottom in January-February 2010. First, the stock formed a reaction low in January (black arrow) and broke below the lower band. Second, there was a bounce back above the middle band. Third, the stock moved below its January low and held above the lower band. Even though the 5-Feb spike low broke the lower band, the signal is not affected since, like Bollinger Bands, it is calculated using closing prices. Fourth, the stock surged with expanding volume in late February and broke above the early February high.

Chart 3 shows Sandisk with a smaller W-Bottom in July-August 2009.

<figure><img src="/files/wSJaz2i91QPbyLNce8xr" alt=""><figcaption><p>Chart 3</p></figcaption></figure>

### Confirming M-Top Chart Patterns <a href="#signalm-tops" id="signalm-tops"></a>

M-Tops were also part of Arthur Merrill's work that identified 16 patterns with a basic M shape. Bollinger uses these various M patterns with Bollinger Bands to identify M-Tops, which are essentially the opposite of W-Bottoms. According to Bollinger, tops are usually more complicated and drawn out than bottoms. Double tops, head-and-shoulders patterns, and diamonds represent evolving tops.

In its most basic form, an M-Top is similar to a double top. However, the reaction highs are not always equal; the first high can be higher or lower than the second high. Bollinger suggests looking for signs of non-confirmation when a security is making new highs. A non-confirmation occurs with three steps. First, a security creates a reaction high above the upper band. Second, there is a pullback towards the middle band. Third, prices move above the prior high but fail to reach the upper band. This is a warning sign. The inability of the second reaction high to reach the upper band shows waning momentum, which can foreshadow a trend reversal. Final confirmation comes with a support break or bearish indicator signal.

<figure><img src="/files/PpLLw4Phq4cw3Xz6dxYL" alt=""><figcaption><p>Chart 4</p></figcaption></figure>

Chart 4 shows Exxon Mobil (XOM) with an M-Top in April-May 2008. The stock moved above the upper band in April, followed by a pullback in May and another push above 90. Even though the stock moved above the upper band on an intraday basis, it did not CLOSE above the upper band. The M-Top was confirmed with a support break two weeks later. Additionally, the MACD formed a bearish divergence and moved below its signal line for confirmation.

<figure><img src="/files/pkWkv1OSGrN8zo6GYdei" alt=""><figcaption><p>Chart 5</p></figcaption></figure>

Chart 5 shows Pulte Homes (PHM) within an uptrend in July-August 2008. Price exceeded the upper band in early September to affirm the uptrend. After a pullback below the 20-day SMA (middle Bollinger Band), the stock moved to a higher high above 17. Despite this new high for the move, price did not exceed the upper band, which was a warning sign. The stock broke support a week later and MACD moved below its signal line. Notice that this M-top is more complex because there are lower reaction highs on either side of the peak (blue arrow). This evolving top formed a small head-and-shoulders pattern.

### Measuring Trend Strength: Walking the Bands <a href="#signalwalking_the_bands" id="signalwalking_the_bands"></a>

Moves above or below the bands are not signals per se. As Bollinger puts it, moves that touch or exceed the bands are not signals, but rather “tags”. On the face of it, a move to the upper band shows strength, while a sharp move to the lower band shows weakness. Momentum oscillators work much the same way. Overbought is not necessarily bullish. It takes strength to reach overbought levels and overbought conditions can extend in a strong uptrend. Similarly, prices can “walk the band” with numerous touches during a strong uptrend. Think about it for a moment. The upper band is 2 standard deviations above the 20-period simple moving average. It takes a pretty strong price move to exceed this upper band. An upper band touch that occurs after a Bollinger Band confirmed W-Bottom would signal the start of an uptrend. Just as a strong uptrend produces numerous upper band tags, it is also common for prices to never reach the lower band during an uptrend. The 20-day SMA sometimes acts as support. In fact, dips below the 20-day SMA sometimes provide buying opportunities before the next tag of the upper band.

<figure><img src="/files/zQupod2HNum86utvkOul" alt=""><figcaption><p>Chart 6</p></figcaption></figure>

Chart 6 shows Air Products (APD) with a surge and close above the upper band in mid-July. First, notice that this is a strong surge that broke above two resistance levels. A strong upward thrust is a sign of strength, not weakness. Trading turned flat in August and the 20-day SMA moved sideways. The Bollinger Bands narrowed, but APD did not close below the lower band. Prices and the 20-day SMA turned up in September. Overall, APD closed above the upper band at least five times over a four-month period. The indicator window shows the 10-period Commodity Channel Index (CCI). Dips below -100 are deemed oversold and moves back above -100 signal the start of an oversold bounce (green dotted line). The upper band tag and breakout started the uptrend. CCI then identified tradable pullbacks with dips below -100. This is an example of combining Bollinger Bands with a momentum oscillator for trading signals.

<figure><img src="/files/kPiV7TrddF8SqkOXsoue" alt=""><figcaption><p>Chart 7</p></figcaption></figure>

Chart 7 shows Monsanto (MON) with a walk down the lower band. The stock broke down in January with a support break and closed below the lower band. From mid-January until early May, Monsanto closed below the lower band at least five times. Notice that the stock did not close above the upper band once during this period. The support break and initial close below the lower band signaled a downtrend. As such, the 10-period Commodity Channel Index (CCI) was used to identify short-term overbought situations. A move above +100 is overbought. A move back below +100 signals a resumption of the downtrend (red arrows). This system triggered two good signals in early 2010.

## The Bottom Line <a href="#final_thoughts" id="final_thoughts"></a>

Bollinger Bands reflect direction with the 20-period SMA and volatility with the upper/lower bands. As such, they can determine if prices are relatively high or low. **According to Bollinger, the bands should contain 88-89% of price action, which makes a move outside the bands significant.** Technically, prices are relatively high when they're above the upper band and relatively low when below the lower band. However, “relatively high” should not be regarded as bearish or a sell signal. Likewise, “relatively low” should not be considered bullish or a buy signal. Prices are high or low for a reason. As with other indicators, Bollinger Bands are not meant to be used as a stand-alone tool. Chartists should combine Bollinger Bands with basic trend analysis and other indicators for confirmation.

***

## Charting with Bollinger Bands <a href="#charting_with_bollinger_bands" id="charting_with_bollinger_bands"></a>

The Bollinger Bands overlay can be added to SharpCharts, ACP Charts, and P\&F Charts.

### Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

[Click here for a live version of this chart.](https://stockcharts.com/sc3/ui/?s=F\&p=D\&b=5\&g=0\&id=p49007926451\&a=952729897)

<figure><img src="/files/kKv6969E6wxB5KnZXw2j" alt=""><figcaption><p>Chart 8</p></figcaption></figure>

Bollinger Bands can be found in SharpCharts as a price overlay. As with a simple moving average, Bollinger Bands should be shown on top of a price plot. Upon selecting Bollinger Bands, the default setting will appear in the parameters window (20,2). The first number (20) sets the periods for the simple moving average and the standard deviation. The second number (2) sets the standard deviation multiplier for the upper and lower bands. These default parameters set the bands 2 standard deviations above/below the simple moving average. Users can change the parameters to suit their charting needs. A Bollinger Band overlay can be set at (50,2.1) for a longer timeframe or at (10,1.9) for a shorter timeframe.

<figure><img src="/files/TxSPufpFvRUGplJY8ZHU" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Learn More:** For more details on the parameters used to configure Bollinger Bands overlays, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#bollinger_bands-1) in the Support Center.
{% endhint %}

### Using With StockChartsACP <a href="#using_with_stockchartsacp" id="using_with_stockchartsacp"></a>

This overlay can be added from the Chart Settings panel for your StockChartsACP chart. Bollinger Bands can be overlaid on the security's price plot or on an indicator panel.\
[Click here for a live version of this chart.](https://schrts.co/AXNcfZkD)

<figure><img src="/files/4d7hcL882vU8FF9rJ44n" alt=""><figcaption><p>Chart 9</p></figcaption></figure>

By default, the overlay uses a 20-period SMA and sets the bands 2.0 standard deviations above or below the SMA. These parameters can be adjusted to meet your technical analysis needs.

### Using With P\&F Charts <a href="#using_with_p_f_charts" id="using_with_p_f_charts"></a>

Bollinger Bands can also be overlaid on P\&F charts. This overlay can be found in the Overlays section on the P\&F Workbench.

[Click here for a live version of this chart.](https://stockcharts.com/freecharts/pnf.php?c=IBM,PWTADANRNO\[PE20,2]\[D]\[F1!3!!!2!20]\&dt=202105122038)

<figure><img src="/files/D784KoRGulIGX4SR1xwC" alt=""><figcaption><p>Chart 10</p></figcaption></figure>

By default, a 20-period SMA and 2 standard deviations are used to calculate the Bollinger Bands. However, since P\&F moving averages are double smoothed, it may be necessary to shorten the moving average period when placing this overlay on a P\&F chart.

{% hint style="info" %}
**Learn More:** [Bollinger Bands on P\&F Charts](/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-indicators.md#bollinger_bands)
{% endhint %}

***

## Scanning for Bollinger Bands <a href="#scanning_for_bollinger_bands" id="scanning_for_bollinger_bands"></a>

StockCharts members can screen for stocks based on Bollinger Band values. Below are some example scans that can be used for Bollinger Bands-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://help.stockcharts.com/scanning-and-alerts/technical-scans/advanced-scan-workbench).

Members can also set up alerts to notify them when a Bollinger Bands-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://help.stockcharts.com/scanning-and-alerts/technical-alerts/technical-alert-workbench).

### Bullish Bollinger Band Crossover <a href="#bullish_bollinger_band_crossover" id="bullish_bollinger_band_crossover"></a>

This scan finds stocks that have just moved above their upper Bollinger Band line. This scan is just a starting point. Further refinement and analysis are required.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 5]

AND [Daily Close x Daily Upper BB(20,2.0)]
```

### Bearish Bollinger Band Crossover <a href="#bearish_bollinger_band_crossover" id="bearish_bollinger_band_crossover"></a>

This scan finds stocks that have just moved below their lower Bollinger Band line. This scan is just a starting point. Further refinement and analysis are required.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 5]

AND [Daily Lower BB(20,2.0) x Daily Close]
```

{% hint style="info" %}
**Learn More:** For more details on the syntax to use for Bollinger Band scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#bollinger_bands) in the Support Center.
{% endhint %}

***


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/bollinger-bands.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
