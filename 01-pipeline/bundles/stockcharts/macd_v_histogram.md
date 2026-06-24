> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-v-histogram.md).

# MACD-V Histogram

The MACD-V Histogram is a natural extension of the work done on the [the MACD-V](/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-v.md).

The MACD-V Histogram is constructed using the following formula.

```
MACD-V = [(12-period EMA – 26-period EMA)/ATR (26)] * 100
Signal line = 9-period EMA of MACD-V
Histogram = MACD-V – Signal Line
where
EMA = exponential moving average
```

1. **RISK.** The market is considered to be in short-term risk (oversold) when the MACD-V Histogram is < -40
2. **RISK.** The market is considered to be in short-term risk (overbought) when the MACD-V Histogram is > 40

## Using MACD-V Histogram in StockCharts ACP <a href="#using_macd-v_histogram_in_stockcharts_acp" id="using_macd-v_histogram_in_stockcharts_acp"></a>

The MACD-V Histogram is available as a standard indicator in StockCharts ACP. To access it:

1. Select Chart Settings
2. Scroll down the list of Standard Indicators and select MACD-V Histogram
3. You can change the MACD-V Histogram parameters by selecting the settings icon next to the indicator name.

<figure><img src="/files/XfFoeirOVhlfGjqqpWZx" alt=""><figcaption><p>MACD-V Histogram applied to SPY in StockChartsACP</p></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-v-histogram.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
