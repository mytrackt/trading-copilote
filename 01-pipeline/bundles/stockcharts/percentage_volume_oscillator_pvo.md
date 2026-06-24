> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/percentage-volume-oscillator-pvo.md).

# Percentage Volume Oscillator (PVO)

## What Is the Percentage Volume Oscillator (PVO) <a href="#introduction" id="introduction"></a>

The Percentage Volume Oscillator (PVO) is a momentum oscillator for volume. The PVO measures the difference between two volume-based moving averages as a percentage of the larger moving average. As with MACD and the [Percentage Price Oscillator (PPO)](/table-of-contents/technical-indicators-and-overlays/technical-indicators/percentage-price-oscillator-ppo.md), it is shown with a signal line, a histogram and a centerline. The PVO is positive when the shorter volume EMA is above the longer volume EMA and negative when the shorter volume EMA is below. This indicator can be used to define the ups and downs for volume, which can then be used to confirm or refute other signals. Typically, a breakout or support break is validated when the PVO is rising or positive.

## Calculating the Percentage Volume Oscillator <a href="#calculation" id="calculation"></a>

```
Percentage Volume Oscillator (PVO):
((12-day EMA of Volume - 26-day EMA of Volume)/26-day EMA of Volume) x 100

Signal Line: 9-day EMA of PVO

PVO Histogram: PVO - Signal Line
```

The default settings for the PVO are (12,26,9), which is the same as MACD or the PPO. This means the PVO is positive when the 12-day Volume EMA moves above the 26-day Volume EMA. The PVO is negative when the 12-day Volume EMA moves below the 26-day Volume EMA.

The positive or negative degree of PVO depends on how far the 12-day Volume EMA is above or below the 26-day Volume EMA. A PVO that equals 5 would indicate that the 12-day Volume EMA was 5% above the 26-day Volume EMA. A PVO that equals -3% would indicate that the 12-day Volume EMA was 3% less than the 26-day Volume EMA.

The PVO-Histogram acts just like the MACD and PPO histograms. The PVO-Histogram is positive when the PVO is trading above its signal line (9-day EMA). The PVO-Histogram is negative when the PVO is below its signal line. Note that the PVO is multiplied by 100 to move the decimal point two places.

<figure><img src="/files/M95k3kaOAHhPm5scinHO" alt=""><figcaption><p>PVO - Chart 1</p></figcaption></figure>

## Interpreting the Percentage Volume Oscillator <a href="#interpretation" id="interpretation"></a>

Generally speaking, volume is above average when the PVO is positive and below average when the PVO is negative. A negative and rising PVO indicates that volume levels are increasing. A positive and falling PVO indicates that volume levels are decreasing. Chartists can use this information to confirm or refute movements on the price chart.

Even though the PVO is based on a momentum oscillator formula, it is important to remember that moving averages lag. A 12-day EMA include 12 days of volume data, with newer data weighted more heavily. A 26-day EMA lags even more because it contains 26 days of data. This means that the PVO(12,26,9) can sometimes be out of sync with price action.

### Validating Breaks <a href="#validating_breaks" id="validating_breaks"></a>

The Percentage Volume Oscillator (PVO) can be used to confirm a [support or resistance](/table-of-contents/chart-analysis/support-and-resistance.md) break. We have all heard that volume validates a price movement. A support break on increasing volume has more credibility than a support break on low volume. Similarly, a resistance break on expanding volume shows more buying interest, increasing the chances of success.

The chart below shows Volero (VLO) with the PVO(12,26,9) confirming a [pennant](/table-of-contents/chart-analysis/chart-patterns/flag-pennant.md) breakout. Volume declined in August as the PVO moved lower until mid-September. The PVO then turned up, but did not move into positive territory until late October. This meant the 12-day Volume EMA finally crossed above the 26-day EMA and volume was increasing. VLO was still stuck in the pennant on the first PVO cross, but broke pennant resistance with the second PVO cross. Volume confirmed the breakout and VLO continued its advance.

<figure><img src="/files/uFXJAcxLvuDBeQTnGqC6" alt=""><figcaption><p>PVO - Chart 2</p></figcaption></figure>

The chart for Archer Daniels Midland (ADM) shows a support and resistance break confirmed by surges in the PVO. The stock broke resistance at the beginning of August as the PVO moved into positive territory with a sharp surge. Expanding volume on an upside breakout is bullish. After a three-month run, the stock broke support with a gap and another surge in the PVO. Notice how the PVO surged to 20 both times. This meant that the 12-day Volume EMA was some 20% above the 26-day Volume EMA.

<figure><img src="/files/qdhLpqzztIeUrSadmGB8" alt=""><figcaption><p>PVO - Chart 3</p></figcaption></figure>

### Fine-Tuning the PVO <a href="#fine-tuning_the_pvo" id="fine-tuning_the_pvo"></a>

Chartists can fine-tune the PVO to highlight volume surges for a specific period. There are around 250 trading days in a year. Therefore, a 250-day EMA would represent average annual volume with a weighting towards the most recent periods. Using this for the long EMA in the PVO, we can choose a short EMA to highlight volume surges that are above this average. A PVO(1,250) would be positive when the 1-day volume was above the 250-day Volume EMA. A PVO(5,250) would be positive when the 5-day Volume EMA is above the 250-day EMA.

The chart for Merck (MRK) shows volume bars with a 5-day EMA in blue and a 250-day EMA in red. The PVO(1,250) is shown in the first indicator window (green) and the PVO(5,250) is shown in the lower indicator window (black). The signal line is not shown because there is no parameter entered. PVO(5,250,9) would show the PVO with a 9-day EMA for the signal line.

<figure><img src="/files/yjMNX6O1rGM1EmkWaj6U" alt=""><figcaption><p>PVO - Chart 4</p></figcaption></figure>

From the chart above, we can see that the PVO(1,250) turned positive when a volume bar surged above the 250-day EMA (green arrows). The PVO(5,250) turned positive when the 5-day Volume EMA moved above the 250-day Volume EMA (blue arrows). As one might expect, PVO(1,250) crosses the zero line more often and is just a little bit quicker. Basically, volume is above average when PVO(1,250) is positive and below average when negative. A breakout on above-average volume is more robust than one with below-average volume. The same is true for a support break.

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The Percentage Volume Oscillator (PVO) is a momentum indicator applied to volume. This oscillator can be quite choppy due to the fact that volume doesn't trend. Bullish and bearish divergences are not well suited for the PVO. Instead, chartists would be better off looking for signs of increasing volume with a move into positive territory and signs of decreasing volume with a move into negative territory. Increasing volume can validate a support or resistance break. Similarly, a surge or significant support break on low volume may be less robust. As with all technical indicators, it is important to use the Percentage Volume Oscillator (PVO) in conjunction with other aspects of technical analysis, such as [chart patterns](/table-of-contents/chart-analysis/chart-patterns.md) and [momentum oscillators](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#momentum_oscillators).

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

PVO can be set as an indicator above, below, or behind a security's price plot. When you select the indicator from the dropdown list, the default parameters will appear (12,26,9). These parameters can be adjusted, as shown in the example below. Click “advanced options” to add the moving average or a horizontal line to an indicator. In the example below, volume was added as an indicator twice in order to show two moving averages. The second volume indicator was placed behind the first volume indicator (behind ind) and the EMA was set at 250 with the Advanced Options.&#x20;

***

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line">[Click here for a live example of the PVO](https://stockcharts.com/sc3/ui/?s=IBM\&p=D\&yr=0\&mn=6\&dy=0\&id=p28625227150\&listNum=30\&a=217316123).

***

<figure><img src="/files/x0Ovzol2qphPOoYiUFcL" alt=""><figcaption><p>PVO - Chart 5</p></figcaption></figure>

<figure><img src="/files/9ZKWpSCYdy7BGILNHiui" alt=""><figcaption><p>PVO - Chart 6</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### PPO Bullish Cross with PVO Positive <a href="#ppo_bullish_cross_with_pvo_positive" id="ppo_bullish_cross_with_pvo_positive"></a>

This scan reveals stocks where the PPO(12,26,9) moved above the PPO Signal Line and the PVO(12,26,9) moved into positive territory to show increasing volume. This scan is just meant as a starter for further refinement.

{% code overflow="wrap" %}

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]
AND [Daily PPO Line(12,26,9,Daily Close) crosses Daily PPO Signal(12,26,9,Daily Close)]
AND [Daily PVO Line(12,26,9) crosses 0]
```

{% endcode %}

### PPO Bearish Cross with PVO Positive <a href="#ppo_bearish_cross_with_pvo_positive" id="ppo_bearish_cross_with_pvo_positive"></a>

This scan reveals stocks where the PPO(12,26,9) moved below the PPO Signal Line and the PVO(12,26,9) moved into positive territory to show increasing volume. This scan is just meant as a starter for further refinement.

{% code overflow="wrap" %}

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]
AND [Daily PPO Signal(12,26,9,Daily Close) crosses Daily PPO Line(12,26,9,Daily Close)]
AND [Daily PVO Line(12,26,9) crosses 0]
```

{% endcode %}

{% hint style="info" %}
**Learn More.** For more details on the syntax for PVO scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#pvo_line_pvo_line) in the Support Center.
{% endhint %}

{% hint style="warning" %}
**Note**: For scanning purposes, daily volume data is incomplete during the trading day. When running scans with volume-based indicators like the PVO, be sure to base the scan on the “Last Market Close.” Examples of other volume-based indicators include Accumulation/Distribution, Chaikin Money Flow, and On Balance Volume.
{% endhint %}

## Additional Resources <a href="#further_study" id="further_study"></a>

### Recommended Books

John Murphy's [*Technical Analysis of the Financial Markets*](https://a.co/d/1eLUbD7) covers all the bases for technical analysis with sections explaining volume, open interest, and volume indicators. Murphy discusses the importance of volume and shows many chart examples.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/percentage-volume-oscillator-pvo.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
