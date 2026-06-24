> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-indicators.md).

# Point & Figure Indicators

Chartists can apply [moving averages](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md), [Bollinger Bands](/table-of-contents/technical-indicators-and-overlays/technical-overlays/bollinger-bands.md), and [Volume-by-Price](/table-of-contents/technical-indicators-and-overlays/technical-overlays/volume-by-price.md) to Point & Figure (P\&F) charts. While the formulas remain unchanged, indicators on P\&F charts are calculated slightly differently than those on bar charts. Instead of daily or weekly closing prices as the database, P\&F charts use the average price of each column. Despite this difference, these indicators can be used like on bar charts.

## Moving Averages <a href="#moving_averages" id="moving_averages"></a>

Moving averages on P\&F charts are based on the average price of each column. In contrast, bar chart moving averages are based on each period's close. A 10-day simple moving average (SMA) on a bar chart would be the average of the last 10 closing prices. On a P\&F chart, a 10-period SMA would be the average price of the last 10 column averages.

A one-period SMA provides an easy example for starters. If an X-Column extends from 43 to 50, the one-period SMA would be 46.5 {(43 + 50)/2 = 46.5}.&#x20;

The chart below shows Agilent with eight Xs extending from 43 to 50 in the most recent X-column. The blue one-day SMA is in the middle of that column (between the 4th X and the 5th X).

<figure><img src="/files/65YLOD9TzhsOv7lAyur7" alt="P&#x26;F chart from StockCharts.com with a one-period moving average overlay"><figcaption><p>A one-period moving average is overlaid on a P&#x26;F chart.</p></figcaption></figure>

A five-period SMA on a P\&F chart would be the average for the last five columns. The chart below shows Agilent with a 1-period SMA (blue) and a 5-period SMA (red). Just like bar chart moving averages, these two moving averages lag price. The longer the moving average is, the bigger the lag.

<figure><img src="/files/RKumxRWQU4MVTCC9fLNH" alt="P&#x26;F chart from StockChart.com with a one-period and five-period moving average overlay"><figcaption><p>A P&#x26;F chart with a one-period and five-period simple moving average overlay.</p></figcaption></figure>

Double smoothing means shorter moving averages can be used. Taking the average of the column smooths the price once. A moving average greater than two periods smooths the price a second time. With P\&F charts, a five-period SMA is a five-period SMA of a one-period SMA. This double smoothing means chartists can use shorter moving averages with P\&F charts. A five-day SMA on a P\&F chart may produce signals similar to a 50-day SMA on a bar chart.

<figure><img src="/files/Tk0Sc8Upw5cx0RgqEOTN" alt="P&#x26;F chart from StockCharts.com showing moving average crossovers"><figcaption><p>Moving average crossovers in a P&#x26;F chart.</p></figcaption></figure>

There are at least three possible moving average signals.&#x20;

1. Look for [price to cross the moving average](/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies/how-to-trade-price-to-moving-average-crossovers.md). A move above the moving average is bullish, while a move below it is bearish.&#x20;
2. Identify the direction of the moving average. A rising moving average is bullish, and a falling moving average is bearish.&#x20;
3. Use two moving averages to generate signals. A bull signal is triggered when the shorter moving average crosses above the longer moving average. A bear signal triggers when the shorter moving average crosses below the longer moving average. You can read more on moving averages in our [detailed ChartSchool article.](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md)

## Bollinger Bands <a href="#bollinger_bands" id="bollinger_bands"></a>

Bollinger Bands are standard deviation bands placed above and below a moving average. Bollinger Bands (20,2) is based on the default setting—20 periods to calculate the moving average and 2 for the standard deviation. The upper band is placed two standard deviations above the moving average, and the lower band is two standard deviations below the moving average. Because P\&F moving averages are double-smoothed, you may need to shorten the moving average period to five or 10. It depends on the price characteristics of the underlying security. Some trial and error may be required to find the right fit.

Bollinger Band analysis and signals are the same for P\&F and bar charts. There are three basic signals. Narrowing bands indicate a consolidation that can lead to a breakout—up or down. As with bar charts, this narrowing does not provide a direction clue. Look for the next P\&F signal to establish direction.

<figure><img src="/files/jFT5EuxcCNJJ0RpFLNXO" alt="P&#x26;F chart from StockCharts.com showing narrowing Bollinger Bands before a breakout"><figcaption><p>P&#x26;F charts showing narrowing Bollinger Bands before a breakout.</p></figcaption></figure>

Bollinger Bands provide a natural filter for moving average breaks. Since price moves above and below moving averages frequently on P\&F charts, Bollinger Bands can be used to filter these signals.&#x20;

A five-period moving average with Bollinger Bands set two standard deviations above and below provides an extra price hurdle. A move above the upper band shows strength, indicative of an uptrend. Conversely, a move below the lower band shows weakness and is more indicative of a downtrend. Bollinger refers to this as “walking the bands.” You can read more on Bollinger Bands in our [detailed ChartSchool article.](/table-of-contents/technical-indicators-and-overlays/technical-overlays/bollinger-bands.md)

<figure><img src="/files/5oSLZFFvh56m1z7U9Bxp" alt="P&#x26;F chart with an example of prices walking up the upper band indicating a strong uptrend"><figcaption><p>Example of P&#x26;F chart with a move above the upper band (walking up the upper band), which indicates a strong uptrend.</p></figcaption></figure>

## Volume-by-Price <a href="#volume-by-price" id="volume-by-price"></a>

Volume-by-Price shows the amount of volume for a particular price range. This is perfect for P\&F charts because each box represents a specific price range. Volume-by-Price bars are shown horizontally on the left side of the chart to match the specific price range. This volume is subdivided into positive and negative volumes. Volume is positive (green) when price moves higher within the range. Volume is negative when price moves lower within the range.

Volume-by-Price can be used to identify support or resistance zones. Long Volume-by-Price bars at or above current prices can be viewed as a potential resistance zone.&#x20;

<figure><img src="/files/UtQyU50apbvISq3zqN27" alt="P&#x26;F chart from StockCharts.com with Volume-by-Price overlay identifying a resistance level"><figcaption><p>Volume-by-Price bars on a P&#x26;F chart showing potential resistance level.</p></figcaption></figure>

Conversely, long Volume-by-Price bars at or below current prices can be considered a potential support zone.&#x20;

<figure><img src="/files/jo06ACE07TEZFKfKegFP" alt="P&#x26;F chart from StockCharts.com showing a potential support level"><figcaption><p>Volume-by-Price bars on a P&#x26;F chart showing potential support level.</p></figcaption></figure>

You can read more about volume-by-price in our [detailed ChartSchool article.](/table-of-contents/technical-indicators-and-overlays/technical-overlays/volume-by-price.md)

## The Takeaway <a href="#conclusion" id="conclusion"></a>

Even though the basic calculations are the same, indicators based on P\&F charts are slightly different than their bar chart cousins. It may take some time to understand and understand how these indicators react to price movements in P\&F charts. However, the time spent understanding them could pay off as P\&F charts give a different perspective of price action.&#x20;

As with all indicators, it's important to confirm indicator signals with P\&F signals. For example, a bullish moving average crossover should be confirmed with a P\&F breakout, such as a double or triple top breakout.

## Further Study <a href="#further_study" id="further_study"></a>

Thomas Dorsey's [*Point & Figure Charting*](https://a.co/d/cxyr4Pq) examines the basic ideas and key patterns of P\&F charts. Dorsey keeps his analysis straightforward; as a relative strength disciple, he devotes a complete chapter to relative strength concepts using P\&F charts. These concepts are tied in with market indicators and sector rotation tools to provide investors with all they need to construct a portfolio. Additionally, Dorsey incorporates lessons on how to use P\&F charts with ETFs.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-indicators.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
