> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/negative-volume-index-nvi.md).

# Negative Volume Index (NVI)

## What Is the Negative Volume Index (NVI)? <a href="#introduction" id="introduction"></a>

The Negative Volume Index (NVI) is a cumulative indicator that uses the change in volume to decide when the smart money is active. Paul Dysart first developed this indicator in the 1930s. Dysart's Negative Volume Index works under the assumption that the smart money is active on days when volume decreases and the not-so-smart money is active on days when volume increases.

## SharpCharts Calculation <a href="#sharpcharts_calculation" id="sharpcharts_calculation"></a>

There are two versions of the Negative Volume Index. In the original version, Dysart formed a cumulative line by adding Net Advances when volume decreased from one period to the other. Net Advances equal advancing issues less declining issues. The cumulative NVI line was unchanged when volume increased from one period to the other. In other words, nothing was done. Norman Fosback (author of *Stock Market Logic*) adjusted the indicator by substituting the percentage price change for Net Advances. The SharpCharts formula uses this Fosback version.

```
1. Cumulative NVI starts at 1000

2. Add the Percentage Price Change to Cumulative NVI when Volume Decreases

3. Cumulative NVI is Unchanged when Volume Increases

4. Apply a 255-day EMA for Signals
```

<figure><img src="/files/W3tGrE4wiWsRJuUgXQuW" alt=""><figcaption><p>Chart 1</p></figcaption></figure>

The spreadsheet example shows the calculation in detail. The Price %Change was multiplied by 100 to reduce the number of decimal places needed. First, notice the Volume %Change column. When this value is negative, the percentage change for the S\&P 500 is entered into the NVI Value column. When this value is positive, nothing appears for the NVI Value. Starting at 1000, the NVI Values are applied each period to create a cumulative indicator that only changes when volume decreases.

<figure><img src="/files/mxMnR3DJ1ORDsTiqpxRf" alt=""><figcaption><p>Spreadsheet 1</p></figcaption></figure>

Click below to download this spreadsheet example.

{% file src="/files/6yytyVizLCCz2LV2eAD1" %}

## Signal <a href="#signal" id="signal"></a>

The traditional use of the Negative Volume Index is quite simple. According to Fosback, the odds favor a bull market when NVI is above its 255-day EMA and the odds favor a bear market when NVI is below. However, Fosback notes that these odds are not symmetrical. There is a 96% chance of a bull market when NVI is above its 255-day EMA, but only a 53% chance of a bear market when NVI is below its 255-day EMA.

<figure><img src="/files/g3bxzQzWaNWhnyBLYIiN" alt=""><figcaption><p>Chart 2</p></figcaption></figure>

The chart above shows the Dow Industrials with NVI in the lower window. Even with a long-term moving average, there are plenty of whipsaws (bad signals). Notice how the indicator crossed the 255-day EMA several times in 1998-1998 as it zigzagged higher. There were also several crosses in 2001-2002 as trading in the Dow Industrials turned volatile. The signals from late 2002 were less prone to whipsaw as stronger trends emerged. Chartists can expect some lag because moving averages lag and a 255-day EMA is being used to generate signals.

## Fine Tuning <a href="#fine_tuning" id="fine_tuning"></a>

Even though NVI was designed with a major stock index in mind, chartists can use NVI with ETFs, stocks or anything that has volume. Keep in mind that the rationale behind the indicator is a bit unconventional because price moves on increasing volume are basically ignored.

<figure><img src="/files/MS4NvdpvrUAU4mY4ulUJ" alt=""><figcaption><p>Chart 3</p></figcaption></figure>

The example above shows the Consumer Discretionary SPDR (XLY) with NVI and two exponential moving averages. The general trend is up when NVI is above its 255-day EMA (red). A move below the 100-day EMA shows a correction within this uptrend. Chartists can also apply basic technical analysis to this indicator by drawing trend lines. There were three corrective periods from January 2010 to July 2012 (blue lines). A break above these trend lines signaled the end of a corrective period and a resumption of NVI's uptrend. These breakout signals also foreshadowed significant price moves in the underlying security (XLY).

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The Negative Volume Index (NVI) is a hybrid indicator that combines inputs from Paul Dysart and Norman Fosback. NVI counts price changes when volume decreases and discounts price changes when volume increases. The assumption is that the smart (informed) money is at work when volume decreases and the not-so-smart (uninformed) money is at work when volume increases. Remember that this indicator was designed for broad market indices and exchange volume. It can be used on stocks and ETFs, but NVI does not always act as expected. NVI will produce some great bullish/bearish divergence signals with some stocks, but look totally out of sync with other stocks. As with all indicators, NVI should not be used on its own. Instead, chartists should use it in conjunction with other analysis techniques.

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Negative Volume Index (NVI) can be found in the Indicators section below the chart. NVI is set as a cumulative indicator and cannot be adjusted. Chartists can adjust the exponential moving average by changing the number in the Parameters box. Setting the parameter to “1” will essentially remove the moving average. The indicator can then be positioned behind, above or below the main charting window. It helps to change the color when placing it behind the main charting window's price plot. Chartists can apply another moving average or indicator to NVI using the “advanced” indicator options. The example below shows the rate-of-change oscillator applied to NVI in the indicator window.

***

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line"> [Click here](https://stockcharts.com/sc3/ui/?s=$COMPQ\&p=D\&yr=0\&mn=8\&dy=0\&id=p79189698479\&a=276034932) for a live example of NVI in action.

***

<figure><img src="/files/ZXhYKcRq7kQ9jCENaHf3" alt=""><figcaption><p>Chart 4</p></figcaption></figure>

<figure><img src="/files/Ea5sDOCQ9CxuqNUNMrMP" alt=""><figcaption><p>Chart 5</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Bullish NVI Signal Line Cross <a href="#bullish_nvi_signal_line_cross" id="bullish_nvi_signal_line_cross"></a>

This scan reveals stocks where NVI has crossed above its signal line, triggering a bullish signal.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [NVI x NVI Signal(255)]
```

### Bearish NVI Signal Line Cross <a href="#bearish_nvi_signal_line_cross" id="bearish_nvi_signal_line_cross"></a>

This scan reveals stocks where NVI has crossed below its signal line, triggering a bearish signal.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [NVI Signal(255) x NVI]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax to use for NVI scans, please see our [Scan Syntax Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#negative_volume_index) in the Support Center.
{% endhint %}

## Further Study <a href="#further_study" id="further_study"></a>

John Murphy's [*Technical Analysis of the Financial Markets*](https://a.co/d/1eLUbD7) has a chapter devoted to volume and a chapter covering breadth indicators in detail. Additionally, Martin Pring's [*Technical Analysis Explained*](https://a.co/d/d6zASNa) has a chapter devoted to making volume a part of your analysis process.

| <p><a href="https://a.co/d/1eLUbD7"><strong>Technical Analysis of the Financial Markets</strong></a><br>John J. Murphy</p> | <p><a href="https://a.co/d/d6zASNa"><strong>Technical Analysis Explained</strong></a><br>Martin Pring</p> |
| -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/negative-volume-index-nvi.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
