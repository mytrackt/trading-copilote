> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/ultimate-oscillator.md).

# Ultimate Oscillator

## What Is the Ultimate Oscillator? <a href="#introduction" id="introduction"></a>

Developed by Larry Williams in 1976 and featured in *Stocks & Commodities Magazine* in 1985, the Ultimate Oscillator is a momentum oscillator designed to capture momentum across three different timeframes. The multiple timeframe objective seeks to avoid the pitfalls of other oscillators. Many [momentum oscillators](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#momentum_oscillators) surge at the beginning of a strong advance, only to form a bearish divergence as the advance continues. This is because they are stuck with one timeframe. The Ultimate Oscillator attempts to correct this fault by incorporating longer timeframes into the basic formula. Williams identified a buy signal a based on a bullish divergence and a sell signal based on a bearish divergence.

## Calculating the Ultimate Oscillator <a href="#calculation" id="calculation"></a>

There are quite a few steps involved in the Ultimate Oscillator (UO) calculation. This example is based on the default settings (7,14,28). First, calculate Buying Pressure (BP) to determine the overall direction of price action. Second, measure Buying Pressure relative to the True Range (TR). This tells us the true magnitude of a gain or loss. Third, create averages based on the three timeframes involved (7,14,28). Fourth, create a weighted average of the three averages.

```
BP = Close - Minimum(Low or Prior Close)
 
TR = Maximum(High or Prior Close)  -  Minimum(Low or Prior Close)

Average7 = (7-period BP Sum) / (7-period TR Sum)
Average14 = (14-period BP Sum) / (14-period TR Sum)
Average28 = (28-period BP Sum) / (28-period TR Sum)

UO = 100 x [(4 x Average7)+(2 x Average14)+Average28]/(4+2+1)
```

Buying Pressure (BP) measures the level of the current close relative to the current low or prior close, whichever is the lowest. True Range (TR) measures the price range from the current high or prior close (whichever is highest) to the current low or prior close (whichever is lowest). Both Buying Pressure and True Range incorporate the prior close to account for possible gaps from one period to the next. Buying Pressure is then shown relative to the True Range by dividing the X-period sum of BP by the X-period Sum of True Range. Averages are created for 7, 14, and 28 periods. These numbers correspond with the default parameters. A weighted mean is then created by multiplying the shortest Average by 4, the middle Average by two, and the longest Average by one. These weighted amounts are then summed and divided by the sum of the weightings (4+2+1).

For Ultimate Oscillator calculations, click below to download an Excel spreadsheet.

{% file src="/files/lnVReKW7C0zYyVK9LkQq" %}

<figure><img src="/files/JnWlQKFl1xl5wbEWHsvZ" alt=""><figcaption><p>Ultimate Oscillator  -  Chart 1</p></figcaption></figure>

## Interpreting the Ultimate Oscillator <a href="#interpretation" id="interpretation"></a>

Buying Pressure and its relationship to the True Range forms the base for the Ultimate Oscillator. Williams believes that the best way to measure Buying Pressure is simply subtracting the Close from the Low or the Prior Close, whichever of the two is the lowest. This will reflect the true magnitude of the advance, and hence, buying pressure. The Ultimate Oscillator rises when Buying Pressure is strong and falls when Buying Pressure is weak.

The Ultimate Oscillator measures momentum for three distinct timeframes. Notice that the second timeframe is double that of the first, and the third timeframe is double that of the second. Even though the shortest timeframe carries the most weight, the longest timeframe is not ignored, which should reduce the number of false divergences. This is important because the basic buy signal is based on a bullish divergence and the basic sell signal is based on a bearish divergence.

## Buy Signal <a href="#buy_signal" id="buy_signal"></a>

There are three steps to a buy signal. First, a [bullish divergence](/table-of-contents/glossary/glossary-b.md#bullish_divergence) forms between the indicator and security price. This means the Ultimate Oscillator forms a higher low as price forges a lower low. The higher low in the oscillator shows less downside momentum. Second, the low of the bullish divergence should be below 30. This is to ensure that prices are somewhat oversold or at a relative extremity. Third, the oscillator rises above the high of the bullish divergence.

Best Buy (BBY) is shown with the Ultimate Oscillator (7,14,28) becoming oversold in late June and forming a large bullish divergence with a higher low in late August. Technically, the indicator did not confirm the divergence until mid-September. Technical analysis, however, requires a little flexibility. Chartists could have used the move above 50 as a trigger for the Ultimate Oscillator instead. This centerline acts as a bull-bear threshold for the indicator. The cup is half full (bullish bias) when above and half empty (bearish bias) when below. Also notice that the stock broke the June trend line and surged above short-term resistance in early September for further confirmation.

<figure><img src="/files/fyyUQLEEdzpzCJc0yCDx" alt=""><figcaption><p>Ultimate Oscillator  -  Chart 2</p></figcaption></figure>

The chart below shows American Eagle (AEO) with a smaller bullish divergence signal. The Ultimate Oscillator moved to oversold levels (<30) as the stock fell in early June. While the stock moved to new lows in late June, the indicator held above its prior low and above 30. The subsequent break above the intermittent high confirmed the bullish divergence signal. Also notice that AEO broke above resistance with a four-day surge. Even those who missed the breakout got a second chance as the stock pulled back in August and again broke resistance.

<figure><img src="/files/Y24cCFU02pqJ3hl3RPDR" alt=""><figcaption><p>Ultimate Oscillator  -  Chart 3</p></figcaption></figure>

## Sell Signal <a href="#sell_signal" id="sell_signal"></a>

There are three steps to a sell signal. First, a [bearish divergence](/table-of-contents/glossary/glossary-b.md#bearish_divergence) forms between the indicator and security price. This means the Ultimate Oscillator forms a lower high as price forges a higher high. The lower high in the oscillator shows less upside momentum. Second, the high of the bearish divergence should be above 70. This is to ensure that prices are somewhat overbought or at a relative extremity. Third, the oscillator falls below the low of the bearish divergence to confirm a reversal.

<figure><img src="/files/AdBBKquUjANcyr2nGKAW" alt=""><figcaption><p>Ultimate Oscillator  -  Chart 4</p></figcaption></figure>

Caterpillar surged to a new high in late April, but the Ultimate Oscillator failed to confirm this high and formed a lower high. Also, notice that the indicator became overbought in mid-April. The subsequent break below the divergence low in late April confirmed the bearish signal. CAT broke trend line support two days later and declined sharply into early June.

<figure><img src="/files/NJOiaZM7e4rie8BzlFv6" alt=""><figcaption><p>Ultimate Oscillator  -  Chart 5</p></figcaption></figure>

The chart above shows Starbucks with an unconfirmed bearish signal and then a confirmed signal. The Ultimate Oscillator became overbought in the latter part of April. As the stock moved to new highs, the indicator forged lower highs in mid-May and again in late June. A bearish divergence was working in mid-May, but the indicator never broke its divergence low for confirmation. After a bigger divergence formed, the indicator broke its divergence low at the end of June to foreshadow a rather sharp decline.

## Timeframes <a href="#timeframes" id="timeframes"></a>

The Ultimate Oscillator can be used on intraday, daily, weekly or monthly charts. It is sometimes necessary to adjust the parameters to generate overbought or oversold readings, which are part of the buy and sell signals. Relatively docile stocks or securities may not generate overbought or oversold readings with the default parameters (7,14,28). Chartists need to increase sensitivity with shorter timeframes. The chart for Boeing (BA) shows the Ultimate Oscillator (7,14,28) trading between 30 and 70 for six months. There were no overbought or oversold readings. Shortening the timeframe to (4,8,16) increased sensitivity and generated at least six overbought or oversold readings. The opposite is true for securities with high volatility. It is sometimes necessary to lengthen the timeframes to reduce sensitivity and the number of signals.

<figure><img src="/files/29T5jvaXlFKFPwi1cxtU" alt=""><figcaption><p>Ultimate Oscillator  -  Chart 6</p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The Ultimate Oscillator is a momentum oscillator that incorporates three different timeframes. Traditional signals are derived from bullish and bearish divergence, but chartists can also look at actual levels for a trading bias. This usually works better with longer parameters and longer trends. For example, the Ultimate Oscillator (20,40,80) and price trend favors the bulls when above 50 and the bears when below 50. As with all indicators, the Ultimate Oscillator should not be used alone. Complementary indicators, [chart patterns](/table-of-contents/chart-analysis/chart-patterns.md) and other analysis tools should be employed to confirm signals.

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Ultimate Oscillator is available as a SharpCharts indicator that can be placed above, below or behind the price plot of the underlying security. Placing it directly behind the price plot in a bright color makes it easy to compare indicator movements with price movements. Users can click the green arrow next to “advanced options” to add horizontal lines or a [moving average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md).\
[Click here for a live version of the chart.](https://stockcharts.com/sc3/ui/?s=IWM\&p=D\&yr=0\&mn=6\&dy=0\&id=p72157742291\&listNum=30\&a=223328852)

<figure><img src="/files/368Tc2NZSKGoOroYYAbv" alt=""><figcaption><p>Ultimate Oscillator  -  Chart 7</p></figcaption></figure>

<figure><img src="/files/JccnJXdVYS0AjgL6xoaK" alt=""><figcaption><p>Ultimate Oscillator - SharpCharts</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Bullish Long-Term Cross <a href="#bullish_long-term_cross" id="bullish_long-term_cross"></a>

This scan reveals stocks where the Ultimate Oscillator crosses above 50, which is a bullish sign. This scan is just a starting point. Further refinement and analysis are required.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [Ultimate Osc(20,40,80) x 50]
```

### Bearish Long-Term Cross <a href="#bearish_long-term_cross" id="bearish_long-term_cross"></a>

This scan reveals stocks where the Ultimate Oscillator crosses below 50, which is a bearish sign. This scan is just a starting point. Further refinement and analysis are required.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [50 x Ultimate Osc(20,40,80)]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax for Ultimate Oscillator scans, please see our [Scan Syntax Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference) in the Support Center.
{% endhint %}

## Further Study <a href="#further_study" id="further_study"></a>

John Murphy's [*Technical Analysis of the Financial Markets*](https://a.co/d/914MMoh)<https://a.co/d/914MMoh> has a chapter devoted to momentum oscillators and their various uses. Murphy covers the pros and cons as well as some examples specific to the Commodity Channel Index.

Martin Pring's [*Technical Analysis Explained*](https://a.co/d/gebcznJ) shows the basics of momentum indicators by covering divergences, crossovers, and other signals. There are two more chapters covering specific momentum indicators, each containing plenty of examples.

| <p><a href="https://a.co/d/914MMoh"><strong>Technical Analysis of the Financial Markets</strong></a><br>John J. Murphy</p> | <p><a href="https://a.co/d/gebcznJ"><strong>Technical Analysis Explained</strong></a> <br>Martin Pring</p> |
| -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/ultimate-oscillator.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
