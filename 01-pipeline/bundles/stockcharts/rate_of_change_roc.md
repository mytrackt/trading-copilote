> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/rate-of-change-roc.md).

# Rate of Change (ROC)

## What Is the Rate of Change Indicator? <a href="#what_is_the_rate_of_change_indicator" id="what_is_the_rate_of_change_indicator"></a>

The Rate of Change (ROC) indicator, which is also referred to as Momentum, is a pure [momentum oscillator](/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators.md#momentum_oscillators) that measures the percent change in price from one period to the next. The ROC calculation compares the current price with the price “n” periods ago. The plot forms an oscillator that fluctuates above and below the zero line as the rate of change moves from positive to negative.&#x20;

<figure><img src="/files/MU6U68FNuTOgzjCrOWT6" alt=""><figcaption></figcaption></figure>

As a momentum oscillator, ROC signals include centerline crossovers, divergences, and overbought-oversold readings. Divergences fail to foreshadow reversals more often than not, so we will forgo a detailed discussion of them. Even though centerline crossovers are prone to whipsaw, especially short-term, these crossovers can be used to identify the overall trend. Identifying overbought or oversold extremes comes naturally to the Rate of Change oscillator.

## Rate of Change Calculation <a href="#how_to_calculate_rate_of_change" id="how_to_calculate_rate_of_change"></a>

```
ROC = [(Close - Close n periods ago) / (Close n periods ago)] * 100
```

<figure><img src="/files/tr5KEoNhwPDH84niLOhN" alt=""><figcaption><p>ROC - Spreadsheet 1</p></figcaption></figure>

Click below to download this spreadsheet example.&#x20;

{% file src="/files/fzOjyqsQYvwAQhJPcImT" %}

<figure><img src="/files/ojS8yiTjuvrzHETXnOi4" alt=""><figcaption><p>ROC - Calculation Example</p></figcaption></figure>

The table above shows the 12-day Rate of Change calculations for the Dow Industrials in May 2010. The yellow cells show the Rate of Change from April 28th to May 14th. It is actually 13 trading days, but the close on the 28th acts as the starting point on the 29th. The blue cells show the 12-day Rate of Change from May 7th until May 25th.

## Interpreting Rate of Change <a href="#how_to_interpret_rate_of_change" id="how_to_interpret_rate_of_change"></a>

As noted above, the Rate of Change indicator is momentum in its purest form. It measures the percentage increase or decrease in price over a given period of time. Think of it as the rise (price change) over the run (time). In general, prices are rising as long as the Rate of Change remains positive. Conversely, prices are falling when the Rate of Change is negative. ROC expands into positive territory as an advance accelerates. ROC dives deeper into negative territory as a decline accelerates.&#x20;

There is no upward boundary on the Rate of Change. The sky is the limit for an advance. There is, however, a downside limit. Securities can only decline 100%, which would be to zero. Even with these lopsided boundaries, Rate of Change produces identifiable extremes that signal [overbought](/table-of-contents/glossary/glossary-o.md#overbought) and oversold conditions.

### Identifying Overbought/Oversold Extremes <a href="#overbought_oversold_extremes" id="overbought_oversold_extremes"></a>

There are three price movements: up, down, and sideways. Momentum oscillators like ROC are ideally suited for sideways price action with regular fluctuations. This makes it easier to identify extremes and forecast turning points. Security prices can also fluctuate when trending. For example, an uptrend consists of a series of higher highs and higher lows as prices zigzag higher. Pullbacks often occur at regular intervals based on the percentage move, time elapsed or both. A downtrend consists of lower lows and lower highs as prices zigzag lower. Counter trend advances retrace a portion of the prior decline and usually peak below the prior high. Peaks can occur at regular intervals based on the percentage move, time elapsed or both. The Rate of Change can be used to identify periods when the percentage change nears a level that foreshadowed a turning point in the past.

#### Oversold Conditions

<figure><img src="/files/WjWstf6kyXf2aCk8eS4H" alt=""><figcaption><p>Using the ROC to identify oversold conditions</p></figcaption></figure>

The chart above shows Intel (INTC) with an uptrend from June 2025 until January 2026. Notice how the stock zigzagged up with a series of higher highs and higher lows. Because the overall trend was up, the Rate of Change indicator was used to identify short-term oversold levels as a chance to partake in the bigger uptrend. Short-term overbought signals were ignored because the bigger trend was up. Based on the July-August 2025 bounce, -10% was set as the oversold boundary. Movements below this level indicated that prices were at a short-term extreme. Overbought and oversold settings depend on the volatility of the underlying security. A more volatile stock may use -15% for oversold, while a less volatile stock may use -5%. Oversold readings serve as an alert to be ready for a turning point. Prices are oversold, but have yet to actually turn. Remember, a security can become oversold and remain oversold as the decline continues. A 20-day [moving average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) was overlaid to identify an actual upturn. After ROC became oversold in mid-November, INTC moved above its 20-day SMA in late November to confirm an upturn. The second oversold reading occurred in mid-December and INTC moved above its 20-day SMA at the end of December.

#### Overbought Conditions

<figure><img src="/files/iLrwSlB4SguLZ2WhPfnA" alt=""><figcaption><p>Using the ROC to identify overbought conditions</p></figcaption></figure>

The chart above shows Salesforce (CRM) in a downtrend from November 2021 until December 2022. This example uses the standard 12-day Rate of Change to identify overbought levels within a bigger downtrend. The number of time periods depends on the individual security and the desired trading timeframe. The late March high occurred with an overbought reading above +10%. This means Microsoft was up over 10% in a 12-day period, which is about 2.5 weeks. That's a pretty good bounce within a bigger downtrend. The next overbought reading did not occur until June, when the Rate of Change again exceeded +10%. It briefly rose above 10% again in late July, before CRM broke trend line support at the end of August to signal a continuation of the downtrend. The next overbought reading occurred in late October 2022. It took a while, but the stock eventually broke support at 138 in early December 2022.

#### Using ROC with High Volatility Stocks

<figure><img src="/files/tol6axzNDaPfMezwMGE7" alt=""><figcaption><p>High volatility stock with ROC</p></figcaption></figure>

The chart above shows Abercrombie & Fitch (ANF) within a trading range from October 2006 to February 2008. The 20-day Rate of Change indicator sets overbought at +10% and oversold at -10%. The overbought and oversold levels identify extremes quite well, but timing the actual turn is more difficult because of the volatility. The following chart reduces this volatility by using an [exponential moving average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md#exponential_moving_average_formulas) in place of the price plot.

<figure><img src="/files/12U3Q3Y49Z4gyTgStiG9" alt=""><figcaption><p>Adjusting the chart to accomodate high volatility</p></figcaption></figure>

The chart above shows ANF as a 10-day EMA (black) and the actual price plot is invisible. A 30-day EMA has been overlaid as a signal line. Furthermore, the 20-day Rate of Change is shown with a 5-day SMA to smooth out the fluctuations. There are fewer overbought and oversold readings using the 5-day SMA. Focusing only on the buy signals, the green dotted line shows when ROC exceeds -10% and the green arrow shows when the 10-day EMA crosses above the 30-day SMA. The oversold readings are usually early, but the moving average crossovers are usually late. Such is life with technical analysis. The point here is to reduce whipsaws by smoothing the data. A 10-day EMA was used because it is faster than a 10-day SMA. A 30-day SMA was used because it is slower than a 30-day EMA. Speeding up the shorter moving average and slowing down the longer moving average makes for slightly quicker signals.

### Identifying Trends With Rate of Change <a href="#identifying_trends_with_rate_of_change" id="identifying_trends_with_rate_of_change"></a>

Even though momentum oscillators are best suited for trading ranges or zigzag trends, they can also be used to define the overall direction of the underlying trend. There are approximately 252 trading days in a year. This can be broken down into 126 days per half year, 63 days per quarter, and 21 days per month. A trend reversal starts with the shortest timeframe and gradually spreads to the other timeframes. The long-term trend is generally up when both the 252-day and 126-day Rate of Change are positive. This means that prices are higher now than 12 and six months ago. Long positions taken six or 12 months ago would be profitable and make buyers happy.

<figure><img src="/files/7KMwjBrT3CEs8h5wNFXT" alt=""><figcaption><p>Identifying the trend using ROC</p></figcaption></figure>

The chart above shows IBM with the 252-day, 126-day, 63-day and 21-day Rate of Change. There have been three big trends in the last three years. The first was up as the 252-day Rate of Change was largely positive until September 2008 (1). The second was down as the indicator turned negative from October 2008 until September 2009 (2). The third is up as the indicator turned positive in late September 2009 (3). Even though the big uptrend remains in force, IBM flattened out on the price chart, which affected the 126-day and 63-day Rate of Change. The 63-day Rate of Change (quarterly) has been flirting with negative territory since February (4). The 126-day Rate of Change (six months) dipped into negative territory for the first time since April 2009 (5). This shows some deterioration in IBM that alerts you to monitor the stock. A break below the six-month trading range would be a bearish development (6).

### Identifying Divergences with Rate of Change

Chartists can look for bullish and bearish divergences between ROC and price, but be wary; these formations can be misleading because of sharp moves. Sustained advances often start with a big surge out of the gate, as shown in the chart below. Subsequent advances are usually less sharp, and this causes a bearish divergence to form in the Rate of Change oscillator. It is important to remember that prices constantly increase as long as the Rate of Change remains positive. Positive readings may be less than before, but a positive Rate of Change still reflects a price increase, not a price decline.

<figure><img src="/files/jtEfTS6bbu2HqU6OUrYo" alt=""><figcaption><p>Using the ROC to identify potential divergences</p></figcaption></figure>

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

The Rate of Change oscillator measures the speed at which prices are changing. An upward surge in the Rate of Change reflects a sharp price advance. A downward plunge indicates a steep price decline. The Rate of Change indicator is best used to identify overbought and oversold extremes in price, typically indicated when ROC values cross above 10 or below -10, respectively. ROC plots for multiple, longer-term timeframes can also help in identifying the overall trend. While divergences between price and ROC can be found, these signals may be misleading, and should be used with caution. Like all technical indicators, the Rate of Change oscillator should be used in conjunction with other aspects of technical analysis.

***

## Charting with Rate of Change (ROC) <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

### Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

Rate of Change can be set as an indicator above, below or behind a security's price plot. When the indicator is first chosen from the dropdown list, its parameter is set to 12 by default; from there, it can be adjusted to increase or decrease sensitivity. Chartists can also add a moving average to act as a signal line or to smooth the data, or add one or more horizontal lines using the Overlay settings for the ROC indicator. In the example below, red lines were added at +10 and -10 to mark overbought and oversold levels.&#x20;

[Click here for a live version of this chart](https://stockcharts.com/sc3/ui/?s=$COMPQ\&p=D\&b=5\&g=0\&id=p79327039629\&listNum=30\&a=201216941).

<figure><img src="/files/ppTfXAGy687y20XwwydR" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/PYWpFE85X4jetKtA5nQm" alt=""><figcaption><p>SharpCharts Settings for the ROC (Rate of Change) Indicator</p></figcaption></figure>

{% hint style="info" %}
**Learn More:** For more details on the parameters used to configure Rate of Change indicators, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#rate_of_change_roc) in the Support Center.
{% endhint %}

### Using with StockChartsACP

This indicator can be added from the Chart Settings panel for your StockChartsACP chart. The indicator can be positioned above, below, or behind the security's price plot.

<figure><img src="/files/r8cuyoEpBSHrLpi2g5mL" alt=""><figcaption></figcaption></figure>

[Click here for a live version of this chart.](https://schrts.co/IEUmVNNi)

By default, the indicator looks at price change across 12 periods. This parameter can be adjusted to meet your technical analysis needs.

## Scanning for Rate of Change <a href="#suggested_scans" id="suggested_scans"></a>

StockCharts members can screen for stocks based on Rate of Change values. Below are some example scans that can be used for ROC-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when a ROC-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-al/al).

### Oversold Rate of Change <a href="#oversold_rate-of-change" id="oversold_rate-of-change"></a>

This scan reveals stocks with a positive 126-day Rate of Change and an oversold 21-day Rate of Change (below -8%). For stocks that meet these criteria, a bullish signal is triggered when the stock closes above the 20-day SMA.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [Daily ROC(126,Daily Close) > 0]
AND [Daily ROC(21,Daily Close) < -8]
AND [Yesterday's Daily Close < Yesterday's Daily SMA(20,Daily Close)]
AND [Daily Close > Daily SMA(20,Daily Close)]
```

### Overbought Rate of Change <a href="#overbought_rate-of-change" id="overbought_rate-of-change"></a>

This scan reveals stocks with a negative 126-day Rate of Change and an overbought 21-day Rate of Change (above 8%). For stocks that meet these criteria, a bearish signal is triggered when the stock closes below the 20-day SMA.

```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]

AND [Daily ROC(126,Daily Close) < 0]
AND [Daily ROC(21,Daily Close) > 8]
AND [Yesterday's Daily Close > Yesterday's Daily SMA(20,Daily Close)]
AND [Daily Close < Daily SMA(20,Daily Close)]
```

{% hint style="info" %}
**Learn More:** For more details on the syntax to use for ROC scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#rate_of_change) in the Support Center.
{% endhint %}

## Additional Resources <a href="#further_study" id="further_study"></a>

### Recommended Books

[*Technical Analysis of the Financial Markets*](https://a.co/d/g2lRQ3h) has a chapter devoted to momentum oscillators and their various uses. John Murphy covers the pros and cons as well as some examples specific to Rate of Change. Martin Pring's [*Technical Analysis Explained*](https://a.co/d/9ima6RX) shows the basics of momentum indicators by covering divergences, crossovers, and other signals. There are two more chapters covering specific momentum indicators, each containing plenty of examples.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/rate-of-change-roc.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
