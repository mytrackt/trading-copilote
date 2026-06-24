> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/overview/multicollinearity.md).

# Multicollinearity

## What Is Multicollinearity?

Multicollinearity is a statistical term referring to the unknowing use of the same type of information more than once. It is a common problem in technical analysis. Analysts need to be careful not to utilize technical indicators that reveal the same type of information.

Here is how John Bollinger puts it: “A cardinal rule for the successful use of technical analysis requires avoiding multicollinearity amid indicators. Multicollinearity is simply the multiple counting of the same information. The use of four different indicators all derived from the same series of closing prices to confirm each other is a perfect example.”

Multicollinearity is a serious issue in technical analysis when your money is at stake. It is a problem because collinear variables contribute redundant information and can cause other variables to appear to be less important than they are. One of the real problems is that, oftentimes, multicollinearity is difficult to spot.

## Indicators From Different Categories

Technical indicators should be arranged in categories to avoid using too many from the same category. Below is a table that categorizes the indicators available at StockCharts.com.

| Category     | Indicators                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Momentum** | [Rate of Change (ROC)](/table-of-contents/technical-indicators-and-overlays/technical-indicators/rate-of-change-roc.md#what_is_the_rate_of_change_indicator) | <p><br><a href="/pages/QVB5cA3WHQlQdjo1YmxN">Stochastics (%K, %D)</a><br><a href="/pages/9khsZaBW4wUv06ioUMJq">Relative Strength Index (RSI)</a><br><a href="/pages/As2eACae5xBmObOdWJPL">Commodity Channel Index (CCI)</a><br><a href="/pages/XGKGYI05wyAYxw8iauUx">Williams %R (Wm%R)</a><br><a href="/pages/EIPZDV7DGWSNaV8WRLV8">StochRSI</a><br><a href="/pages/ag6FyqlfStx80g0BxcqN">TRIX</a><br><a href="/pages/sMrdzaIPdAEZBBiC3GR4">Ultimate Oscillator</a><br><a href="/pages/n7ZAiyFPdBc6eYW5mgfw">Aroon</a></p> |
| **Trend**    | [Moving Averages](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md)                         | <p><br><a href="/pages/XOLAxeUiWCg1jEl4OHxh">Moving Average Convergence Divergence (MACD)</a><br><a href="/pages/ht7rDG6TrQsmHoYYnEaS">Average True Range (ATR)</a><br><a href="/pages/QiB3Wf3FWxPbSXotleHf">Wilder's DMI (ADX)</a><br><a href="/pages/9QwAOEXf9dmW4Fkyz4Yb">Price Oscillator (PPO)</a></p>                                                                                                                                                                                                                 |
| **Volume**   | [Accumulation Distribution](/table-of-contents/technical-indicators-and-overlays/technical-indicators/accumulation-distribution-line.md)                     | <p><br><a href="/pages/a2ONRarqe28reriXnrZk">Chaikin Money Flow (CMF)</a><br>Volume Rate of Change<br><a href="/pages/AujMj8CJKpAa7EHWRU4k">Volume Oscillator (PVO)</a><br>Demand Index<br><a href="/pages/6LBgNd8ivgN5v8EWoJP8">On Balance Volume (OBV)</a><br><a href="/pages/IWo2r0YaS0nSMK3NIqPc">Money Flow Index</a></p>                                                                                                                                                                                              |

The best way to quickly determine if an indicator is collinear with another one is to chart it. Make sure you have enough data on the chart to get a good indication. If they rise and fall in the same areas, the odds are that they're collinear and you should just use one of them.

The first chart below shows some examples of indicators that are collinear. Notice that all three indicators are basically saying the same thing. If your analysis was that this was supportive information, you would be falling into the multicollinearity trap. Pick one of the indicators for your analysis and do not use the others.

<figure><img src="/files/VhnOAgjfom4IbUkpFOmg" alt="A chart from StockCharts.com displaying three indicators (RSI, CCI, Wm %R) that show similar scenarios"><figcaption><p>The RSI, CCI, and Wm%R all indicate similar scenarios. </p></figcaption></figure>

Below are some examples of indicators that are not collinear. When interpreted correctly, each will give different information. The indicators can be used to confirm a trading signal.

<figure><img src="/files/aWyUgFE0QYl8JhSXjed9" alt="A chart from StockCharts.com displaying three indicator that indicate different information about a stock"><figcaption><p>Three indicators that are not collinear show different information about a stock. They can be used as confirmation tools.</p></figcaption></figure>

## **The Takeaway**&#x20;

If you are randomly selecting indicators to support your analysis, you will more than likely fall into the multicollinearity trap of using multiple indicators that are all saying the same thing. They are not giving you any additional information; in fact, they are restricting your overall view of the market. Don't search for supporting information among collinear indicators; though they can be appealing, they are ultimately misleading.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/overview/multicollinearity.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
