> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-average-envelopes.md).

# Moving Average Envelopes

## What Are Moving Average Envelopes? <a href="#introduction" id="introduction"></a>

Moving Average Envelopes are percentage-based envelopes set above and below a moving average. The moving average, which forms the base for this indicator, can be a simple or exponential moving average. Each envelope is then set the same percentage above or below the moving average. This creates parallel bands that follow price action.

<figure><img src="/files/ZZuyNp2dNhb00cmeXwaJ" alt=""><figcaption></figcaption></figure>

[Click here for a live version of this chart.](https://stockcharts.com/sc3/ui/?s=HLT\&p=D\&b=5\&g=0\&id=p29369358695)

With a moving average as the base, Moving Average Envelopes can be used as a trend following indicator. Beyond simply trend following, though, the envelopes can also be used to identify overbought and oversold levels when the trend is relatively flat.

***

## Moving Average Envelope Calculation <a href="#moving_average_envelope_calculation" id="moving_average_envelope_calculation"></a>

### Formulas <a href="#formulas" id="formulas"></a>

Calculating Moving Average Envelopes is straightforward. First, choose a simple moving average or exponential moving average. Simple moving averages weight each data point (price) equally. Exponential moving averages put more weight on recent prices and have less lag. Second, select the number of time periods for the moving average. Third, set the percentage for the envelopes. A 20-day moving average with a 2.5% envelope would show the following two lines:

{% code overflow="wrap" %}

```
Upper Envelope: 20-day SMA + (20-day SMA x .025)
Lower Envelope: 20-day SMA - (20-day SMA x .025)
```

{% endcode %}

<figure><img src="/files/Hd9itUfRuiH9kAVM2sAm" alt=""><figcaption></figcaption></figure>

The chart above shows IBM with 20-day SMA envelopes set at 2.5% (blue). Note that the 20-day SMA (red) was added to this SharpChart for reference. Notice how the envelopes move parallel with the 20-day SMA. They remain a constant 2.5% above and below the moving average.

### Adjusting the Settings <a href="#adjusting_the_settings" id="adjusting_the_settings"></a>

The parameters for the Moving Average Envelopes depend on your trading/investing objectives and the characteristics of the security involved. Traders will likely use shorter (faster) moving averages and relatively tight envelopes. Investors will likely prefer longer (slower) moving averages with wider envelopes.

A security's volatility will also influence the parameters. Bollinger Bands and Keltner Channels have built-in mechanisms that automatically adjust to a security's volatility. [Bollinger Bands](/table-of-contents/technical-indicators-and-overlays/technical-overlays/bollinger-bands.md) use the standard deviation to set bandwidth. [Keltner Channels](/table-of-contents/technical-indicators-and-overlays/technical-overlays/keltner-channels.md) use the Average True Range (ATR) to set channel width. These automatically adjust for volatility. Chartists must independently account for volatility when setting the Moving Average Envelopes. Securities with high volatility will require wider bands to encompass most price action. Securities with low volatility can use narrower bands.

<figure><img src="/files/lPuVwsnFB9mNruX70HYD" alt=""><figcaption></figcaption></figure>

In choosing the right parameters, it often helps to overlay a few different Moving Average Envelopes and compare. The chart above shows the S\&P 500 ETF with three Moving Average Envelopes based on the 20-day SMA. The 2.5% envelopes (red) were touched several times, the 5% envelopes (green) were only touched during the July surge. The 10% envelopes (pink) were never touched, which means this band is too wide. A medium-term trader might use the 5% envelopes, while a short-term trader could use the 2.5% envelopes.

<figure><img src="/files/SWTGZU5IoQ7Bw3mnhjzF" alt=""><figcaption></figcaption></figure>

Stock indexes and ETFs require tighter envelopes because they are typically less volatile than individual stocks. The Alcoa chart has the same Moving Average Envelopes as the SPY chart. However, notice that Alcoa breached the 10% envelopes numerous times because it is more volatile.

***

## Interpreting Moving Average Envelopes <a href="#interpreting_moving_average_envelopes" id="interpreting_moving_average_envelopes"></a>

Indicators based on channels, bands and envelopes are designed to encompass most price action. Therefore, moves above or below the envelopes warrant attention. Trends often start with strong moves in one direction or another. A surge above the upper envelope shows extraordinary strength, while a plunge below the lower envelope shows extraordinary weakness. Such strong moves can signal the end of one trend and the beginning of another.

With a moving average as its foundation, Moving Average Envelopes are a natural trend following indicator. As with moving averages, the envelopes will lag price action. The direction of the moving average dictates the direction of the channel. In general, a downtrend is present when the channel moves lower, while an uptrend exists when the channel moves higher. The trend is flat when the channel moves sideways.

Sometimes a strong trend does not take hold after an envelope break and prices move into a trading range. Such trading ranges are marked by a relatively flat moving average. The envelopes can then be used to identify overbought and oversold levels for trading purposes. A move above the upper envelope denotes an overbought situation, while a move below the lower envelope marks an oversold condition.

{% hint style="info" %}
**Learn More.** [Moving Averages](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md)
{% endhint %}

### Trend Identification <a href="#trend_identification" id="trend_identification"></a>

Moving Average Envelopes can be used to identify strong moves that signal the start of an extended trend. The trick, as always, is picking the correct parameters, which takes practice, trial and error. The chart below shows Dow Chemical (DOW) with the Moving Average Envelopes (20,10). Closing prices are used because moving averages are calculated with closing prices. Some chartists prefer bars or candlesticks to utilize the intraday day high and low. Notice how DOW surged above the upper envelope in mid-July and continued moving above this envelope until early August. This shows extraordinary strength. Also, note that the Moving Average Envelopes turned up and followed the advance. After a move from 14 to 23, the stock was clearly overbought. However, this move established a strong precedent that marked the beginning of an extended trend.

<figure><img src="/files/JIzatlcrHxhUNGSca1Rx" alt=""><figcaption></figcaption></figure>

With DOW becoming overbought soon after establishing its uptrend, it was time to wait for a playable pullback. Traders can look for pullbacks with basic chart analysis or with indicators. Pullbacks often come in the form of falling flags or wedges. DOW formed a picture perfect falling flag in August and broke resistance in September. Another flag formed in late October with a breakout in November. After the November surge, the stock pulled back with a five-week flag into December. The Commodity Channel Index (CCI) is shown in the indicator window. Moves below -100 show oversold readings. When the bigger trend is up, oversold readings can be used to identify pullbacks to improve the risk-reward profile for a trade. Momentum turns bullish again when CCI moves back into positive territory (green dotted lines).

The inverse logic can be applied for a downtrend. A strong move below the lower envelope signals extraordinary weakness that can foreshadow an extended downtrend. The chart below shows International Game Tech (IGT) breaking below the 10% envelope to establish a downtrend in late October 2009. Because the stock was quite oversold after this sharp decline, it would have been prudent to wait for a bounce. We can then use basic price analysis or another momentum indicator to identify bounces.

<figure><img src="/files/TqZOlbifzte0ED7dBMWp" alt=""><figcaption></figcaption></figure>

The indicator window shows the Stochastic Oscillator being used to identify overbought bounces. A move above 80 is considered overbought. Once above 80, chartists can then look for a chart signal or a move back below 80 to signal a downturn (red dotted lines). The first signal was confirmed with a support break. The second signal resulted in a whipsaw (loss) because the stock moved above 20 a few weeks later. The third signal was confirmed with a trend line break that resulted in a rather sharp decline.

### Overbought/Oversold <a href="#overbought_oversold" id="overbought_oversold"></a>

Moving Average Envelopes are actually quite similar to the Percent Price Oscillator (PPO), a momentum oscillator which is often used to identify overbought and oversold levels. Moving Average Envelopes tell us when a security is trading a certain percentage above or below a moving average, while the PPO shows the percentage difference between a short EMA and a longer EMA.

<figure><img src="/files/XwULKfjvpIzFmNLhl1gS" alt=""><figcaption></figcaption></figure>

In the example chart above, we can see that the PPO (1,20), which shows the difference between a 1-day EMA (essentially the close) and a 20-day EMA, is giving the exact same signals as the 20-day EMA Envelopes. Notice that prices move above the 2.5% envelope when PPO moves above 2.5% (yellow shading); and prices move below the -2.5% envelope when PPO moves below -2.5% (orange shading).

These PPO moves above or below a specified threshhold can indicate overbought or oversold conditions; by extension, moves above or below the Moving Average Envelopes can be interpreted in the same way. Price moves above the upper envelope line can indicate that a security is overbought; conversely, price moves below the lower envelope line can indicate oversold conditions.

However, measuring overbought and oversold conditions is tricky. Even though one would expect an overbought stock to fall in price, securities can become overbought and remain overbought for some time during a strong uptrend. Similarly, securities in a strong downtrend can become oversold and remain oversold. In a strong uptrend, prices often move above the upper envelope and continue above this line. In fact, the upper envelope will rise as price continues above the upper envelope. Overbought moving average envelope readings can actually be a sign of strength during a strong uptrend. For this reason, **overbought and oversold readings are best used when the trend flattens**.

The following chart for Nokia has it all. The pink lines represent the Moving Average Envelopes (50,10). A 50-day simple moving average is in the middle (red). The envelopes are set 10% above and below this moving average. The chart starts with an overbought level that stayed overbought as a strong trend emerged in April-May. Price action turned choppy from June to April, which is the perfect scenario for overbought and oversold levels. Overbought levels in September and mid-March foreshadowed reversals. Similarly, oversold levels in August and late October foreshadowed advances. The chart ends with an oversold condition that remains oversold as a strong downtrend emerges.

<figure><img src="/files/CLds9IcqfYV9u3j5Etcz" alt=""><figcaption></figcaption></figure>

Overbought and oversold conditions should serve as alerts for further analysis. Overbought levels should be confirmed with chart resistance. Chartists can also look for bearish patterns to reinforce reversal potential at overbought levels. Similarly, oversold levels should be confirmed with chart support. Chartist can also look for bullish patterns to reinforce reversal potential at oversold levels.

{% hint style="info" %}
**Learn More.** [Percent Price Oscillator (PPO)](/table-of-contents/technical-indicators-and-overlays/technical-indicators/percentage-price-oscillator-ppo.md)
{% endhint %}

## Conclusion <a href="#conclusion" id="conclusion"></a>

Moving Average Envelopes are mostly used as a trend following indicator, but can also be used to identify overbought and oversold conditions. After a consolidation period, a strong envelope break can signal the start of an extended trend. Once an uptrend is identified, chartists can turn to momentum indicators and other techniques to identify oversold readers and pullbacks within that trend. Overbought conditions and bounces can be used as selling opportunities within a bigger downtrend.

In the absence of a strong trend, the Moving Average Envelopes can be used like the Percent Price Oscillator. Moves above the upper envelope signal overbought readings, while moves below the lower envelope signal oversold readings. It is also important to incorporate other aspects of technical analysis to confirm overbought and oversold readings. Resistance and bearish reversal patterns can be used to corroborate overbought readings, while support and bullish reversal patterns can be used to affirm oversold conditions.

***

## Charting with Moving Average Envelopes <a href="#charting_with_moving_average_envelopes" id="charting_with_moving_average_envelopes"></a>

Moving Average Envelopes can be added to SharpCharts and ACP Charts.

### Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

<figure><img src="/files/wY2054f72vR9lTVpK0uT" alt="Chart from StockCharts.com displaying moving average envelopes"><figcaption><p>Chart displaying Moving Average Envelopes in SharpCharts.</p></figcaption></figure>

[Click here for a live version of this chart.](https://stockcharts.com/sc3/ui/?s=GE\&p=D\&b=5\&g=0\&id=p81554262635)

Moving Average Envelopes can be found in SharpCharts as a price overlay. As with a moving average, the envelopes should be shown on top of a price plot. When you select the indicator from the dropdown box, the default setting will appear in the parameters window (20,2.5). “SMA Envelopes” are based on a simple moving average. “EMA Envelopes” are based on an exponential moving average. The first number (20) sets the periods for the moving average. The second number (2.5) sets the percentage offset. Users can change the parameters to suit their charting needs. The corresponding moving average can be added as a separate overlay, as in the example chart above.

<figure><img src="/files/SJyHY7o6viSSBc40XX7s" alt="SharpCharts settings for moving average envelopes"><figcaption><p>SharpChart settings for Moving Average Envelopes.</p></figcaption></figure>

{% hint style="info" %}
**Learn More.** For more details on the parameters used to configure Moving Average Envelope overlays, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#sma_envelopes-1) in the Support Center.
{% endhint %}

### Using with StockChartsACP <a href="#using_with_stockchartsacp" id="using_with_stockchartsacp"></a>

Moving Average Envelopes overlays based on either SMAs or EMAs can be added from the Chart Settings panel for your StockChartsACP chart. They are listed as “EMA Envelopes” and “SMA Envelopes” in the panel. Both types of Moving Average Envelopes can be overlaid on the security's price plot or an indicator panel.

<figure><img src="/files/m6u4ZF2uVbESMsUKBsTS" alt="Chart from StockChartsACP with moving average envelopes overlaid on price chart"><figcaption><p>Moving Averages Envelopes overlaid on a price chart in StockChartsACP.</p></figcaption></figure>

***

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line">[Click here for a live version of this chart.](https://schrts.co/VqjedzIe)

***

By default, the overlay uses a 20-period SMA or EMA and sets the bands 2.5 standard deviations above or below the moving average. These parameters can be adjusted to meet your technical analysis needs.

## Scanning for Moving Average Envelopes <a href="#scanning_for_moving_average_envelopes" id="scanning_for_moving_average_envelopes"></a>

StockCharts members can screen for stocks based on Moving Average Envelope values. Below are some example scans that can be used for MA Envelope-based signals. Copy and paste the scan text into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when a Moving Average Envelope-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can also be used as a starting point for setting up alerts. Copy and paste the scan text into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-al/al).

### Oversold after Break above Upper Envelope <a href="#oversold_after_break_above_upper_envelope" id="oversold_after_break_above_upper_envelope"></a>

This scan looks for stocks that broke above their upper exponential Moving Average Envelope (50,10) twenty days ago to affirm or establish an uptrend. The current 10-period CCI is below -100 to indicate a short-term oversold condition.

{% code overflow="wrap" %}

```
[type = stock] AND [country = US] 
AND [SMA(20,Volume) > 40000] 
AND [SMA(60,Close) > 10] 

AND [20 days ago Close > 20 days ago Upper MA Env(50,10.0,Close)] 
AND [CCI(10) < -100]
```

{% endcode %}

### Overbought after Break below Lower Envelope <a href="#overbought_after_break_below_lower_envelope" id="overbought_after_break_below_lower_envelope"></a>

This scan looks for stocks that broke below their lower exponential Moving Average Envelope (50,10) twenty days ago to affirm or establish a downtrend. The current 10-period CCI is above +100 to indicate a short-term overbought condition.

{% code overflow="wrap" %}

```
[type = stock] AND [country = US] 
AND [SMA(20,Volume) > 40000] 
AND [SMA(60,Close) > 10] 

AND [20 days ago Close < 20 days ago Lower MA Env(50,10.0,Close)] 
AND [CCI(10) > 100]
```

{% endcode %}

{% hint style="info" %}
**Learn More.** For more details on the scan syntax for Moving Average Envelope scans, please see our [Scanning Indicator Reference](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-average-envelopes.md) in the Support Center.
{% endhint %}

## Additional Resources <a href="#additional_resources" id="additional_resources"></a>

### Recommended Books <a href="#recommended_books" id="recommended_books"></a>

Even though Moving Average Envelopes are not used specifically in Thomas Carr's [*Trend Trading for a Living*](https://a.co/d/3FNuqiR), the book shows traders how to trade in the direction of the underlying trend. Carr also shows readers how to configure a bullish and bearish watch list from which to set your entry and exit prices.

Michael Covel's [*Trend Following*](https://a.co/d/1dpMk5k) introduces the fundamental concepts and techniques for a variety of trend following systems. Covel shows why market prices contain all available information, and readers will learn how to interpret price movements and profit from trend following.

| <p><a href="https://a.co/d/3FNuqiR"><strong>Trend Trading for a Living</strong></a><br>Thomas Carr</p> | <p><strong>Trend Following</strong><br>Michael Covel</p> |
| ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-average-envelopes.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
