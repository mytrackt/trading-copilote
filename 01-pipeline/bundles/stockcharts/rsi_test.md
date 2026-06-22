> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi.md).

# Relative Strength Index (RSI)

## What Is the Relative Strength Index (RSI)? <a href="#what_is_the_relative_strength_index_rsi" id="what_is_the_relative_strength_index_rsi"></a>

The RSI, a momentum oscillator developed by J. Welles Wilder, measures the speed and change of price movements. The RSI moves up and down (oscillates) between zero and 100. When the RSI is above 70, it generally indicates overbought conditions; when the RSI is below 30, it indicates oversold conditions. The RSI also generates trading signals via divergences, failure swings, and centerline crossovers. You could also use the RSI to identify the general trend.

<figure><img src="/files/R5qSHPrhrx3MVf1obaqS" alt=""><figcaption></figcaption></figure>

RSI is a popular [momentum indicator](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#momentum_oscillators) that has been featured in a number of articles, interviews, and books over the years. In particular, Constance Brown's book, *Technical Analysis for the Trading Professional*, features the concept of bull and bear market ranges for RSI. Andrew Cardwell, Brown's RSI mentor, introduced positive and negative reversals for RSI and turned the notion of divergence, literally and figuratively, on its head.

Wilder features RSI in his 1978 book, *New Concepts in Technical Trading Systems*. This book also includes the Parabolic SAR, Average True Range, and the Directional Movement Concept (ADX). Despite being developed before the computer age, Wilder's indicators have stood the test of time and continue to be applied by chart analysts.

***

## RSI Calculation <a href="#calculating_the_rsi" id="calculating_the_rsi"></a>

There are three basic components in the RSI—**RS**, **Average Gain**, and **Average Loss**. This RSI calculation is based on 14 periods, the default Wilder suggested in his book. Losses are expressed as positive values, not negative values.

```
                  100
    RSI = 100 - --------
                 1 + RS

    RS = Average Gain / Average Loss
```

The first calculations for average gain and average loss are simple 14-period averages:

* First Average Gain = Sum of Gains over the past 14 periods / 14.
* First Average Loss = Sum of Losses over the past 14 periods / 14.

The second and subsequent, calculations are based on the prior averages and the current gain loss:

* Average Gain = \[(previous Average Gain) x 13 + current Gain] / 14.
* Average Loss = \[(previous Average Loss) x 13 + current Loss] / 14.

Taking the prior value plus the current value is a smoothing technique similar to calculating an exponential moving average. This also means RSI values become more accurate as the calculation period extends. SharpCharts uses at least 250 data points before the starting date of any chart (assuming that much data exists) when calculating its RSI values. A formula will need at least 250 data points to replicate our RSI numbers.

Wilder's formula normalizes RS and turns it into an oscillator that fluctuates between zero and 100. The normalization step makes it easier to identify extremes because RSI is range-bound. When the Average Gain equals zero, RSI is zero. So, if you're using a 14-period RSI, a zero RSI value means prices moved lower in all 14 periods. There were no gains to measure. RSI is 100 when the Average Loss equals zero. This means prices moved higher in all 14 periods, and there were no losses to measure.

<figure><img src="/files/K9RR3VkSKkPUPwMFPPnP" alt=""><figcaption><p>RS vs. RSI Plots</p></figcaption></figure>

Below is an Excel spreadsheet that shows the start of an RSI calculation.

<figure><img src="/files/mVB7vpPyZ5wzezGnXlGR" alt=""><figcaption><p>RSI Calculation Example</p></figcaption></figure>

Click below to download the spreadsheet.

{% file src="/files/V3LMMrvMgsp2MbNXziRi" %}

{% hint style="warning" %}
**Note:** The smoothing process affects RSI values. RS values are smoothed after the first calculation. Average Loss equals the sum of the losses divided by 14 for the first calculation. Subsequent calculations multiply the prior value by 13, add the most recent value, and divide the total by 14. This creates a smoothing effect. The same applies to Average Gain. Because of this smoothing, RSI values may differ based on the total calculation period. 250 periods will allow for more smoothing than 30 periods, which will slightly affect RSI values. StockCharts.com goes back 250 days whenever possible. If the Average Loss equals zero, a “divide by zero” situation occurs for RS, and RSI is set to 100 by definition. Similarly, RSI equals 0 when Average Gain equals zero.
{% endhint %}

### Adjusting RSI Parameters <a href="#what_are_the_best_rsi_parameters" id="what_are_the_best_rsi_parameters"></a>

The default look-back period for RSI is 14, but you can lower it to increase sensitivity or raise it to decrease sensitivity. A 10-day RSI is more likely to reach overbought or oversold levels than a 20-day RSI. The look-back parameters also depend on a security's volatility. The 14-day RSI for a volatile stock such as Amazon (AMZN) is more likely to become overbought or oversold than a 14-day RSI for a utility company such as Duke Energy (DUK).

The traditional overbought and oversold levels can be adjusted to better fit the security or analytical requirements. Raising the overbought threshold to 80 or lowering the oversold threshold to 20 could reduce the number of overbought/oversold readings. Short-term traders sometimes use 2-period RSI to look for overbought readings above 80 and oversold readings below 20.

{% hint style="success" %}
**Cool Tip:** While many of the examples in this article use daily charts, the RSI can be added to many timeframes - daily, weekly, hourly, and minute charts. The best timeframe to use depends on your trading strategy and goals.
{% endhint %}

***

## Interpreting RSI <a href="#overbought_and_oversold_rsi_levels" id="overbought_and_oversold_rsi_levels"></a>

### Overbought and Oversold RSI Levels <a href="#overbought_and_oversold_rsi_levels" id="overbought_and_oversold_rsi_levels"></a>

Wilder considered RSI [overbought](/table-of-contents/glossary/glossary-o.md#overbought) above 70 and [oversold](/table-of-contents/glossary/glossary-o.md#oversold) below 30. The chart below shows McDonalds with a 14-day RSI. This chart features daily bars in gray with a one-day SMA in pink to highlight closing prices (as RSI is based on closing prices). Working from left to right, the stock became oversold in late July and found support around 44 (1).

Notice that the bottom **evolved** after the oversold reading. Bottoming can be a process—this stock did not bottom as soon as the oversold reading appeared. From oversold levels, RSI moved above 70 in mid-September to become overbought. Despite this overbought reading, the stock did not decline; instead, it stalled for a couple weeks and then continued higher.

Three more overbought readings occurred before the stock finally peaked in December (2). Momentum oscillators can become overbought (oversold) and remain so in a strong up (down) trend. The first three overbought readings foreshadowed consolidations. The fourth coincided with a significant peak. RSI then moved from overbought to oversold in January. The stock ultimately bottomed around 46 a few weeks later (3); the final bottom did not coincide with the initial oversold reading.

<figure><img src="/files/WteqdAojvXbFNliCWwRB" alt=""><figcaption><p>Overbought and Oversold RSI</p></figcaption></figure>

Like many momentum oscillators, **overbought and oversold readings for RSI work best when prices move sideways within a range**. The chart below shows MEMC Electronics (WFR) trading between 13.5 and 21 from April to September 2009. The stock peaked soon after RSI reached 70 and bottomed soon after the stock reached 30.

<figure><img src="/files/EPph3ooDb3EaCTKbuuLC" alt=""><figcaption><p>Overbought/Oversold RSI in a Trading Range</p></figcaption></figure>

***

### Bullish and Bearish Divergences in RSI <a href="#bullish_and_bearish_divergences_in_rsi" id="bullish_and_bearish_divergences_in_rsi"></a>

According to Wilder, divergences signal a potential reversal point because directional momentum does not confirm price. A bullish divergence occurs when the underlying security makes a lower low, and RSI forms a higher low. RSI does not confirm the lower low, and this shows strengthening momentum. A bearish divergence forms when the security records a higher high and RSI forms a lower high. RSI does not confirm the new high and this shows weakening momentum.&#x20;

The chart below shows Ebay (EBAY) with a bearish divergence in August–October. The stock moved to new highs in September–October, but RSI formed lower highs for the bearish divergence. The subsequent breakdown in mid-October confirmed weakening momentum.

<figure><img src="/files/sHzcJiTaWTFQZIbjWzGZ" alt=""><figcaption><p>RSI Divergences</p></figcaption></figure>

A bullish divergence formed in January–March. The bullish divergence formed with eBay moving to new lows in March and RSI holding above its prior low. RSI reflected less downside momentum during the February-March decline. The mid-March breakout confirmed improving momentum. Divergences tend to be more robust when they form after an overbought or oversold reading.

Before getting too excited about divergences as great trading signals, it must be noted that divergences are misleading in a strong trend. A strong uptrend can show numerous bearish divergences before a top materializes.&#x20;

Conversely, bullish divergences can appear in a strong downtrend, yet the downtrend continues. The chart below shows the SPDR S\&P 500 ETF (SPY) with three bearish divergences and a continuing uptrend. These bearish divergences may have warned of a short-term pullback, but there was clearly no major trend reversal.

<figure><img src="/files/3lCMGzjNJNLcqybo2Mz0" alt=""><figcaption><p>RSI Divergences in a strong trend</p></figcaption></figure>

***

### RSI Failure Swings <a href="#rsi_failure_swings" id="rsi_failure_swings"></a>

Wilder also considered failure swings as strong indications of an impending reversal. Failure swings are independent of price action, focusing solely on RSI for signals and ignoring the concept of divergences. A bullish failure swing forms when RSI moves below 30 (oversold), bounces above 30, pulls back, holds above 30 and then breaks its prior high. It is basically a move to oversold levels and then a higher low above oversold levels. The chart below shows Research in Motion (RIMM) with 10-day RSI forming a bullish failure swing.

<figure><img src="/files/M9ZHt9hAOr6RQGvhnnaV" alt=""><figcaption><p>Bullish RSI Failure Swing</p></figcaption></figure>

A bearish failure swing forms when RSI moves above 70, pulls back, bounces, fails to exceed 70, and then breaks its prior low. It is a move to overbought levels, followed by a lower high beneath those levels. The chart below shows Texas Instruments (TXN) with a bearish failure swing in May–June 2008.

<figure><img src="/files/IFOc1q1owdQDunlvExjd" alt=""><figcaption><p>Bearish RSI Failure Swing</p></figcaption></figure>

***

### Using RSI To Identify Trends <a href="#how_to_use_rsi_to_identify_trends" id="how_to_use_rsi_to_identify_trends"></a>

In *Technical Analysis for the Trading Professional*, Constance Brown suggests that oscillators do not travel between 0 and 100. This also happens to be the name of the first chapter. Brown identifies a bull market range and a bear market for RSI. RSI tends to fluctuate between 40 and 90 in a bull market (uptrend) with the 40–50 zones acting as support. These ranges may vary depending on RSI parameters, strength of trend and volatility of the underlying security.&#x20;

The chart below shows 14-week RSI for SPY during the bull market from 2003 until 2007. RSI surged above 70 in late 2003 and then moved into its bull market range (40–90). There was one overshoot below 40 in July 2004, but RSI held the 40–50 zone at least five times from January 2005 until October 2007 (green arrows). In fact, notice that pullbacks to this zone provided low risk entry points to participate in the uptrend.

<figure><img src="/files/7ay0ITfmXGvWLXih1Anc" alt=""><figcaption><p>Using RSI to identify an uptrend</p></figcaption></figure>

On the flip side, RSI tends to fluctuate between 10 and 60 in a bear market (downtrend) with the 50-60 zone acting as resistance. The chart below shows 14-day RSI for the US Dollar Index ($USD) during its 2009 downtrend. RSI moved to 30 in March to signal the start of a bear range. The 50–60 zone subsequently marked resistance until a breakout in December.

<figure><img src="/files/NUsNxaiLjWlZBvIyODc6" alt=""><figcaption><p>Using RSI to identify a downtrend</p></figcaption></figure>

***

### Identifying Positive and Negative Reversals With RSI <a href="#identifying_positive_and_negative_reversals_with_rsi" id="identifying_positive_and_negative_reversals_with_rsi"></a>

Andrew Cardwell developed positive and negative reversals for RSI, which are the opposite of bearish and bullish divergences. Cardwell's books are out of print, but he offers seminars detailing these methods. Cardwell's interpretation of divergences differs from Wilder's. Cardwell considered bearish divergences to be bull market phenomena. In other words, bearish divergences are more likely to form in uptrends. Similarly, bullish divergences are considered bear market phenomena and are indicative of a downtrend.

A positive reversal forms when RSI forges a lower low, and the security forms a higher low. This lower low is not at oversold levels but is usually between 30 and 50. The chart below shows MMM with a positive reversal forming in June 2009. MMM broke resistance a few weeks later, and RSI moved above 70. Despite weaker momentum with a lower low in RSI, MMM held above its prior low and showed underlying strength. In essence, price action overruled momentum.

<figure><img src="/files/Wh7iaZXjU5eJrPDgRnUJ" alt=""><figcaption><p>Identifying a positive reversal with RSI</p></figcaption></figure>

A negative reversal is the opposite of a positive reversal. RSI forms a higher high, but the security forms a lower high. Again, the higher high is usually just below overbought levels in the 50-70 area. The chart below shows Starbucks (SBUX) forming a lower high as RSI forms a higher high. Even though RSI forged a new high and momentum was strong, the price action failed to confirm as lower high formed. This negative reversal foreshadowed the big support break in late June and sharp decline.

<figure><img src="/files/IQDqCnqdwUARkaIR0FWP" alt=""><figcaption><p>Identifying a negative reversal with RSI</p></figcaption></figure>

***

## The Bottom Line <a href="#final_thoughts" id="final_thoughts"></a>

RSI is a versatile momentum oscillator that has stood the test of time. Despite changes in [volatility](/table-of-contents/glossary/glossary-v.md#volatility) and the markets, RSI remains as relevant now as it was in Wilder's days. While Wilder's original interpretations help understand the indicator, the work of Brown and Cardwell takes RSI interpretation to a new level. But adjusting to this level takes some rethinking.

Wilder considers overbought conditions ripe for a reversal, but overbought can also be a sign of strength. Bearish divergences still produce some good sell signals, but you must be careful in strong trends when bearish divergences are normal. Even though the concept of positive and negative reversals may seem to undermine Wilder's interpretation, the logic makes sense. Wilder would hardly dismiss the value of putting more emphasis on price action. Positive and negative reversals put price action of the underlying security first and the indicator second, which is how it should be. Bearish and bullish divergences place the indicator first and price action second. By emphasizing price action, the concept of positive and negative reversals challenges our thinking toward momentum oscillators.

Like all technical indicators, RSI should be used in conjunction with other tools and indicators to confirm signals and avoid potential false alarms.

***

## Charting with RSI <a href="#using_rsi_in_sharpcharts" id="using_rsi_in_sharpcharts"></a>

### Using with SharpCharts <a href="#using_rsi_in_sharpcharts" id="using_rsi_in_sharpcharts"></a>

RSI is available as an indicator for SharpCharts. Select RSI from the **Indicator** dropdown, select the **Parameter** and the position (above, below, or behind the underlying price plot). Placing RSI directly on top of the price plot accentuates the movements relative to price action of the underlying security. You can apply “advanced options” to smooth the indicator with a moving average or add a horizontal line to mark overbought or oversold levels.

[Click here for a live version of this chart.](https://stockcharts.com/sc3/ui/?s=QQQ\&id=p98665714007)

<figure><img src="/files/WqBClyS69OW2J993eto8" alt=""><figcaption><p>Using RSI on a SharpChart</p></figcaption></figure>

<figure><img src="/files/I58qcjuNco65ZdvU8zRm" alt=""><figcaption><p>RSI Settings on the SharpCharts Workbench</p></figcaption></figure>

{% hint style="info" %}
**Learn More:** For more details on the parameters used to configure RSI indicators, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#rsi) in the Support Center.
{% endhint %}

### Using with StockChartsACP

This indicator can be added from the Chart Settings panel for your StockChartsACP chart. The indicator can be positioned above, below, or behind the security's price plot.

<figure><img src="/files/ZyOb6TlYbzvJfvU1HnNf" alt=""><figcaption><p>Using RSI on an ACP chart</p></figcaption></figure>

[Click here for a live version of this chart.](https://schrts.co/ditCCjbJ)

By default, this indicator is calculated using 14 periods. This parameter can be adjusted to meet your technical analysis needs.

***

## Scanning for RSI <a href="#recommended_rsi_scans" id="recommended_rsi_scans"></a>

StockCharts members can screen for stocks based on Rate of Change values. Below are some example scans that can be used for ROC-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when a ROC-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-al/al).

### RSI Oversold in Uptrend <a href="#rsi_oversold_in_uptrend" id="rsi_oversold_in_uptrend"></a>

This scan reveals stocks that are in an uptrend with oversold RSI. First, stocks must be above their 200-day moving average to be in an overall uptrend. Second, RSI must cross below 30 to become oversold.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [Daily Close > Daily SMA(200,Daily Close)]
AND [Daily RSI(5,Daily Close) <= 30]
```

### RSI Overbought in Downtrend <a href="#rsi_overbought_in_downtrend" id="rsi_overbought_in_downtrend"></a>

This scan reveals stocks that are in a downtrend with overbought RSI turning down. First, stocks must be below their 200-day moving average to be in an overall downtrend. Second, RSI must cross above 70 to become overbought.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [Daily Close < Daily SMA(200,Daily Close)]
AND [Daily RSI(5,Daily Close) >= 70]
```

{% hint style="info" %}
**Learn More:** For more details on the syntax to use for RSI scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#relative_strength_index_rsi) in the Support Center.
{% endhint %}

## Additional Resources <a href="#further_study" id="further_study"></a>

### Recommended Books

Constance Brown's [*Technical Analysis for the Trading Professional*](https://a.co/d/ehJRi4x) takes RSI to a new level with bull market and bear market ranges, positive and negative reversals, and projections based on RSI. Some methods of Andrew Cardwell, her RSI mentor, are also explained and refined in the book.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
