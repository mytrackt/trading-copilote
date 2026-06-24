> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/price-channel.md).

# Price Channel

A price channel is a continuation pattern that [slopes](/table-of-contents/glossary/glossary-s.md#slope) up or down and is bound by an upper and lower trend line. The upper trend line marks [resistance](/table-of-contents/glossary/glossary-r.md#resistance), and the lower trend line marks [support](/table-of-contents/glossary/glossary-s.md#support). Price channels with negative slopes (down) are considered bearish, and those with positive slopes (up) are considered bullish. Consider a “**bullish price channel**” as a channel with a positive slope and a “**bearish price channel**” as one with a negative slope.

The chart below shows an example of a price channel.&#x20;

<figure><img src="/files/tnt1AzZ1KwOoXR0BCHqJ" alt="A chart displaying a price channel from StockCharts.com"><figcaption><p>Example of a price channel.</p></figcaption></figure>

* **Main Trend Line.** It takes at least two points to draw the main trend line. This line sets the tone for the trend and slope. The main trend line extends up for a bullish price channel—at least two reaction lows are required to draw it. The main trend line extends down for a bearish price channel—at least two reaction highs are required to draw it.
* **Channel Line.** The line drawn parallel to the main trend line is called the channel line. Ideally, the channel line will be based on two [reaction highs](/table-of-contents/glossary/glossary-r.md#reaction_high) or [reaction lows](/table-of-contents/glossary/glossary-r.md#reaction_low). However, after establishing the main trend line, some analysts draw the parallel channel line using only one reaction high or low. The channel line marks support in a bearish price channel and resistance in a bullish price channel.
* **Bullish Price Channel.** The trend is considered bullish as long as prices advance and trade within the channel. The first warning of a trend change occurs when prices fall short of channel line resistance. A subsequent break below the main trendline support would indicate a trend change. A break above the channel line resistance would be bullish and indicate an acceleration of the price advance.
* **Bearish Price Channel.** The trend is considered bearish as long as prices decline and trade within the channel. The first warning of a trend change occurs when price fails to reach channel line support. A subsequent break above the main trend line resistance would indicate a trend change. A break below channel line support would be bearish and indicate an acceleration of the decline.
* **Scaling.** Even though it's a matter of personal preference, trend lines seem to match reaction highs and lows best when [semi-log](/table-of-contents/glossary/glossary-s.md#semi-logarithmic_percentage_scaling) scales are used. Semi-log scales reflect price movements in percentage terms. A move from 50 to 100 will appear the same distance as one from 100 to 200.

In a bullish price channel, some traders look to buy when prices reach main trend line support. Conversely, some traders look to sell (or short) when prices reach main trend line resistance in a bearish price channel. As with most price patterns, other aspects of technical analysis should be used to confirm signals.

Because technical analysis is just as much art as science, there is room for flexibility. Even though exact trend line touches are ideal, it is up to you to judge the relevance and placement of the main trend and channel line. By that same token, a channel line parallel to the main trend line is ideal.

The price chart of Cisco Systems (CSCO) provides an example of an 11-month bullish price channel developed in 1999.

<figure><img src="/files/6yMrU5HHzLSn9Xn2wv3j" alt="Chart displaying a price channel in Cisco Systems (CSCO) stock from StockCharts.com"><figcaption><p>Example of a price channel in Cisco Systems (CSCO) stock.</p></figcaption></figure>

* **Main Trend Line.** The January, February, and March reaction lows formed the beginning of the main trend line, which was confirmed by subsequent lows in April, May, and August.
* **Channel Line.** Once the main trend line was in place, the channel line beginning from the January high was drawn. A visual assessment reveals that these trend lines look parallel. More precise analysts may want to test the slope of each line, but a visual inspection is usually enough to ensure the “essence” of the pattern.
* **Bullish Price Channel.** Subsequent touches along the main trend line offered good buying opportunities in mid-April, late May, and mid-August.
* The stock didn't reach channel line resistance until July (red arrow), marking a significant reaction high.
* The September high (blue arrow) fell short of channel line resistance by a small margin that was probably insignificant.
* The break above channel line resistance in December 1999 marked an acceleration of the advance. Some analysts might consider the stock overextended after this move, but the advance was powerful, and the trend never turned bearish. Price channels will not last forever, but the underlying trend remains until proven otherwise.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/price-channel.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
