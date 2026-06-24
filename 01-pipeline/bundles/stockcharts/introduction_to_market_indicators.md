> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/market-indicators/introduction-to-market-indicators.md).

# Introduction to Market Indicators

Market Indicators are used to measure the health of a group of related stocks, usually by measuring group participation in a trend. The group can be the members of a broad index, a specific sector, or even an entire market.

## Market Indicators vs. Technical Indicators <a href="#market_indicators_vs_technical_indicators" id="market_indicators_vs_technical_indicators"></a>

Like a technical indicator, a market indicator is a series of data points derived from a formula. With market indicators, however, the formula for market indicators is applied to the price data for multiple securities within the market, instead of just one security. Price data can come from open, high, low or close points for the securities, their volume or both. This data is entered into the indicator formula, producing the desired data point.

Unlike technical indicators, market indicators are not charted above or below the chart. Market indicators are what is being charted, and as such have their own ticker symbols. There are often many symbols that apply the same market indicator formula to different markets; for example, the $BPSPX and $BPNDX track the Bullish Percent Index for the S\&P 500 and the NASDAQ 100, respectively.

## Market Breadth Indicators <a href="#market_breadth_indicators" id="market_breadth_indicators"></a>

Breadth indicators measure the number or percentage of stocks in the group that are participating in a trend. Market breadth indicators are typically based on the price data of the stocks in the group. For example, the Advance-Decline Line is calculated using the number of stocks in the group that increased in price (“advancers”) vs. the number that decreased in price (“decliners”). The Net New 52-Week Highs indicator measures the difference between the percentage of stocks making new 52-week highs and those making new 52-week lows.

Popular market breadth indicators include the [Advance-Decline Line](/table-of-contents/market-indicators/advance-decline-line.md), [McClellan Oscillator](/table-of-contents/market-indicators/mcclellan-oscillator.md), and [Net New 52-Week Highs](/table-of-contents/market-indicators/net-new-52-week-highs.md).&#x20;

{% hint style="info" %}
**Learn More.** For a complete list of market breadth indicators available in StockCharts, visit the [Market Indicators](/table-of-contents/market-indicators.md) page in ChartSchool.
{% endhint %}

## Sentiment Indicators <a href="#sentiment_indicators" id="sentiment_indicators"></a>

Not all market indicators measure market participation using price and volume. Sentiment Indicators measure whether investors feel bullish or bearish about the market, called investor sentiment. The data used to calculate these indicators varies more widely than traditional market breadth indicators: it is often a count of the investors themselves or the volume of money they are investing rather than price and volume. For example, the [DecisionPoint Rydex Ratio](/table-of-contents/market-analysis/decisionpoint-rydex-asset-analysis.md) is calculated using the money invested in bullish and bearish mutual funds. The AAII sentiment indicators are based on investors' poll results.

Popular sentiment indicators include the [Put Call Ratio](/table-of-contents/market-indicators/put-call-ratio.md), [Volatility Indices](/table-of-contents/market-indicators/volatility-indices.md), and the [DecisionPoint Rydex Ratio](/table-of-contents/market-analysis/decisionpoint-rydex-asset-analysis.md).&#x20;

{% hint style="info" %}
**Learn More.** For a complete list of sentiment indicators StockCharts offers, see our [Market Indicators](/table-of-contents/market-indicators.md).
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/market-indicators/introduction-to-market-indicators.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
