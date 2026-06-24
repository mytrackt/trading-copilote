> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/trix.md).

# TRIX

## What Is the TRIX? <a href="#introduction" id="introduction"></a>

TRIX is a momentum oscillator that displays the percent [rate of change](/table-of-contents/technical-indicators-and-overlays/technical-indicators/rate-of-change-roc.md) of a triple exponentially smoothed moving average. It was developed in the early 1980's by Jack Hutson, an editor for *Technical Analysis of Stocks and Commodities* magazine. With its triple smoothing, TRIX is designed to filter out insignificant price movements. Chartists can use TRIX to generate signals similar to MACD. A signal line can be applied to look for signal line crossovers. A directional bias can be determined with the absolute level. Bullish and bearish divergences can be used to anticipate reversals.

## Calculating TRIX <a href="#calculation" id="calculation"></a>

TRIX is the one-period percentage rate-of-change for a triple smoothed exponential [moving average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) (EMA), which is an EMA of an EMA of an EMA. Here is a breakdown of the steps involved for a 15 period TRIX.

1. Single-Smoothed EMA = 15-period EMA of the closing price
2. Double-Smoothed EMA = 15-period EMA of Single-Smoothed EMA
3. Triple-Smoothed EMA = 15-period EMA of Double-Smoothed EMA
4. TRIX = 1-period percent change in Triple-Smoothed EMA

The table and chart below provide examples for the 15-day EMA, double-smoothed EMA and triple-smoothed EMA. Notice how each EMA lags price a little more. Even though exponential moving averages put more weight on recent data, they still contain past data that produces a lag. This lag increases with each smoothing.

<figure><img src="/files/8VpJzEwIRMMcNlxDtugH" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/bBfz2g3vRiduZO1klTba" alt=""><figcaption><p>TRIX - Chart 1</p></figcaption></figure>

The blue line is the price plot for SPY. It is clearly the most jagged (volatile) of the four lines. The red line is the 15-day EMA, which follows the price plot the closest. The green line is the double-smoothed EMA and the purple line is the triple-smoothed EMA. Notice how these two lines turn flatter as the lag increases.

TRIX is negative as long as the triple-smoothed 15-day EMA is moving lower. TRIX turns positive when the triple-smoothed 15-day EMA turns up. The extra smoothing ensures that upturns and downturns are kept to a minimum. In other words, it takes more than a one-day advance to reverse a downtrend.

<figure><img src="/files/n7e6gKzYhv0joZHPoy1k" alt=""><figcaption><p>TRIX - Chart 2</p></figcaption></figure>

## Interpreting the TRIX <a href="#interpretation" id="interpretation"></a>

TRIX (15,9) is similar to [MACD (12,26,9)](/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator.md). Both are momentum oscillators that fluctuate above and below the zero line. Both have signal lines based on a 9-day EMA. Most notably, both lines have similar shapes, signal line crossovers, and centerline crosses. The biggest difference between TRIX and MACD is that TRIX is the smoother of the two; TRIX lines are less jagged and tend to turn a bit later.

<figure><img src="/files/Ab051OwciyVWQonpvubQ" alt=""><figcaption><p>TRIX - Chart 3</p></figcaption></figure>

With the similarities outweighing the differences, signals applicable to MACD are also applicable to TRIX. There are three main signals to watch for. First, signal line crossovers are the most common signals. These indicate a change in direction for TRIX and price momentum. A cross above the signal line is the first bullish indication, while a cross below is the first negative implication. Second, centerline crossovers provide chartists with a general momentum bias. The triple-smoothed moving average is rising when TRIX is positive and falling when negative. Similarly, momentum favors the bulls when TRIX is positive and the bears when negative. Third, bullish and bearish divergences can alert chartists of a possible trend reversal.

## Signal Line Crossovers <a href="#signal_line_crossovers" id="signal_line_crossovers"></a>

Signal line crossovers are the most common TRIX signals. The signal line is a 9-day EMA of the TRIX. As a moving average of the indicator, it trails TRIX and makes it easier to spot turns. A bullish crossover occurs when TRIX turns up and crosses above the signal line. A bearish crossover occurs when TRIX turns down and crosses below the signal line. Crossovers can last a few days or a few weeks, depending on the strength of the move. Due diligence is required before relying on these frequent signals. Volatility in the underlying security can also increase the number of crossovers.

<figure><img src="/files/L43Hc67p2v5tdH7oguQe" alt=""><figcaption><p>TRIX - Chart 4</p></figcaption></figure>

The chart above shows Intel (INTC) and TRIX with six signal line crosses in a seven-month period. That is almost one per month. There were three good signals and three bad signals resulting in whipsaws (yellow area). The bullish crossover in June occurred near the top, the bearish crossover in late June occurred near the low and the bullish crossover in July occurred near the top. In the absence of a strong move, the lag from the triple-smoothed EMA results in late signals that produce losses. The bearish signal line cross in August foreshadowed a sharp decline and the bullish signal line cross in mid-September foreshadowed a strong advance.

## Centerline Crossovers <a href="#centerline_crossovers" id="centerline_crossovers"></a>

The [centerline crossover](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#centerline_crossovers) indicates when the cup is half full (bullish) or half empty (bearish). Think of the centerline as the 50-yard line in a football game. The offense has the edge after crossing the 50 (midpoint), while the defense has the edge as long as the ball remains beyond the 50. As with signal line crossovers, these centerline crossovers produce both good signals and bad signals. The key, as always, is to minimize losses on the bad signals and maximize gains with the good signals.

<figure><img src="/files/GTMIfrxnrUnWDY1xXogZ" alt=""><figcaption><p>TRIX - Chart 5</p></figcaption></figure>

The chart above shows Raytheon (RTN) with five signals over a 16 month period. The first three were bad because the stock changed direction soon after the signals. In other words, a trend failed to take hold. The fourth signal (November 2009) coincided with a resistance breakout and foreshadowed a 20% advance. Great signal! This is also a classic example of combining indicator signals with chart signals for reinforcement. The resistance breakout on the price chart and the centerline cross for the TRIX reinforced each other. TRIX produced a nice bearish signal in May 2010 as RTN subsequently declined around 20%.

## Divergences <a href="#divergences" id="divergences"></a>

Bullish and bearish divergences form when the security and the indicator do not confirm one another. A bullish divergence forms when the security forges a lower low, but the indicator forms a higher low. This higher low shows less downside momentum that may foreshadow a bullish reversal. A bearish divergence forms when the security forges a higher low, but the indicator forms a lower high. This lower high shows waning upside momentum that can sometimes foreshadow a bearish reversal. Before looking at a successful divergence, note the BHP Billiton (BHP) chart with several unsuccessful divergences.

<figure><img src="/files/gUttJPcBh7MFDvvxOrYW" alt=""><figcaption><p>TRIX - Chart 6</p></figcaption></figure>

Bearish divergences do not work well in strong uptrends. Even though momentum seems to be waning because the indicator is producing lower highs, momentum still has a bullish bias as long as the indicator is above its centerline. Upward momentum may be less positive, but it is still positive as long as the cup is half full. The rise is just not as fast as before. The opposite is true for bullish divergences. These do not work well in strong downtrends. Even though the indicator shows less downside momentum with higher lows, downward momentum is still stronger than upward momentum as long as the indicator remains below its centerline.

When bullish and bearish divergences work, they really work. The trick is separating the bad signals from the good signals. The chart below shows eBay (EBAY) with a successful bullish divergence. The stock moved to a lower low in early July, but TRIX held well above its prior low and formed a bullish divergence. The first potential confirmation came when TRIX moved above its signal line. However, there were no confirmations on the chart at the time. These came a little later. The green arrows show EBAY breaking chart resistance with good volume and TRIX moving into positive territory. Even though confirmation occurred well off the low, there were enough signs of strength to validate the breakout.

<figure><img src="/files/9uplrrZa5BGlqdfExrMe" alt=""><figcaption><p>TRIX - Chart 7</p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

TRIX is an indicator that combines trend with momentum. The triple smoothed moving average covers the trend, while the 1-period percentage change measures momentum. In this regard, TRIX is similar to MACD and PPO. The standard setting for TRIX is 15 for the triple smoothed EMA and 9 for the signal line. Chartists looking for more sensitivity should try a shorter timeframe (5 versus 15). This will make the indicator more volatile and better suited for centerline crossovers. Chartists looking for less sensitivity should try a longer timeframe (45 versus 15). This will smooth the indicator and make it better suited for signal line crossovers. As with all indicators, TRIX should be used in conjunction with other aspects of technical analysis, such as [chart patterns](/table-of-contents/chart-analysis/chart-patterns.md).

<figure><img src="/files/nD5IG2uojcH8IK9obsa4" alt=""><figcaption><p>TRIX - Chart 8</p></figcaption></figure>

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

TRIX can be set as an indicator above, below or behind a security's price plot. It is easy to compare indicator/price movements when the indicator is placed behind the price plot. Once the indicator is chosen from the dropdown list, the default parameter setting appears (15,9). These parameters can be adjusted to increase or decrease sensitivity. The signal line default is 9, which can also be adjusted. [Click here for a live example of TRIX](https://stockcharts.com/sc3/ui/?s=SPY\&p=D\&yr=0\&mn=6\&dy=0\&id=p97840257416\&listNum=30\&a=218370394).

<figure><img src="/files/svXRnBxB5mREEIHlMmMV" alt=""><figcaption><p>TRIX - Chart 7</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### TRIX Bullish Signal Line Cross <a href="#trix_bullish_signal_line_cross" id="trix_bullish_signal_line_cross"></a>

This scan reveals stocks that meet four criteria. First, they must be above their 200-day moving average to be in an overall uptrend. Second, the TRIX must be negative to signal a pullback. Third, the TRIX crossed its signal line and turned up. Fourth, volume moved above the 250-day average to show an increase in buying pressure.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [Daily Close > Daily SMA(200,Daily Close)]
AND [Yesterday's Daily TRIX(15,9,Daily Close) crosses Daily TRIX Signal(15,9,Daily Close)]
AND [Daily Volume > Daily SMA(250,Daily Volume)]
AND [Daily TRIX(15,9,Daily Close) < 0]
```

### TRIX Bearish Signal Line Cross <a href="#trix_bearish_signal_line_cross" id="trix_bearish_signal_line_cross"></a>

This scan reveals stocks that meet four criteria. First, they must be below their 200-day moving average to be in an overall downtrend. Second, the TRIX must be positive to signal a bounce. Third, the TRIX crossed its signal line and turned down. Fourth, volume moved above the 250-day average to show an increase in selling pressure.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [Daily Close < Daily SMA(200,Daily Close)]
AND [Yesterday's Daily TRIX Signal(15,9,Daily Close) crosses Daily TRIX(15,9,Daily Close)]
AND [Daily Volume > Daily SMA(250,Daily Volume)]
AND [Daily TRIX(15,9,Daily Close) > 0]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax to use for TRIX scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#trix) in the Support Center.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/trix.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
