> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies.md).

# Moving Average Trading Strategies

**KEY TAKEAWAYS**

* Three ways to trade with moving averages are moving average crossovers, support & resistance levels, and moving average ribbons
* Crossovers can help identify entry and exit points
* Support and resistance levels help identify turning points in trends

***

Moving averages are among the most popular technical indicators traders and investors use. Talking heads mention them on financial media channels. You can find moving averages on popular financial sites and in just about every stock charting software. Even fundamental analysts apply them in their analyses.

But how do you use moving averages to exit and enter trades? There are different ways to trade with moving averages. We'll explore how to make entry and exit decisions with moving average and/or price crossovers, utilize moving averages as support and resistance levels, and identify trends and/or trend reversals using moving average ribbons. Moving averages are easily incorporated into platforms like [SharpCharts](https://help.stockcharts.com/charts-and-tools/sharpcharts), [StockChartsACP](https://help.stockcharts.com/charts-and-tools/stockchartsacp), or [P\&F charts](/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-basics/introduction-to-point-and-figure-charts.md).

## Why Use Moving Average Trading Strategies? <a href="#why_use_moving_average_trading_strategies" id="why_use_moving_average_trading_strategies"></a>

The financial markets can be complex. Sometimes, a simpler approach to understanding market activity can be more efficient and effective than complicated analytical methods. This is where moving average-based strategies can come into play.

### Simpler Trend Analysis <a href="#simpler_trend_analysis" id="simpler_trend_analysis"></a>

Moving averages can help eliminate market noise, making it easier to interpret and analyze market direction.

### Versatility <a href="#versatility" id="versatility"></a>

The difference in approaches—crossovers, support & resistance levels, and MA ribbons—offers multiple ways to identify potential entry and exit points. This allows you to choose various methods that best fit a market opportunity.

### Dynamic Support and Resistance Levels <a href="#dynamic_support_and_resistance_levels" id="dynamic_support_and_resistance_levels"></a>

Moving averages dynamically adjust based on new price data. This makes support and resistance more fluid and adaptable to changing market conditions.

### Visual Cues on Trend Strength <a href="#visual_cues_on_trend_strength" id="visual_cues_on_trend_strength"></a>

Moving averages, in relation to price or other moving averages (e.g., ribbons), can provide a graphical representation of trend direction and strength. This information can be helpful when making trading decisions.

***

## Trading Moving Average Crossovers <a href="#trading_moving_average_crossovers" id="trading_moving_average_crossovers"></a>

Two popular ways to use crossovers are price-to-moving-average and moving-average crossovers.

### Price Crossovers <a href="#price_crossovers" id="price_crossovers"></a>

Trading with moving averages can be helpful to trend traders. When the price crosses above a moving average, it could be bullish. When price moves below a moving average, it could be considered a bearish signal. But a lot depends on what moving average you use and if that price crossover is a follow-through move.

You've probably heard the adage, “The trend is your friend until it bends.” Based on this premise, you could combine a price crossover with the major trend so your trading aligns with the trend.

{% hint style="info" %}
**Learn More.** [**How To Trade Price-to-Moving Average Crossovers**](/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies/how-to-trade-price-to-moving-average-crossovers.md)
{% endhint %}

### Moving Average Crossovers <a href="#moving_average_crossovers" id="moving_average_crossovers"></a>

Moving average crossovers occur when one moving average crosses another. Say you have a 50-day simple moving average (SMA) and a 100-day SMA overlaid on your price chart.

A bullish crossover is when the shorter moving average crosses above the longer one; in this case, it's when the 50-day SMA crosses above the 100-day SMA, called a [Golden Cross](/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies/trading-using-the-golden-cross.md). A bearish crossover, or [**a Death Cross**](/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies/trading-the-death-cross.md), is when the shorter moving average crosses below the longer SMA.

Moving average crossovers can also be used for short-term trading. The [5-8-13 EMA crossover](/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies/using-the-5-8-13-ema-crossover-for-short-term-trades.md) is a popular strategy among short-term traders. The crossovers between the three [exponential moving averages](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) (EMAs) can indicate price moves in the near term.

***

## Support and Resistance <a href="#support_and_resistance" id="support_and_resistance"></a>

Moving averages can be used as support and resistance levels. You may notice that prices often bounce off a moving average. The moving average is acting as a support level. Sometimes, prices are reluctant to move beyond a moving average. That's when a moving average acts as a resistance level. Traders often use the levels to identify entry and exit points.

{% hint style="info" %}
**Learn More.** [**Finding Support and Resistance in Moving Averages**](/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies/finding-support-and-resistance-in-moving-averages.md)
{% endhint %}

***

## Moving Average Ribbons <a href="#moving_average_ribbons" id="moving_average_ribbons"></a>

When you plot a bunch of moving averages on a price chart, the appearance resembles a ribbon moving across the chart. You can use Moving Average Ribbons to identify long and short-term trend direction, trend strength, and trend reversals.

The width of the ribbon, that is, the distance between the moving averages, also helps to identify trend strength, the end of a trend, and the beginning of a trend.

There are different ways to apply [Moving Average Ribbons](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-average-ribbon.md). The Guppy Multiple Moving Average is a popular method which combines 12 exponential moving averages.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
