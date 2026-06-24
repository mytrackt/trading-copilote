> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/volume-weighted-average-price-vwap.md).

# Volume-Weighted Average Price (VWAP)

## What Is the Volume-Weighted Average Price? <a href="#introduction" id="introduction"></a>

Volume-Weighted Average Price (VWAP) is exactly what it sounds like: **the average price weighted by volume.** VWAP equals the dollar value of all trading periods divided by the total trading volume for the current day. The VWAP overlay is calculated using intraday data from a single market day, starting when trading opens and ending when it closes.&#x20;

<figure><img src="/files/xulvu7N0greA6xfBJ7jZ" alt=""><figcaption></figcaption></figure>

Originally developed by institutional investors in order to place large orders without disrupting the market, VWAP can also be used by retail investors. The VWAP line functions almost like a single-day moving average. Chartists can assess the position of price relative to the VWAP line in order to determine the intraday trend, or to set favorable entry and exit points for trades.

## Calculating VWAP <a href="#vwap_calculation" id="vwap_calculation"></a>

VWAP is calculated using intraday data for a single day, starting from the first trade of the day and ending when the market closes. The calculated values for each period produce a line that is overlaid on the chart.

{% hint style="success" %}
**Cool Tip:** Sometimes you want to start the VWAP line at a specific date and time (e.g. at a significant high or low, earnings announcement, or some other indicator of a change in market psychology). This way, the VWAP line would be calculated using only price action since the significant event. You can use the [Anchored VWAP overlay](/table-of-contents/technical-indicators-and-overlays/technical-overlays/anchored-vwap.md) to set a specific start time.&#x20;
{% endhint %}

### Tick vs. Minute Data <a href="#tick_versus_minute" id="tick_versus_minute"></a>

Traditional VWAP is based on tick data. As you can imagine, there are many ticks (trades) during each minute of the day. Active securities during active periods can have 20–30 ticks in one minute alone. With 390 minutes in a typical stock exchange trading day, many stocks end up with well over 5000 ticks per day. Over 5000 stocks are traded every day, and these ticks start adding up exponentially. Needless to say, tick data is very resource-intensive.

Instead of VWAP based on tick data, StockCharts.com offers intraday VWAP based on intraday periods (1, 5, 10, 15, 30, or 60 minutes). Note that VWAP is not defined for daily, weekly, or monthly periods due to the nature of the calculation (see below).

### VWAP Formulas

The formula for VWAP is fairly simple:

{% code overflow="wrap" %}

```
Cumulative(Volume x Typical Price)/Cumulative(Volume)
```

{% endcode %}

There are five steps involved in this calculation:

1. Compute the typical price for the intraday period. This is the average of the high, low, and close: `(H+L+C)/3)`.&#x20;
2. Multiply the typical price by the period's volume.&#x20;
3. Create a running total of these values. This is also known as a cumulative total.&#x20;
4. Create a running total of volume (cumulative volume).&#x20;
5. Divide the running total of price-volume by the running total of volume.

The spreadsheet example below shows one-minute VWAP for the first 30 minutes of trading in IBM. Dividing cumulative price volume by cumulative volume produces a price level adjusted (weighted) by volume. The first VWAP value is always the typical price because volume is equal in the numerator and the denominator. They cancel each other out in the first calculation.&#x20;

<figure><img src="/files/FTtAgy4HGJMe0MjmZhAA" alt=""><figcaption><p>VWAP calculation example for IBM</p></figcaption></figure>

The chart below shows one-minute bars with VWAP for IBM covering the same time period as the spreadsheet. For the first 30 minutes of trading, prices ranged from $127.36 on the high to $126.67 on the low. It was a volatile first 30 minutes. VWAP ranged from 127.21 to 127.09 and spent its time in the middle of this range.

<figure><img src="/files/Y07XJy1kKH1PfSe2FtTz" alt="Chart from StockCharts.com of one-minute bars with a VWAP overlay."><figcaption><p>One-minute bars with VWAP on the IBM chart</p></figcaption></figure>

### VWAP vs. Moving Averages <a href="#characteristics" id="characteristics"></a>

The VWAP line behaves similarly to a moving average, but because VWAP only uses values from a single trading day, the VWAP values at the beginning of that day use very few data points, and the values at market close are calculated using far more data.&#x20;

The one-minute VWAP value at the end of the day is often close to the ending value for a 390-minute moving average. Both moving averages are based on the one-minute bars for that day. At the close, both are based on 390 minutes of data (one full day).&#x20;

You cannot compare the 390-minute moving average to VWAP during the day, however. A 390-minute moving average at 12:00 PM will include data from the previous day. VWAP will not. Remember, VWAP calculations start fresh at the open and end at the close. Since 150 minutes of trading have elapsed by 12:00 PM, VWAP at 12:00 PM would need to be compared with a 150-minute moving average instead.

<figure><img src="/files/nm1FK24lq7Q0jKv7GQeY" alt="Chart from StockCharts.com comparing a one-minute VWAP and a 390-minute moving average"><figcaption><p>VWAP compared with a 150-minute SMA at noon and a 390-minute SMA at close.</p></figcaption></figure>

## Interpreting VWAP

While VWAP was originally developed for institutional investors to use when making large trades, individual investors can also use this overlay to determine the intraday trend and to assess entry/exit points.

### Determining the Intraday Trend

Like moving averages, VWAP lags price because it is an average based on past data. The more data there is, the greater the lag.&#x20;

Despite this lag, you can compare VWAP with the current price to determine the general direction of intraday prices. It works like a moving average. In general, intraday prices fall when below VWAP and rise when above VWAP. VWAP will fall somewhere between the day's high-low range when prices are range-bound for the day.&#x20;

The next three charts show examples of flat, rising, and falling VWAP lines.

In the first chart, Merck (MRK) was in a trading range all day, and the VWAP line was flat across most of the chart. Because the first VWAP data point uses only one bar of price data in its calculations, the VWAP line starts closer to the opening price, but it quickly drops into a flat line as more price bars are added to the calculation.

<figure><img src="/files/DHcpxvNIPP4nZJvXZAUB" alt="Chart from StockCharts.com showing a flat VWAP"><figcaption><p>Example of flat VWAP line</p></figcaption></figure>

In the second chart, the price of General Electric (GE) was rising throughout the day, and the VWAP line rose accordingly. Notice that the price bars are above the VWAP line throughout most of the day. Again, the early VWAP values are a little erratic because so few data points have been accumulated for the calculation.&#x20;

<figure><img src="/files/n4E6FWRmZkotJCfxFZmx" alt="Chart from StockCharts.com showing a rising VWAP"><figcaption><p>Example of rising VWAP line</p></figcaption></figure>

The third chart shows the price of Microsoft (MSFT) falling throughout the day, with the VWAP line falling accordingly. In this case, the price bars spend most of the day below the VWAP line.

<figure><img src="/files/jMaTlvygWwwMV5l8qHj6" alt="Chart from StockCharts.com showing a falling VWAP"><figcaption><p>Example of falling VWAP line</p></figcaption></figure>

In all three examples, the direction of the VWAP line and its position relative to the price bars give chartists clues as to the intraday trend.

### Assessing Entry and Exit Points

VWAP is used to identify [liquidity](/table-of-contents/glossary/glossary-l.md#liquidity) points. As a volume-weighted price measure, VWAP reflects price levels weighted by volume. This can help institutions with large orders. The idea is not to disrupt the market when entering large buy or sell orders. VWAP helps these institutions determine the liquid and illiquid price points for a specific security over a very short time.

VWAP can also be used to measure trading efficiency. After buying or selling a security, institutions or individuals can compare its price to VWAP values. A buy order executed below the VWAP value would be considered a good fill because the security was bought at a below-average price. Conversely, a sell order executed above the VWAP would be deemed a good fill because it was sold at an above-average price.

***

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

VWAP serves as a reference point for one day's prices. Because of this, it's best suited for **intraday analysis.** Chartists can compare current prices with the VWAP values to determine the intraday trend. VWAP can also be used to determine relative value. Prices below VWAP values are relatively low for that day or that specific time. By contrast, prices above VWAP values are relatively high for that day or that specific time. **Remember that VWAP is a cumulative indicator, which means the number of data points progressively increases throughout the day.** On a one-minute chart, IBM will have 90 data points (minutes) by 11:00 AM, 210 data points by 1:00 PM, and 390 data points by the close. The number dramatically increases as the day extends. This is why VWAP lags price, and this lag increases as the day extends.

***

## Charting with VWAP <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The VWAP overlay can be added to intraday SharpCharts and ACP Charts.

### Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

Volume-Weighted Average Price (VWAP) can be plotted as a price overlay on Sharpcharts. After entering the security symbol, choose an **intraday** period and a **range**. The Period determines the data used to calculate the overlay. The range can set be for one day or "fill the chart." If you want more detail, choose "fill the chart," and if you want general levels, choose one day.&#x20;

VWAP can be plotted over more than one day, but the overlay will jump from its prior closing value to the typical price for the next open as a new calculation period begins. Also, note that VWAP values can sometimes fall off the price chart. VWAP at 45.50 will not show up on a chart with a price range from $45.80 to $47. You may sometimes need to extend the range to a full day to see VWAP on the chart. The VWAP value is always displayed in the legend at the top left of the chart.

[Click here for a live version of this chart.](https://stockcharts.com/sc3/ui/?s=INTU\&a=2277810739\&p=1\&yr=0\&mn=0\&dy=1\&id=p13211053241)

<figure><img src="/files/n9WuPHPbJyEzMtoQPhNW" alt="Chart from StockCharts.com showing a VWAP overlay on a one-minute chart of INTC"><figcaption></figcaption></figure>

<figure><img src="/files/F2dnA8SQplW6S2buhsH6" alt="Screenshot of Chart Attributes settings in SharpCharts"><figcaption><p>SharpCharts settings for the VWAP overlay</p></figcaption></figure>

{% hint style="info" %}
**Learn More.** For more details on the parameters used to configure VWAP overlays, please see our [SharpCharts Parameter Reference](https://help.stockcharts.com/charts-and-tools/sharpcharts/sharpcharts-workbench/editing-sharpcharts/sharpcharts-parameter-reference#vwap) in the Support Center.
{% endhint %}

### Using with StockChartsACP

This overlay can be added from the Chart Settings panel for your intraday StockChartsACP chart.&#x20;

<figure><img src="/files/Y4jaou7PW7GrzAosgKOd" alt=""><figcaption></figcaption></figure>

[Click here for a live version of this chart.](https://schrts.co/hHEsRsyE)

This overlay takes no parameters, but the color and style of the VWAP line can be customized for your chart.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/volume-weighted-average-price-vwap.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
