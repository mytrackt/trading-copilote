> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/williams-r.md).

# Williams %R

## What Is the Williams %R Indicator? <a href="#introduction" id="introduction"></a>

Developed by Larry Williams, Williams %R is a momentum indicator that is the inverse of the Fast [Stochastic Oscillator](/table-of-contents/technical-indicators-and-overlays/technical-indicators/stochastic-oscillator-fast-slow-and-full.md). Also referred to as %R, Williams %R reflects the level of the close relative to the highest high for the look-back period. In contrast, the Stochastic Oscillator reflects the level of the close relative to the lowest low. %R corrects for the inversion by multiplying the raw value by -100. As a result, the Fast Stochastic Oscillator and Williams %R produce the exact same lines, but with different scaling. Williams %R oscillates from 0 to -100; readings from 0 to -20 are considered overbought, while readings from -80 to -100 are considered oversold. Unsurprisingly, signals derived from the Stochastic Oscillator are also applicable to Williams %R.

## Calculating the Williams %R <a href="#calculation" id="calculation"></a>

```
%R = (Highest High - Close)/(Highest High - Lowest Low) * -100

Lowest Low = lowest low for the look-back period
Highest High = highest high for the look-back period
%R is multiplied by -100 correct the inversion and move the decimal.
```

The default setting for Williams %R is 14 periods, which can be days, weeks, months or an intraday timeframe. A 14-period %R would use the most recent close, the highest high over the last 14 periods and the lowest low over the last 14 periods.

<figure><img src="/files/smMCyDYOnmv3AIXCxW1T" alt=""><figcaption><p>Williams %R - Spreadsheet 1</p></figcaption></figure>

Click below to download this spreadsheet example.

{% file src="/files/DfpyPDcuu5KohCvanHAU" %}

<figure><img src="/files/eKu3jgR4sZYbOwAtvhXS" alt=""><figcaption><p>Williams %R - Chart 1</p></figcaption></figure>

## Interpreting the Williams %R <a href="#interpretation" id="interpretation"></a>

As with the Stochastic Oscillator, Williams %R reflects the level of the close relative to the high-low range over a given period of time. Assume that the highest high equals 110, the lowest low equals 100 and the close equals 108. The high-low range is 10 (110 - 100), which is the denominator in the %R formula. The highest high less the close equals 2 (110 - 108), which in turn is divided by 10, resulting in 0.20. Multiply this number by -100 to get -20 for %R. If the close was 103, Williams %R would be -70 (((110-103)/10) x -100).

The centerline, -50, is an important level to watch. Williams %R moves between 0 and -100, which makes -50 the midpoint. Think of it as the 50-yard line in football. The offense has a higher chance of scoring when it crosses the 50-yard line. The defense has an edge as long as it prevents the offense from crossing the 50-yard line. A Williams %R cross above -50 signals that prices are trading in the upper half of their high-low range for the given look-back period. This suggests that the cup is half full. Conversely, a cross below -50 means prices are trading in the bottom half of the given look-back period. This suggests that the cup is half empty.

Low readings (below -80) indicate that price is near its low for the given time period. High readings (above -20) indicate that price is near its high for the given time period. The IBM example above shows three 14-day ranges (yellow areas) with the closing price at the end of the period (red dotted) line. Williams %R equals -9 when the close was at the top of the range. The Williams %R equals -87 when the close was near the bottom of the range. The close equals -43 when the close was in the middle of the range.

## Overbought/Oversold <a href="#overbought_oversold" id="overbought_oversold"></a>

As a [bound oscillator](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#banded_oscillators), Williams %R makes it easy to identify overbought and oversold levels. The oscillator ranges from 0 to -100. No matter how fast a security advances or declines, Williams %R will always fluctuate within this range. Traditional settings use -20 as the overbought threshold and -80 as the oversold threshold. These levels can be adjusted to suit analytical needs and security characteristics. Readings above -20 for the 14-day Williams %R would indicate that the underlying security was trading near the top of its 14-day high-low range. Readings below -80 occur when a security is trading at the low end of its high-low range.

Before looking at some chart examples, it is important to note that overbought readings are not necessarily bearish. Securities can become overbought and remain overbought during a strong uptrend. Closing levels that are consistently near the top of the range indicate sustained buying pressure. In a similar vein, oversold readings are not necessarily bullish. Securities can also become oversold and remain oversold during a strong downtrend. Closing levels consistently near the bottom of the range indicate sustained selling pressure.

Chart 3 shows Arch Coal (ACI) with 14-day Williams %R hitting overbought and oversold levels on a regular basis. The red dotted lines mark a move below -50 that occurs after an overbought reading. The green dotted lines mark a move above -50 that occurs after an oversold reading. As noted above, overbought is not necessarily bearish and oversold is not necessarily bullish. Top and bottom pickers can act when overbought or oversold, but it is often prudent to wait for a confirmation move. A move below -50 confirms a downturn after an overbought reading. A move above -50 confirms an upturn after an oversold reading.

<figure><img src="/files/Wd3YgGKe1hovA8qwVPmE" alt=""><figcaption><p>Williams %R - Chart 2</p></figcaption></figure>

## Momentum Failure <a href="#momentum_failure" id="momentum_failure"></a>

The failure to move back into overbought or oversold territory signals a change in momentum that can foreshadow a significant price move. The ability to consistently move above -20 is a show of strength. After all, it takes buying pressure to push %R into overbought territory. Once a security shows strength by pushing into overbought territory more than once, a subsequent failure to exceed this level shows weakening momentum that can foreshadow a decline.

<figure><img src="/files/OdHVHmc0woeJ9GvcLzvH" alt=""><figcaption><p>Williams %R - Chart 3</p></figcaption></figure>

The chart above shows Cisco with 14-day %R. The stock was strong, with numerous overbought readings occurring from February to April. Even after the plunge below -80 in early April, %R surged back above -20 to show continuing strength. After a few more weeks of overbought readings, %R plunged to oversold levels in early May. This deep plunge showed strong selling pressure. The subsequent recovery fell short of -20 and did not reach overbought territory. This provided the second sign of weakness. After failing below -20, the decline below -50 signaled a downturn in momentum and the stock declined rather sharply. Another failure just below -20 in mid-June also resulted in a sharp decline.

<figure><img src="/files/1Co1Xg3BlnI94zxXsO1B" alt=""><figcaption><p>Williams %R - Chart 4</p></figcaption></figure>

The chart above shows TJX Companies (TJX) with 28-day Williams %R. Chartists can adjust the look-back period to suit their analysis objectives. A longer timeframe makes the indicator less sensitive. After becoming overbought in October, the indicator moved lower and became oversold twice in December. The January surge carried %R into overbought territory and the stock broke channel resistance. These were promising signs. On the subsequent pullback, %R held above -80 and did not become oversold. This showed underlying strength. The subsequent move above -50 foreshadowed a sharp advance over the next few months.

## Conclusion <a href="#conclusion" id="conclusion"></a>

Williams %R is a momentum oscillator that measures the level of the close relative to the high-low range over a given period of time. In addition to the signals mentioned above, chartists can use %R to gauge the six-month trend for a security. 125-day %R covers around 6 months. Prices are above their 6-month average when %R is above -50, which is consistent with an uptrend. Readings below -50 are consistent with a downtrend. In this regard, %R can be used to help define the bigger trend (six months). Like all technical indicators, it is important to use the Williams %R in conjunction with other technical analysis tools. Volume, [chart patterns](/table-of-contents/chart-analysis/chart-patterns.md) and breakouts can be used to confirm or refute signals produced by Williams %R.

<figure><img src="/files/Qub9BtMqmagwD7mKcu6u" alt=""><figcaption><p>Williams %R - Chart 5</p></figcaption></figure>

***

## Using With SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

Williams %R is available as an indicator for SharpCharts. The default setting is 14, but users can opt for a shorter or longer timeframe to produce a more or less sensitive oscillator, respectively. Once selected, the indicator can be placed above, below or behind the underlying price plot. Click on “Advanced Options” to add a moving average, horizontal line or another indicator. A 3-day SMA can be added as a signal line.

***

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line"> [Click here for a live example](https://stockcharts.com/sc3/ui/?s=QQQ\&p=D\&yr=0\&mn=6\&dy=0\&id=p67764551359\&listNum=30\&a=219822109).

***

<figure><img src="/files/2yZI0t28HMoJr8xyxpRB" alt=""><figcaption><p>Williams %R - Chart 6</p></figcaption></figure>

<figure><img src="/files/NWfW5uHvROTeGy952yb0" alt=""><figcaption><p>Williams %R - SharpCharts</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Williams %R Turns Up from Oversold Levels <a href="#williams_r_turns_up_from_oversold_levels" id="williams_r_turns_up_from_oversold_levels"></a>

This scan searches for stocks that are trading above their 200-day moving average to define a long-term uptrend. A pullback is identified when %R moves below -80 and a subsequent upturn occurs when %R moves above -50.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [Daily Close > Daily SMA(200,Daily Close)]
AND [20 days ago Daily Williams %R(14) < -80]
AND [Daily Williams %R(14) crosses -50]
```

### Williams %R Turns Down from Overbought Levels <a href="#williams_r_turns_down_from_overbought_levels" id="williams_r_turns_down_from_overbought_levels"></a>

This scan searches for stocks that are trading below their 200-day moving average to define a long-term downtrend. An oversold bounce is identified when %R moves above -20 and a subsequent downturn occurs when %R moves below -50.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [Daily Close < Daily SMA(200,Daily Close)]
AND [20 days ago Daily Williams %R(14) > -20]
AND [-50 crosses Daily Williams %R(14)]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax to use for Williams %R scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#williams_r_williams_r) in the Support Center.
{% endhint %}

## Further Study <a href="#further_study" id="further_study"></a>

John Murphy's [*Technical Analysis of the Financial Markets*](https://a.co/d/aSkaxU9) has a chapter devoted to momentum oscillators and their various uses. Murphy covers the pros and cons, along with some examples specific to the %R and the Stochastic Oscillator.

Martin Pring's [*Technical Analysis Explained*](https://a.co/d/9jTh264) illustrates the basics of momentum indicators by covering divergences, crossovers, and other signals. There are two more chapters covering specific momentum indicators, each containing plenty of examples.

| <p><a href="https://a.co/d/aSkaxU9"><strong>Technical Analysis of the Financial Markets</strong></a><br>John J. Murphy</p> | <p><a href="https://a.co/d/9jTh264"><strong>Technical Analysis Explained</strong></a><br>Martin Pring</p> |
| -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/williams-r.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
