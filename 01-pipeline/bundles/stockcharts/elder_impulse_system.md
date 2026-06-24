> For the complete documentation index, see [llms.txt](https://chartschool.stockcharts.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/elder-impulse-system.md).

# Elder Impulse System

## What Is the Elder Impulse System? <a href="#introduction" id="introduction"></a>

The Elder Impulse System was designed by Alexander Elder and featured in his book [*Come Into My Trading Room*](https://store.stockcharts.com/products/come-into-my-trading-room-a-complete-guide-to-trading). According to Elder, “the system identifies inflection points where a trend speeds up or slows down.” The Impulse System is based on two indicators: a 13-day exponential moving average and the [MACD-Histogram](/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-histogram.md). The moving average identifies the trend, while the MACD-Histogram measures momentum. As a result, the Impulse System combines trend following and momentum to identify tradable impulses. This unique indicator combination is color coded into the price bars for easy reference.

## Calculating the Elder Impulse System <a href="#calculation" id="calculation"></a>

```
Green Price Bar: (13-period EMA > previous 13-period EMA) and 
                 (MACD-Histogram > previous period's MACD-Histogram)

Red Price Bar: (13-period EMA < previous 13-period EMA) and 
               (MACD-Histogram < previous period's MACD-Histogram)

Price bars are colored blue when conditions for a Red Price Bar or 
Green Price Bar is not met. The MACD-Histogram is based on MACD(12,26,9). 
```

**Green price bars** show that the bulls are in control of trend and momentum as both the 13-day EMA and MACD-Histogram are rising. A **red price bar** indicates that the bears have taken control because the 13-day EMA and MACD-Histogram are falling. A **blue price bar** indicates mixed technical signals— neither buying nor selling pressure predominating.

<figure><img src="/files/DULBTycFXWqL50TQhche" alt="An Elder Impulse System chart from StockCharts.com showing when bulls and bears are in control"><figcaption><p>Example of an Elder Impulse System chart showing when bulls and bears are in control of the market.</p></figcaption></figure>

## Timeframe <a href="#timeframe" id="timeframe"></a>

The Elder Impulse System can be used across different timeframes, but trading should be in harmony with the bigger trend. Elder recommends setting your trading timeframe and then calling it intermediate; then multiply this intermediate timeframe by five to get your long-term timeframe.&#x20;

Traders using daily charts for an intermediate timeframe can move to weekly charts for a long-term timeframe. The choice is not as clear-cut for smaller or longer timeframes. A little judgment is required.&#x20;

Traders using 10-minute charts to chart their “intermediate” timeframe can use 60-minute charts for their “long-term” timeframe. Investors using weekly charts can base the bigger picture on monthly charts.&#x20;

Once you've decided on your trading timeframe, you'd use the longer timeframe to identify the bigger trend. This can even be accomplished using one chart.&#x20;

The chart below shows daily bars with the Elder Impulse System and the 65-da[y exponential moving average](/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md) (EMA), five times the 13-day EMA. The long-term trend is considered up when SPY is above the 65-day EMA or when [Moving Average Convergence/Divergence](/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator.md) or MACD (1,65,1) is positive.

<figure><img src="/files/gQN4noRHQx6ErnsoOPiV" alt="Chart from StockCharts.com showing Elder Impulse System on SPY with a 65-day EMA overlay and the MACD"><figcaption><p>Daily bars with the Elder Impulse System with an EMA overlay and MACD in the lower panel. </p></figcaption></figure>

There are other methods for determining the weekly trend besides the MACD(1,65,1) zero crossover on the daily chart. For the sake of simplicity, the examples on this page apply the MACD. &#x20;

## Entries and Exits <a href="#entries_and_exits" id="entries_and_exits"></a>

A buy signal occurs when the long-term trend is deemed bullish, and the Elder Impulse System turns bullish on the intermediate-term trend. In other words, the weekly chart has to show a clear uptrend for a daily buy signal to be valid. Daily buy signals that occur when the weekly chart is not in a clear uptrend are ignored.

A sell signal occurs when the long-term trend is deemed bearish, and the Elder Impulse System turns bearish on the intermediate-term trend. For example, the weekly chart has to show a clear downtrend for a daily sell signal to be valid. Daily sell signals that happen when the weekly chart is not in a clear downtrend are ignored.

The daily chart below adds the MACD(1,65,1) indicator to show the weekly trend. If the MACD is above zero, the weekly trend is up. If it is below zero, the weekly trend is down.&#x20;

<figure><img src="/files/3QozKnvsQrUlKsynVIXS" alt="Elder Impulse System chart from StockCharts.com showing bullish and bearish signals"><figcaption><p>Elder Impulse System chart displaying bullish and bearish signals. </p></figcaption></figure>

The first three green arrows on the chart show valid daily buy signals (i.e., new clusters of green daily bars). Note, however, that the first few red bars on the chart are *not* valid sell signals in this case because the weekly trend is still positive (according to the MACD indicator). After the weekly trend turns down, the red arrow shows the first valid sell signal. Similarly, the weekly trend must turn positive again before valid buy signals are given (as indicated by the last three green arrows on the chart).

## The Takeaway <a href="#conclusion" id="conclusion"></a>

The Elder Impulse System is designed to catch relatively short price moves. Elder notes, "***The Impulse System encourages you to enter cautiously but exit fast. This is the professional approach to trading, the total opposite of the amateur's style. Beginners jump into trades without thinking too much and take forever to get out, hoping and waiting for the market to turn their way.”***

In addition to trading setups, the Elder Impulse System can prevent bad trades by consulting it before entering a trade. Use the Impulse System to confirm bullish or bearish setups. Traders can ignore bullish setups when the Impulse System is not in full-blown bull mode (green bars) and ignore bearish signals when the system is not in full-blown bear mode (red bars).&#x20;

The impulse system can also be used to anticipate patterns or reversals. If you think a [bull flag](/table-of-contents/chart-analysis/chart-patterns/flag-pennant.md#what_are_flag_and_pennant_chart_patterns) is taking shape or support from a [Fibonacci retracement level](/table-of-contents/chart-analysis/chart-annotation-tools/fibonacci-retracements.md) is near, the Impulse System can identify a short-term reversal for confirmation.

***

## Using Elder Impulse System With SharpCharts <a href="#using_with_sharpcharts" id="using_with_sharpcharts"></a>

The Elder Impulse System can be accessed in SharpCharts by selecting **Elder Impulse System** from the **Chart Type** dropdown menu in the **Attributes** area of the Chart Settings. Overlays and indicators can be added to see how the Elder Impulse System works or to determine the longer trend. For example, you can add an EMA as an overlay or the MACD as an indicator. [Click here](https://stockcharts.com/sc3/ui/?s=$INDU\&p=D\&yr=0\&mn=8\&dy=0\&id=p09590891724\&listNum=30\&a=198207528) for a live example of the Elder Impulse System.

<figure><img src="/files/hwws0SXRDfxjuiaDQ3Wu" alt="Image displaying how to access Elder Impulse System chart type in SharpCharts from StockCharts.com"><figcaption><p>Elder Impulse System SharpChart</p></figcaption></figure>

<figure><img src="/files/YlRWIMwKpV0g8eIcGBej" alt=""><figcaption><p>How to access Elder Impulse System chart type in SharpCharts.</p></figcaption></figure>

***

## Further Study <a href="#further_study" id="further_study"></a>

| <p><a href="https://a.co/d/b12Hly2"><strong>The New Trading for a Living</strong></a><br>Alexander Elder</p> | <p><a href="https://a.co/d/e0NLp8h"><strong>Come Into My Trading Room</strong></a><br>Alexander Elder</p> | <p><a href="https://a.co/d/3hlzn8q"><strong>The New Sell and Sell Short</strong></a><br>Alexander Elder</p> |
| ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| ![](/files/ODdaegyb0baIvMDo07sw)                                                                             | ![](/files/PG9aRylHdOfmcddI5DI2)                                                                          | ![](/files/rV7i6cJaLzmtYwRlnpFv)                                                                            |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/elder-impulse-system.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
