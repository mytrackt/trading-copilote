> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-8.md).

# TA 101 – Part 8

*This is the eighth part of a series of articles about technical analysis from a new course we're developing. If you are new to charting, these articles will give you the “big picture” behind the charts on our site. If you are an “old hand”, these articles will help ensure you haven't “strayed too far” from the basics. Enjoy!*

{% hint style="success" %}
**Tip.** See the entire series [Technical Analysis 101](/table-of-contents/overview/technical-analysis-101.md)
{% endhint %}

## Trend Psychology <a href="#trend_psychology" id="trend_psychology"></a>

The psychology of fear and greed of market participants ultimately determines the direction of prices in a market. Prices rise with greed (demand) and fall with fear (supply). A price **trend** is simply a sustained directional price move. It can be thought of as a *tilted* support/resistance zone.

A trend will continue as long as either fear or greed is in control of a market. Trends fade or change direction as the balance of fear and greed changes. The extent of fear and greed in a market can be seen by how quickly prices are trending down or up.

## Trending <a href="#trending" id="trending"></a>

As stated earlier, a trend is a sustained, directional price move. Rising peaks and troughs constitute an **uptrend**; falling peaks and troughs constitute a **downtrend**. A **trading range** is characterized by horizontal peaks and troughs. Trends are generally classified into major (longer than six months), intermediate (one to six months), or minor (less than a month). Long term investors are most interested with identifying long-term trends where short-term investors are more interested in minor and intermediate trends. The following SharpChart shows examples of the different types and categories of trends.

<figure><img src="/files/aRJmZzR8tec2Q3p9zxaj" alt=""><figcaption></figcaption></figure>

## Trend lines <a href="#trend_lines" id="trend_lines"></a>

A **trend line** is a straight line that connects two or more low or high price points and then extends into the future to act as a line of support or resistance. The first two points establish the trend line while additional points validate it.

<figure><img src="/files/T9ofNEd8ObOvaGQ01Lag" alt=""><figcaption></figcaption></figure>

The following SharpChart contains a real example of how an uptrend line is drawn with a trend change.

<figure><img src="/files/bBCGT32ZfAOilKASDtMu" alt=""><figcaption></figcaption></figure>

An **uptrend line** has a positive slope and is formed by connecting two or more low points. Uptrend lines act as support. As long as prices remain above the trend line, the uptrend is considered intact. A break below the uptrend line indicates that demand has weakened and a change in trend could be imminent.

<figure><img src="/files/mLywvh7fs2e4lh9GxRiq" alt=""><figcaption></figcaption></figure>

A **downtrend line** has a negative slope and is formed by connecting two or more high points. Downtrend lines act as resistance. As long as prices remain below the downtrend line, the downtrend is intact. A break above the downtrend line indicates that supply is decreasing and that a change of trend could be imminent.

*In part 9 we'll look at trend channels and trend changes.*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-8.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
