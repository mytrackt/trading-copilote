> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-atr.md).

# Average True Range (ATR)

## What Is the Average True Range (ATR)? <a href="#what_is_the_average_true_range_atr" id="what_is_the_average_true_range_atr"></a>

Developed by J. Welles Wilder, the Average True Range (ATR) is an indicator that measures [volatility](/table-of-contents/glossary/glossary-v.md#volatility). As with most of his indicators, Wilder designed ATR with commodities and daily prices in mind. Commodities are frequently more volatile than stocks. They are often subject to gaps and limit moves, which occur when a commodity opens up or down its maximum allowed move for the session. A volatility formula based only on the high-low range would fail to capture volatility from gap or limit moves. Wilder created the Average True Range to capture this “missing” volatility. It is important to remember that ATR doesn't indicate price direction, just volatility.

Wilder features ATR in his 1978 book, *New Concepts in Technical Trading Systems*. This book also includes the Parabolic SAR, RSI, and the Directional Movement Concept (ADX). Despite being developed before the computer age, Wilder's indicators have stood the test of time and remain extremely popular.

## True Range <a href="#true_range" id="true_range"></a>

Wilder started with a concept called **True Range (TR)**, which is defined as the greatest of the following:

* Method 1. Current High less the current Low
* Method 2. Current High less the previous Close (absolute value)
* Method 3. Current Low less the previous Close (absolute value)

Absolute values are used to ensure positive numbers. After all, Wilder was interested in measuring the distance between two points, not the direction. If the current period's high is above the prior period's high and the low is below the prior period's low, then the current period's high-low range will be used as the True Range. This is an outside day that would use Method 1 to calculate the TR. This is pretty straightforward. Methods 2 and 3 are used when there is a gap or an inside day. A gap occurs when the previous close is greater than the current high (signaling a potential gap down or limit move) or the previous close is lower than the current low (signaling a potential gap up or limit move). The image below shows examples of when methods 2 and 3 are appropriate.

<figure><img src="/files/vJKtvqkiWufxA2PrxfeK" alt=""><figcaption><p>ATR - True Range Image</p></figcaption></figure>

**Example A.** A small high/low range formed after a gap up. The TR equals the absolute value of the difference between the current high and the previous close.

**Example B.** A small high/low range formed after a gap down. The TR equals the absolute value of the difference between the current low and the previous close.

**Example C.** Even though the current close is within the previous high/low range, the current high/low range is quite small. In fact, it is smaller than the absolute value of the difference between the current high and the previous close, which is used to value the TR.

## How To Calculate ATR <a href="#how_to_calculate_atr" id="how_to_calculate_atr"></a>

Typically, the Average True Range (ATR) is based on 14 periods and can be calculated on an intraday, daily, weekly or monthly basis. For this example, the ATR will be based on daily data. Because there must be a beginning, the first TR value is simply the High minus the Low, and the first 14-day ATR is the average of the daily TR values for the last 14 days. After that, Wilder sought to smooth the data by incorporating the previous period's ATR value.

```
Current ATR = [(Prior ATR x 13) + Current TR] / 14

  - Multiply the previous 14-day ATR by 13.
  - Add the most recent day's TR value.
  - Divide the total by 14
```

<figure><img src="/files/2MXnLflZO4bQWKcITcXv" alt=""><figcaption></figcaption></figure>

Click below to download an Excel spreadsheet that shows the beginning of an ATR calculation.

{% file src="/files/Kv71lyq3rt54y6pc3pVS" %}

In the spreadsheet example, the first True Range value (0.91) equals the High minus the Low (yellow cells). The first 14-day ATR value (0.56) was calculated by finding the average of the first 14 True Range values (blue cell). Subsequent ATR values were smoothed using the formula above. The spreadsheet values correspond with the yellow area on the chart below; notice how ATR surged as QQQ plunged in May with many long candlesticks.

<figure><img src="/files/RtfEtbplu1pn2bZTX8Yo" alt=""><figcaption><p>ATR plotted on chart using StockCharts.com - Chart 1</p></figcaption></figure>

For those trying this at home, a few caveats apply. First, just like with [Exponential Moving Averages (EMAs)](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md), ATR values depend on how far back you begin your calculations. The first True Range value is the current high minus the current low, and the first ATR is an average of the first 14 True Range values. The real ATR formula kicks in on day 15. Even so, the remnants of these first two calculations “linger” to slightly affect subsequent ATR values. **Spreadsheet values for a small subset of data may not match exactly with what is seen on the price chart.** Decimal rounding can also slightly affect ATR values. On our charts, we calculate back at least 250 periods (typically much further) to ensure a much greater degree of accuracy for our ATR values.

## Absolute ATR <a href="#absolute_atr" id="absolute_atr"></a>

ATR is based on the True Range, which uses absolute price changes. As such, ATR reflects volatility at an absolute level. In other words, ATR is not shown as a percentage of the current close. This means low-priced stocks will have lower ATR values than high-price stocks. For example, a $20-30 security will have much lower ATR values than a $200-300 security. Because of this, ATR values are not comparable. Large price movements for a single security, such as a decline from 70 to 20, can make long-term ATR comparisons impractical. Chart 4 shows Google with double-digit ATR values, and chart 5 shows Microsoft with ATR values below 1. Despite different values, their ATR lines have similar shapes.

<figure><img src="/files/TbNrYCnxtgXZ8GAf4cPD" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/cPioD1IeEXAcH2IQnRBL" alt=""><figcaption></figcaption></figure>

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

ATR is not directional indicators like MACD or RSI. Instead, it's a unique volatility indicator that reflect the degree of interest or disinterest in a move. Large ranges or True Ranges often accompany strong moves in either direction, which can be volatile. This is especially true at the beginning of a move. Relatively narrow ranges can accompany low-volatility moves. The ATR can validate the enthusiasm behind a move or breakout. A bullish reversal with increased ATR would show strong buying pressure and reinforce the reversal. A bearish support break with increased ATR would show strong selling pressure and reinforce the support break.

***

## Using ATR with SharpCharts <a href="#using_atr_with_sharpcharts" id="using_atr_with_sharpcharts"></a>

Listed as “Average True Range,” ATR is on the Indicators drop-down menu. The “parameters” box to the right of the indicator contains the default value, 14, for the number of periods used to smooth the data. To adjust the period setting, highlight the default value and enter a new setting. In his work, Wilder often used an 8-period ATR. SharpCharts also allows users to position the indicator above, below or behind the price plot. A moving average can be added to identify upturns or downturns in ATR. Click “advanced options” to add a moving average as an indicator overlay. [Click here](https://stockcharts.com/sc3/ui/?s=$INDU\&p=D\&b=5\&g=0\&id=p51341747448\&listNum=30\&a=202613287) for a live example of ATR.

<figure><img src="/files/BvgwXJc4E9YuikSdgijE" alt=""><figcaption><p>ATR - SharpCharts</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Weeding Out High Volatility <a href="#weeding_out_high_volatility" id="weeding_out_high_volatility"></a>

The Average True Range indicator can be used in scans to weed out securities with extremely high volatility. This simple scan searches for S\&P 600 stocks that are in an uptrend. The final scan clause excludes high volatility stocks from the results. Note that the ATR is converted to a percentage of sorts so that the ATR of different stocks can be compared on the same scale.

```
[group is SP600]
AND [Daily EMA(50,close) > Daily EMA(200,close)]  

AND [ATR(250) / SMA(20,Close) * 100 < 4] 
```

For more details on the syntax to use for ATR scans, please see our [Scanning Indicator Reference](https://support.stockcharts.com/doku.php?id=scans:indicators#average_true_range_atr) in the Support Center.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-atr.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
