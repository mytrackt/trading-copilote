> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/arms-candlevolume.md).

# Arms CandleVolume

## What Is Arms CandleVolume? <a href="#introduction" id="introduction"></a>

Arms CandleVolume charts merge candlesticks and EquiVolume to create a price chart that focuses on volume, the price range, and the candlestick. EquiVolume charts are the brainchild of Richard Arms, creator of the [Arms Index (aka TRIN)](/table-of-contents/glossary/glossary-a.md#arms_index_trin). Arms CandleVolume charts came about after a conversation between Richard Arms and Chip Anderson. In a nutshell, Arms was not entirely happy with CandleVolume charts because they did not emphasize the high-low range enough. Now, with just a glance, chartists can easily determine the relative volume level, the period's range and the price movement from open to close. Arms CandleVolume allows chartists to validate important candlestick patterns with volume and analyze the overall supply-demand dynamics on a chart.

## EquiVolume Overview <a href="#equivolume_overview" id="equivolume_overview"></a>

Arms CandleVolume charts are created by placing a candlestick inside an EquiVolume box. The EquiVolume box dictates the width based on relative volume. Let's look at each individually and then show the merged product.

An EquiVolume box consists of three components—price high, price low, and volume. The price high forms the upper boundary, the price low forms the lower boundary, and volume dictates the width. EquiVolume boxes are black when the close is above the prior close and red when the close is below the prior close.

<figure><img src="/files/LPQbkTvT61j6A9B0hOYK" alt="Illustration displaying three types of EquiVolume boxes."><figcaption><p>Three types of EquiVolume boxes.</p></figcaption></figure>

When calculating EquiVolume charts, note that volume is normalized to show it as a percentage of the lookback period. For a four-month daily chart, each day's volume would be divided by the total volume for those four months. As such, the width of each Arms CandleVolume box represents the percentage of total volume for the lookback period. High-volume days occupy more space on the X-axis (horizontal) than low-volume days.&#x20;

The varying width means the date axis will not be uniform. Some weeks will extend longer because of high volume, while others will be shorter because of low volume.&#x20;

The chart below shows IPG with Arms CandleVolume over four months. Notice how October extends more than the other months. That's because the Arms CandleVolume boxes are wide during this month.&#x20;

<figure><img src="/files/XrOBkWibO3hbJ17jZ894" alt="Chart displaying wide, high volume boxes versus low volume, narrow boxes in a CandleVolume chart type from StockCharts.com"><figcaption><p>Note the wide Arms CandleVolume boxes in October compared to the lower volume, narrower boxes during November and December.</p></figcaption></figure>

The next chart shows IPG with standard candlesticks for reference.

<figure><img src="/files/lSLDbQrnsbERAmEkMIoF" alt="Standard candlestick chart using StockCharts.com"><figcaption><p>Price chart using standard candlesticks.</p></figcaption></figure>

## Candlestick Overview <a href="#candlestick_overview" id="candlestick_overview"></a>

Traditional candlesticks capture the high-low range and the price movement from open to close. Four variations, using colored candlesticks, are shown in the chart below.&#x20;

<figure><img src="/files/2yBq1aGGgQ8Og5ljC4Z5" alt="Colored candlestick charts using StockCharts.com showing four variations of filled and hollow candlestick bars"><figcaption><p>Colored standard candlestick bars have four variations of price action: black-filled, black-hollow, red-filled, and red-hollow.</p></figcaption></figure>

The price change from the close to the prior close determines the candlestick color. Candlesticks are black when the close is higher and red when the close is lower.&#x20;

The price movement from open to close determines whether a candlestick is hollow or filled. The candlestick is hollow when the close is above the open and filled (solid) when the close is below the open.&#x20;

The upper and lower shadows (the thin lines above and below the body) capture the high-low range and match the height of the Arms CandleVolume box.

## Arms CandleVolume <a href="#arms_candlevolume1" id="arms_candlevolume1"></a>

The following three charts show how EquiVolume boxes and candlesticks merge to create Arms CandleVolume charts.

<figure><img src="/files/9WKxEveyqU0Fbjq5nDJs" alt="Example of a standard candlestick chart of Intel Corp. (INTC) from StockCharts.com"><figcaption><p>Standard Candlestick chart. </p></figcaption></figure>

<figure><img src="/files/g3HohuWDTRg5pSVWkmGK" alt="An EquiVolume chart type of Intel Corp. (INTC) from StockCharts.com"><figcaption><p>EquiVolume Chart of Intel Corp. (INTC).</p></figcaption></figure>

<figure><img src="/files/shAsjKsReyEVyVog1Bjq" alt="Example of an Arms CandleVolume chart that combines EquiVolume and candlesticjk charts"><figcaption><p>An Arms CandleVolume chart combines EquiVolume and candlestick charts. </p></figcaption></figure>

## Interpretation <a href="#interpretation" id="interpretation"></a>

Chartists can use Arms CandleVolume charts to find candlestick reversal patterns and analyze volume flows to complement these patterns. The example below shows a chart of Costco (COST) with a high-volume bullish engulfing pattern on October 9. The candlestick is long and wide because volume surged to its highest level in over two months.&#x20;

<figure><img src="/files/HUOsGRYPhGfHW17imAO9" alt="Volume chart using StockCharts.com showing high volume day"><figcaption><p>Arms CandleVolume chart shows a high volume day on October 9.</p></figcaption></figure>

Arms CandleVolume captures the volume surge with the widest box on the chart. Volume validates the bullish engulfing pattern and affirms support from the late August low. Notice how the stock continued higher for three days as buying pressure remained. Subsequently, the stock advanced to 126 and recorded several new highs in November.

It is also worth noting two other features on this chart. First, COST broke out with a gap and wide Arms CandleVolume box on September 5. Second, a bearish engulfing on high volume marked the mid-September peak and the stock broke support closing on the low. Note, however, that the true width of Arms CandleVolume boxes is shown when the chart ends on that particular date. For example, COST broke out with a gap and wide Arms CandleVolume box on September 5 (see chart below). The width of this box is not finalized until after the market close on September 5.

<figure><img src="/files/geM1iMOOoSKmIeH1ai0O" alt="Chart showing a gap and wide Arms CandleVolume box using StockCharts.com"><figcaption><p>On Sept. 5, there was a gap and wide CandleVolume box. Also, a bearish engulfing on high volume marked the mid-September peak. The stock broke support with a close on the low. </p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

Arms CandleVolume charts put candlestick action and volume together for easy visual analysis. Wide Arms CandleVolume boxes can also be used to affirm a support level or validate resistance. A bounce off support with a wide Arms CandleVolume box is stronger than a bounce with a narrow Arms CandleVolume box. The same is true for a decline from resistance. [**Click here**](https://stockcharts.com/h-sc/ui?s=SPY\&p=D\&yr=0\&mn=4\&dy=0\&id=p70410277337) for a live chart featuring Arms CandleVolume.

***

## Arms CandleVolume in SharpCharts <a href="#arms_candlevolume_and_sharpcharts" id="arms_candlevolume_and_sharpcharts"></a>

In SharpCharts you can find Arms CandleVolume under **Chart Type** in the **Attributes** area of the Chart Settings. There is also a Volume setting in the Attributes area. You can choose to have volume off, separate, or as an overlay. Volume can also be skipped (off) because it is reflected on the Arms CandleVolume chart. The example below also shows the checkbox for selecting **Color Volume** which you can use to display the up and down days of volume bars in different colors. You can choose your colors for both price bars and volume using **Up Color** and **Down Color**.

<figure><img src="/files/lddWCPWR35oEOYlL3aZ0" alt="Arms CandleVolume chart settings in SharpCharts from StockCharts.com"><figcaption><p>Arms CandleVolume in SharpCharts</p></figcaption></figure>

<figure><img src="/files/gzGVjVIO9aDzPqk3uH6g" alt="Chart displaying custom colors for CandleVolume boxes in StockCharts.com"><figcaption><p>Customizing colors for CandleVolume boxes in SharpCharts.</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/arms-candlevolume.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
