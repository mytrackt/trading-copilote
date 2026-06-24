> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/coppock-curve.md).

# Coppock Curve

## What Is the Coppock Curve? <a href="#introduction" id="introduction"></a>

The Coppock Curve is a momentum indicator developed by Edwin “Sedge” Coppock, who was an economist by training. Coppock introduced the indicator in *Barron's* in October 1965. The goal of this indicator is to identify long-term buying opportunities in the S\&P 500 and Dow Industrials. The signal is very simple. Coppock used monthly data to identify buying opportunities when the indicator moved from negative territory to positive territory. Although Coppock did not use it for sell signals, many technical analysts consider a cross from positive to negative territory as a sell signal.

## SharpCharts Calculation <a href="#sharpcharts_calculation" id="sharpcharts_calculation"></a>

```
Coppock Curve = 10-period WMA of (14-period RoC + 11-period RoC)

WMA = Weighted Moving Average
RoC = Rate-of-Change
```

The [Rate-of-Change indicator](/table-of-contents/technical-indicators-and-overlays/technical-indicators/rate-of-change-roc.md) is a momentum oscillator that oscillates above and below the zero line. Coppock used 11 and 14 periods because, according to an Episcopal priest, this was the average mourning period when grieving the loss of a loved one. Coppock theorized that the recovery period for stock market losses would be similar to this timeframe.

<figure><img src="/files/4tPtr1e5NkzUpslVOrnH" alt=""><figcaption><p>Chart 1</p></figcaption></figure>

The Rate-of-Change indicators were then smoothed with a weighted [moving average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md). As its name implies, a weighted moving average puts more weight on recent data and less weight on older data. For example, a three-period WMA would multiply the first data point by one, the second by two, and the third by three. The sum of these three numbers is then divided by six, the sum of the weightings (1 + 2 + 3), to create a weighted average. The table below shows a calculation from an Excel spreadsheet.

<figure><img src="/files/flXhALYt4YXn0mo5WRXm" alt=""><figcaption><p>Spreadsheet 1</p></figcaption></figure>

Click below to download the spreadsheet.

{% file src="/files/QEsKSQJZjro5oLMFxqrX" %}

## Signals <a href="#signals" id="signals"></a>

Using monthly data, this indicator will not trigger very many signals. A buy signal triggers with a cross into positive territory, while a sell signal triggers with a cross into negative territory. Unsurprisingly, there have been only five signals since the late 1980s. The chart below shows the last four signals. The first signal triggered in 1988, which was after the 1987 crash.

<figure><img src="/files/G0A9L6BFCMZHLXshXXSc" alt=""><figcaption><p>Chart 2</p></figcaption></figure>

Chartists following the two sell signals would have avoided the last two bear markets. The February 2001 sell signal would have avoided most of the bear market from 2000 to 2002. The June 2008 sell signal would have gotten investors out before the market plunge in the second half of 2008. These sell signals could have been used to simply exit the stock market and move into cash, which would have lowered market exposure and overall risk.

## Flexibility <a href="#flexibility" id="flexibility"></a>

As noted above, the Coppock Curve is simply a smoothed momentum oscillator. The Rate-of-Change indicator measures momentum and the weighted moving average smooths the data. This means the indicator can be used on any timeframe. Intraday, daily and weekly data can be used to fit one's trading/investing style and time horizon. The chart below shows the Coppock Curve using weekly data on the Dow Industrials. As expected, the weekly chart produced many more signals than the monthly chart.

<figure><img src="/files/KWXcxSMdPQVRUdzpfdwl" alt=""><figcaption><p>Chart 3</p></figcaption></figure>

In addition to different timeframes, the parameters can be adjusted to make the indicator faster or slower. A shorter Rate-of-Change setting will make the Coppock Curve more sensitive and faster, while a longer setting will make it less sensitive and slower. The chart below shows daily bars for the Nasdaq 100 ETF (QQQ) and the Coppock Curve (20,10,10). This setting makes the Coppock Curve a little less sensitive, which may be better suited for daily charts.

<figure><img src="/files/5X5WWaJFUuy1dpqntX35" alt=""><figcaption><p>Chart 4</p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The Coppock Curve is simply a smoothed momentum oscillator. Even though it was originally designed for monthly charts and long-term analysis, it can be used on intraday, daily or weekly charts and the settings can be adjusted to suit one's style. The main signals are generated with crosses above and below the zero line. More aggressive chartists can consider looking for bullish and bearish divergences to anticipate such crossovers. Use caution, however. Divergences do not always result in trend reversals because the trend can simply slow and continue in the same direction.

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Coppock Curve can be found in the Indicators section below the chart. Users can adjust the settings by changing the numbers in the Parameters box. The indicator can then be positioned “behind price,” “above” the main window or “below” the main window. It helps to change the color when placing it behind the price. Chartists can also add a moving average using the “advanced” options. This moving average acts like a signal line, similar to [MACD](/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator.md).

<figure><img src="/files/0qjvELvJGQFh4hy7v3BM" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/keEeYJQTdzqwbFzE5lXW" alt=""><figcaption></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Coppock Curve Crosses above Zero <a href="#coppock_curve_crosses_above_zero" id="coppock_curve_crosses_above_zero"></a>

This simple scan searches for stocks where the Coppock Curve crossed from negative territory to positive territory and daily volume was above the 50-day moving average of volume. In other words, the bullish crossover occurred with expanding volume.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Daily Coppock(20,10,10) crosses 0] 
AND [Daily Volume > Daily SMA(50,Daily Volume)]
```

### Coppock Curve Crosses below Zero <a href="#coppock_curve_crosses_below_zero" id="coppock_curve_crosses_below_zero"></a>

This simple scan searches for stocks where the Coppock Curve crossed from positive territory to negative territory and daily volume was above the 50-day moving average of volume. In other words, the bearish crossover occurred with expanding volume.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [0 crosses Daily Coppock(20,10,10)] 
AND [Daily Volume > Daily SMA(50,Daily Volume)]
```

{% hint style="info" %}
For more details on the syntax to use for Coppock Curve scans, please see our [Scan Syntax Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#coppock_curve_coppock) in the Support Center.
{% endhint %}

## Further Study <a href="#further_study" id="further_study"></a>

John Murphy's [*Technical Analysis of the Financial Markets*](https://a.co/d/2g3jchk) has a chapter devoted to momentum oscillators and their various uses. Murphy covers the pros and cons as well as some examples specific to Rate-of-Change.

Martin Pring's [*Technical Analysis Explained*](https://a.co/d/ahkphoZ) shows the basics of momentum indicators by covering divergences, crossovers and other signals. There are two more chapters covering specific momentum indicators with plenty of examples.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/coppock-curve.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
