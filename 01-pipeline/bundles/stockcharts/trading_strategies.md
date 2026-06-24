> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies.md).

# Trading Strategies

[**Bollinger Band Squeeze**](/table-of-contents/technical-indicators-and-overlays/technical-indicators/bollinger-bandwidth.md)\
This strategy uses Bollinger Bands to identify volatility contraction that may foreshadow a significant advance or decline.

[**CCI Correction**](/table-of-contents/trading-strategies-and-models/trading-strategies/cci-correction.md)\
A strategy that uses weekly CCI to dictate a trading bias and daily CCI to generate trading signals.

[**CVR3 VIX Market Timing**](/table-of-contents/trading-strategies-and-models/trading-strategies/cvr3-vix-market-timing.md)\
Developed by Larry Connors and Dave Landry, this is a strategy that uses overextended readings in the CBOE Volatility Index ($VIX) to generate buy and sell signals for the S\&P 500.

[**Faber's Sector Rotation Trading Strategy**](/table-of-contents/trading-strategies-and-models/trading-strategies/fabers-sector-rotation-trading-strategy.md)\
Based on research from Mebane Faber, this sector rotation strategy buys the top-performing sectors and re-balances once per month.

[**Gap Trading Strategies**](/table-of-contents/trading-strategies-and-models/trading-strategies/gap-trading-strategies.md)\
Various strategies for trading based on opening price gaps.

[**Harmonic Patterns**](/table-of-contents/trading-strategies-and-models/trading-strategies/harmonic-patterns.md)\
An in-depth examination of harmonic chart patterns, their advantages and disadvantages, and strategies for how to trade them.

[**Hindenburg Omen**](/table-of-contents/trading-strategies-and-models/trading-strategies/hindenburg-omen.md) \
A technical market pattern that indicates the potential risk of a stock market downturn and how you can use it to strategize your trades or investments.

[**Ichimoku Cloud**](/table-of-contents/technical-indicators-and-overlays/technical-overlays/ichimoku-cloud.md)\
A strategy that uses the Ichimoku Cloud to set the trading bias, identify corrections, and signal short-term turning points.

[**The 'Last' Stochastic Technique**](/table-of-contents/trading-strategies-and-models/trading-strategies/the-last-stochastic-technique.md)\
This strategy uses the Slow Stochastic Oscillator to reduce whipsaws and provide more accurate buy and sell signals.

[**MACD Zero-Line Crosses With Swing Points**](/table-of-contents/trading-strategies-and-models/trading-strategies/macd-zero-line-crosses-with-swing-points.md)\
A strategy that applies the MACD zero line cross to swing points.

[**Moving Average Trading Strategies**](/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies.md)\
Helpful trading strategies such as moving average crossovers, moving averages as support and resistance, and Moving Average Ribbons to identify trend direction, strength, and trend reversals.

[**Moving Momentum**](/table-of-contents/trading-strategies-and-models/trading-strategies/moving-momentum.md)\
A strategy that uses a three-step process to identify the trend, wait for corrections within that trend, and then identify reversals that signal an end to the correction.

[**Narrow Range Day NR7**](/table-of-contents/trading-strategies-and-models/trading-strategies/narrow-range-day-nr7.md)\
Developed by Tony Crabel, the narrow range day strategy looks for range contractions to predict range expansions. Advanced scan code included that tweaks this strategy by adding Aroon and CCI qualifiers.

[**Percent Above 50-day SMA**](/table-of-contents/trading-strategies-and-models/trading-strategies/percent-above-50-day-sma.md)\
A strategy that uses the breadth indicator, percent above the 50-day moving average, to define the tone for the broad market and identify corrections.

[**Percent B Money Flow**](/table-of-contents/trading-strategies-and-models/trading-strategies/percent-b-money-flow.md)\
In this strategy, the %B indicator and the Money Flow Index are used to identify the start of a new trend when both reach a bullish or bearish threshold.

[**The Pre-Holiday Effect**](/table-of-contents/trading-strategies-and-models/trading-strategies/the-pre-holiday-effect.md)\
How the market has performed before major US holidays and how that can affect trading decisions.

[**RSI(2)**](/table-of-contents/trading-strategies-and-models/trading-strategies/rsi-2.md)\
An overview of Larry Connors' mean reversion strategy using 2-period RSI.

[**Six-Month Cycle MACD**](/table-of-contents/trading-strategies-and-models/trading-strategies/six-month-cycle-macd.md)\
Developed by Sy Harding, this strategy combines the six-month bull-bear cycle with MACD signals for timing.

[**Slope Performance Trend**](/table-of-contents/trading-strategies-and-models/trading-strategies/slope-performance-trend.md)\
Using the slope indicator to quantify the long-term trend and measure relative performance for a trading strategy with the nine sector SPDRs.

[**Stochastic Pop and Drop**](/table-of-contents/trading-strategies-and-models/trading-strategies/stochastic-pop-and-drop.md)\
Developed by Jake Berstein and modified by David Steckler, this strategy uses the Average Directional Index (ADX) and Stochastic Oscillator to identify price pops and breakouts.

[**Swing Charting**](/table-of-contents/trading-strategies-and-models/trading-strategies/swing-charting.md)\
An overview of swing trading and how it can be used to profit under certain market conditions.

[**Trend Quantification and Asset Allocation**](/table-of-contents/trading-strategies-and-models/trading-strategies/trend-quantification-and-asset-allocation.md)\
This article shows chartists how to define long-term trend reversals by smoothing the price data with four different Percentage Price Oscillators. Chartists can also use this technique to quantify trend strength and determine asset allocation.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
