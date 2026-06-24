> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/atr-bands.md).

# ATR Bands

## What Are ATR Bands?

ATR Bands are a volatility-based indicator that plots bands above and below a moving average of the underlying price. Expanding on the [Average True Range (ATR)](/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-atr.md) concept, developed by J. Welles Wilder, ATR Bands create a visual representation of volatility around price and its central moving average.&#x20;

## How to Interpret ATR Bands

You can use ATR Bands in various ways to analyze a market or to fine-tune your trading approaches. Here are a few ideas for interpreting and using them.

### Analyzing Volatility

Most traders use ATR Bands to gauge market volatility. By visually projecting volatility thresholds around a stock’s prices, the bands can help you assess the current market environment, which, in turn, can help you adjust your strategies accordingly.

### Setting Stop-Loss and Take-Profit Levels

Another common use of ATR Bands is to set stop-loss and take-profit levels. By placing stop-loss orders a certain multiple of the ATR below the entry price, you can give your trades enough room to fluctuate without being prematurely stopped out. Similarly, take-profit levels can be set using a multiple of the ATR above the entry price to align profit targets with market volatility​​.

### Position Sizing

You can use ATR Bands aid in position sizing. By assessing the ATR value, you can determine the appropriate trade size relative to the volatility of the asset. Higher volatility (indicated by a higher ATR) might suggest smaller position sizes to manage risk, while lower volatility might allow for larger positions.

### Combining with Other Indicators

ATR Bands are often used with other technical indicators to improve analysis and trading signals. For example, combining ATR Bands with the Relative Strength Index (RSI) can help you identify overbought or oversold conditions. Using ATR Bands with moving averages might give you a clearer picture of trend direction and volatility​.

These are just a few ways to use ATR Bands. You can explore numerous other methods and combinations to develop a trading approach that’s more tailored to your preferences.<br>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/atr-bands.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
