> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/high-low-bands.md).

# High Low Bands

## What Are High Low Bands (HLB)?

The High Low Bands (HLB) indicator helps traders identify and analyze price trends and volatility. It's made up of three lines: an upper band, a middle band, and a lower band. HLB is based on the triangular moving average—a “smoothed” moving average using a particular calculation that gives greater weight to the most recent price data.

Three lines are derived from this triangular moving average—one above and one below the original average, which appears in the middle. The distance between the upper and lower bands from the middle band is adjusted by a specific percentage according to your preference. The StockChartsACP’s default HLB percentage is set to 5.

## How Do You Interpret High Low Bands?

There are several ways in which you can interpret High Low Bands.

<figure><img src="/files/DauhhCc1FrUVcEIQHjuU" alt="Example of a chart overlaid with High Low Bands indicator showing a strong uptrend, oversold conditions, overbought conditions from StockChartsACP"><figcaption><p>The High Low Bands indicator can identify trend direction, overbought/oversold conditions, support and resistance levels, and volatile trading conditions.</p></figcaption></figure>

**Trend Direction.** If the price consistently touches or exceeds the upper band, the indicator suggests a strong uptrend. Conversely, if the price persistently touches or falls below the lower band, it indicates a strong downtrend.

**Overbought/Oversold Conditions.** Prices near the upper band might indicate an overbought condition. Prices near the lower band might indicate an oversold condition. It’s best to check these readings with other indicators that interpret potential overbought/oversold readings (such as the [Relative Strength Index](/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi.md) or the [Stochastic Oscillator](/table-of-contents/technical-indicators-and-overlays/technical-indicators/stochastic-oscillator-fast-slow-and-full.md)).

**Support and Resistance.** The upper and lower bands can sometimes serve as dynamic support and resistance levels, with the middle band serving as a mean reversion level toward which prices may gravitate.

**Volatility.** Although the bands don't dynamically adjust to volatility like Bollinger Bands, High Low Bands can still be a visual reference to gauge price volatility.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/high-low-bands.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
