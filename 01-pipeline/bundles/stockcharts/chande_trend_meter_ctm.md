> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/chande-trend-meter-ctm.md).

# Chande Trend Meter (CTM)

## What Is the Chande Trend Meter? <a href="#introduction" id="introduction"></a>

The Chande Trend Meter (CTM), developed by Tushar Chande, assigns a numerical score to a stock or other security, based on several different technical indicators covering six different timeframes. Distilling all this technical information down into a single number provides an easy way to identify the strength of the trend for a given security.

## How To Calculate the Chande Trend Meter <a href="#calculation" id="calculation"></a>

The calculation of the Chande Trend Meter is based on the following technical indicators:

* The positions of the high, low and close relative to the [Bollinger Bands](/table-of-contents/technical-indicators-and-overlays/technical-overlays/bollinger-bands.md) in four different timeframes (20-day, 50-day, 75-day, and 100-day)
* The price change relative to the [standard deviation](/table-of-contents/technical-indicators-and-overlays/technical-indicators/standard-deviation-volatility.md) over the past 100 days
* The 14-day [RSI value](/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi.md)
* The existence of any short-term (2-day) [price channel breakouts](/table-of-contents/technical-indicators-and-overlays/technical-overlays/price-channels.md)

The resulting score is converted to a 0-100 scale for ease of comparison.

## Interpreting the Chande Trend Meter <a href="#interpretation" id="interpretation"></a>

On the Chande Trend Meter scale of 0 to 100, stocks with a CTM score of 100 are in very strong uptrends. Conversely, stocks with a score of 0 are in very strong downtrends.

This scale can be divided into 5 different levels:

* Stocks with a score of 90-100 are in very strong uptrends
* Stocks with a score of 80-90 are in strong uptrends
* Stocks with a score of 60-80 are in weak uptrends
* Stocks with a score of 20-60 are either flat or in weak downtrends
* Stocks with a score of 0-20 are in very strong downtrends

Momentum traders should look for stocks with a Chande Trend Meter score of 80 or higher. This indicates a strong uptrend. The stronger the uptrend, the more likely it is to continue that trend.

The Chande Trend Meter can also be used with indexes and ETFs to get an idea of the relative trend for specific sectors and industries, or even entire markets.

One advantage of the Chande Trend Meter is that the value is set on an absolute scale, not relative to other stocks in a group. So, when you compare CTM scores of several different types of securities, you are making apples-to-apples comparisons across all securities.

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

The Chande Trend Meter provides a simple way to determine whether a stock is in an uptrend or a downtrend and makes it easy to gauge the strength of that trend. By combining several different proven technical trend indicators and boiling them down into one number, the CTM gives chartists a wealth of trend information at a glance.

***

## Using CTM With SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Chande Trend Meter can be found in the Indicators section under the chart. The CTM indicator can be positioned above, below or behind the main price plot.

When placed above or below the main price plot, the background is color-coded to indicate the different trend strength levels:

* **Dark Green**: 90-100 (very strong uptrend)
* **Medium Green**: 80-90 (strong uptrend)
* **Light Green**: 60-80 (weak uptrend)
* **Yellow**: 20-60 (flat or weak downtrend)
* **Pink**: 0-20 (strong downtrend)

<figure><img src="/files/fd8eP7OhvV2EwYcf8MYx" alt=""><figcaption></figcaption></figure>

## Suggested CTM Scans <a href="#suggested_scans" id="suggested_scans"></a>

### CTM Crosses Above 60 on Heavy Volume <a href="#ctm_crosses_above_60_on_heavy_volume" id="ctm_crosses_above_60_on_heavy_volume"></a>

This scan reveals stocks where the Chande Trend Meter has crossed above 60 with heavier than normal volume.

```
[type = stock] AND [country = US] 
AND [Daily SMA(60,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [Chande Trend Meter x 60.0]
AND [volume > SMA(50,volume) * 1.5]
```

### Stocks with Consistently High CTM <a href="#stocks_with_consistently_high_ctm" id="stocks_with_consistently_high_ctm"></a>

This scan reveals stocks where the Chande Trend Meter for a US stock is consistently high, averaging 80 or more over the last 50 trading days.

```
[type = stock] AND [country = US] 
AND [Daily SMA(60,Daily Volume) > 100000] 
AND [Daily SMA(60,Daily Close) > 20] 

AND [SMA(50,Chande Trend Meter) > 80.0]
```

{% hint style="info" %}
**Learn More.** For more details on the syntax for Chande Trend Meter scans, please see our [Scanning Indicator Reference](https://help.stockcharts.com/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#chande_trend_meter) in the Support Center.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/chande-trend-meter-ctm.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
