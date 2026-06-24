> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/kagi-charts.md).

# Kagi Charts

## What Are Kagi Charts?  <a href="#introduction" id="introduction"></a>

Kagi charts are based strictly on price action. They ignore time. In this way, Kagi charts are similar to [Point & Figure ](/table-of-contents/chart-analysis/point-and-figure-charts.md)charts. According to Steve Nison, author of *Beyond Candlesticks*, Kagi charts were invented in the late 19th century in Japan. They are line charts that change direction when prices move by a required amount. There is also the added aspect of yin and yang as the lines change thickness when prices break above a prior high or below a prior low.

## Reversal Amount <a href="#reversal_amount" id="reversal_amount"></a>

As Kagi charts are all about reversals, chartists must start by setting the reversal amount. This can be a fixed number of points, a set percentage or a variable [Average True Range](/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-atr.md) (ATR). Note that this reversal amount can also be based on closing prices or the high-low range. The following examples will use closing prices for simplicity. (Chartists looking for more sensitivity and more reversals can opt for the high-low range.)

The reversal amount is the minimum price change required for the Kagi line to reverse direction. Let's start with an example using a close-only chart for the S\&P 500 and a 20 point reversal amount. If the Kagi line is rising and the S\&P 500 reaches 1951, the Kagi line will not reverse until the S\&P 500 declines to 1931 or lower (20 or more points). Conversely, if the Kagi line is falling and the S\&P 500 declines to 1900, the Kagi line will not reverse until the S\&P 500 advances to 1920 or higher (20 or more points).&#x20;

The example below shows the upside reversals with green arrows and downside reversals with red arrows. The last Kagi value (1951.27) is marked with the y-axis label. The S\&P 500, however, is currently at 1943.89, which is below the high of the Kagi line. Again, the Kagi line will not reverse until the index moves below 1931 (20 points).

<figure><img src="/files/xoGfs1ML6SCvpFW1cjUT" alt="Kagi line chart from StockCharts.com showing upside reversals (green arrows) and downside reversals (red arrows)."><figcaption><p>The green arrows point to upside reversals, whereas the red arrows point to downside reversals.</p></figcaption></figure>

The chart below shows daily close-only prices for the S\&P 500. Notice that the advance from 1870.85 to 1951.27 looks different because it extends from May 15 to June 11 (yellow area).&#x20;

<figure><img src="/files/XNwm8MzdP17zGjBZR3rr" alt="A close-only line chart from StockCharts.com shows how different this is from a Kagi line chart."><figcaption><p>Chart showing close-only prices. Note the difference between this chart and the Kagi line chart.</p></figcaption></figure>

The Kagi line ignored the date changes and rose vertically because it is based purely on price. This price focus means the x-axis (date range) will be different and irregular on the Kagi chart. A line or bar chart has a uniform x-axis with daily price data. The date on the Kagi chart doesn't change until there's a reversal. If the S\&P 500 falls to 1930, more than 20 points from the Kagi high, a small horizontal line would be drawn at 1951.27, and a down line would be drawn to 1930. This new line would then warrant a date marker on the x-axis.

## Fixed Amount versus ATR <a href="#fixed_amount_versus_atr" id="fixed_amount_versus_atr"></a>

The reversal amount can also be set as a percentage, a fixed amount that will not change as new data is incorporated into the chart. In other words, new price data is added every trading day, and the reversal amount will remain constant when using points or percentages.

The reversal amount is subject to change when using the ATR, a volatility measure. The default ATR is based on 14 periods and fluctuates along with price volatility. Also, note that the ATR value changes as new days and data points come into play.&#x20;

When the chart is created, the reversal amount is based on the prevailing ATR value. Should the ATR value change in the following days or weeks, this new value would be used as the reversal amount. This means the look of the Kagi chart will also change. Also note that ATR values on a line or bar chart are based on the actual trading periods (14 days, 14 weeks, 14 months, etc.). Therefore, ATR values on a Kagi chart will not match ATR values on a chart with a uniform date axis.

The chart below shows a regular close-only chart ending on April 15.&#x20;

<figure><img src="/files/wQ6yhBTkodMOmrLxJhS5" alt="A close-only chart from StockCharts.com"><figcaption><p>A close-only chart.</p></figcaption></figure>

The chart below shows a Kagi chart created on April 15, which is also the last date.&#x20;

<figure><img src="/files/n2gLTFQyQ8d7Sr3IQvjT" alt="Kagi chart from StockCharts.com"><figcaption><p>Kagi chart.</p></figcaption></figure>

First, notice that the ATR value on the Kagi chart is different than the ATR value on the close-only chart. Second, notice that the ATR value from the close-only chart is used to set the reversal amount on the Kagi chart. If this Kagi chart were created in early January, the ATR reversal value would be around 12.5 and this chart would look different. Remember that ATR reversal amounts will change as new data is added to the chart. Reversal amounts based on points and percentages are fixed.

## Yin and Yang <a href="#yin_and_yang" id="yin_and_yang"></a>

The prior Kagi charts used one color to focus on the reversals. The following Kagi charts show thick black lines for the yang lines and thin red lines for the yin lines. Note that a Kagi peak or trough forms whenever there's a reversal, marked by a small horizontal line. A yang line forms when a Kagi line breaks above the prior peak. A yin line forms when a Kagi line breaks below the prior trough.

The chart below shows some examples of yin and yang lines.&#x20;

<figure><img src="/files/v91uuwFj9hGJSxbK00eu" alt="Yin or thin red lines, and yang, thick black lines on a Kagi chart from StockCharts.com."><figcaption><p>Yin (thin red) and yang (thick black) lines on a Kagi chart.</p></figcaption></figure>

A peak can form with thick black or thin red lines. A thick black line (yang) remains in play until a break below the most recent trough. The thick black line turns into a thin red line at the break point. This thin red line (yin) remains in play until a break above the most recent peak. The thin red line then changes into a thick black line at the break point.

## Signals <a href="#signals" id="signals"></a>

In *Beyond Candlesticks*, Steve Nison highlights several signals and setups using Kagi charts. These include buy on a new yang line, sell on a new yin line, buy rising shoulders, sell falling waists, multi-level breaks, double windows, trend line breaks, tweezers, three Buddha reversals and record sessions. Rather than cover every setup in his great book, this article will highlight a few setups with some chart examples.

The next three Kagi charts use percentage for reversal amount and the high-low range for the price field. A peak on a Kagi chart is also called a shoulder, while a trough is called a waist. Nison notes that a series of rising shoulders defines an advance, while a series of falling waists defines a decline.&#x20;

The CVS chart below shows a steady advance in October–November and a decline in January. Notice how trend lines can be drawn on these charts. We can also use the troughs to mark support. The March–April waists (troughs) are used to mark a support zone.

<figure><img src="/files/ItsTycaRO78qYDz4l2Yw" alt=""><figcaption><p>Chart showing advancing and declining periods. Note the series of waists that mark a support zone.</p></figcaption></figure>

The Humana chart below shows a pair of inverted three Buddha bottoms. As the name implies, these look like inverse head-and-shoulders patterns. The left waist forms the first low, the Buddha's head forms the middle low, and the right waist forms the third low. The Buddha low is the lowest of the three, while the other two are relatively equal. A break above resistance confirms the reversal.

<figure><img src="/files/rJnRYZyst9HFsU7ZdMAd" alt="Kagi chart from StockCharts.com showing an inverted three Buddha bottom pattern."><figcaption><p>Inverted three Buddha bottoms.</p></figcaption></figure>

Kagi peaks (shoulders) and troughs (waists) are also called levels. A series of shoulders can mark a resistance zone, while a series of waists can mark a support zone. You can look for a break of two or more levels to trigger a trend change.&#x20;

The example below shows KLA-Tencor (KLAC) with a few trend line breaks and some multi-level breaks. Notice how the stock broke above three levels and broke the October trend line in February. After advancing above 71, the stock broke below the early February trend line and below three levels in early April. The far right side of the chart shows the stock breaking another trend line and moving above three levels with a surge above 64.

<figure><img src="/files/dMaEyTWH60T8nWcplr0B" alt="Kagi chart from StockCharts.com showing trendline and multi-level breaks."><figcaption><p>Chart showing trendline and multi-level breaks.</p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

Like their Japanese cousins, Renko and Three Line Break, Kagi charts filter the noise by focusing on minimum price changes. Kagi lines do not reverse unless price changes by a minimum amount. Like Point & Figure charts, it is easy to spot important highs and lows, and identify key support and resistance levels. With this information, chartists can define uptrends with higher highs and higher lows or downtrends with lower lows and lower highs. As with all charting techniques, chartists should employ other technical analysis tools to confirm or refute their findings on Kagi charts.

***

## Kagi Charts In SharpCharts <a href="#sharpcharts" id="sharpcharts"></a>

Chartists can create Kagi charts by going to the **Attributes** area of the Chart Settings and selecting Kagi as the **Chart Type**. You can choose points, percentage, or ATR for the reversal amount. The **Price Field** can be set at close or high-low range.&#x20;

If you're looking for more sensitivity, choose the high-low range and if you're looking to focus on end-of-day price data, choose the close. Yin and yang line colors can also be changed using the **Up Color** and **Down Color** dropdown menus in the Chart Settings.&#x20;

***

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="" data-size="line">[**Click here**](https://stockcharts.com/sc3/ui/?s=QQQ\&p=D\&yr=0\&mn=11\&dy=0\&id=p29043089916) for a live example.

***

<figure><img src="/files/2FyvOTTvn1FgkuaodTzg" alt=""><figcaption><p>Kagi chart for QQQ</p></figcaption></figure>

<figure><img src="/files/lpE4Pn8VXNb8ldepoan0" alt="The SharpCharts settings for Kagi charts when using StockCharts.com"><figcaption><p>SharpChart settings for Kagi charts.</p></figcaption></figure>

***

## Further Study <a href="#further_study" id="further_study"></a>

*Beyond Candlesticks*, a book by Steve Nison, shows chartists advanced techniques for candlesticks and other technical analysis techniques that originated in Japan. Nison devotes an entire chapter to Kagi charts; additionally, he covers Three Line Break charts, Renko charts and explains how Japanese traders use moving averages.

| <p><a href="https://a.co/d/4B1HdkV"><strong>Beyond Candlesticks</strong></a><br>Steve Nison</p> |
| ----------------------------------------------------------------------------------------------- |
| <img src="/files/we1PnaOLag2ULhNx5MLq" alt="" data-size="original">                             |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/kagi-charts.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
