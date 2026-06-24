> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-percent-atrp.md).

# Average True Range Percent (ATRP)

## What is Average True Range Percent (ATRP)? <a href="#average_true_range_percent_atrp" id="average_true_range_percent_atrp"></a>

The Average True Range Percent (ATRP) is an indicator that measures the volatility of a security. The ATRP is lower when the security is in a trading range, and moves higher during dramatic price changes in either direction.

<figure><img src="/files/NuOisSekr7r1MufLv2Jz" alt=""><figcaption></figcaption></figure>

ATRP is a variation of the Average True Range (ATR), a popular volatility indicator developed by Welles Wilder. The ATR indicator has one limitation: the ATR values are tied to the underlying security's price, so higher-priced stocks will always have a higher ATR than lower-priced stocks, regardless of their relative volatility.

ATRP seeks to overcome this limitation by expressing the ATR value as a percentage of the price. This puts all securities' volatility measurements on the same scale, making it easier to compare the volatility of securities with very different prices.&#x20;

{% hint style="info" %}
**Learn More:** [Average True Range (ATR)](/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-atr.md)
{% endhint %}

## Calculating ATRP

The ATRP is calculated by dividing the ATR value by the closing price and multiplying the result by 100.

```
ATRP = (ATR / Close) * 100
```

Please see [our ChartSchool article on Average True Range](/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-atr.md) for more information on calculating ATR values.&#x20;

## Interpreting ATRP

Like ATR, ATRP remains low during trading ranges, and rises during dramatic price changes in either direction. In the chart below, the ATRP for XLY rises sharply as the price drops in March and April. It peaks at 4.48% in mid-April. The price slowly rises from May to September, but it does so in such a tight range that the volatility remains relatively low during this period. The price drop in mid-November is not large or sustained enough to cause more than a small bump in ATRP, peaking at 1.99%.

<figure><img src="/files/toaNG1I3jK1U86Xb0XLk" alt=""><figcaption><p>ATRP increases during strong moves and decreases during trading ranges.</p></figcaption></figure>

Note that because ATRP values are expressed as a percentage of price, the ATRP values shown in the previous example can be compared with volatility spikes on charts for other symbols.

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

Like its relative ATR, Average True Range Percent (ATRP) is not a directional indicator. Instead, it's a unique volatility indicator that reflects the degree of interest or disinterest in a move. Large price ranges often accompany strong moves in either direction, especially at the beginning of a move. Relatively narrow ranges can accompany low-volatility moves.&#x20;

Because it is expressed as a percentage of price, ATRP can help chartists compare the ATR values of multiple securities to determine which securities are more volatile than others.

***

## Charting with ATRP

### Using with StockChartsACP <a href="#using_atrp_with_stockchartsacp" id="using_atrp_with_stockchartsacp"></a>

This indicator can be added from the Chart Settings panel for your StockChartsACP chart. The indicator can be positioned above or below the security's price plot.

<figure><img src="/files/cezeUkqdQSe5QKY954UT" alt=""><figcaption></figcaption></figure>

[Click here for a live version of this chart.](https://schrts.co/ADBKMdnw)

By default, the indicator is calculated using 14 periods. This parameter can be adjusted to meet your technical analysis needs.

## Scanning for ATRP <a href="#suggested_scans" id="suggested_scans"></a>

StockCharts members can screen for stocks based on ATRP values. Below is an example scan that can be used for ATRP-based signals. Simply copy the scan text and paste it into the Scan Criteria box in the [Advanced Scan Workbench](https://stockcharts.com/def/servlet/ScanUI).

Members can also set up alerts to notify them when a ATRP-based signal is triggered for a stock. Alerts use the same syntax as scans, so the sample scans below can be used as a starting point for setting up alerts as well. Simply copy the scan text and paste it into the Alert Criteria box in the [Technical Alert Workbench](https://stockcharts.com/h-al/al).

### Weeding Out High Volatility

The Average True Range Percent (ATRP) indicator can be used in scans to weed out securities with extremely high volatility. This simple scan searches for S\&P 600 stocks that are in an uptrend. The final scan clause excludes high-volatility stocks (those with average ATRP of more than 4% over the last year) from the results. Since ATRP is expressed as a percentage of a stock's price, it is ideal for comparing the volatility of different stocks in a scan.

```
[group is SP600]
AND [Daily EMA(50,close) > Daily EMA(200,close)]  

AND [ATRP(250) < 4] 
```

{% hint style="info" %}
**Learn More.** For more details on the syntax to use for ATRP scans, please see our [Scanning Indicator Reference](https://app.gitbook.com/o/MGzj6GZhi21NtnKqLOyR/s/ELJo6JImRKx7nLaFjAPl/scanning-and-alerts/scan-writing-resource-center/scan-syntax-reference/scan-syntax-technical-indicators#average_true_range_atr-1) in the Support Center.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-percent-atrp.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
