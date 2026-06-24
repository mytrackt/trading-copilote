> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/chaikin-oscillator.md).

# Chaikin Oscillator

## What Is the Chaikin Oscillator? <a href="#introduction" id="introduction"></a>

Developed by Marc Chaikin, the Chaikin Oscillator measures the momentum of the [Accumulation Distribution Line](/table-of-contents/technical-indicators-and-overlays/technical-indicators/accumulation-distribution-line.md) (ADL) using the [MACD formula](/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator.md). (This makes it an indicator of an indicator.)&#x20;

The Chaikin Oscillator is the difference between the three-day and 10-day [exponential moving averages](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) (EMAs) of the ADL. Like other momentum indicators, this indicator is designed to anticipate directional changes in the ADL by measuring the momentum behind the movements. A momentum change is the first step to a trend change. Anticipating trend changes in the ADL can help chartists anticipate trend changes in the underlying security. The Chaikin Oscillator generates signals with crosses above/below the zero line or with bullish/bearish divergences.

## Calculating the Chaikin Oscillator <a href="#calculation" id="calculation"></a>

The first step is calculating the ADL. This involves the following steps:

1. Calculate the Money Flow Multiplier.&#x20;
2. Multiply this value by volume to find Money Flow Volume.&#x20;
3. Create a running total of Money Flow Volume to form the ADL.
4. Take the difference between two moving averages to calculate the Chaikin Oscillator.

```
               
  1. Money Flow Multiplier = [(Close  -  Low) - (High - Close)] /(High - Low) 

  2. Money Flow Volume = Money Flow Multiplier x Volume for the Period

  3. ADL = Previous ADL + Current Period's Money Flow Volume

  4. Chaikin Oscillator = (3-day EMA of ADL)  -  (10-day EMA of ADL)		
```

The ADL rises when the Money Flow Multiplier is positive and falls when it is negative. This multiplier is positive when the close is in the upper half of the period's high-low range and negative when the close is in the lower half. As a MACD-type oscillator, the Chaikin Oscillator turns positive when the faster three-day EMA moves above the slower 10-day EMA. Conversely, the indicator turns negative when the three-day EMA moves below the 10-day EMA.

The chart below shows the ADL (gray) with the three-day EMA (blue) and the 10-day EMA (red). The price for General Electric (GE) is invisible so we can focus on the relationship between the ADL and the Chaikin Oscillator. Notice how the Chaikin Oscillator moves into negative territory as the three-day EMA moves below the 10-day EMA. Conversely, the oscillator turns positive when the three-day EMA crosses above the 10-day EMA.

<figure><img src="/files/zsN9t3FD66Qz0sDlPcIg" alt=""><figcaption><p>Chart 1  -  Chaikin Oscillator</p></figcaption></figure>

## Interpreting the Chaikin Oscillator <a href="#interpretation" id="interpretation"></a>

First and foremost, it is important to remember that the Chaikin Oscillator is an indicator of an indicator measuring momentum for the ADL. This makes it at least three steps removed from the price of the underlying security. First, price and volume are reshaped into the ADL. Second, exponential moving averages are applied to the ADL. Third, the difference between [the moving averages](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) is used to form the Chaikin Oscillator. As the third derivative, the indicator is more prone to disconnect from the price of the underlying security.

<figure><img src="/files/Al0uzKkQ6dWRMWy8xsa9" alt=""><figcaption><p>Chart 2  -  Chaikin Oscillator</p></figcaption></figure>

Having clarified that, the indicator is designed to measure the momentum behind buying and selling pressure (ADL). A move into positive territory indicates that the ADL is rising and buying pressure prevails. A move into negative territory indicates that the Accumulation Distribution Line is falling and selling pressure prevails. Chartists can anticipate crosses into positive or negative territory by looking for bullish or bearish divergences, respectively.

### Buying/Selling Bias <a href="#buying_selling_bias" id="buying_selling_bias"></a>

The Chaikin Oscillator can be used to define a general buying or selling bias simply with positive or negative values. The indicator oscillates above/below the zero line. Generally, buying pressure is stronger when the indicator is positive and selling pressure is stronger when the indicator is negative.

The default settings for the Chaikin Oscillator (3,10) often produce a line that frequently crosses zero. Chartists can smooth the indicator by lengthening the moving averages. The example below shows the Chaikin Oscillator (6,20). Both moving averages were doubled to maintain the ratio and smooth the indicator.

<figure><img src="/files/Bw0BlLx3VHcvO6GAI7cp" alt=""><figcaption><p>Chart 3  -  Chaikin Oscillator</p></figcaption></figure>

The Chaikin Oscillator for US Steel (X) crossed the zero line six times over 12 months. There were some good signals, such as the April sell signal and the October buy signal. There were also some bad signals or whipsaws. The key, as with all indicators, is to confirm the oscillator signals with other aspects of technical analysis, such as a pure price momentum oscillator or pattern analysis.

<figure><img src="/files/Jls5wY8SLGIOY1Q7BLoX" alt=""><figcaption><p>Chart 4  -  Chaikin Oscillator</p></figcaption></figure>

### Divergences <a href="#divergences" id="divergences"></a>

Bullish and bearish divergences alert chartists to a momentum shift in buying or selling pressure that can foreshadow a trend reversal on the price chart. A bullish divergence forms when price moves to new lows and the Chaikin Oscillator forms a higher low. This higher low shows less selling pressure. It is important to wait for some sort of confirmation, such as an upturn in the indicator or a cross into positive territory. A move into positive territory shows upside momentum in the Accumulation Distribution Line.

The Fastenal (FAST) chart shows five divergences for the Chaikin Oscillator in 2010. The default settings (3,10) produce a rather sensitive oscillator that will generate many divergences. The key is to differentiate the robust signals from the bogus signals by waiting for confirmation. Even with a bullish divergence, selling pressure outweighs buying pressure until there is a cross above the zero line. Buying pressure dominates until there is a cross into negative territory.

The chart for Alcoa (AA) shows six zero-line crosses in 2010. The first five did not generate good signals, but the sixth was a dandy. Chartists should experiment with the settings and consider adding trend lines to enhance their analysis. Trend line breaks are often earlier than zero line crosses. A trend line also captures the direction of the indicator. A rising Chaikin Oscillator reflects a steady increase in buying pressure. A falling Chaikin Oscillator reflects a steady increase in selling pressure.

<figure><img src="/files/QDLmB1GLFq3awTGs7XwH" alt=""><figcaption><p>Chart 5  -  Chaikin Oscillator</p></figcaption></figure>

The green lines show the Chaikin Oscillator forming a higher low as the stock forms a lower low for a bullish divergence. The green dotted lines show when the indicator moves into positive territory to confirm the signal. The mid-February, early September, and late November signals were great; the mid-June buy signal, however, resulted in a whipsaw. There was little weakness after the October sell signal from the bearish divergence.

A bearish divergence forms when price moves to a new high, and the Chaikin Oscillator fails to confirm this higher high. This failure reflects lessened buying pressure, which can sometimes foreshadow a bearish reversal on the price chart. Confirmation comes when the oscillator moves into negative territory.

The chart for Kohls (KSS) shows three bearish divergences and two bullish divergences over 12 months. The bearish divergences (red lines) were confirmed when the Chaikin Oscillator moved into negative territory to show actual downside momentum in the Accumulation Distribution Line. Remember, the Chaikin Oscillator (3,10) turns negative when the 3-day EMA of the Accumulation Distribution Line moves below the 10-day EMA.

<figure><img src="/files/JYrsjGskgr0BMvlPkhPq" alt=""><figcaption><p>Chart 6  -  Chaikin Oscillator</p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The Chaikin Oscillator is a momentum indicator for the Accumulation Distribution Line. The Chaikin Oscillator turbo-charges the Accumulation Distribution Line by measuring momentum. Signals are more frequent and often easier to quantify using the Chaikin Oscillator. As a money flow oscillator, it can be used with pure price oscillators, such as [MACD](/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator.md) or [RSI](/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi.md). As with all indicators, the Chaikin Oscillator should not be used as a stand-alone indicator.

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Chaikin Oscillator can be set as an indicator above, below or behind a security's price plot. It is easy to compare indicator/price movements when the indicator is placed behind the price plot. Once the indicator is chosen from the dropdown list, the default parameter setting appears (3,10). These parameters can be adjusted to increase or decrease sensitivity. Users can click on “advanced options” to add a horizontal line or moving average. [Click here for a live example](https://stockcharts.com/sc3/ui/?s=IBM\&p=D\&yr=0\&mn=6\&dy=0\&id=p43640188268\&listNum=30\&a=222998125).

<figure><img src="/files/4TtLqU8ETQ94WerqwU6N" alt=""><figcaption><p>Chart 7  -  Chaikin Oscillator</p></figcaption></figure>

<figure><img src="/files/Zzp6734LxHWB1PpmQgnH" alt=""><figcaption><p>SharpCharts  -  Chaikin Oscillator</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Chaikin Oscillator Turns Positive and RSI Moves Above 55 <a href="#chaikin_oscillator_turns_positive_and_rsi_moves_above_55" id="chaikin_oscillator_turns_positive_and_rsi_moves_above_55"></a>

This scan starts with a base of stocks that are averaging at least $10 in price and 100,000 in daily volume over the last 60 days. Upturns on good volume are identified when the Chaikin Oscillator moves above +1000, which is just above its centerline (0). This is confirmed with price momentum because RSI is required to move above 55, which is just above its centerline (50). This scan is a starting point for further analysis and due diligence.

```
[type = stock] AND [country = US] 
AND [Daily SMA(60,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 10] 

AND [Daily Chaikin Osc(3,10) crosses 1000] 
AND [Daily RSI(14,Daily Close) crosses 55]
```

### Chaikin Oscillator Turns Negative and RSI Moves Below 45 <a href="#chaikin_oscillator_turns_negative_and_rsi_moves_below_45" id="chaikin_oscillator_turns_negative_and_rsi_moves_below_45"></a>

This scan starts with a base of stocks that are averaging at least $10 in price and 100,000 in daily volume over the last 60 days. Downturns on good volume are identified when the Chaikin Oscillator moves below -1000, which is just below its centerline (0). This is confirmed with price momentum because RSI is required to move below 45, which is just below its centerline (50). This scan is meant as a starting point for further analysis and due diligence.

```
[type = stock] AND [country = US] 
AND [Daily SMA(60,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 10] 

AND [-1000 crosses Daily Chaikin Osc(3,10)] 
AND [45 crosses Daily RSI(14,Daily Close)]
```

{% hint style="info" %}
For more details on the syntax to use for Chaikin Oscillator scans, please see our [Scan Syntax Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference) in the Support Center.
{% endhint %}

{% hint style="warning" %}
**Note**: For scanning purposes, daily volume data is incomplete during the trading day. When running scans with volume-based indicators like Chaikin Oscillator, base the scan on the “Last Market Close.” Examples of other volume-based indicators include Accumulation/Distribution, On Balance Volume, and the PVO.
{% endhint %}

## Additional Resources <a href="#further_study" id="further_study"></a>

### Recommended Books

John Murphy's [*Technical Analysis of the Financial Markets*](https://a.co/d/6YfGrAK) provides simple and clear explanations for almost all of the major chart patterns and indicators. A complete chapter is devoted to understanding volume and open interest.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/chaikin-oscillator.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
