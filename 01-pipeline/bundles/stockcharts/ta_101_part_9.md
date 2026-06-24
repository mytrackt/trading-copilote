> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-9.md).

# TA 101 – Part 9

*This is the ninth part of a series of articles about technical analysis from a new course we're developing. If you are new to charting, these articles will give you the “big picture” behind the charts on our site. If you are an “old hand,” these articles will help ensure you haven't “strayed too far” from the basics. Enjoy!*

{% hint style="success" %}
Tip. See the entire series [Technical Analysis 101](/table-of-contents/overview/technical-analysis-101.md)
{% endhint %}

## Price Channels <a href="#price_channels" id="price_channels"></a>

Trending prices often form a channel where prices can be bounded above and below by parallel trend lines. When trend channels form, it is helpful to draw the top and bottom trend lines and monitor how well prices stay within the channel.

If prices in an uptrend fail to reach the upper channel line, the uptrend may be weakening and getting ready to reverse. Also, if prices suddenly break above the upper channel line, the uptrend may be either beginning to exhaust itself and reverse direction or be starting a new, steeper trend. Similar behavior also happens in downtrend price channels.

<figure><img src="/files/rx8t375V21xfepYghloY" alt=""><figcaption></figcaption></figure>

## Trend Changes <a href="#trend_changes" id="trend_changes"></a>

Trending prices can only go three directions: continue in the direction of the trend, change to a trading range, or reverse the direction of the trend. Trend changes are most easily recognized by watching the price peaks and troughs. An uptrend makes higher price peaks and troughs. A downtrend makes lower price peaks and troughs. In a trading range, price peaks and troughs are roughly equal over time.

A change in uptrend begins when a new price peak is similar to or lower than the previous price peak. The change is confirmed when the next price trough is similar to or lower than the last price trough.

Changes in downtrends and price ranges occur in the same way. New price peaks or troughs break the pattern of prior ones, with the next peak or trough confirming the change.

<figure><img src="/files/L9aq2oosqDTVW8E3ugSD" alt=""><figcaption></figcaption></figure>

## Price and Volume Data Adjustments <a href="#price_and_volume_data_adjustments" id="price_and_volume_data_adjustments"></a>

When a company pays out a dividend or a fund makes a distribution, it can affect the price of the underlying security. For example, after a company pays out dividends (ex-dividend date), the price of the stock drops by the dividend amount. Because of the change, price and volume data adjustments are necessary for technical indicators to be valid.&#x20;

Technical analysts generally view charts with adjusted price data. In the **SharpCharts Workbench**, if you'd like to view unadjusted price data, you can uncheck the **Adjust For Dividends** box in the Chart Settings area below the chart. You can also use unadjusted data in any of our charting tools by typing an underscore before the ticker symbol, e.g. **\_MSFT**.

<figure><img src="/files/VzNn9XKOrsX6IeI9oOm5" alt="You can view charts with data unadjusted for dividends and distributions in StockCharts.com"><figcaption><p>Uncheck the Adjust For Dividends box to view charts with data that is unadjusted for dividends and distributions.</p></figcaption></figure>

*In part 10 we'll look at how volume can confirm trend-change signals.*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-9.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
