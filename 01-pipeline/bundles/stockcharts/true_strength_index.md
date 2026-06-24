> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/true-strength-index.md).

# True Strength Index

## What Is the True Strength Index?

Developed by William Blau and introduced in *Stocks & Commodities Magazine*, the True Strength Index (TSI) is a momentum oscillator based on a double smoothing of price changes. Even though several steps are needed for calculation, the indicator is actually pretty straightforward. By smoothing price changes, TSI captures the ebbs and flows of price action with a steadier line that filters out the noise. As with most momentum oscillators, chartists can derive signals from overbought/oversold readings, centerline crossovers, bullish/bearish divergences and signal line crossovers.

## Calculating True Strengh Index <a href="#calculation" id="calculation"></a>

The True Strength Index (TSI) can be divided into three parts: the double smoothed price change, the double smoothed absolute price change and the TSI formula. First, calculate the price change from one period to the next. Second, calculate a 25-period EMA of this price change. Third, calculate a 13-period EMA of this 25-period EMA to create a double smoothing. The same double smoothing technique is used for the absolute price change. After these initial calculations, divide the double smoothed price change by the absolute double smoothed price change and multiply by 100 to move the decimal two places.

<figure><img src="/files/MvUfKZkqFo3ySH4yTc77" alt=""><figcaption><p>Chart 1</p></figcaption></figure>

```
Double Smoothed PC
------------------
PC = Current Price minus Prior Price
First Smoothing = 25-period EMA of PC
Second Smoothing = 13-period EMA of 25-period EMA of PC

Double Smoothed Absolute PC
---------------------------
Absolute Price Change |PC| = Absolute Value of Current Price minus Prior Price
First Smoothing = 25-period EMA of |PC|
Second Smoothing = 13-period EMA of 25-period EMA of |PC|

TSI = 100 x (Double Smoothed PC / Double Smoothed Absolute PC)
```

The first part, which is the double smoothed price change, sets the positive or negative tone for TSI. The indicator is negative when the double smoothed price change is negative and positive when it is positive. The double smoothed absolute price change normalizes the indicator and limits the range of the ensuing oscillator. In other words, this indicator measures the double smoothed price change relative to the double smoothed absolute price change. A string of large positive price changes results in relatively high positive readings, signaling strong upside momentum. A string of large negative price changes pushes TSI deep into negative territory.

The table above comes from an Excel spreadsheet. Note that [exponential moving averages](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) are used in the calculations. These start with a simple moving average and then use a multiplier for calculation, which means additional historical data is needed to reach true values.

Click below to download a spreadsheet example.&#x20;

{% file src="/files/TEkSHBashKHMmswdxkyn" %}

## Interpreting the True Strength Index <a href="#interpretation" id="interpretation"></a>

The True Strength Index (TSI) is an oscillator that fluctuates between positive and negative territory. As with many momentum oscillators, the centerline defines the overall bias. The bulls have the momentum edge when TSI is positive and the bears have the edge when it's negative. As with MACD, a signal line can be applied to identify upturns and downturns. Signal line crossovers are, however, quite frequent and require further filtering with other techniques. Chartists can also look for bullish and bearish divergences to anticipate trend reversals; however, keep in mind that divergences can be misleading in a strong trend.

TSI is somewhat unique because it tracks the underlying price quite well. In other words, the oscillator can capture a sustained move in one direction or the other. The peaks and troughs in the oscillator often match the peaks and troughs in price. In this regard, chartists can draw trend lines and mark support/resistance levels using TSI. Line breaks can then be used to generate signals.

## Center Line Crossover <a href="#center_line_crossover" id="center_line_crossover"></a>

The centerline crossover is the purest signal. The double smoothed momentum of price changes is positive when TSI is above zero and negative when below zero. Prices are generally rising when TSI is positive and falling when TSI is negative. The example below shows Nike (NKE) turning bullish in September 2011 as TSI moved into positive territory (green line). The stock remained bullish as the uptrend extended into the spring of 2012. Nike turned bearish when TSI turned negative and the stock broke support.

<figure><img src="/files/pnXzWOpdkAKyJdejTS34" alt=""><figcaption><p>Chart 2</p></figcaption></figure>

## Trend Lines <a href="#trend_lines" id="trend_lines"></a>

TSI often produces support and resistance levels that chartists can use to identify breakouts or breakdowns. The example below shows Citigroup (C) with TSI establishing support in March. The indicator broke support in early April and this breakdown foreshadowed a significant decline into May. TSI then rebounded in June and formed a flat consolidation into July. This consolidation resembled a falling flag and TSI broke above the trend line in late July. This breakout preceded further strength into August.

<figure><img src="/files/lo5BrMFyyPRoKfUqfjmW" alt=""><figcaption><p>Chart 3</p></figcaption></figure>

## Overbought/Oversold <a href="#overbought_oversold" id="overbought_oversold"></a>

Overbought and oversold levels for the True Strength Index vary based on a security's volatility and the indicator's period settings. The TSI range will be smaller for stocks with low volatility, such as utilities. The TSI range will be larger for stocks with high volatility, such as biotechs. Using shorter time periods for the smoothing will result in a wider range and choppier indicator line. Longer time periods will result in a smaller range and smoother line. It's the classic technical analysis tradeoff—shorter periods provide quicker signals and less lag but at the cost of more whipsaws and false signals. Longer periods reduce the whipsaws, but the signals come with more lag and a less favorable reward-to-risk ratio.

The chart below shows the Nasdaq 100 ETF (QQQ) with TSI using two different timeframes. The upper indicator window shows TSI (40,20,7) fluctuating between -20 and +44 with 20/-20 marking overbought/oversold. The lower window shows TSI (13,7,7) fluctuating between +78 and -69 with 50/-50 marking overbought/oversold.&#x20;

<figure><img src="/files/qoQsL2ZOAYKJFP5xZ3nv" alt=""><figcaption><p>TRUE STRENGTH INDEX USING TWO TIMEFRAMES. </p></figcaption></figure>

Notice how TSI in the lower window is much more volatile than TSI in the upper window. Also, notice that the more sensitive TSI produced two oversold readings and four overbought readings (blue arrows). Overbought and oversold are not signals of an impending reversal. They simply suggest that prices have come too far too fast. Chartists must wait for a confirming signal to suggest an actual reversal. The blue lines mark support and resistance using trend lines, peaks or troughs. Once an overbought or oversold reading occurs, chartists can use these lines to define a price reversal. This will not illuminate whipsaws, but it will reduce bad signals.

## Signal Line Crossovers <a href="#signal_line_crossovers" id="signal_line_crossovers"></a>

The last parameter in the TSI setting is the signal line, which is simply an exponential moving average of TSI. Signal line crossovers are by far the most common signals, meaning there will be good, bad and ugly signals. In an effort to reduce signals and noise, chartists should consider increasing the settings for TSI or the price chart settings. The example below shows TSI(40,20,10) using a weekly chart. This means the signal line is a 10-period EMA of TSI. There was no shortage of signals on this chart as TSI crossed the signal line at least 12 times from April 2007 to July 2012.

<figure><img src="/files/eqnmcqaN72Ccxc9R3q9M" alt=""><figcaption><p>Chart 5</p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The True Strength Index (TSI) is a unique indicator based on double smoothed price changes. Price change represents momentum in its truest form. The double smoothing with two exponential moving averages reduces the noise and produces an oscillator that tracks price quite well. In addition to the usual oscillator signals, chartists can often draw trend lines, support lines and resistance lines directly on TSI. These can then be used to generate signals based on breakouts and breakdowns. As with all indicators, TSI signals should be confirmed with other indicators and analysis techniques.

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The True Strength Index (TSI) is available as an indicator for SharpCharts. Once selected, users can place the indicator above, below or behind the underlying price plot. Placing TSI directly behind the price plot accentuates the movements relative to the price action of the underlying security. Users can apply “advanced options” to add horizontal lines for setting overbought and oversold levels. Adjusting the numbers in the Parameters box will change the settings. [Click here](https://stockcharts.com/sc3/ui/?s=$COMPQ\&p=D\&yr=0\&mn=6\&dy=0\&id=p28704616394\&a=276577901) for a live example of TSI in action.

<figure><img src="/files/a3tYF218PJgw2EYjgxLv" alt=""><figcaption><p>Chart 6</p></figcaption></figure>

<figure><img src="/files/TgmLOd73QoMu4HSlKCD3" alt=""><figcaption><p>Chart 7</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Bullish TSI Signal Line Cross <a href="#bullish_tsi_signal_line_cross" id="bullish_tsi_signal_line_cross"></a>

This scan reveals stocks where TSI is in positive territory. A bullish signal is triggered when TSI crosses above its signal line.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [TSI(40,20,10) > 0]
AND [TSI(40,20,10) x TSI Signal(40,20,10)]
```

### Bearish TSI Signal Line Cross <a href="#bearish_tsi_signal_line_cross" id="bearish_tsi_signal_line_cross"></a>

This scan reveals stocks where TSI is in negative territory. A bearish signal is triggered when TSI crosses below its signal line.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [TSI(40,20,10) < 0]
AND [TSI Signal(40,20,10) x TSI(40,20,10)]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax to use for TSI scans, please see our [Scan Syntax Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference) in the Support Center.
{% endhint %}

## Further Study <a href="#further_study" id="further_study"></a>

John Murphy's [*Technical Analysis of the Financial Markets*](https://a.co/d/598OGRx) has a chapter devoted to momentum oscillators and their various uses. Murphy covers the pros and cons as well as some examples specific to Rate-of-Change. Martin Pring's [*Technical Analysis Explained*](https://a.co/d/2ssrqwM) shows the basics of momentum indicators by covering divergences, crossovers and other signals. There are two more chapters covering specific momentum indicators, each containing plenty of examples.

| <p><a href="https://a.co/d/598OGRx"><strong>Technical Analysis of the Financial Markets</strong></a><br>John J. Murphy</p> | <p><a href="https://a.co/d/2ssrqwM"><strong>Technical Analysis Explained by Martin Pring</strong></a><br>Martin Pring</p> |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/true-strength-index.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
