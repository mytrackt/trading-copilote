> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/the-last-stochastic-technique.md).

# The 'Last' Stochastic Technique

Many techniques using the Stochastic Oscillator produce consistent losses over time. In particular, overbought/oversold signals often degrade overall performance because one does not take advantage of longer trends. The Last Stochastic Technique addresses this shortfall.

For more information on the Stochastic Oscillator, please see our [ChartSchool article](/table-of-contents/technical-indicators-and-overlays/technical-indicators/stochastic-oscillator-fast-slow-and-full.md) on this indicator.

***

## Stochastic Signals <a href="#stochastic_signals" id="stochastic_signals"></a>

A study published in “The Encyclopedia of Technical Market Indicators” found that some very good signals were given using the 39-period Fast Stochastic. A buy signal is generated when %K crosses above 50 and the closing price is above the previous week's highest close. Sell signals are created when %K crosses below 50 and the closing price is below the previous week's lowest close.

Taking a longer period setting and not smoothing the data with a 3-period moving average allows chartists to use the Stochastic Oscillator in its purest form (Fast Stochastic Oscillator). This unsmoothed version, however, can increase whipsaws. It is often useful to smooth %K with a 3-period SMA and use the Slow Stochastic Oscillator.

On the daily chart below for MSFT, we see the Slow Stochastic Oscillator (39,1) crossing above 50 on June 14th for a bullish signal.

<figure><img src="/files/0sHiLz7yWVg96f5St2CF" alt=""><figcaption></figcaption></figure>

Chartists with a long-term outlook can turn to weekly data. On the three-year Microsoft chart below, we see that the Slow Stochastic (39,1) was above 50 for over two years and did not cross below 50 until late February 2000.

<figure><img src="/files/eYtgbCkG8kss59a9Movc" alt=""><figcaption></figcaption></figure>

On the daily Cisco (CSCO) chart, we can see the Slow Stochastic Oscillator (39,1) moving above 50 in November 1999 and not crossing back below it until April 2000. This was a good trend, but there were whipsaws (bad signals) on either side.

<figure><img src="/files/tPY5YCMzoBzLTyID7frT" alt=""><figcaption></figcaption></figure>

Since the Stochastic is a price momentum indicator, one should pair it with a volume assessment for trade confirmation. In the chart below, the [On Balance Volume](/table-of-contents/glossary/glossary-o.md#on_balance_volume_obv) (OBV) indicator has been added, along with a 30-day MA as a signal line.

[Click here for a live version of the chart.](https://stockcharts.com/h-sc/ui?c=CSCO,ULDACLYYMY%5BDD%5D%5BP%5D%5BVC60%5D%5BILH39,1%21LG30%5D)

<figure><img src="/files/AIeVLFcHR5w2U1tRyaTN" alt=""><figcaption></figcaption></figure>

Notice that there was a bullish OBV crossover in early November 1999, while %K was above 50. %K moved below 50 in April; this move was confirmed as OBV moved below its 30-day SMA. %K moved back above 50 in late April, but the price momentum signal was not confirmed by OBV. Thus, no signal. Both indicators triggered bullish again in early June.

***

## The Bottom Line <a href="#conclusion" id="conclusion"></a>

Keep in mind that all stocks are unique. While the 39-period Slow Stochastic Oscillator is a useful technical indicator, one should always map the performance against your specific stock. For example, some stocks have evidenced a tendency to signal entry when %K crosses above 40 and a sell when %K crosses below 60. Furthermore, chartists should consider using another indicator or two for confirmation when dealing with volatile stocks.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/the-last-stochastic-technique.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
