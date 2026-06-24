> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/vortex-indicator.md).

# Vortex Indicator

## What Is the Vortex Indicator?

Developed by Etienne Botes and Douglas Siepman, the Vortex Indicator consists of two oscillators that capture positive and negative trend movement. In creating this indicator, Botes and Seipman drew on the work of Welles Wilder and Viktor Schauberger, who is considered the father of implosion technology. Despite a rather involved formula, the indicator is quite easy to interpret. A bullish signal triggers when the positive trend indicator crosses above the negative trend indicator or a key level. A bearish signal triggers when the negative trend indicator crosses above the positive trend indicator or a key level. The Vortex Indicator is either above or below these levels, which means it always has a clear bullish or bearish bias.

## SharpCharts Calculation <a href="#sharpcharts_calculation" id="sharpcharts_calculation"></a>

<figure><img src="/files/yd8Rj4RvICKtfHEqYrvE" alt=""><figcaption><p>Chart 1</p></figcaption></figure>

Calculation of the Vortex Indicator (VTX) can be divided into three parts. First, calculate the positive and negative trend movements based on the highs and lows of the last two periods. Positive trend movement is the distance from the current high to the prior low. The further the current high is from the prior low, the more positive the trend movement. Negative trend movement is the distance from the current low to the prior high. The further the current low is from the prior high, the more negative the trend movement. These periodic values are then summed based on the indicator setting, which is the usually 14 periods.

The second part involves the True Range, which was created by Welles Wilder. This indicator uses the current high, current low and prior close to measure volatility. See the formula box below for details.

The third part normalizes the positive and negative trend movements by dividing them by the True Range. In effect, the Vortex Indicator shows volatility-adjusted positive trend movement and volatility-adjusted negative trend movement. The end result creates two indicators that oscillate above/below 1.

```
Positive and negative trend movement:

+VM = Current High less Prior Low (absolute value)
-VM = Current Low less Prior High (absolute value)

+VM14 = 14-period Sum of +VM
-VM14 = 14-period Sum of -VM


True Range (TR) is the greatest of:

  * Current High less current Low
  * Current High less previous Close (absolute value)
  * Current Low less previous Close (absolute value)

TR14 = 14-period Sum of TR

Normalize the positive and negative trend movements:

+VI14 = +VM14/TR14
-VI14 = -VM14/TR14
```

<figure><img src="/files/G3EeYwTN5eab6LFHYGlM" alt=""><figcaption><p>Spreadsheet</p></figcaption></figure>

For Vortex Indicator calculations, download the spreadsheet below.

{% file src="/files/jA1hMKJ0ReTPZD64jp1E" %}

## Interpreting the Vortex Indicator  <a href="#interpretation" id="interpretation"></a>

The Vortex Indicator (VTX) can be used to identify the start of a trend and subsequently affirm trend direction. First, a simple cross of the two oscillators can be used to signal the start of a trend. After this crossover, the trend is up when +VI is above -VI and down when -VI is greater than +VI. Second, a cross above or below a particular level can signal the start of a trend and these levels can be used to affirm trend direction.

## VM Crossovers <a href="#vm_crossovers" id="vm_crossovers"></a>

The simplest signal triggers when +VI and -VI cross. The example below shows the Invesco QQQ Trust ETF (QQQ) using weekly bars and a 26-period VTX, which amounts to around six months. There were over a dozen crossovers in a six-and-a-half-year period. The yellow areas show bullish crossovers that lasted more than six months. This is what happens in a strong uptrend. There was also a significant bearish crossover in the second half of 2008. Even though there were plenty of good signals, there were also whipsaws. This is simply the nature of of indicators. The blue circles show periods of indecision when both trend indicators hovered around 1 and the S\&P 500 consolidated.

<figure><img src="/files/5DIah7gvCSW7RZz0QzHQ" alt=""><figcaption><p>Chart 2</p></figcaption></figure>

The second example shows Baxter (BAX) using daily charts and the 23-period VTX, which covers around one month. Not every crossover results in a clear trend signal. Notice how VTX traded in a narrow range around 1 from October to early November (yellow area). This marked a consolidation as prices formed a triangle. There were some whipsaws at the beginning of 2012 (blue circle) and then a few good signals later in the year. It sometimes helps to qualify a signal by waiting for confirmation with a move above 1. A bullish crossover is further validated when +VM moves above 1 and a bearish crossover is validated when -VM moves above 1.

<figure><img src="/files/GWzh60s9PEQLY0ij2MoZ" alt=""><figcaption><p>Chart 3</p></figcaption></figure>

## VM Thresholds <a href="#vm_thresholds" id="vm_thresholds"></a>

Traders can reduce whipsaws by setting signal thresholds just above and below 1. A bullish signal can be divided into two parts. First, downward trend movement weakens. Second, upward trend movement strengthens. -VI often weakens and moves below 0.90 before an uptrend starts. After this weakening in downward trend movement, upward movement strengthens as +VI moves above 1.10 to complete the bullish signal. This bullish signal remains in play until countered by a bearish signal. The reverse logic can be applied to generate bearish signals. First, upward trend movement weakens with a move below 0.90. Second, downward trend movement strengthens with a move above 1.10.

<figure><img src="/files/6bwwc7DWWPtVJgFX2TYl" alt=""><figcaption><p>Chart 4</p></figcaption></figure>

The chart above shows Microchip Technology using a daily chart and 23-period VTX. Despite numerous crosses of the two oscillators, there were only three “threshold” signals over twelve months. First, -VM moved below 0.90 in early September, and +VI crossed above 1.1 a few days later. Even though +VM moved below 0.90 several times, this bullish signal was not completely reversed because -VI never confirmed with a move above 1.10. The second signal occurred when +VI moved below 0.90 in late February and -VI crossed above 1.1 in early March. The third signal occurred when -VI dipped below 0.90 in mid-June and +VI crossed above 1.1 a few days later.

Decreasing the look-back period will increase sensitivity and result in more threshold crosses. For example, a daily chart with a 14-period VTX will be much more sensitive (volatile) than the 23-period version.&#x20;

Keep in mind that VTX is not designed as a standalone indicator. Chartists should use other aspects of technical analysis to confirm VTX, improve the reward-to-risk ratio for a trade setup, or derive buy-sell signals. The bullish VTX signal in early January was confirmed by a wedge breakout. After the bearish VTX signal in April, CMI formed a rising wedge and broke wedge support with a sharp decline in early May. VTX provided the alert and the price chart provided the signals.

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The Vortex Indicator is a unique directional indicator that provides clear signals and defines the overall trend. As with all technical analysis tools and indicators, the Vortex Indicator can be used on a range of securities and across various timeframes. For example, VTX can be applied to weekly and monthly charts to define the bigger trend and then applied to daily charts to generate signals within that trend. Using the daily chart, chartists could focus exclusively on bullish signals when VTX on the weekly chart indicates an uptrend. Conversely, chartists can focus on bearish signals when VTX on the daily chart is in bear mode.

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Vortex Index is available as an indicator for SharpCharts. Once selected, users can place the indicator above, below or behind the underlying price plot. Placing the indicator directly behind the price plot accentuates the movements relative to the price action of the underlying security. Users can apply “advanced options” to add horizontal lines and set signal thresholds. [Click here](https://stockcharts.com/sc3/ui/?s=$COMPQ\&p=D\&yr=0\&mn=6\&dy=0\&id=p98321339986\&a=277125891) for a live example of the Vortex Indicator in action.

<figure><img src="/files/25gWKdbwb50mwgJcEptQ" alt=""><figcaption><p>Chart 6</p></figcaption></figure>

<figure><img src="/files/LnuaQLtLnqN5PIRLrzrV" alt=""><figcaption></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Overall Uptrend with +VI Crossing above -VI <a href="#overall_uptrend_with_vi_crossing_above_-vi" id="overall_uptrend_with_vi_crossing_above_-vi"></a>

This scan starts with stocks that average 100,000 shares daily volume and have an average closing price above 10. An uptrend is present when trading above the 50-day SMA. A buy signal materializes when +VI crosses above -VI.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 10]

AND [Daily VTX Plus(14) x Daily VTX Minus(14)]
AND [Daily Close > Daily SMA(50,Daily Close)]
```

### Overall Downtrend with -VI Crossing above +VI <a href="#overall_downtrend_with_-vi_crossing_above_vi" id="overall_downtrend_with_-vi_crossing_above_vi"></a>

This scan starts with stocks that average 100,000 shares daily volume and have an average closing price above 10. An downtrend is present when trading below the 50-day SMA. A sell signal materializes when -VI crosses above +VI.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 10]

AND [Daily VTX Minus(14) x Daily VTX Plus(14)]
AND [Daily Close < Daily SMA(50,Daily Close)]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax to use for Vortex Indicator scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#vortex_indicator) in the Support Center.
{% endhint %}

## Further Study <a href="#further_study" id="further_study"></a>

| <p><a href="https://a.co/d/8uzuEYz"><strong>Technical Analysis of the Financial Markets</strong></a><br>John J. Murphy</p> | <p><a href="https://a.co/d/ccJMNp8"><strong>Technical Analysis Explained by Martin Pring</strong></a><br>Martin Pring</p> |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/vortex-indicator.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
