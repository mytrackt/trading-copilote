> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/overview/arthur-hill-on-moving-average-crossovers.md).

# Arthur Hill on Moving Average Crossovers

## Moving Average Crossovers <a href="#moving_average_crossovers" id="moving_average_crossovers"></a>

A popular use for [moving averages](/table-of-contents/glossary/glossary-m.md#moving_average_ma) is to develop simple trading systems based on moving average crossovers. A trading system using two moving averages would give a buy signal when the shorter (faster) moving average crosses above the longer (slower) moving average. A sell signal would be given when the shorter moving average crosses below the longer moving average.&#x20;

The speed of the systems and the number of signals generated will depend on the length of the moving averages. Shorter moving average systems will be faster, generate more signals, and be nimble for early entry. However, they will generate more false signals than systems with longer moving averages.

### Some Examples <a href="#some_examples" id="some_examples"></a>

In Apple, Inc.'s (AAPL) daily chart below, a 30/100 [exponential moving average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) (EMA) crossover generated buy and sell signals.

<figure><img src="/files/gsdyaKkjjhsT6bIf19Hp" alt="Chart of Apple stock showing how exponential moving average crossovers and the PPO indicator can be used to generate buy and sell signals"><figcaption><p>Applying exponential moving averages and Percentage Price Oscillator to generate buy and sell signals.</p></figcaption></figure>

A buy signal is generated when the 30-day EMA moves above the 100-day EMA. A sell signal is in force when the 30-day EMA falls below the 100-day EMA. A 30/100 differential plot is shown below the price chart using the [Percentage Price Oscillator](/table-of-contents/technical-indicators-and-overlays/technical-indicators/percentage-price-oscillator-ppo.md) (PPO) set to (30,100,1). The 30-day EMA is greater than the 100-day EMA when the differential is positive. When negative, the 30-day EMA is less than the 100-day EMA.

As with all trend-following systems, the signals work well when the stock develops a strong trend but are ineffective when the stock is in a trading range. The one generated in Nov 2023 was a good entry point for a long position. However, the exit signal based on the moving average crossover generated on March 2024 would have given back some profits.&#x20;

In the example below, a 20/60 EMA crossover system generated several buy and sell signals.

<figure><img src="/files/kqfH87DJUFLK6ddF21f1" alt=""><figcaption></figcaption></figure>

The plot below the price is the 20/60 EMA differential, shown as a percent and displayed using the PPO set at (20,60,1). The dashed blue lines above and below zero (the centerline) represent the buy and sell trigger points. Using zero as the crossover point for the buy and sell signals generated too many false signals. To reduce the number of signals, you can set the buy signal just above the zero line, say at +2%, and the sell signal just below the zero line, at -2%. A buy signal is in force when the 20-day EMA is more than 2% above the 60-day EMA. A sell signal is in force when the 20-day EMA is more than 2% below the 60-day EMA.

You can find many good signals, but you may also find some [whipsaws](/table-of-contents/glossary/glossary-w.md#whipsaw). Although much would depend on the exact entry and exit points, you could have made profitable trades using this system, but some may not be large profits that are probably not enough to justify the risk.&#x20;

If a stock fails to hold a trend, you'd have to place tight stop-losses to lock in profits. A trailing stop or use of the parabolic SAR might have helped lock in profits.

## The Bottom Line <a href="#the_bottom_line" id="the_bottom_line"></a>

Moving average crossover systems can be effective but should be used with other aspects of technical analysis (patterns, candlesticks, momentum, volume, and so on). While it's easy to find a system that worked well in the past, there is no guarantee it will work in the future.

***

{% hint style="info" %}
**Learn More.** [**Trading With Moving Averages**](/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies.md)
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/overview/arthur-hill-on-moving-average-crossovers.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
