> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/stochrsi.md).

# StochRSI

## What Is the StochRSI? <a href="#introduction" id="introduction"></a>

Developed by Tushar Chande and Stanley Kroll, StochRSI [is an oscillator](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#oscillator_types) that measures [the level of RSI](/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi.md) relative to its high-low range over a set time period. StochRSI applies the Stochastics formula to RSI values, rather than price values, making it an indicator of an indicator. The result is an oscillator that fluctuates between 0 and 1.

In their 1994 book, *The New Technical Trader*, Chande and Kroll explain that RSI can oscillate between 80 and 20 for extended periods without reaching extreme levels. Notice that 80 and 20 are used for overbought and oversold instead of the more traditional 70 and 30. Traders looking to enter a stock based on an overbought or oversold reading in RSI might find themselves continuously on the sidelines. Chande and Kroll developed StochRSI to increase sensitivity and generate more overbought/oversold signals.

## How To Calculate StochRSI <a href="#calculation" id="calculation"></a>

```
StochRSI = (RSI - Lowest Low RSI) / (Highest High RSI - Lowest Low RSI)
```

StochRSI measures the value of RSI relative to its high/low range over a set number of periods. The number of periods used to calculate StochRSI is transferred to RSI in the formula. For example, 14-day StochRSI would use the current value of 14-day RSI and the 14-day high-low range for 14-day RSI.

* 14-day StochRSI equals 0 when RSI is at its lowest point for 14 days.
* 14-day StochRSI equals 1 when RSI is at its highest point for 14 days.
* 14-day StochRSI equals .5 when RSI is in the middle of its 14-day high-low range.
* 14-day StochRSI equals .2 when RSI is near the low of its 14-day high-low range.
* 14-day StochRSI equals .80 when RSI is near the high of its 14-day high-low range.

<figure><img src="/files/KIQj6uHqrHU5BGq97Qfz" alt=""><figcaption><p>RSI - Spreadsheet 1</p></figcaption></figure>

Click below for an Excel spreadsheet showing the beginning of a StockRSI calculation.&#x20;

{% file src="/files/zlVcUohRJUXSMXn69imi" %}

## Interpretation <a href="#interpretation" id="interpretation"></a>

It is important to remember that StochRSI is an indicator of an indicator, which makes it the second derivative of price. This means it is two steps (formulas) removed from the price of the underlying security. Price has undergone two changes to become StochRSI. Converting prices to RSI is one change. Converting RSI to the Stochastic Oscillator is the second change. This is why the end product (StochRSI) looks much different than the original (price).

<figure><img src="/files/KXURKvprHEKLZRiLaWyw" alt=""><figcaption><p>StochRSI - Chart 1</p></figcaption></figure>

StochRSI has characteristics similar to most bound momentum oscillators. First, it can be used to identify overbought or oversold conditions. A move above .80 is considered overbought, while a move below .20 is considered oversold. Second, it can be used to identify the short-term trend. As a bound oscillator, the centerline is at .50. StochRSI reflects an uptrend when consistently above .50 and a downtrend when consistently below .50. Because this indicator is quite volatile, some smoothing with a moving average can help for short-term trend identification.

## Overbought/Oversold <a href="#overbought_oversold" id="overbought_oversold"></a>

Trend identification is the key to successfully choosing between overbought and oversold levels. It is essential to look for oversold conditions when the bigger trend is up and overbought conditions when the bigger trend is down. In other words, look for trades in the direction of the bigger trend. 14-day StochRSI would be considered a short-term indicator. Therefore, it is important to identify the medium-term trend when looking for overbought and oversold conditions.

Chart 2 shows Boeing in a medium-term uptrend with StochRSI(14) becoming oversold in January and February. First, the medium-term was deemed up because the 10-day SMA was above the 60-day SMA. With an uptrend in place, oversold conditions were preferred to overbought conditions. StochRSI became oversold at least four times from December to February. For what it's worth, 14-day RSI did not become oversold during this timeframe because it is less sensitive. However, oversold is not the same thing as bullish; oversold conditions instead serve as a warning to watch for a bounce. A catalyst is still needed to solidify the low and signal an actual upturn. In this example, chartists could look for prices to break above the 10-day SMA or for StochRSI to break above .50, its centerline.

<figure><img src="/files/vwSTrmfQZpQo7lAL61to" alt=""><figcaption><p>StochRSI - Chart 2</p></figcaption></figure>

Chart 3 shows Flour Corp (FLR) within a downtrend and StochRSI registering overbought readings. First, the medium-term trend is down because the 10-day SMA is below the 60-day SMA. This means oversold readings are ignored and overbought readings become the focus. StochRSI moved above .80 in mid-October and early November (red arrows). These overbought readings suggested that the oversold bounce could end soon. Confirmation came when StochRSI moved back below .50 (red dotted lines). Chartists could also look for the stock to break back below its 10-day SMA to signal a short-term downturn.

<figure><img src="/files/T5DvH00rfPYuImLODwV5" alt=""><figcaption><p>StochRSI - Chart 3</p></figcaption></figure>

## Trend Identification <a href="#trend_identification" id="trend_identification"></a>

StochRSI is quite a volatile oscillator that frequently becomes overbought and oversold. For short-term trend identification, it can help to lengthen the calculation period and apply a short moving average to smooth the data. Momentum favors rising prices when the 10-day SMA of StochRSI is above .50 and falling prices when below .50. Chart 4 shows Chevron (CVX) with 20-day StochRSI and a 5-day SMA of the indicator. The 5-day SMA moved above .50 in mid-February just after the stock gapped higher. The gap and moving average cross above .50 were short-term bullish signals. A falling flag/wedge formed in late February. Notice how CVX found support in the gap zone. The uptrend continued with a flag/wedge breakout and the stock advanced above 80. Even though StochRSI dipped below .50 in late March, the 5-day SMA held above .50 to keep the uptrend alive until late April. This short-term signal turned into a two-month uptrend.

<figure><img src="/files/BrilBQpzbYUbzH5t9Wbn" alt=""><figcaption><p>StochRSI - Chart 4</p></figcaption></figure>

Unfortunately, not all signals are this picture perfect. There will be whipsaws, even when using a 5-day SMA with 20-day StochRSI. For example, a consolidation during a trend can cause the 5-day SMA of StochRSI to gyrate above/below the .50 line before continuing or reversing the trend. Chart 5 shows Yahoo! with 20-day StochRSI and its 5-day SMA for smoothing. The moving average broke above .50 in mid-February to turn momentum bullish. This was followed by a resistance breakout for Yahoo! on the first day of March. As the stock consolidated with a falling channel in late March, the 5-day SMA for StochRSI(20) dipped below .50 twice (red oval). These dips proved short-lived as the stock broke channel resistance and StochRSI moved above .80 to show strength. The trend did not end until the 5-day SMA moved below .50 AND Yahoo! gapped down.

<figure><img src="/files/5oadVjysLVhQoFDgHasd" alt=""><figcaption><p>StochRSI - Chart 5</p></figcaption></figure>

Chart 6 shows Yahoo! with a bearish signal from StochRSI that did not take hold right away. The 5-day SMA for 20-day StochRSI moved below .50 to turn momentum bearish the second week of October. Yahoo! broke support for confirmation, but this break did not hold as the stock surged to 18 a few days later. The immediate recovery and bounce back above 17 formed a bear trap. Even though Yahoo! surged, the 5-day SMA for StochRSI remained below .50 and momentum did not confirm. The subsequent gap above 17.50 turned out to be an exhaustion gap as Yahoo! failed at resistance (18), filled the gap, broke support again and moved sharply lower into November. Talk about volatility.

<figure><img src="/files/zcBN56woRLpYWlN9r0NM" alt=""><figcaption><p>StochRSI - Chart 1</p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

StochRSI is like RSI on steroids. RSI produces relatively fewer signals and StochRSI dramatically increases the signal count. There will be more overbought/oversold readings, more centerline crosses, more good signals and more bad signals. Speed comes at a price. This means it is important to use StochRSI with other aspects of technical analysis for confirmation. The examples above use gaps, support/resistance breaks, and price patterns to confirm StochRSI signals. Chartists can also employ other complementary indicators, such as On Balance Volume (OBV) or the Accumulation Distribution Line. These volume-based indicators do not overlap with momentum oscillators. Chartists should also experiment with various settings and learn the nuances of StochRSI before using it in the real world.

***

## Using With SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The StochRSI indicator can be charted as an indicator using the SharpCharts tool. The “parameters” value specifies the number of periods used in the calculation (default is 14). The indicator can be set above, below or behind the underlying price plot. A moving average can be applied by clicking the advanced options arrow (green) and adding an overlay. [Click here](https://stockcharts.com/sc3/ui/?s=QQQ\&p=D\&yr=0\&mn=5\&dy=0\&id=p80628063848\&listNum=30\&a=203042536) to see a live example of StochRSI.

<figure><img src="/files/LBWi27aSLB9p39dvKmdX" alt=""><figcaption><p>StochRSI - SharpCharts</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Oversold StochRSI in medium-term uptrend <a href="#oversold_stochrsi_in_medium-term_uptrend" id="oversold_stochrsi_in_medium-term_uptrend"></a>

This scan starts with stocks that have an average price of $10 or greater over the last three months and average volume greater than 40,000. The first filter selects securities within a medium-term uptrend by looking for those where the 10-day SMA is greater than the 60-day SMA. The screen then selects stocks that are short-term oversold by looking for those trading below their 10-day SMA and with StochRSI(14) below .10. This scan often returns many stocks and further refinement may be needed.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 10]

AND [Daily SMA(10,Daily Close) > Daily SMA(60,Daily Close)]
AND [Daily Stoch RSI(14) < 0.1]
AND [Daily Close < Daily SMA(10,Daily Close)]
```

### Overbought StochRSI within a medium-term downtrend <a href="#overbought_stochrsi_within_a_medium-term_downtrend" id="overbought_stochrsi_within_a_medium-term_downtrend"></a>

This scan starts with stocks that have an average price of $10 or greater over the last three months and average volume greater than 40,000. The first filter selects securities within a medium-term downtrend by looking for those where the 10-day SMA is less than the 60-day SMA. The screen then selects stocks that are short-term overbought by looking for those trading above their 10-day SMA and with StochRSI(14) above .90. This scan often returns many stocks and further refinement may be needed.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 10]

AND [Daily SMA(10,Daily Close) < Daily SMA(60,Daily Close)]
AND [Daily Stoch RSI(14) > 0.9]
AND [Daily Close > Daily SMA(10,Daily Close)]
```

For more details on the syntax to use for StochRSI scans, please see our [Scan Syntax Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#stochastic_rsi_stoch_rsi) in the Support Center.

## Further Study <a href="#further_study" id="further_study"></a>

Constance Brown's [*Technical Analysis for the Trading Professional*](https://a.co/d/0qv03l0) takes our exploration of RSI to the next level with bull market and bear market ranges, positive and negative reversals, and projections based on RSI. Some methods of Andrew Cardwell, her RSI mentor, are also explained and refined in this book.

| <p><a href="https://a.co/d/0qv03l0"><strong>Technical Analysis for the Trading Professional</strong></a><br>Constance Brown</p> |
| ------------------------------------------------------------------------------------------------------------------------------- |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/stochrsi.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
