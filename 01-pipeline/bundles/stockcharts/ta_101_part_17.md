> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-17.md).

# TA 101 – Part 17

*This is the seventeenth article in our technical analysis series. If you are new to charting, these articles will give you the “big picture” behind the charts on our site. If you are an “old hand,” these articles will help ensure you haven't “strayed too far” from the basics. Enjoy!*

{% hint style="success" %}
**Tip.** See the entire series [Technical Analysis 101](/table-of-contents/overview/technical-analysis-101.md)
{% endhint %}

## Comparison Charting <a href="#comparison_charting" id="comparison_charting"></a>

Comparison charting allows the analyst to study individual price performance and performance relative to other stocks. John Murphy, who provides expert market commentary on StockCharts.com, uses comparison charting extensively in his market analysis.

## Individual Price Performance <a href="#individual_price_performance" id="individual_price_performance"></a>

[Click here for a live version of the chart](https://stockcharts.com/h-sc/ui?s=%24INDU\&p=D\&st=2018-01-01\&en=2018-06-29\&id=p12160522302\&a=656650162) to see how it was created with the “Performance” chart type setting.

<figure><img src="/files/aPGe2EXTkPZ8efBzJ2Wf" alt=""><figcaption></figcaption></figure>

The SharpChart above shows how the Performance plotting style can be used to monitor the year-to-date performance of the Dow Jones Industrial Average. Once this chart is generated, the page can be bookmarked as a favorite in your browser for quick access in the future.

[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?s=AA\&p=D\&st=2018-01-01\&en=2018-06-29\&id=p81051545129\&a=656650449)

<figure><img src="/files/K6lDuaJdVWgiqCyv2PMb" alt=""><figcaption></figcaption></figure>

Multiple symbols can be plotted and compared in this manner by using the Price indicator and other ticker symbols as parameters with a Behind Price position setting. The SharpChart above shows the performance of AA compared with BA and IBM.

## Relative Performance Comparison <a href="#relative_performance_comparison" id="relative_performance_comparison"></a>

<figure><img src="/files/1znzzexJOw4cVpiGf7ok" alt=""><figcaption></figcaption></figure>

[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?s=BA\&p=D\&st=2018-08-21\&en=2019-02-19\&id=p28908325906\&a=656652909)

The SharpChart above illustrates how the performance between Boeing (BA) and the Dow Jones Industrial Average (DJIA) index can be compared in the Indicator Panel above the Price Plot Area. The relative performance indicator is displayed by selecting Price as an indicator on the workbench and inserting BA:$INDU as a parameter.

A positive slope of the indicator line shows that the first symbol in the ratio is outperforming the second symbol. A negative slope indicates the opposite; the first ticker symbol is underperforming the second ticker symbol. And a flat line indicates that both symbols have similar performance.

This information can be used in several ways. In the case of comparing a stock to a market index, the analyst can quickly determine whether or not a stock is outperforming the market. In the case of comparing two stocks, the analyst can easily determine how the stocks are performing relative to each other.

*You've reached the end of Technical Analysis 101!* [*Click here* ](/table-of-contents/overview/technical-analysis-101.md)*to return to the main Technical Analysis 101 menu to revisit any topics, or* [*here*](/table-of-contents/overview.md) *to return to the main Overview page.*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-17.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
