> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-annotation-tools/raff-regression-channel.md).

# Raff Regression Channel

The Raff Regression Channel is a linear regression developed by Gilbert Raff with evenly spaced [trend lines ](/table-of-contents/chart-analysis/trend-lines.md)above and below. The width of the channel is based on the high or low, which is the furthest from the linear regression. The trend is up as long as prices **rise** within this channel. An uptrend reverses when price breaks below the channel extension. The trend is down as long as prices **decline** within the channel. Similarly, a downtrend reverses when price breaks above the channel extension.

## How To Calculate the Raff Regression Channel

The Raff Regression Channel (RRC) is based on linear regression, the least-squares line-of-best fit for a price series. Even though the formula is beyond the scope of this article, linear regressions are easy to understand with a visual example.

The chart below shows the Invesco QQQ Trust ETF (QQQ) with the Raff Regression Channel in red. The middle line is the linear regression extending from the March closing low to the July closing high. Note that the linear regression is based on **closing prices**. This makes the linear regression the line of best fit from the low to the high.&#x20;

<figure><img src="/files/OXHfdv1WajsOb6kDUGgl" alt="Chart from StockCharts.com with a Raff Regression channel in an uptrend" width="563"><figcaption><p>Raff Regression Channel in an uptrend. </p></figcaption></figure>

The width is set by determining the high or low that is furthest from the linear regression. In the example below, the June high is the furthest and is used to set the upper channel trend line. The lower trend line is set the same distance from the linear regression as the upper trend line.

The chart below shows an example of QQQ in a downtrend. The Raff Regression Channel extends from the July high to the October low. The August low defines the width of the channel because it is the **furthest** low from the linear regression. The upper trend line is set at the same distance from the linear regression as the lower trend line.

<figure><img src="/files/HjQYJdvwHeNIz1Ex0wOI" alt="Raff Regression Channel in a downtrend in StockCharts.com" width="563"><figcaption><p>Raff Regression Channel in a downtrend,</p></figcaption></figure>

## Drawing and Signals <a href="#drawing_and_signals" id="drawing_and_signals"></a>

The Raff Regression Channel can be drawn to cover and define the existing trend. Once established, extension lines can be drawn to identify the [support, resistance](/table-of-contents/chart-analysis/support-and-resistance.md), or reversal points.&#x20;

An uptrend extends from the lowest closing low to the highest closing high for a move. A downtrend extends from the highest closing high to the lowest closing low. Keep in mind that closing prices are used when drawing the Raff Regression Channel, but intraday highs and lows are used to set the channel trend lines.

The chart below shows Urban Outfitters (URBN) with the Raff Regression Channel drawn from the July 2007 low to the September 2008 high (weekly closes). This covers the uptrend so far. Had URBN moved to a new closing high in October, the Raff Regression Channel would have extended to that high. Instead, URBN broke below the regression channel extension to reverse the uptrend. Notice that the lower trend line was extended to extrapolate the channel.

<figure><img src="/files/kDNEAPAC5gNQpjukzEIY" alt="Chart from StockCharts.com showing how a break below the Reff Regression Channel indicated a trend reversal"><figcaption><p>A break below the Raff Regression channel indicated a trend reversal.</p></figcaption></figure>

The chart below shows Nvidia (NVDA) in a downtrend extending from the October 2007 high to the November 2008 low. The Raff Regression Channel did not extend further because the stock traded flat and held above its November low into 2009. The red dotted line shows the channel extension of the regression channel top. NVDA broke this extension in February–March to start an uptrend.

<figure><img src="/files/BQP3vsZBLDBTzEc9RE3h" alt="Chart from StockCharts.com showing how a break above a Raff Regression channel indicated a reversal from the downtrend"><figcaption><p>Chart of NVDA showing that a break above the Raff Regression Channel indicated the downtrend may have reversed. </p></figcaption></figure>

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

As a channel based on a linear regression, the Raff Regression Channel is well suited for trend identification. The width of the channel depends on the furthest high or low from the linear regression. As such, spike highs and lows will result in very wide channels that may not capture the true range. When an uptrend starts with a sharp surge, the low that follows this initial surge is often the furthest high-low from the linear regression. By extension, when a downtrend starts with a sharp decline, the high of this initial decline is often the furthest high-low from the linear regression. Sharp initial moves create wide channels with few, if any, reaction highs or lows touching the upper and lower trend lines. Such was the case with the surge off of the March 2009 lows (see the QQQQ chart further below). Even though this article only focused on trend identification, the Raff Regression Channel can be drawn early in the trend and extended to forecast future support or resistance levels as well as [overbought](/table-of-contents/glossary/glossary-o.md#overbought) or [oversold](/table-of-contents/glossary/glossary-o.md#oversold) levels. Channel extensions can act as support or resistance. Moves outside the channel extensions can also denote overbought or oversold conditions.

## Using with SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

You can use our [ChartNotes annotation tool](https://help.stockcharts.com/charts-and-tools/sharpcharts/chartnotes#adding_annotations) to add Raff Regression Channels to your charts using the following steps:&#x20;

1. Click the **Annotate** button.
2. Select the Raff Regression annotation (found under the fifth annotation button).
3. Identify a high and low point.
4. Extend your cursor from the specific high and low points.

Below, you'll find an example of a chart annotated with two Raff Regression Channel annotations.

<figure><img src="/files/7fDA3sJ4CjJBA6I2NVZO" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To learn more about how to add this annotation to your charts, check out our Support Center article on [ChartNotes' Line Study Tools](https://help.stockcharts.com/charts-and-tools/sharpcharts/chartnotes#line_studies).
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-annotation-tools/raff-regression-channel.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
