> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/bollinger-bandwidth.md).

# Bollinger BandWidth

## What Is Bollinger BandWidth? <a href="#what_is_bollinger_bandwidth" id="what_is_bollinger_bandwidth"></a>

Bollinger BandWidth is an indicator derived from [Bollinger Bands](/table-of-contents/technical-indicators-and-overlays/technical-overlays/bollinger-bands.md). In his book, [*Bollinger on Bollinger Bands*](https://a.co/d/3GheeTh), John Bollinger refers to Bollinger BandWidth as one of two indicators that can be derived from Bollinger Bands (the other being %B).

A Bollinger Band indicator consists of a middle band with two outer bands. The middle band is a [simple moving average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) usually set at 20 periods. The outer bands are usually set two standard deviations above and below the middle band. The settings can be modified depending on the characteristics of a security or your trading style. &#x20;

The Bollinger BandWidth measures the percentage difference between the upper and lower band. BandWidth decreases as Bollinger Bands narrow and increases as Bollinger Bands widen. Because Bollinger Bands are based on the standard deviation, falling BandWidth reflects decreasing volatility and rising BandWidth reflects increasing volatility.

## SharpCharts Bollinger BandWidth Calculation <a href="#sharpcharts_bollinger_bandwidth_calculation" id="sharpcharts_bollinger_bandwidth_calculation"></a>

```
( (Upper Band - Lower Band) / Middle Band) * 100
```

When calculating BandWidth, the first step is to subtract the value of the lower band from the value of the upper band. This shows the absolute difference. This difference is then divided by the middle band, which normalizes the value. This normalized Bandwidth can then be compared across different timeframes or with the BandWidth values for other securities.

The chart below shows the Nasdaq 100 ETF (QQQ) with Bollinger Bands, BandWidth, and the Standard Deviation.

<figure><img src="/files/cfh5KXN7KWyRMvlZNzLv" alt="Chart from StockCharts showing Bollinger Bands, BandWidth, and Standard Deviation"><figcaption><p>Chart of Bollinger Bands, BandWidth, and Standard Deviation.</p></figcaption></figure>

Notice how BandWidth tracks the Standard Deviation (volatility). Both rise and fall together. The image below shows a spreadsheet with a calculation example.

<figure><img src="/files/ToJ3acjA4yQkb29hSm6y" alt="Spreadsheet showing how Bollinger BandWidth is calculated."><figcaption><p>Spreadsheet calculating BandWidth.</p></figcaption></figure>

## Defining Narrowness <a href="#defining_narrowness" id="defining_narrowness"></a>

Narrow BandWidth is relative. BandWidth values should be gauged relative to prior BandWidth values over a period of time. It is important to get a good look-back period to define BandWidth range for a particular ETF, index, or stock. For example, an eight- to 12-month chart will show BandWidth highs and lows over a significant timeframe. BandWidth is considered narrow as it approaches the lows of this range and wide as it approaches the high end.

Securities with low volatility will have lower BandWidth values than securities with high volatility. For example, the Utilities SPDR (XLU) represents utility stocks, which have relatively low volatility (see lower chart). The Technology SPDR (XLK) represents technology stocks, which have relatively high volatilities. Because of lower volatility, XLU will have consistently lower BandWidth values than XLK. The 200-day moving average of XLU BandWidth is below five, while the 200-day moving average of XLK BandWidth is above seven.

<figure><img src="/files/1RJJj3LU28Ht3iejmWJg" alt=""><figcaption><p>BB Bandwidth applied to XLK.</p></figcaption></figure>

<figure><img src="/files/p9et8X0GG2jvLdgaqm04" alt=""><figcaption><p>BB BandWidth applied to XLU.</p></figcaption></figure>

## Signal: The Squeeze <a href="#signalthe_squeeze" id="signalthe_squeeze"></a>

Bollinger BandWidth is best known for identifying **The Squeeze**. This occurs when volatility falls to a low level, as evidenced by the narrowing bands. The upper and lower bands are based on the standard deviation, which measures volatility. The bands narrow as price flattens or moves within a relatively narrow range. The theory is that periods of low volatility are followed by periods of high volatility. Relatively narrow BandWidth (a.k.a. the Squeeze) can foreshadow a significant advance or decline. After a Squeeze, a price surge and subsequent band break signal the start of a new move. A new advance starts with a Squeeze and subsequent break above the upper band. A new decline starts with a Squeeze and subsequent break below the lower band.

The chart below shows Alaska Airlines (ALK) with a squeeze in mid-June. After the April–May decline, ALK stabilized in early June as Bollinger Bands narrowed. BandWidth dipped below 10 to put the Squeeze play on in mid-June. Keep in mind that 10 refers to 10%. In other words, the width of the bands is equal to 10% of the middle band. Even though this level seems high, it is actually quite low for ALK. With the stock trading at around $15–$16, BandWidth was less than 10% and at its lowest level in over a year. With the subsequent surge above the upper band, the stock broke out to trigger an extended advance.

<figure><img src="/files/YJ1eyx3WwkxV3uzdpJyR" alt=""><figcaption><p>Bollinger BandWidth applied to Alaska Airlines.</p></figcaption></figure>

The chart below shows Aeropostale (ARO) with a couple of Squeezes. A horizontal line was added to the indicator window. This line marks 8, which is deemed relatively low based on the historical range. The BandWidth indicator alerted traders to be ready for a move in mid-August. Note that the stock surged above the upper band and continued higher throughout September. The advance stalled in late September and BandWidth narrowed again in October. Notice how BandWidth declined below the lows set in August and then flattened out. The subsequent break below the lower Bollinger Band triggered a bearish signal in late October.

<figure><img src="/files/mn0CJzBtUvUX76YabiiX" alt=""><figcaption><p>Bollinger Bandwidth applied to Aerospotale.</p></figcaption></figure>

The Squeeze can also be applied to weekly charts or longer timeframes. Volatility and BandWidth are typically higher on the weekly timeframe than a daily timeframe. This makes sense because larger price movements can be expected over longer timeframes.&#x20;

The chart below shows Barrick Gold (ABX) consolidating throughout 2006 and into 2007. As the consolidation narrowed and a triangle formed, Bollinger Bands contracted and BandWidth dipped below $10 in January 2007. Notice how BandWidth remained at low levels as the consolidation extended. A bullish signal triggered with the breakout in July 2007. BandWidth also rose as prices moved sharply in one direction and Bollinger Bands widened.

<figure><img src="/files/CIJCOLOOgJeL3Uq25Mre" alt=""><figcaption><p>Chart 6</p></figcaption></figure>

The chart below shows Honeywell (HON) with an extended trading range in the $50–$55 area. There was a move to the upper band in May, but no breakout for a signal. Instead, HON clearly broke below the lower band to trigger a bearish signal in June 2007.

<figure><img src="/files/DlPARDLjk0ioJ01izPyb" alt=""><figcaption><p>Chart 7</p></figcaption></figure>

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

Derived from Bollinger Bands, the BandWidth indicator is a tool to identify periods of low and high market volatility. This, in turn, can give you some insight into potential market movements. The direction depends on the subsequent band break. The condition known as “The Squeeze” happens when the BandWidth is at a historically low level, suggesting that a significant price move is imminent, more or less. Once you identify the squeeze, it's time to watch for a breakout above the upper band, indicating an upward trend, or a break below the lower band, hinting at a downward trend. Like all indicators, you should approach its signals with caution, as initial breaks can sometimes fail, and not all signals are reliable.

***

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

Bollinger BandWidth can be found in the indicator list on SharpCharts. The default parameters (20,2) are based on the default parameters for Bollinger Bands. These can be changed accordingly. 20 represents the simple moving average. 2 represents the number of standard deviations for the upper and lower band. BandWidth can be positioned above, below or behind the price plot. [Click here](https://stockcharts.com/sc3/ui/?s=SPY\&p=D\&yr=0\&mn=6\&dy=0\&id=p38029592805\&listNum=30\&a=195096097) to see a live example of BandWidth.

<figure><img src="/files/IYYat8Bl7rg6Bfrc4eqv" alt=""><figcaption><p>Chart 8</p></figcaption></figure>

## Using with MarketCarpets <a href="#using_with_marketcarpets" id="using_with_marketcarpets"></a>

You can compare BandWidth for several securities by using normalized Bollinger BandWidth in MarketCarpet. Using the [S\&P Sector MarketCarpet](https://stockcharts.com/marketcarpet/?group=SEC) as an example, choose Bollinger BandWidth from the **Measurements** dropdown menu. From the **Color By** dropdown menu, select **Latest Value** to view absolute levels.

If you're using the Red to Green color scheme, the darker green boxes identify stocks with relatively wide BandWidths. The lighter colored boxes represent stocks with relatively narrow BandWidths (see legend below the MarketCarpet).

Hover your mouse over any box to view a mini price chart of the stock. To find more details, double-click on the box. This will take you to the **Symbol Summary** page of the specific stock.&#x20;

In addition to viewing the stocks as a MarketCarpet, you can view them as a list by clicking the **Table** button. This lists all the stocks which you can sort in ascending or descending order.

If you wish to dive into each sector, click on the sector heading (e.g. Technology). This allows you to  view all stocks within a sector that have wide or narrow BandWidths.

<figure><img src="/files/QlRqPyTafAIsLXORupRM" alt="The MarketCarpet from StockCharts.com comparing Bollinger BandWidths of stocks in the S&#x26;P 500 sectors"><figcaption><p>Comparing BandWidths for stocks in the S&#x26;P 500 sectors.</p></figcaption></figure>

## Suggested Scans <a href="#suggested_scans" id="suggested_scans"></a>

### Bollinger Band Breakout <a href="#bollinger_band_breakout" id="bollinger_band_breakout"></a>

This scan reveals stocks whose Bollinger Bands just expanded rapidly after being contracted for 5 or more days.

```
[type = stock] AND [country = US] 
AND [Daily SMA(20,Daily Volume) > 40000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Daily BB Width(20,2) > Yesterday's max(5, BB Width(20,2)) * 2]
```

For more details on the syntax to use for BandWidth scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference) in the Support Center.

## FAQs: Bollinger BandWidth <a href="#bollinger_bandwidth_faqs" id="bollinger_bandwidth_faqs"></a>

<details>

<summary>What do increasing and decreasing BandWidth values indicate?</summary>

An increasing BandWidth reflects increasing volatility in the price, while a decreasing BandWidth reflects decreasing volatility.

</details>

<details>

<summary>What is the significance of the "Squeeze" in the Bollinger BandWidth context?</summary>

The “Squeeze” is when volatility falls to a very low level, causing the bands to narrow. This phenomenon can foreshadow a significant price movement either upwards or downwards.

</details>

<details>

<summary>How should BandWidth values be gauged over time?</summary>

BandWidth values should be compared to prior BandWidth values over a significant timeframe, like an eight- to 12-month chart, to determine what is considered “narrow” or “wide” for that particular security.

</details>

<details>

<summary>Can BandWidth values be compared across different securities?</summary>

Yes, but it's crucial to note that securities with lower volatility will naturally have lower BandWidth values than those with higher volatility. For instance, utility stocks generally have lower BandWidth values than technology stocks.

</details>

<details>

<summary>What caution should you take after observing a Squeeze followed by a band break?</summary>

You should be cautious of “head-fakes” or false signals. Sometimes, after a Squeeze, the initial band break might not hold, causing prices to reverse in the opposite direction. It's essential to observe the strength of the breakout; strong breaks are less likely to revert, while weak breakouts followed by immediate pullbacks should serve as warnings.

</details>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/bollinger-bandwidth.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
