> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays.md).

# Technical Overlays

**Technical Indicators** are the often squiggly lines found above, below, and on top of the price information on a technical chart. Indicators that use the same scale as prices are typically plotted on top of the price bars and are therefore referred to as “Overlays.”

***

## Technical Overlays <a href="#technical_overlays" id="technical_overlays"></a>

[**Alligator**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/alligator.md)\
An indicator that helps you identify the presence and direction of market trends.

[**Anchored VWAP**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/anchored-vwap.md)\
A version of the VWAP overlay where the chartist defines the starting point for overlay calculations.

[**Bollinger Bands**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/bollinger-bands.md)\
A chart overlay that shows the upper and lower limits of 'normal' price movements based on the Standard Deviation of prices.

[**Chandelier Exit**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/chandelier-exit.md)\
An indicator that can be used to set trailing stop-losses for both long and short positions.

[**Double Exponential Moving Average (DEMA)**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/double-exponential-moving-average-dema.md)\
A faster moving average calculation that offsets values to reduce the traditional lag found in moving averages.

[**Highest High Value**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/highest-high-value.md) \
Shows a security's highest trading value during a specific period.

[**Hull Moving Average (HMA)**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/hull-moving-average-hma.md) \
A very responsive moving average calculation that weights recent prices more heavily than those earlier in the period.

[**Ichimoku Cloud**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/ichimoku-cloud.md)\
A comprehensive indicator that defines support and resistance, identifies trend direction, gauges momentum, and provides trading signals.

[**Kaufman's Adaptive Moving Average (KAMA)**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/kaufmans-adaptive-moving-average-kama.md)\
A unique moving average that accounts for volatility and automatically adjusts to price behavior.

[**Keltner Channels**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/keltner-channels.md)\
A chart overlay that shows upper and lower limits for price movements based on the Average True Range of prices.

[**Linear Regression Forecast**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/linear-regression-forecast.md)\
Forecasts stock price values using past values. LRF can determine the underlying trend and when prices are overextended to the upside or downside.&#x20;

[**Linear Regression Intercept**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/linear-regression-intercept.md)\
Identifies underlying trends and when prices are overextended to the upside and downside.&#x20;

[**Lowest Low Value**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/lowest-low-value.md) \
Shows a security's lowest trading value within a specific period.

[**Moving Averages**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md)\
Chart overlays that show the 'average' value over time. Simple Moving Averages (SMAs) and Exponential Moving Averages (EMAs) are explained.

[**Moving Average Ribbon**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-average-ribbon.md)\
A quick way to plot several moving averages with different look-back periods on a chart at once.

[**Moving Average Envelopes**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-average-envelopes.md)\
A chart overlay consisting of a channel formed from simple moving averages.

[**Parabolic SAR**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/parabolic-sar.md)\
A chart overlay that shows reversal points below prices in an uptrend and above prices in a downtrend.

[**Pivot Points**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/pivot-points.md)\
A chart overlay that shows reversal points below prices in an uptrend and above prices in a downtrend.

[**Price Channels**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/price-channels.md)\
A chart overlay that shows a channel made from the highest high and lowest low for a given period.

[**Triple Exponential Moving Average (TEMA)**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/triple-exponential-moving-average-tema.md)\
A more responsive moving average indicator that significantly reduces the lag present in traditional moving average calculations.

[**Volume By Price**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/volume-by-price.md)\
A chart overlay with a horizontal histogram showing the amount of activity at various price levels.

[**Volume-Weighted Average Price (VWAP)**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/volume-weighted-average-price-vwap.md)\
An intraday indicator based on total dollar value of all trades for the current day divided by the total trading volume for the current day.

[**ZigZag**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/zigzag.md)\
A chart overlay that shows filtered price movements that are greater than a given percentage.

{% hint style="warning" %}
**Note:** We also have an extensive collection of [Technical Indicators](/table-of-contents/technical-indicators-and-overlays/technical-indicators.md) and  [Market Indicators](/table-of-contents/market-indicators/introduction-to-market-indicators/market-indicator-dictionary.md).
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
