> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types.md).

# Chart Types

## Chart Types <a href="#chart_types" id="chart_types"></a>

[**Arms CandleVolume**](/table-of-contents/chart-analysis/chart-types/arms-candlevolume.md)\
A price chart that merges traditional candlesticks with EquiVolume boxe

[**CandleVolume**](/table-of-contents/chart-analysis/chart-types/candlevolume.md)\
A price chart that merges traditional candlesticks with volume.

[**Elder Impulse System**](/table-of-contents/chart-analysis/chart-types/elder-impulse-system.md)\
A charting system developed by Alexander Elder that colors price bars based on simple technical signals.

[**EquiVolume**](/table-of-contents/chart-analysis/chart-types/equivolume.md)\
Price boxes that are sized based on their trading volume.

[**Heikin-Ashi**](/table-of-contents/chart-analysis/chart-types/heikin-ashi-candlesticks.md)\
A candlestick method that uses price data from two periods instead of one.

[**Kagi Charts**](/table-of-contents/chart-analysis/chart-types/kagi-charts.md)\
A Japanese charting method based on volatility and reversal amounts.

[**Renko Charts**](/table-of-contents/chart-analysis/chart-types/renko-charts.md)\
A Japanese charting method where boxes rise and fall in 45-degree patterns.

[**Three Line Break Charts**](/table-of-contents/chart-analysis/chart-types/three-line-break-charts.md)\
A Japanese charting method that ignores time and only represents change in terms of price movements.

[**MarketCarpets**](/table-of-contents/chart-analysis/chart-types/marketcarpets.md)\
A charting tool used to visually scan large groups of securities.

[**Relative Rotation Graphs (RRG Charts)**](/table-of-contents/chart-analysis/chart-types/relative-rotation-graphs-rrg-charts.md)\
A visualization tool for relative strength and momentum analysis.

[**Seasonality Charts**](/table-of-contents/chart-analysis/chart-types/seasonality-charts.md)\
A unique StockCharts tool for identifying monthly seasonal patterns.

[**Yield Curve**](/table-of-contents/chart-analysis/chart-types/yield-curve.md)\
A visualization tool using bond yields to analyze market conditions and the economic cycle.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
