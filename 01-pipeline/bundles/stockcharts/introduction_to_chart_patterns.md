> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/introduction-to-chart-patterns.md).

# Introduction to Chart Patterns

## What Are Chart Patterns? <a href="#what_are_chart_patterns" id="what_are_chart_patterns"></a>

Market participants buy and sell securities for many reasons: the hope of gain, fear of loss, tax consequences, short-covering, hedging, stop-loss triggers, price target triggers, fundamental analysis, technical analysis, broker recommendations, etc. Determining why investors buy and sell can take time and effort, so making sense of chart patterns can help.

Chart patterns put all buying and selling into perspective by consolidating the forces of supply and demand into a concise picture. This visual record of all trading provides a framework to analyze the battle between bulls and bears. More importantly, chart patterns and technical analysis help determine whether bulls or bears are winning the battle. This allows traders and investors to position themselves accordingly.

In many ways, chart patterns are more complex versions of trend lines. So before continuing, it's important to read and understand [Support and Resistance](/table-of-contents/chart-analysis/support-and-resistance.md) levels and [Trend Lines](/table-of-contents/chart-analysis/trend-lines.md).

Chart pattern analysis can be used to make short-term or long-term forecasts. The data can be intraday, daily, weekly, or monthly, and the patterns can be as short as one day or as long as many years. Gaps and outside reversals may form in one trading session, while broadening tops and dormant bottoms may require many months to form.

The [head and shoulders pattern](/table-of-contents/chart-analysis/chart-patterns/head-and-shoulders-top.md) in the chart below took seven months to form.

<figure><img src="/files/CjjfyxR5E6MJTbI2P0h6" alt="An example of a head and shoulders top that took seven days to form using StockCharts.com"><figcaption><p>Example of a head and shoulders pattern that took seven days to form.</p></figcaption></figure>

\
The pattern in CIENA Corp. (CIEN), on the other hand, formed in a single day.

<figure><img src="/files/5qfWgsp057nHlW4mxgMr" alt="Example of an outside reversal or bearish engulfing pattern that took one day to form"><figcaption><p>Example of an outside reversal or bearish engulfing pattern that took one day to complete.</p></figcaption></figure>

## An Oldie but Goodie <a href="#an_oldie_but_goodie" id="an_oldie_but_goodie"></a>

Much of our understanding of chart patterns can be attributed to the work of Richard Schabacker. His 1932 classic, *Technical Analysis and Stock Market Profits*, laid the foundations for modern pattern analysis. In [*Technical Analysis of Stock Trends*](https://a.co/d/3xKIOBg) (1948), Edwards and Magee credit Schabacker for most of the concepts put forth in the first part of their book. We would also like to acknowledge Messrs. Schabacker, Edwards and Magee, and John Murphy as the driving forces behind these articles and our understanding of chart patterns.

Pattern analysis may seem straightforward, but it is no easy task. Schabacker states:

***

“The science of chart reading, however, is not as easy as the mere memorizing of certain patterns and pictures and recalling what they generally forecast. Any general stock chart is a combination of countless different patterns and its accurate analysis depends upon constant study, long experience and knowledge of all the fine points, both technical and fundamental, and, above all, the ability to weigh opposing indications against each other, to appraise the entire picture in the light of its most minute and composite details as well as in the recognition of any certain and memorized formula.”

***

Even though Schabacker refers to “the science of chart reading”, technical analysis can at times be less science and more art. In addition, pattern recognition can be open to interpretation, which can be subject to personal biases. To defend against biases and confirm pattern interpretations, other aspects of technical analysis should be employed to verify or refute the conclusions drawn. While many patterns may seem similar in nature, no two patterns are exactly alike. False breakouts, bogus reads, and exceptions to the rule are all part of the ongoing education.

Careful and constant study is required for successful chart analysis. In the earlier example of the head and shoulders reversal pattern in AMZN, the stock broke below the neckline of the head and shoulders. This is a bearish signal, but you must continue your analysis to confirm the bearish trend.&#x20;

Some analysts might have labeled the pattern in the chart below as a head and shoulders pattern with neckline support around 17.50. Whether or not this is robust remains open to debate. Even though the stock broke neckline support at 17.50, it repeatedly moved back above its support break. This might be considered a sign of strength, which would warrant a reassessment of the pattern.

<figure><img src="/files/hN5GCrhBdAJSUO75viCA" alt="An example of a stock that broke below a head and shoulders neckline but didn&#x27;t continue to decline."><figcaption><p>Even though the stock price broke below the head and shoulders neckline, price moved back above it. This could be considered a sign of strength, and it would make sense to continue to analyze the chart.</p></figcaption></figure>

## Continuation Patterns vs. Reversal Patterns <a href="#continuation_patterns_vs_reversal_patterns" id="continuation_patterns_vs_reversal_patterns"></a>

Two basic tenets of technical analysis are that prices trend and history repeats itself. **An uptrend indicates the forces of demand (bulls) are in control, while a downtrend indicates the forces of supply (bears) are in control.** But prices don't trend forever, and as the balance of power shifts, a chart pattern begins to emerge.&#x20;

Certain patterns, such as a parallel channel, denote a strong trend (see chart below). However, most chart patterns fall into two main groups—reversals and continuations. Reversal patterns indicate a trend change and can be broken down into top and bottom formations. Continuation patterns indicate a pause in trend and that the previous direction will resume after some time.

<figure><img src="/files/3P1dnLHc6eAydmEkGfG0" alt="Chart showing an upward sloping price channel from StockCharts.com"><figcaption><p>Example of an upward-sloping parallel channel.</p></figcaption></figure>

Just because a pattern forms after a significant advance or decline does not mean it is a reversal pattern. Many patterns, such as a rectangle, can be classified as either reversal or continuation. Much depends on the previous price action, volume, and other indicators as the pattern evolves. This is where the science of technical analysis becomes the art of technical analysis.

{% hint style="info" %}
For detailed explanations of specific continuation and reversal chart patterns, see the [Chart Patterns](/table-of-contents/chart-analysis/chart-patterns.md) page in ChartSchool.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/introduction-to-chart-patterns.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
