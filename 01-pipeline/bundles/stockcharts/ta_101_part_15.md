> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-15.md).

# TA 101 – Part 15

*This is the fifteenth part of a series of articles about technical analysis from a new course we're developing. If you are new to charting, these articles will give you the “big picture” behind the charts on our site. If you are an “old hand,” these articles will help ensure you haven't “strayed too far” from the basics. Enjoy!*

{% hint style="success" %}
**Tip.** See the entire series [Technical Analysis 101](/table-of-contents/overview/technical-analysis-101.md)
{% endhint %}

## Gaps <a href="#gaps" id="gaps"></a>

Price charts often have blank spaces known as **gaps**. They represent times when no shares were traded within a particular price range. Gaps result from extraordinary buying or selling interest developing when the market is closed. When the market opens, the price is raised or lowered enough to satisfy all of the buying or selling orders.

<figure><img src="/files/G6rppoX1XPRySxWOSSoG" alt=""><figcaption></figcaption></figure>

For an **up gap** to form, the low price after market close on the day of the up gap must be higher than the high price of the previous day. Up gaps are generally considered bullish.

A **down gap** is just the opposite of an up gap; the high price of the down gap day after market close must be lower than the low price of the previous day. Down gaps are usually considered bearish.

Up and down gaps can form on daily, weekly or monthly charts and are considered significant when accompanied with higher than average volume.

A price chart with gaps almost every day is typical for very lightly traded securities and should be avoided. Prices often gap up or down at market open and then close the gap before market close. Such temporary intraday gaps should not be considered as having anything more significance than normal market volatility.

Many investors mistakenly believe that gaps influence future prices to the point of eventually filling the gap. Instances where gaps close within a few days of forming can be significant. However, gaps have little to no influence on price action weeks or months after forming.

<figure><img src="/files/UkQJ0z45srVI11JlZRSF" alt=""><figcaption></figcaption></figure>

**Breakaway gaps** signal a change in market psychology about the future prospect of a security, especially when accompanied by above average volume. A bullish breakaway gap forms when a security gaps up after an extended decline, extended base or a consolidation period. A bearish breakaway gap forms when a security gaps down after an extended advance, an extended top or a consolidation period.

**Common gaps** occur within a trading range or shortly after a sharp move as a reaction. These gaps do not reflect a change in market psychology, but rather represent price volatility or temporary imbalance of supply and demand. For instance, if a security has declined 20% in a week and gaps up, it would be considered a common gap and not likely to signify a change in trend. Or, if a trading range develops between $20 and $30, and a gap forms in the middle, it is probably a common gap.

**Continuation gaps** form near the middle of a short or intermediate trend in the same direction. These gaps signal a continuation of the preceding trend. Continuation gaps are also known as measuring or runaway gaps. These gaps can be triggered by news events that bring more market attention to a security.

**Exhaustion gaps** occur in the direction of extended trends. For an exhaustion gap to be considered valid, prices should reverse soon after the gap and close the gap. In the later stages of a trend, the extent of the trend becomes widely reported; eventually causing a surge in trading that cannot be sustained. These events often mark the end of the trend.

*In part 16 we'll take a look at Candlestick Chart Patterns*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-15.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
