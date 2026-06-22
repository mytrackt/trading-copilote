> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator.md).

# MACD (Moving Average Convergence/Divergence) Oscillator

## What Is the Moving Average Convergence/Divergence Oscillator? <a href="#what_is_the_moving_average_convergence_divergence_oscillator" id="what_is_the_moving_average_convergence_divergence_oscillator"></a>

Developed by Gerald Appel in the late seventies, the Moving Average Convergence/Divergence oscillator (MACD), due to its simplicity and general effectiveness, is one of the most popular momentum indicators. The MACD turns two trend-following indicators,[ moving averages](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md), into a momentum oscillator by subtracting the longer moving average from the shorter one. As a result, the MACD offers the best of both worlds: **trend following and momentum.** The MACD fluctuates above and below the zero line as the moving averages converge, cross and diverge. Traders can look for signal line crossovers, centerline crossovers and divergences to generate signals. Because the MACD is unbounded, it is not particularly useful for identifying overbought and oversold levels.

{% hint style="warning" %}
**Note:** MACD can be pronounced as either “Mac-Dee” or “M-A-C-D.”
{% endhint %}

{% embed url="<https://youtu.be/jJzo1fxbEEw>" %}

Below is an example chart with the MACD indicator in the lower panel.

&#x20;[Click here to see a live version of the chart.](https://schrts.co/htjRIViR)

<figure><img src="/files/G4Cz9AUtijeuEoU3uKHI" alt=""><figcaption></figcaption></figure>

## How Do You Calculate the MACD? <a href="#how_do_you_calculate_the_macd" id="how_do_you_calculate_the_macd"></a>

```
MACD Line: (12-day EMA - 26-day EMA)

Signal Line: 9-day EMA of MACD Line

MACD Histogram: MACD Line - Signal Line
```

The MACD line is the 12-day [Exponential Moving Average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) (EMA) less the 26-day EMA. Closing prices are used for these moving averages. A nine-day EMA of the MACD line is plotted with the indicator, which acts as a signal line and identifies reversals. The MACD Histogram represents the difference between MACD and its nine-day EMA, the signal line. The histogram is positive when the MACD line is above its signal line and negative when the MACD line is below its signal line.

The values of **12, 26, and 9** are the typical settings used with the MACD, though other values can be substituted depending on your trading style and goals.

## How Do You Interpret the MACD? <a href="#how_do_you_interpret_the_macd" id="how_do_you_interpret_the_macd"></a>

### **Convergence/Divergence**

As its name implies, the MACD is all about the convergence and divergence of the two moving averages. Convergence occurs when the moving averages move towards each other. Divergence occurs when the moving averages move away from each other. The shorter moving average (12-day) is faster and responsible for most MACD movements. The longer moving average (26-day) is slower and less reactive to price changes in the underlying security.

### **Oscillator**

The MACD line oscillates above and below the zero line, also known as the centerline. These crossovers signal that the 12-day EMA has crossed the 26-day EMA. The direction, of course, depends on the direction of the moving average cross. Positive MACD indicates that the 12-day EMA is above the 26-day EMA. Positive values increase as the shorter EMA diverges further from the longer EMA. **This means upside momentum is increasing.** Negative MACD values indicate the 12-day EMA is below the 26-day EMA. Negative values increase as the shorter EMA diverges further below the longer EMA. **This means downside** [**momentum**](/table-of-contents/glossary/glossary-m.md#momentum) **is increasing.**

<figure><img src="/files/jw7pKZv3mi4fV7tpwbzK" alt=""><figcaption><p>StockCharts MACD interpretation</p></figcaption></figure>

In the example above, the golden shaded area shows the MACD line in negative territory as the 12-day EMA trades below the 26-day EMA. In mid-February, the MACD moved further into negative territory as the 12-day EMA diverged further from the 26-day EMA. The red area highlights a period of positive MACD values, when the 12-day EMA was above the 26-day EMA.

## Signal Line Crossovers <a href="#signal_line_crossovers" id="signal_line_crossovers"></a>

Signal line crossovers are the most common MACD signals. The signal line is a 9-day EMA of the MACD line. As a moving average of the indicator, it trails the MACD and makes it easier to spot MACD turns. A bullish crossover occurs when the MACD turns up and crosses above the signal line. A bearish crossover occurs when the MACD turns down and crosses below the signal line. Crossovers can last a few days or a few weeks, depending on the strength of the move.

Due diligence is required before relying on these common signals. Signal line crossovers at positive or negative extremes should be viewed with caution. Even though the MACD does not have upper and lower limits, chartists can estimate historical extremes with a simple visual assessment. It takes a strong move in the underlying security to push momentum to an extreme. Even though the move may continue, momentum is likely to slow and this will usually produce a signal line crossover at the extremities. Volatility in the underlying security can also increase the number of crossovers.

The chart below shows IBM with its 12-day EMA (green), 26-day EMA (red) and the 12,26,9 MACD in the indicator window. There were eight signal line crossovers in six months: four up and four down. There were some good signals and some bad signals. The yellow area highlights a period when the MACD line surged above 2 to reach a positive extreme. There were two bearish signal line crossovers in April and May, but IBM continued trending higher. Even though upward momentum slowed after the surge, it was still stronger than downside momentum in April-May. The bearish signal line crossover in June resulted in a good signal.

<figure><img src="/files/4herkCsOaYDAAh5F8Kzi" alt=""><figcaption></figcaption></figure>

## Centerline Crossovers <a href="#centerline_crossovers" id="centerline_crossovers"></a>

Centerline crossovers are the next most common MACD signals. A bullish centerline crossover occurs when the MACD line moves above the zero line to turn positive. This happens when the 12-day EMA of the underlying security moves above the 26-day EMA. A bearish centerline crossover occurs when the MACD moves below the zero line to turn negative. This happens when the 12-day EMA moves below the 26-day EMA.

Centerline crossovers can last a few days or a few months, depending on the strength of the trend. The MACD will remain positive as long as there is a sustained uptrend. The MACD will remain negative when there is a sustained downtrend. The next chart shows Pulte Homes (PHM) with at least four centerline crosses in nine months. The resulting signals worked well because strong trends emerged with these centerline crossovers.

<figure><img src="/files/6c1eJZ9pdK61TGOsnpxt" alt=""><figcaption></figcaption></figure>

Below is a chart of Cummins Inc (CMI) with seven centerline crossovers in five months. In contrast to Pulte Homes, these signals would have resulted in numerous whipsaws because strong trends did not materialize after the crossovers.

<figure><img src="/files/gHyNf0LWK1Q6IhTnJ3jG" alt=""><figcaption></figcaption></figure>

The next chart shows 3M (MMM) with a bullish centerline crossover in late March 2009 and a bearish centerline crossover in early February 2010. This signal lasted 10 months. In other words, the 12-day EMA was above the 26-day EMA for 10 months. This was one strong trend.

<figure><img src="/files/5MxIqhgsWHnlVsiILTCi" alt=""><figcaption></figcaption></figure>

## Divergences <a href="#divergences" id="divergences"></a>

[Divergences](/table-of-contents/glossary/glossary-d.md#divergence) form when the MACD diverges from the price action of the underlying security. A bullish divergence forms when a security records a lower low and the MACD forms a higher low. The lower low in the security affirms the current downtrend, but the higher low in the MACD shows less downside momentum. Despite decreasing, downside momentum is still outpacing upside momentum as long as the MACD remains in negative territory. Slowing downside momentum can sometimes foreshadow a trend reversal or a sizable rally.

The next chart shows Google (GOOG) with a bullish divergence in October-November 2008. First, notice that we are using closing prices to identify the divergence. The MACD's moving averages are based on closing prices and we should consider closing prices in the security as well. Second, notice that there were clear reaction lows (troughs) as both Google and its MACD line bounced in October and late November. Third, notice that the MACD formed a higher low as Google formed a lower low in November. The MACD turned up with a bullish divergence and a signal line crossover in early December. Google confirmed a reversal with a resistance breakout.

<figure><img src="/files/nhDAclYha7anS1doMHTI" alt=""><figcaption></figcaption></figure>

A bearish divergence forms when a security records a higher high and the MACD line forms a lower high. The higher high in the security is normal for an uptrend, but the lower high in the MACD shows less upside momentum. Even though upside momentum may be less, upside momentum is still outpacing downside momentum as long as the MACD is positive. Waning upward momentum can sometimes foreshadow a trend reversal or sizable decline.

Below we see Gamestop (GME) with a large bearish divergence from August to October. The stock forged a higher high above 28, but the MACD line fell short of its prior high and formed a lower high. The subsequent signal line crossover and support break in the MACD were bearish. On the price chart, notice how broken support turned into resistance on the throwback bounce in November (red dotted line). This throwback provided a second chance to sell or sell short.

<figure><img src="/files/TXB4rocl31DphfrhkZRQ" alt=""><figcaption></figcaption></figure>

Divergences should be taken with caution. Bearish divergences are commonplace in a strong uptrend, while bullish divergences occur often in a strong downtrend. Yes, you read that right. Uptrends often start with a strong advance that produces a surge in upside momentum (MACD). Even though the uptrend continues, it continues at a slower pace that causes the MACD to decline from its highs. Upside momentum may not be as strong, but it will continue to outpace downside momentum as long as the MACD line is above zero. The opposite occurs at the beginning of a strong downtrend.

The next chart shows the S\&P 500 ETF (SPY) with four bearish divergences from August to November 2009. Despite less upside momentum, the ETF continued higher because the uptrend was strong. Notice how SPY continued its series of higher highs and higher lows. Remember, upside momentum is stronger than downside momentum as long as the MACD is positive. The MACD (momentum) may have been less positive (strong) as the advance extended, but it was still largely positive.

<figure><img src="/files/4RNcs0dZUpmP6XErkeDf" alt=""><figcaption></figcaption></figure>

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

The MACD indicator is special because it brings together momentum and trend in one indicator. This unique blend of trend and momentum can be applied to daily, weekly or monthly charts. The standard setting for MACD is the difference between the 12- and 26-period EMAs. Chartists looking for more sensitivity may try a shorter short-term moving average and a longer long-term moving average. MACD(5,35,5) is more sensitive than MACD(12,26,9) and might be better suited for weekly charts. Chartists looking for less sensitivity may consider lengthening the moving averages. A less sensitive MACD will still oscillate above/below zero, but the centerline crossovers and signal line crossovers will be less frequent.

The MACD is not particularly good for identifying overbought and oversold levels. Even though it is possible to identify levels that are historically overbought or oversold, the MACD does not have any upper or lower limits to bind its movement. During sharp moves, the MACD can continue to over-extend beyond its historical extremes.

Finally, remember that the MACD line is calculated using the actual difference between two moving averages. This means MACD values are dependent on the price of the underlying security. The MACD values for a $20 stocks may range from -1.5 to 1.5, while the MACD values for a $100 may range from -10 to +10. It is not possible to compare MACD values for a group of securities with varying prices. If you want to compare momentum readings, you should use [the Percentage Price Oscillator (PPO)](/table-of-contents/technical-indicators-and-overlays/technical-indicators/percentage-price-oscillator-ppo.md), instead of the MACD.

***

## Using MACD With SharpCharts <a href="#using_macd_with_sharpcharts" id="using_macd_with_sharpcharts"></a>

The MACD can be set as an indicator above, below or behind a security's price plot. Placing the MACD “behind” the price plot makes it easy to compare momentum movements with price movements. Once the indicator is chosen from the drop-down menu, the default parameter setting appears: (12,26,9). These parameters can be adjusted to increase or decrease sensitivity. The MACD Histogram appears with the indicator or can be added as a separate indicator. Setting the signal line to 1 or leaving it blank, i.e. (12,26,1) or (12,26), will remove the MACD Histogram and the signal line. A separate signal line, without the histogram, can be added by choosing “Exp. Moving Avg” from the Advanced Options Overlays menu.

[Click here](https://stockcharts.com/sc3/ui/?s=$INDU\&p=D\&b=5\&g=0\&id=p18754900449\&listNum=30\&a=199515976) for a live chart of the MACD indicator.

<figure><img src="/files/IQRvKI1lgcFPzQGmgQtm" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/SeJr27hzH3EWLSoFvYlB" alt=""><figcaption></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

Here are some sample scans that StockCharts members can use to scan for various MACD signals:

### MACD Bullish Signal Line Cross <a href="#macd_bullish_signal_line_cross" id="macd_bullish_signal_line_cross"></a>

This scan reveals stocks that are trading above their 200-day moving average and have a bullish signal line crossover in MACD. Notice that MACD is required to be negative to ensure this upturn occurs after a pullback. This scan is just meant as a starter for further refinement.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 40000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Daily Close > Daily SMA(200,Daily Close)] 
AND [Yesterday's Daily MACD Line(12,26,9,Daily Close) < Daily MACD Signal(12,26,9,Daily Close)] 
AND [Daily MACD Line(12,26,9,Daily Close) > Daily MACD Signal(12,26,9,Daily Close)] 
AND [Daily MACD Line(12,26,9,Daily Close) < 0]
```

### MACD Bearish Signal Line Cross <a href="#macd_bearish_signal_line_cross" id="macd_bearish_signal_line_cross"></a>

This scan reveals stocks that are trading below their 200-day moving average and have a bearish signal line crossover in MACD. Notice that MACD is required to be positive to ensure this downturn occurs after a bounce. This scan is just meant as a starter for further refinement.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 40000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Daily Close < Daily SMA(200,Daily Close)] 
AND [Yesterday's Daily MACD Line(12,26,9,Daily Close) > Daily MACD Signal(12,26,9,Daily Close)] 
AND [Daily MACD Line(12,26,9,Daily Close) < Daily MACD Signal(12,26,9,Daily Close)] 
AND [Daily MACD Line(12,26,9,Daily Close) > 0]
```

{% hint style="info" %}
For more details on the syntax to use for MACD scans, please see our [Scan Syntax Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#macd_line_macd_line) in the Support Center.
{% endhint %}

***

## MACD FAQs <a href="#macd_faqs" id="macd_faqs"></a>

<details>

<summary>What does the MACD indicate in trading?</summary>

The MACD can be used to analyze the state of the price action and identify potential buy and sell signals. Traders look for signal line crossovers, centerline crossovers, and divergences to generate signals. Positive MACD values indicate that the 12-day EMA is above the 26-day EMA, suggesting increasing upside momentum, while negative values suggest increasing downside momentum.

</details>

<details>

<summary>What is the difference between signal line crossovers and centerline crossovers in MACD?</summary>

Signal line crossovers occur when the MACD line crosses above or below the signal line, indicating bullish or bearish signals, respectively. Centerline crossovers occur when the MACD line crosses above or below the zero line, implying that the shorter-term EMA has crossed the longer-term EMA. This can suggest a change in the overall trend of the market.

</details>

<details>

<summary>Can the MACD be used to identify overbought and oversold levels?</summary>

The MACD is not particularly useful for identifying overbought and oversold levels as it does not have upper or lower limits to bind its movement. During sharp moves, the MACD can continue to over-extend beyond its historical extremes.

</details>

<details>

<summary>What is the standard setting for MACD?</summary>

The standard setting for MACD is the difference between the 12- and 26-period Exponential Moving Averages (EMAs). However, these values can be adjusted to increase or decrease sensitivity depending on the trader's style and goals.

</details>

<details>

<summary>Can MACD values be compared for different securities?</summary>

It's important to note that MACD values are dependent on the price of the underlying security, meaning it's not possible to compare MACD values for a group of securities with varying prices. For comparing momentum readings across different securities, the Percentage Price Oscillator (PPO) should be used instead of the MACD.

</details>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
