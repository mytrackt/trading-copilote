> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-histogram.md).

# MACD-Histogram

## What Is the MACD Histogram? <a href="#what_is_the_macd_histogram" id="what_is_the_macd_histogram"></a>

The MACD-Histogram measures the distance between the [Moving Average Convergence/Divergence](/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator.md) (MACD) and its signal line (the 9-day EMA of MACD). Like MACD, the MACD-Histogram is also an oscillator that fluctuates above and below the zero line.&#x20;

Thomas Aspray developed the MACD-Histogram to anticipate signal line crossovers in MACD. Because MACD uses moving averages and moving averages lag price, signal line crossovers can come late and affect the reward-to-risk ratio of a trade. Bullish or bearish divergences in the MACD-Histogram can alert you to an imminent signal line crossover in MACD.&#x20;

## How Do You Calculate the MACD Histogram? <a href="#how_do_you_calculate_the_macd_histogram" id="how_do_you_calculate_the_macd_histogram"></a>

```
MACD: (12-day EMA - 26-day EMA) 

Signal Line: 9-day EMA of MACD

MACD Histogram: MACD - Signal Line
```

Standard MACD is the 12-day Exponential [Moving Average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) (EMA) less the 26-day EMA. Closing prices are used to form the MACD's moving averages. A 9-day EMA of MACD is plotted along side to act as a signal line to identify turns in the indicator. Since the MACD-Histogram represents the difference between MACD and its 9-day EMA (signal line), the histogram is positive when MACD is above its 9-day EMA and negative when MACD is below its 9-day EMA.

<figure><img src="/files/DJ33W4h5ATcGSO0ysUy7" alt="Chart from StockCharts.com showing the MACD indicator and identifying the signal line, the MACD histogram, and the MACD line."><figcaption><p>Example of the MACD.</p></figcaption></figure>

## How Is the MACD Four Steps Removed From a Stock's Price? <a href="#how_is_the_macd_four_steps_removed_from_a_stock_s_price" id="how_is_the_macd_four_steps_removed_from_a_stock_s_price"></a>

The MACD-Histogram is an indicator of an indicator. The MACD itself is an indicator of an indicator. This means that the MACD-Histogram is four steps removed from the price of the underlying security. In other words, it is the fourth derivative of price.

* First derivative: 12-day EMA and 26-day EMA
* Second derivative: MACD (12-day EMA less the 26-day EMA)
* Third derivative: MACD signal line (9-day EMA of MACD)
* Fourth derivative: MACD-Histogram (MACD less MACD signal line)

The base for this indicator is the security's price. It takes four steps to get from the price to the MACD-Histogram. Talk about massaging the data. While not necessarily a bad thing, keep this in mind when analyzing the MACD-Histogram. It is an indicator of an indicator. Therefore, it's designed to anticipate signals in MACD, which in turn is designed to identify changes in the price [momentum](/table-of-contents/technical-indicators-and-overlays/technical-indicators/rate-of-change-roc.md) of the underlying security.

## How Do You Interpret the MACD Histogram? <a href="#how_do_you_interpret_the_macd_histogram" id="how_do_you_interpret_the_macd_histogram"></a>

Like the MACD, the MACD-Histogram is also designed to identify convergence, divergence, and crossovers. The MACD-Histogram, however, measures the distance between MACD and its signal line. The histogram is positive when MACD is above its signal line. Positive values increase as MACD diverges further from its signal line (to the upside) and decrease as MACD and its signal line converge. The MACD-Histogram crosses the zero line as MACD crosses below its signal line. The indicator is negative when MACD is below its signal line. Negative values increase as MACD diverges further from its signal line (to the downside). Conversely, negative values decrease as MACD converges on its signal line.

The chart below shows the MACD and MACD-Histogram. A bearish signal line crossover occurred in late September, turning the MACD-Histogram negative. A bullish signal line crossover occurred in early December, turning the MACD-Histogram positive for the rest of the month. There was a period of divergence as MACD moved further from its signal line (green line) and a period of convergence as MACD moved closer to its signal line (red line).

<figure><img src="/files/chL5fVyuDl8M0Oyl5kxy" alt="Chart from StockCharts.com showing the MACD and MACD Histogram and how to interpret crossovers, convergences, and divergences."><figcaption><p>MACD and MACD Histogram showing crossovers, convergences, and divergences. </p></figcaption></figure>

## How Do You Interpret Peak-Trough Divergence Using the MACD Histogram? <a href="#how_do_you_interpret_peak-trough_divergence_using_the_macd_histogram" id="how_do_you_interpret_peak-trough_divergence_using_the_macd_histogram"></a>

The MACD-Histogram anticipates signal line crossovers in MACD by forming bullish and [bearish divergences](/table-of-contents/glossary/glossary-b.md#bearish_divergence). These divergences signal that MACD is converging on its signal line and could be ripe for a cross.&#x20;

There are two types of divergences: peak-trough and slant. A peak-trough divergence forms with two peaks or two troughs in the MACD-Histogram. A peak-trough bullish divergence forms when MACD forges a lower low and the MACD-Histogram forges a higher low. Well-defined troughs are important to the robustness of a peak-trough divergence. Chart 2 shows Caterpillar with a bullish divergence in the MACD-Histogram. Notice that MACD moved to a lower low in June-July, but the MACD-Histogram formed a higher low (trough). There are two distinct troughs. This bullish divergence foreshadowed the bullish signal line crossover in mid-July and a big rally.

<figure><img src="/files/kKZENJ8PFWsVhTJzgHta" alt=""><figcaption><p>MACD-Histogram - Chart 2</p></figcaption></figure>

Chart 3 shows Aeropostale (ARO) with a bearish divergence in August-September 2009. MACD moved to a new high in September, but the MACD-Histogram formed a lower high. Notice that there are two definitive peaks (higher) with a dip in between on the MACD-Histogram (red line). The subsequent bearish signal line crossover foreshadowed a sharp decline in the stock.

<figure><img src="/files/iFowcFy4gTnaea2h4sGs" alt=""><figcaption><p>MACD-Histogram - Chart 3</p></figcaption></figure>

## Slant Divergence <a href="#slant_divergence" id="slant_divergence"></a>

As its name implies, slant divergences form without well-defined peaks or troughs. Instead of two reaction highs, there is simply a slant lower as the MACD-Histogram moves towards the zero line. A MACD-Histogram slant towards the zero line reflects a convergence between MACD and its signal line. In other words, they are getting closer to each other. Momentum shows strength when MACD is moving away from its signal line and the MACD-Histogram expands. Momentum weakens as MACD moves closer to its signal line and the MACD-Histogram contracts. Contracting MACD-Histogram is the first step towards a signal line crossover.

Chart 4 shows Boeing with a classic slant divergence in the MACD-Histogram. MACD moved sharply lower after the bearish signal line crossover in June 2009. MACD moved to a new low in mid-July, but the MACD-Histogram held well above its prior low. In fact, the MACD-Histogram bottomed towards the end of June and formed a bullish slant divergence. The thick red lines show the distance between MACD and its signal line. It is sometimes hard to gauge distance on the chart so these lines highlight the difference between 26-June and 8-July. This slant divergence foreshadowed the bullish signal line crossover in mid-July and a sharp advance in the stock.

<figure><img src="/files/9tIYG9YIVgcppJameKLI" alt=""><figcaption><p>MACD-Histogram - Chart 4</p></figcaption></figure>

Chart 5 shows Disney (DIS) with a bearish slant divergence in May 2008. Notice how MACD continued to a new high on 16-May, but the MACD-Histogram peaked on 8-May and formed a slant divergence. The advance in MACD was losing momentum and the indicator moved below its signal line to foreshadow a sharp decline in the stock. This chart also shows a nice bullish divergence in March-April.

<figure><img src="/files/vlREcSsSs1QQgho6VjoS" alt=""><figcaption><p>MACD-Histogram - Chart 5</p></figcaption></figure>

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

The MACD-Histogram is an indicator designed to predict signal line crossovers in MACD. By extension, it is designed as an early warning system for these signal line crossovers, which are the most frequent of MACD signals. Divergences in the MACD-Histogram can be used to filter signal line crossovers, which will reduce the number of signals. Even with a filter, the robustness of MACD-Histogram divergences is still an issue. Short and shallow divergences are much more frequent than long and large divergences. In other words, divergences that develop over a few days with shallow movements are generally less robust than divergences that develop over a few weeks with more pronounced movements. The signal line crossover provides the ultimate confirmation, but aggressive traders may try to improve the reward-to-risk ratio by making their move just before the crossover. This is when the MACD-Histogram is as close to the zero line as it can be without actually making a cross, usually between -.20 and +.20.

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

MACD comes with the MACD-Histogram, but the MACD-Histogram can be shown as a stand-alone indicator. This makes it much easier to identify divergences and crossovers. The MACD-Histogram can be set as an indicator above, below or behind the price plot of the underlying security. The histogram covers a lot of chart space so it is often best to place it above or below the main window. It is possible to show MACD without the histogram in the main window. Choose MACD as an indicator and change the signal line number from 9 to 1 (9,26,1). This will remove the signal line and the histogram. The signal line can be added separately by clicking the advanced indicator options and adding a 9-day EMA.

[Click here for a live chart](https://stockcharts.com/sc3/ui/?s=$INDU\&p=D\&b=5\&g=0\&id=p59749230423\&listNum=30\&a=199515976) featuring the MACD-Histogram.

<figure><img src="/files/sDLXZ2QKqOHufARAaNsY" alt=""><figcaption><p>MACD-Histogram - Chart 6</p></figcaption></figure>

<figure><img src="/files/plBnANQQnXSin51eJePr" alt=""><figcaption><p>MACD - Chart 7</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### MACD-Histogram Turns Positive <a href="#macd-histogram_turns_positive" id="macd-histogram_turns_positive"></a>

First, this scan only considers stocks trading above their 200-day moving average, which implies an uptrend overall. Second, the MACD-Histogram moves from negative territory to positive territory. Also notice that MACD is required to be negative to ensure this upturn occurs after a pullback. This scan is just meant as a starter for further refinement.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [Daily Close > Daily SMA(200,Daily Close)]
AND [Yesterday's Daily MACD Hist(12,26,9,Daily Close) < 0]
AND [Daily MACD Hist(12,26,9,Daily Close) > 0]
AND [Daily MACD Line(12,26,9,Daily Close) < 0]
```

### MACD-Histogram Turns Negative <a href="#macd-histogram_turns_negative" id="macd-histogram_turns_negative"></a>

First, this scan only considers stocks trading below their 200-day moving average, which implies a downtrend overall. Second, the MACD-Histogram moves from positive territory to negative territory. Also notice that MACD is required to be positive to ensure this downturn occurs after a bounce. This scan is just meant as a starter for further refinement.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [Daily Close < Daily SMA(200,Daily Close)]
AND [Yesterday's Daily MACD Hist(12,26,9,Daily Close) > 0]
AND [Daily MACD Hist(12,26,9,Daily Close) < 0]
AND [Daily MACD Line(12,26,9,Daily Close) > 0]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax for MACD-Histogram scans, please see our [Scan Syntax Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#macd_histogram_macd_hist) in the Support Center.
{% endhint %}

***

## MACD-Histogram FAQs <a href="#macd_histogram_faqs" id="macd_histogram_faqs"></a>

<details>

<summary>What is meant by the MACD-Histogram being "four steps removed" from the price of a security?</summary>

This means that the MACD-Histogram is an indicator of an indicator, with four steps between it and the actual price. These steps are: 12-day EMA and 26-day EMA, MACD (12-day EMA minus the 26-day EMA), MACD signal line (9-day EMA of MACD), and MACD-Histogram (MACD less MACD signal line).

</details>

<details>

<summary>What role does the MACD-Histogram play in analyzing price action?</summary>

The MACD-Histogram serves as an early warning system for MACD signal line crossovers, which are the most frequent MACD signals. It helps to predict potential shifts in the market and assist traders in making informed decisions.

</details>

<details>

<summary>How reliable are divergences in the MACD-Histogram?</summary>

While divergences can be used to filter signal line crossovers, the robustness of MACD-Histogram divergences is still an issue. Short and shallow divergences are much more frequent than long and large divergences. Divergences that develop over a few days with shallow movements are generally less robust than divergences that develop over a few weeks with more pronounced movements.

</details>

<details>

<summary>What is a slant divergence in the MACD-Histogram?</summary>

Slant divergences form without well-defined peaks or troughs. Instead, the divergence between a stock’s price and the MACD histogram is visible through a slant in the price action.

</details>

<details>

<summary>How might a trader make an aggressive entry based on the MACD-Histogram?</summary>

While the signal line crossover provides the ultimate confirmation, aggressive traders may try to improve the reward-to-risk ratio by making their move just before the crossover. This is when the MACD-Histogram is as close to the zero line as it can be without actually making a cross, usually between -0.20 and +0.20.

</details>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-histogram.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
