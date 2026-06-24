> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/prings-know-sure-thing-kst.md).

# Pring's Know Sure Thing (KST)

## What Is Pring's Know Sure Thing (KST)? <a href="#introduction" id="introduction"></a>

Developed by Martin Pring, Know Sure Thing (KST) is a momentum oscillator based on the smoothed rate-of-change for four different timeframes. Pring first described the indicator in the 1992 “Summed Rate of Change (KST)” in *Stocks & Commodities* magazine. In short, KST measures price momentum for four different price cycles, combining them into a single momentum oscillator. Like any other unbound momentum oscillator, chartists can use KST to look for divergences, signal line crossovers, and centerline crossovers. Pring frequently applied trend lines to KST. Although trend line signals do not occur often, Pring notes that such breaks reinforce signal line crossovers.

## SharpCharts Calculation <a href="#sharpcharts_calculation" id="sharpcharts_calculation"></a>

Even though the formula for KST looks complicated, it is simply a weighted average of four different rate-of-change values that have been smoothed. For example, calculate the 10-period rate-of-change and smooth it with a 10-period [simple moving average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md).&#x20;

The chart below shows the four different rate-of-change indicators with the appropriate moving averages for smoothing.

<figure><img src="/files/hT1Qeuc8dqftkGrM3vF3" alt=""><figcaption><p>Chart 1</p></figcaption></figure>

The formula box below shows the four different combinations with their default settings. These combinations are then weighted and summed. The shortest timeframe carries the least weight (1) and the longest timeframe carries the most weight (4). A 9-period simple moving average is added as a signal line.

```
RCMA1 = 10-Period SMA of 10-Period Rate-of-Change
RCMA2 = 10-Period SMA of 15-Period Rate-of-Change
RCMA3 = 10-Period SMA of 20-Period Rate-of-Change
RCMA4 = 15-Period SMA of 30-Period Rate-of-Change

KST = (RCMA1 x 1) + (RCMA2 x 2) + (RCMA3 x 3) + (RCMA4 x 4)

Signal Line = 9-period SMA of KST
```

The default parameters are as follows: KST(10,15,20,30,10,10,10,15,9). The first four numbers represent the rate-of-change settings, the second four represent the moving averages for these rate-of-change indicators, and the last number is the signal line moving average.

<figure><img src="/files/d1VEeCiGNUymv6WKJfOm" alt=""><figcaption><p>Spreadsheet</p></figcaption></figure>

Click below to download this spreadsheet example.

{% file src="/files/okdXaDtAW5TYDMFfNMDJ" %}

## Interpretating KST <a href="#interpretation" id="interpretation"></a>

KST fluctuates above/below the zero line. At its most basic, momentum favors the bulls when KST is positive and favors the bears when KST is negative. A positive reading means the weighted and smoothed [rate-of-change values](/table-of-contents/technical-indicators-and-overlays/technical-indicators/rate-of-change-roc.md) are mostly positive, and prices are moving higher. A negative reading indicates that prices are moving lower.

<figure><img src="/files/JiCyKMKRaYxuMXMFxu7r" alt=""><figcaption><p>Chart 2</p></figcaption></figure>

After basic centerline crossovers, chartists can look for signal line crossovers and gauge general direction. KST generally rises when above its signal line and falls when below its signal line. A rising and negative KST line indicates that downside momentum is waning. Conversely, a falling and positive KST line indicates that upside momentum is waning.

Even though many different signals are possible with KST, the basic centerline and signal line crossovers are usually the most robust. Unlike the [Relative Strength Index](/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi.md) (RSI) and [Stochastic Oscillator](/table-of-contents/technical-indicators-and-overlays/technical-indicators/stochastic-oscillator-fast-slow-and-full.md), KST does not have upper or lower limits. This makes it relatively ill-suited for overbought and oversold signals.

## Divergences <a href="#divergences" id="divergences"></a>

Bullish and [bearish divergences](/table-of-contents/glossary/glossary-b.md#bearish_divergence) are also possible for signals, but chartists must be selective when using these. Most divergences in the basic rate-of-change indicator do not result in price reversals. Similarly, divergences in MACD and RSI are also prone to failure. It is probably best to use divergences when there is a large and blatant divergence. The example below shows a chart with a large bearish and bullish divergence. These divergences were finalized with subsequent signal line crossovers (red and green arrows).

<figure><img src="/files/eHnJv6jFiHm7IqFqVAZn" alt=""><figcaption><p>Chart 3</p></figcaption></figure>

## Strong Trends <a href="#strong_trends" id="strong_trends"></a>

Chartists should be careful with bearish signal line crossovers in strong uptrends and bullish signal line crossovers in strong downtrends. KST can move into positive territory and remain in positive territory for an extended period during a strong uptrend. The indicator will reach a relatively high level and then turn down but never move into negative territory. This simply signals that upside momentum is slowing; it is still stronger than downside momentum but not as strong as in previous periods. The example below shows Sherwin Williams (SHW) with a strong uptrend from November 2011 to August 2012. Even though KST fluctuated up and down, it never broke below zero and remained in positive territory the entire time. The bearish signal line crossovers indicated a slowing in upside momentum, not a trend change.

<figure><img src="/files/iBwiN1MufDK7fS8nWlIo" alt=""><figcaption><p>Chart 4</p></figcaption></figure>

## Timeframes <a href="#timeframes" id="timeframes"></a>

* Short-term Daily = KST(10,15,20,30,10,10,10,15,9)
* Medium-term Weekly = KST(10,13,15,20,10,13,15,20,9)
* Long-term Monthly = KST(9,12,18,24,6,6,6,9,9)

As noted in Pring's articles, KST can be used on a short-term, medium-term or long-term timeframe. Instead of just shifting between daily, weekly and monthly charts, Pring suggested changing the settings to suit each timeframe. KST is even smoother when using the weekly and monthly settings. This means chartists should use signal line crossovers to detect directional changes in price. The lag for centerline crossovers is often too great. The table below shows the rate-of-change settings and moving average settings for the short-term, medium-term and long-term studies.

<figure><img src="/files/xrGjoNo4aLgJ7VFv6UCK" alt=""><figcaption><p>Chart 5</p></figcaption></figure>

<figure><img src="/files/KG1Rh9J66pODsvNrV3ZS" alt=""><figcaption><p>Chart 6</p></figcaption></figure>

<figure><img src="/files/jURa13XaNatD33PcxjIv" alt=""><figcaption><p>Chart 7</p></figcaption></figure>

## Further Tweaks <a href="#further_tweaks" id="further_tweaks"></a>

Martin Pring would be the first to admit that KST is not a perfect indicator. There is no such thing. However, KST does have its uses. Pring encourages chartists to try different settings because one size does not fit all. Utility and consumer staples are less volatile and may require more sensitive settings, while technology stocks are more volatile and may require less sensitive settings.

Chartists can also mix and match the rate-of-change and moving average settings. The chart below shows the default KST in the first indicator window and a KST weighted in favor of the short-term rate-of-change in the second window. Instead of KST(10,15,20,30,10,10,10,15,9) the second window shows KST(30,20,15,10,10,10,10,10,9). The first rate-of-change setting carries the least weight and the fourth one carries the most weight. Note that the first four numbers represent the rate-of-change settings. The second four numbers represent the moving averages to smooth these four rate-of-change indicators. The final number is the signal line.

<figure><img src="/files/nJaAoIZbDXkg3AFpqn9T" alt=""><figcaption><p>Chart 8</p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

Know Sure Thing (KST) is a momentum oscillator based on the smoothed rate of change over four different periods. In this regard, it is designed to capture four different price cycles. KST can be used like other unbound momentum oscillators, such as MACD, the [Percentage Price Oscillator](/table-of-contents/technical-indicators-and-overlays/technical-indicators/percentage-price-oscillator-ppo.md) (PPO), and [TRIX](/table-of-contents/technical-indicators-and-overlays/technical-indicators/trix.md). KST closely resembles TRIX. Because it is unbound, KST is not well suited for identifying overbought and oversold conditions. KST's creator, Martin Pring, favors signal line crossovers and trend line breaks for signals. As with all indicators, KST should be combined with other analysis techniques.

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

KST is available as an indicator for SharpCharts. Once selected, users can place the indicator above, below or behind the underlying price plot. Placing KST directly behind the price plot accentuates the movements relative to the price action of the underlying security. Users can apply “advanced options” to add a horizontal line. Adjusting the numbers in the parameters box will change the settings.

<figure><img src="/files/HlZAca3Jgzl7JhGGXkb2" alt=""><figcaption><p>Chart 9</p></figcaption></figure>

<figure><img src="/files/aJlg3jDfCcb1hznkhISP" alt=""><figcaption><p>Chart 10</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Bullish KST Signal Line Cross <a href="#bullish_kst_signal_line_cross" id="bullish_kst_signal_line_cross"></a>

This scan reveals stocks where KST is in positive territory. A bullish signal is triggered when KST crosses above its signal line.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [KST > 0]
AND [KST x KST Signal]
```

### Bearish KST Signal Line Cross <a href="#bearish_kst_signal_line_cross" id="bearish_kst_signal_line_cross"></a>

This scan reveals stocks where KST is in negative territory. A bearish signal is triggered when KST crosses below its signal line.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [KST < 0]
AND [KST Signal x KST]
```

For more details on the syntax to use for KST scans, please see our [Scan Syntax Reference](https://support.stockcharts.com/doku.php?id=scans:indicators#pring_s_know_sure_thing) in the Support Center.

## Further Study <a href="#further_study" id="further_study"></a>

[*Technical Analysis of the Financial Markets*](https://a.co/d/1eLUbD7) has a chapter devoted to momentum oscillators and their various uses. Murphy covers the pros and cons as well as some examples specific to Rate-of-Change. Martin Pring's [*Technical Analysis Explained*](https://a.co/d/7KcWIbb) explores the basics of momentum indicators by covering divergences, crossovers and other signals. There are two more chapters covering specific momentum indicators, each containing plenty of examples.

| <p><a href="https://a.co/d/1eLUbD7"><strong>Technical Analysis of the Financial Markets</strong></a><br>John J. Murphy</p> | <p><a href="https://a.co/d/cDWIIxN"><strong>Technical Analysis Explained by Martin Pring</strong></a><br>Martin Pring</p> |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/prings-know-sure-thing-kst.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
