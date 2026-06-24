> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-basics.md).

# Point and Figure Basics

Point & Figure (P\&F) charts focus on price movement using X and O columns. The X columns represent rising prices and the O columns represent declining prices. These columns make it easier to identify price breakouts, which in turn can generate buy or sell signals.&#x20;

The P\&F charts available from StockCharts.com can be modified to suit your needs. You can change chart attributes, chart scaling, and add overlays such as trend lines, moving averages, and Volume by Price, to name a few.

In this section, we cover all the basics of P\&F charts so you can create a P\&F chart, use the appropriate price intervals and timeframes, and better understand the automatic trend lines.

## P\&F Basics <a href="#p_f_basics" id="p_f_basics"></a>

[**Introduction to Point & Figure Charts**](/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-basics/introduction-to-point-and-figure-charts.md). Learn how to construct P\&F charts with a step-by-step example. Understand how to identify support and resistance levels and draw P\&F trend lines.

[**P\&F Scaling and Timeframes**](/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-basics/point-and-figure-scaling-and-timeframes.md). Learn to apply different price intervals to choose a charting timeframe. Intraday intervals can be used for medium-term timeframes, while daily intervals are often best for long-term charts.

[**P\&F Trend Lines**](/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-basics/p-and-f-trend-lines.md). P\&F trend lines are unique because they are drawn at a specific angle to represent a certain rate of ascent or descent. Understand how automatic trend lines appear on a P\&F chart, when they reverse, and how to identify a break.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-basics.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
