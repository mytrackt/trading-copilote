> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/decisionpoint-price-momentum-oscillator-pmo.md).

# DecisionPoint Price Momentum Oscillator (PMO)

Developed by Carl Swenlin, the DecisionPoint Price Momentum Oscillator (PMO) is an oscillator based on a [Rate of Change (ROC)](/table-of-contents/technical-indicators-and-overlays/technical-indicators/rate-of-change-roc.md) calculation that is smoothed twice with exponential moving averages that use a custom smoothing process. Because the PMO is normalized, it can also be used as a relative strength tool. Stocks can thus be ranked by their PMO value as an expression of relative strength.

## Calculating the PMO <a href="#calculation" id="calculation"></a>

The DecisionPoint Price Momentum Oscillator is derived by taking a 1-period rate of change and smoothing it with two custom smoothing functions. The custom smoothing functions are very similar to Exponential Moving Averages, but, instead of adding one to the time period setting to create the smoothing multiplier (as in a true EMA), the smoothing functions just use the period by itself.

```
Smoothing Multiplier = (2 / Time period)

Custom Smoothing Function = {Close - Smoothing Function(previous day)} *
 Smoothing Multiplier + Smoothing Function(previous day) 

PMO Line = 20-period Custom Smoothing of
(10 * 35-period Custom Smoothing of
 ( ( (Today's Price/Yesterday's Price) * 100) - 100) )

PMO Signal Line = 10-period EMA of the PMO Line
```

<figure><img src="/files/XdVlE7oO8ji690a4kl9f" alt=""><figcaption></figcaption></figure>

The table below shows the calculation for Amazon's PMO:

<figure><img src="/files/cEVZ624Sm0UkZScaXfTB" alt=""><figcaption></figcaption></figure>

Click below to download an Excel spreadsheet with these calculations.

{% file src="/files/E4oYHZwPlAmp5a2IadH3" %}

## Interpretation <a href="#interpretation" id="interpretation"></a>

The PMO oscillates in relation to a zero line. Normally, the PMO direction indicates if strength is increasing or decreasing, while the steepness of the trend angle demonstrates the power behind the move. Since this is an internal ratio calculation (versus external, like the standard relative strength calculation, which divides one price by another price index), it returns a result that is normalized and can be compared to the PMO result of any other security or index. Therefore, chartists can rank a list of securities or indexes in relative strength order simply by using their PMO values. The list does not have to be homogeneous; ­the PMO can be used to rank market indexes, stocks and mutual funds in the same list.

An indicator that looks very similar to the PMO is the MACD ([Moving Average Convergence-Divergence](/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator.md)) indicator invented by Gerald Appel. The main difference between the PMO and MACD is the absolute value of each indicator. The MACD is based on moving average calculations - one stock's MACD reading bears no relationship to another's - whereas the PMO, as explained above, is an internal ratio. The chart below shows the PMO and MACD together.

<figure><img src="/files/z0R03DjrlqtNxiVLuFFq" alt=""><figcaption></figcaption></figure>

While the PMO and MACD have similar shapes on shorter-term charts, the advantage of the ratio-type calculation for the PMO is evident on longer-term charts because the PMO is fairly constant, unlike the MACD. See the weekly and monthly charts below.

<figure><img src="/files/27irt4SEg1zhwNgI1IiK" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/8kQEzKCR6AQSy8XMZRbd" alt=""><figcaption></figcaption></figure>

## Overbought/Oversold Indicator <a href="#overbought_oversold_indicator" id="overbought_oversold_indicator"></a>

As demonstrated below, the PMO can help determine if a price index is overbought or oversold. Below is a five-year chart of the S\&P 500 index, showcasing a wide range of extreme market conditions. The normal PMO range for this index is from about +2.5 (overbought) to -2.5 (oversold); when the PMO approaches or breaches those limits, it often signals a price reversal. When the PMO changes direction at or beyond the extremes of its normal range, it is a fairly reliable indication that an intermediate-term change in price direction is taking place.

<figure><img src="/files/RjHbMIg5tygj2PEPKerP" alt=""><figcaption></figcaption></figure>

While +2.5 to -2.5 is the usual range for broad stock market indexes, each price index will have its own “signature” range. For example, the chart of Microsoft (MSFT) below shows a range of +5.0 to -5.0. Always check a longer-term chart to verify the normal range for the index you are analyzing.

<figure><img src="/files/7HnXGm8gv9UuSrO3HEcR" alt=""><figcaption></figcaption></figure>

Also, remember that technical indicators are calculated based on a specific number of time periods within the timeframe being addressed, so a monthly PMO looks completely different from a daily PMO. See the monthly based chart below which uses the same seven-year period as the daily MSFT chart above.

<figure><img src="/files/2VolBChnBZh9jUkztLnS" alt=""><figcaption></figcaption></figure>

## Momentum Indicator <a href="#momentum_indicator" id="momentum_indicator"></a>

As a momentum indicator, the PMO expresses the direction and velocity of price movement. In this regard, it is much like other momentum indicators. On the chart of the Gold ETF (GLD) below, the strongest moves in either direction are characterized by straight, steep, smooth PMO movement. More halting trends usually are accompanied by frequent PMO direction changes. PMO bottoms and tops suggest that price momentum has shifted direction, so they can provide early flags to price tops and bottoms. They are usually more reliable when the PMO is in overbought or oversold territory.

<figure><img src="/files/Dhln1XXTvLwXpwX3D7CS" alt=""><figcaption></figcaption></figure>

Finally, like other oscillators, the PMO gives hints of important direction changes by forming divergences against the price index. Three separate divergences have been highlighted below. The two negative divergences (red lines) warn of important tops as the price index makes a higher high and the PMO makes a lower high. The Positive divergence (green lines) signal an important bottom with price making a lower low while the PMO makes a higher low.

<figure><img src="/files/ypUavocCMz59gJLTXv2D" alt=""><figcaption></figcaption></figure>

## Signal Generator <a href="#signal_generator" id="signal_generator"></a>

The PMO generates a crossover signal when it crosses through its 10-period EMA. These signals tend to be short-term in duration, but they can last for several weeks. Do not take them at face value because they can whipsaw quite a bit. They should be used to alert you to possible trading opportunities, rather than as a mechanical trading model. Always check the chart to verify the price pattern and the configuration of the PMO. Signals are best when price appears extended, is near support or resistance, and the PMO is very overbought or oversold. These signals may also be used with [DecisionPoint Trend Analysis](/table-of-contents/trading-strategies-and-models/decisionpoint-trend-model.md) using 20/50/200-EMA crossovers, which determine long-term, intermediate-term, and short-term bull or bear bias.

The most reliable signals are generated when the PMO is near the extremes of its normal range, or when a direction change and crossover occurs following a strong, clean, straight PMO move. Quite a bit of “noise” can be generated around the zero line and while the PMO is moving in a relatively flat pattern. Crossover signals have been highlighted on the chart below:

<figure><img src="/files/CH0xoRGydHOgynLBU0fA" alt=""><figcaption></figcaption></figure>

## PMO Configurations <a href="#pmo_configurations" id="pmo_configurations"></a>

### **Sideways Wiggle**

The following chart illustrates a common PMO formation that emphasizes why all PMO crossover signals cannot be taken literally. The area circled in red is typical of PMO movement during a steady rising price trend. There is little volatility in price movement, so the PMO moves sideways. The fact that the PMO remains above the zero line testifies to the strength of the price move; however, minor zigzags in price movement cause the PMO to whipsaw above and below its 10-period EMA, generating many unprofitable crossover bull signals. This chart also shows how sideways wiggle ultimately will end and how it can offer subtle clues that the end of the trend is near.

<figure><img src="/files/qZfcEM0ax73RMAakYgd3" alt=""><figcaption></figcaption></figure>

### **Bear Kiss**

The “bear kiss” is the final part of three distinct topping actions often displayed by the PMO. When we see this classic formation, it offers additional reassurance that a tradable top is in place. We start looking for this formation when the PMO has become relatively overbought and the price index has experienced a substantial move up. This formation doesn't always occur at tops, but, when it does, it helps build our confidence in the reliability of the signal.

The first action is a false PMO top. Major tops are always accompanied by an overbought PMO top, but not all PMO tops signal major price tops. The false top alerts us that a price top is probably just a few weeks away.

Next, we'll see a slightly higher PMO top followed by a crossover sell signal, which is generated when the PMO (green line) crosses down through its 10-period EMA (blue line). When these signals occur at very overbought levels, they may tentatively be taken at face value, but, when they have been preceded by very strong price action, it is possible for prices to make yet another new high, causing the PMO to begin rising again.

Finally, as prices roll over from the final top, the PMO turns up again, this time topping after just barely “kissing” the underside of the 10-period EMA. Some refer to this as the “kiss of death,” but this seems a tad dramatic, so a bear kiss seems more appropriate. Besides, there is a reciprocal formation at important bottoms, and the term “bull kiss” seems more apt than “kiss of life.”

Note that an important aspect of this analysis is that the price index has broken a rising trend line in conjunction with the bear kiss.

<figure><img src="/files/hM6CKjUeWXqtfAwal6pz" alt=""><figcaption></figcaption></figure>

### **Bull Kiss**

The “bull kiss” occurs shortly after a PMO crossover buy signal, and is the result of a price pullback after the initial up thrust that generates the crossover signal. While the bull kiss and bear kiss are essentially equal but opposite formations, price behavior between the two is different. Normally, the bear kiss is a non-confirmation which coincides with the final price high in a rally, while the bull kiss normally coincides with a higher price low in a new rally.

<figure><img src="/files/5Rb04gBvvn8ipOpBZ480" alt=""><figcaption></figcaption></figure>

### **Clean Signals**

While the bull and bear kiss formations are quite common, it is also possible to have very clean PMO reversals and crossovers, which lack the gyrations associated with blow-offs and retests as the change in price trend is relatively smooth. The point is that reversals and crossover actions can cover a wide range of configurations. A study of the charts will lead to a better understanding of the kind of price action that begets a certain type of PMO behavior. The PMO behavior also gives clues as to what kind of price behavior to expect.

<figure><img src="/files/Z178260eGPYyY7HVAttx" alt=""><figcaption></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The DecisionPoint Price Momentum Oscillator (PMO) can be used as both a measure of relative strength, momentum and overbought/oversold conditions. It can also be used to determine price reversals using bull and bear crossovers.

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The DecisionPoint PMO is available as an indicator for SharpCharts. The default settings use a 35-period and 20-period EMA with a 10-period EMA signal line, but users can opt for a shorter or longer timeframe to produce an oscillator with increased or decreased sensitivity. Once selected, the indicator can be placed above, below or behind the underlying price plot.

<figure><img src="/files/2vSOlcOc2KhutbvrhfUW" alt=""><figcaption></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### PMO Rising But Not Yet Crossed Over Signal Line <a href="#pmo_rising_but_not_yet_crossed_over_signal_line" id="pmo_rising_but_not_yet_crossed_over_signal_line"></a>

This scan starts with a base of stocks that are averaging at least $10 in price and 100,000 in daily volume over the last 60 days. The stock's PMO must have been rising for the last three days, but has not yet crossed over its signal line. In addition, the 20-day EMA is above the 50-day EMA, which is above the 200-day EMA, indicating the stock is in an intermediate- or long-term bull market. This scan is meant as a starting point for further analysis and due diligence.

```
[type = stock] AND [country = US] 
AND [Daily SMA(60,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 10] 

AND [today's PMO Line(35,20,10) > yesterday's PMO Line(35,20,10)]
AND [yesterday's PMO Line(35,20,10) > 2 days ago PMO Line(35,20,10)] 
AND [2 days ago PMO Line(35,20,10) > 3 days ago PMO Line(35,20,10)]
AND [today's PMO Line(35,20,10) < today's PMO Signal(35,20,10)]
AND [today's EMA(20,close) > today's EMA(50,close)]
AND [today's EMA(50,close) > today's EMA(200,close)]
```

### PMO Falling But Not Yet Crossed Below Signal Line <a href="#pmo_falling_but_not_yet_crossed_below_signal_line" id="pmo_falling_but_not_yet_crossed_below_signal_line"></a>

This scan starts with a base of stocks that are averaging at least $10 in price and 100,000 in daily volume over the last 60 days. The stock's PMO must have been in decline for the last three days, but has not yet crossed below its signal line. In addition, the 20-day EMA is below the 50-day EMA, which is below the 200-day EMA, indicating the stock is in an intermediate- or long-term bear market. This scan is meant as a starting point for further analysis and due diligence.

```
[type = stock] AND [country = US] 
AND [Daily SMA(60,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 10] 

AND [today's PMO Line(35,20,10) < yesterday's PMO Line(35,20,10)]
AND [yesterday's PMO Line(35,20,10) < 2 days ago PMO Line(35,20,10)] 
AND [2 days ago PMO Line(35,20,10) < 3 days ago PMO Line(35,20,10)]
AND [today's PMO Line(35,20,10) > today's PMO Signal(35,20,10)]
AND [today's EMA(20,close) < today's EMA(50,close)]
AND [today's EMA(50,close) < today's EMA(200,close)]
```

{% hint style="info" %}
For more details on the syntax to use for PMO scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#decisionpoint_price_momentum_oscillator_pmo) in the Support Center.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/decisionpoint-price-momentum-oscillator-pmo.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
