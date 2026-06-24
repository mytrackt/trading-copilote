> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-4.md).

# TA 101 – Part 4

*This is the fourth part of a series of articles about technical analysis from a new course we're developing. If you are new to charting, these articles will give you the “big picture” behind the charts on our site. If you are an “old hand”, these articles will help ensure you haven't “strayed too far” from the basics. Enjoy!*

{% hint style="success" %}
**Tip.** See the entire series [Technical Analysis 101](/table-of-contents/overview/technical-analysis-101.md)
{% endhint %}

## Line Charts <a href="#line_charts" id="line_charts"></a>

Line charts are created by plotting a line between the closing prices for each period set on the chart. On a daily chart, a line is plotted between the daily closing prices. Line charts are useful to help visualize the direction of prices. The extent of rallies and reactions in trends can also be quickly deduced.

<figure><img src="/files/rqOnFzDwk4uJMhMb6f5p" alt=""><figcaption><p>Line chart showing higher highs and lower lows</p></figcaption></figure>

A five-month price SharpChart of Apple, Inc. (AAPL) is plotted above in a line format. Higher highs and lows are annotated with green dashes and lower highs and lows with red dashes. Between March and mid-May 2008, the direction of prices is readily apparent with higher highs and lows. After mid-May 2008, prices began to make lower highs and lows.

A line chart is plotted by default when only end-of-day (closing) prices are available for a symbol. Examples of such symbols include all mutual funds and some market indices. However, weekly and monthly price bars can be charted for ticker symbols with only end-of-day (EOD) quotes.

## OHLC Charts <a href="#ohlc_charts" id="ohlc_charts"></a>

Open-High-Low-Close (OHLC) bar charts provide volatility information that line charts lack. The attributes of an OHLC bar are shown below. The chartist can evaluate volatility by the height of the bars and the conviction of the buyers and sellers by the price range between the open and close marks.

<figure><img src="/files/wHv8qHeM3TUfKF0DxnBM" alt=""><figcaption><p>Illustration of an Open-High-Low-Close (OHLC) chart</p></figcaption></figure>

For the left price bar, the CLOSE mark is above the OPEN mark indicating price ended higher for the day, known as an up day. This price bar is considered bullish. Bullish sentiment is present when greed for gain exceeds fear of loss and prices move higher.

With the price bar on the right, the OPEN is higher than the CLOSE indicating price ended lower for the day, known as a down day. This is a bearish price bar. Bearish sentiment is present when fear of loss is greater than greed for gain and prices move lower.

<figure><img src="/files/oyXKUI8EPZMrvAzdUDMq" alt=""><figcaption><p>SharpChart of AAPL  illustrating the OHLC format</p></figcaption></figure>

The SharpChart of AAPL above illustrates the OHLC format.

Notice how intraday price swings pass through the red and green reference marks made at the closing price levels on the previous Line chart. This illustrates why line charts are useful for visualizing price direction.

## OHLC Bar Colors <a href="#ohlc_bar_colors" id="ohlc_bar_colors"></a>

<figure><img src="/files/RMEkotEgSdvGziVe1AxA" alt=""><figcaption><p>Illustration showing bar colors of an OHLC chart</p></figcaption></figure>

When the 'Color Prices' option is selected on the Chart Attributes workbench, the price bars will be colored black or red, depending on how a price bar's closing price relates to the previous day's closing price. If the closing price is higher than the previous day's closing price, the price bar will be black. If the closing price is lower than the previous day's, the price bar will be red. With this convention, it is possible to have a black price bar with the close being lower than the open.\ <br>

<figure><img src="/files/TyMGacB7fttO8RvVLx9o" alt=""><figcaption><p>Example of colored OHLC price bars are shown in the AAPL SharpChart</p></figcaption></figure>

Colored OHLC price bars are shown in the AAPL SharpChart above. As discussed earlier, the color of the price bar is only based on the previous day's closing price, not the current day's opening price. *Up day* and *down day* price bars are usually black and red respectively, but that is not always the case as shown in the chart above.

*In part 5 we'll get into the specifics of candlestick charts.*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-4.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
