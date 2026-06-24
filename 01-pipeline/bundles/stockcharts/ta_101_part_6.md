> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-6.md).

# TA 101 – Part 6

*This is the sixth part of a series of articles about technical analysis from a new course we're developing. If you are new to charting, these articles will give you the “big picture” behind the charts on our site. If you are an “old hand”, these articles will help ensure you haven't “strayed too far” from the basics. Enjoy!*

{% hint style="success" %}
**Tip.** See the entire series [Technical Analysis 101](/table-of-contents/overview/technical-analysis-101.md)
{% endhint %}

## Chart Scaling <a href="#chart_scaling" id="chart_scaling"></a>

Charts are created with one of two different kinds of vertical price scales. An arithmetic scale evenly spaces price along the right side of the chart. Arithmetic chart spacing between $10 and $20 is half as tall as the spacing between $20 and $40. A log scale evenly spaces price in percentage terms. Chart spacing between $10 and $20 has the exact same chart spacing as between $20 and $40 since they represent the same percentage increase.

<figure><img src="/files/xg0jQ7k4VHFBUQ59g3g6" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/IRPGxqoadhrOqNM9NIba" alt=""><figcaption></figcaption></figure>

The SharpCharts above illustrate the differences between the two scaling methods. On the arithmetic scale, three different trend lines were required to keep pace with the price advance. On the log scale, the trend line fits the price trend during the entire rally. Log scaling should be the first scaling choice when using trend lines, especially over long timeframes.

## Volume <a href="#volume" id="volume"></a>

StockCharts.com provides several ways to plot volume data on a chart. The following price and volume SharpChart of AAPL illustrates how volume is typically plotted.

Volume can be plotted in an 'indicator panel' above or below the 'price plot area' or in the price plot area as an 'overlay.'

<figure><img src="/files/iXLtGkQrP4RoXk3GiIzC" alt=""><figcaption></figcaption></figure>

When the 'Color Volume' option is used, the volume bars are shown as black for up days and red for down days. Color volume bars allow the chartist to quickly see where heavy or weak buying and selling activity is happening.

## CandleVolume Charts <a href="#candlevolume_charts" id="candlevolume_charts"></a>

CandleVolume charts are similar to candlestick charts except that each candle's width is proportional to its corresponding volume value. This charting style allows one to visualize the volume activity “in” rather than “below” price moves. Depending on the style of analysis, volume bars could be omitted to simplify the chart.

<figure><img src="/files/jUFmiil7t3Wv7Z9GKjTp" alt=""><figcaption></figcaption></figure>

The time axis for these charts is not uniformly spaced as candlestick bar widths vary with volume values. As a result, trend line analysis using CandleVolume charts should always be confirmed with a standard candlestick or OHLC chart. The SharpChart of AAPL above shows how volume bars correlate to the candlestick widths.

*That wraps up our look at how charts are constructed. In part 7 we're going to start to talk about how charts are analyzed - starting with Support and Resistance analysis.*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-6.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
