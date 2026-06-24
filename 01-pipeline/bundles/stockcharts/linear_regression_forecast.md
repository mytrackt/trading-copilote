> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/linear-regression-forecast.md).

# Linear Regression Forecast

## What Is the Linear Regression Forecast?

The Linear Regression Forecast (LRF) is based on the premise of linear regression, a statistical tool used to forecast stock price values using past values. LRF can be applied to determine the underlying trend and when prices are overextended to the upside or downside.

LRF uses the least squares method, a straight line plotted through prices that best fit the price data. This minimizes the distance between price and the resulting trendline. Instead of being plotted as a straight line, the LRF is a moving series that plots the forecasted value of the derived trend line for each data point. As a result, it follows the stock market like a moving average. The last point of the trendline is the forecasted value.

## The Linear Regression Forecast Formula

We won't get into the details of the formula behind the LRF overlay. In a nutshell, the formula used to calculate LRF is based on [the slope of a line](/table-of-contents/technical-indicators-and-overlays/technical-indicators/slope.md): y = mx + b. You may remember this from high school algebra. The slope (m) and the intercept (b) values will find the best-fitting line.

## Chart LRF With StockChartsACP

Adding the LRF overlay in StockChartsACP is a snap.

<figure><img src="/files/mnycXWHJRZ8lrflDOzlJ" alt="Adding the Linear Regression Forecast in StockCharts" width="299"><figcaption><p>How to add the Linear Regression Forecast overlay</p></figcaption></figure>

**1—** Enter the symbol for the stock, index, or exchange-traded fund you want to analyze.

**2—** From Chart Settings, scroll down the list of Standard Indicators.

**3—** Select Linear Regression Forecast.

Want to change the color, style, or any other overlay parameter? Select the settings icon next to the overlay and choose your parameters.

<figure><img src="/files/WBBaUSZ5nR3EHXCZ5iKC" alt="Changing Linear Regression Forecast indicator parameters in StockCharts.com" width="266"><figcaption><p>Changing Linear Regression Forecast parameters </p></figcaption></figure>

**Periods.** The default setting is 14, but you can change it to any number of bars you wish to use to calculate LRF.

**Calculated From.** There are various choices here—solid, solid (thin), solid (thick), dashed, etc. Take your pick. Select the value you want to use for calculations. This can be the open, high, low, close, (H + L)/2, (H + L + C)/3, (H + L + 2C)/4, (O + H + L + C)/4

**Line Style.** You have a few choices here—solid, solid (thin), solid (thick), dashed, etc. Take your pick.

**Opacity.** Use the slider to select the transparency of LRF.

**Colors.** Choose the color for LRF that you prefer to view on your chart.

**Add Overlays.** Sometimes, additional overlays can help confirm trend direction. This dropdown menu offers several overlays to choose from.

The chart below shows an example of a StockChartsACP chart with the LRF overlay.

<figure><img src="/files/nLgoJFwOQokXlNiPF6mB" alt="Chart showing the Linear Regression Forecast in StockCharts.com"><figcaption><p>The Linear Regression Forecast overlay in action.</p></figcaption></figure>

***

<img src="/files/b07jJGtLwGuwhQqHk82b" alt="https://schrts.co/ufcfrGfw" data-size="line">[View the live chart](https://schrts.co/ufcfrGfw)**.**

***

So, how can the LRF overlay help you invest or trade? The last point forecasts price direction. In the chart above, the short-term trend is up. If the stock price continues moving upward, you can add other indicators or overlays, such as moving averages, to confirm the trend’s strength and/or momentum. This can help you decide whether to buy, hold, or sell an asset.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/linear-regression-forecast.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
