> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/atr-trailing-stops.md).

# ATR Trailing Stops

## What is the ATR Trailing Stops Indicator?

The ATR (Average True Range) Trailing Stop is a volatility-based indicator that sets dynamic stop-loss levels for market exits or entries. This indicator uses the [Average True Range](/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-atr.md), a metric that evaluates market volatility, to determine where the trailing stops will be placed. By doing so, the indicator can help you manage risk (or identify market entry points) by dynamically adjusting the stop levels to the changing market conditions.

## How are the ATR Trailing Stops Calculated?

ATR Trailing Stops calculation requires a few steps. They are as follows:

1. **Calculate the ATR (Average True Range).** The ATR is a moving average of the true ranges over a specified period. In the StockChartsACP platform, the ATR is set to 21 days.
2. **Decide on the Multiplier.** This multiplier adjusts how far the trailing stop should be from the price. The choice of multiplier (such as 2x, 3x, or higher) depends on the anticipated level of volatility and the aggressiveness of your risk management approach. In the StockChartsACP platform, the multiplier is set to a default of 3.&#x20;
3. **Calculate the Trailing Stop.**
   * **For a Long Position.** Subtract the product of the ATR and the chosen multiplier from the highest price. This gives you the stop-loss level if you’re holding a long position.
   * **For a Short Position.** Add the product of the ATR and the chosen multiplier to the lowest price. This provides the stop-loss level for a short position.
4. **Update the Stop.** The trailing stop is adjusted only in the direction of the trend. For a long position, the stop level increases if the price makes new highs. For a short position, the stop level decreases if the price makes new lows.&#x20;

## How Do You Interpret ATR Trailing Stops?

### Trend Identification

You can use the ATR Trailing Stops as a tool for trend identification. If the ATR Trailing Stops is below the price, the market is in an uptrend. Conversely, if the training stop is above the price, it suggests that the market is in a downtrend.

### Exit and Entry Points&#x20;

* **Exits.** The most common use of the ATR Trailing Stops is to set stop losses (exit points). For a long position, you would exit when the price drops below the ATR line. For a short position, the exit signal is when the price rises above the ATR line. This can help protect your profits by allowing positions to run during favorable conditions and closing them when markets reverse.
* **Entries.** While primarily used for exit signals, ATR Trailing Stops can also be used as entry signals in a trend-following strategy. For instance, you can enter a long position when the price moves above the ATR Trailing Stop and enter a short position when the price moves below the ATR Trailing Stop.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/atr-trailing-stops.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
